"""
compile_index.py — the index compiler as a deep, testable module

build-index.py owns the filesystem (scanning pages, writing artifacts, atomic
publish) and the clock (build_id, timestamps). Everything between — turning a
list of Pages into rows, edges, evidence, a routing queue, and the
critical/warning ledgers — lives here behind one interface:

    compile_index(pages, *, target_exists) -> BuildResult

It reads no clock and touches no filesystem: the one filesystem fact it needs
(does a finding's candidate target page exist?) is injected as `target_exists`,
so the whole compile is deterministic and assertable in memory. This is the test
surface main() never had (see test_compile.py).
"""

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

from schema import REL_FIELDS, TERMINAL_FINDING_STATUS
from lint_rules import GraphCtx, RuleCtx, run_graph_rules, run_rules
from bm25 import build_term_index


@dataclass
class Page:
    path: Path
    rel_path: str
    frontmatter: Dict[str, Any]
    body: str


@dataclass
class BuildResult:
    page_rows: List[Dict[str, Any]] = field(default_factory=list)
    section_rows: List[Dict[str, Any]] = field(default_factory=list)
    evidence_rows: List[Dict[str, Any]] = field(default_factory=list)
    valid_edges: List[Dict[str, Any]] = field(default_factory=list)
    unresolved_edges: List[Dict[str, Any]] = field(default_factory=list)
    routing_pending: List[Dict[str, Any]] = field(default_factory=list)
    critical: List[Dict[str, Any]] = field(default_factory=list)
    warnings: List[Dict[str, Any]] = field(default_factory=list)
    # Ranker inputs (ADR-0002): per-page inbound-link count (centrality) and a
    # BM25 term index over title + body.
    inbound_degree: Dict[str, int] = field(default_factory=dict)
    term_index: Dict[str, Any] = field(default_factory=dict)

    @property
    def status(self) -> str:
        if self.critical:
            return "invalid"
        if self.warnings:
            return "valid_with_warnings"
        return "valid"


def normalize_source_id(source_id: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9-]+", "-", source_id).strip("-")
    return f"S-{slug}"


def edge_targets(field_name: str, value: Any) -> List[str]:
    if value is None:
        return []
    if field_name == "source_basis":
        targets = []
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    sid = item.get("source_id")
                    if sid:
                        targets.append(str(sid))
                elif isinstance(item, str):
                    targets.append(item)
        return [t for t in targets if t]

    if isinstance(value, list):
        return [str(v) for v in value if str(v).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def section_line_ranges(
    body: str, sections: List[Dict[str, Any]]
) -> Tuple[List[Dict[str, Any]], List[str]]:
    warnings: List[str] = []
    out: List[Dict[str, Any]] = []
    lines = body.splitlines()
    starts: List[Tuple[int, str, str]] = []

    for sec in sections:
        sid = str(sec.get("id", "")).strip()
        anchor = str(sec.get("anchor", "")).strip()
        anchor_id = anchor[1:] if anchor.startswith("#") else anchor
        if not sid or not anchor_id:
            warnings.append(f"invalid_section_entry:{sid or 'missing'}")
            continue
        patt = re.compile(rf"<a\s+id=[\"']{re.escape(anchor_id)}[\"']\s*></a>")
        line_no = None
        for idx, line in enumerate(lines, start=1):
            if patt.search(line):
                line_no = idx
                break
        if line_no is None:
            warnings.append(f"missing_anchor:{anchor_id}")
            continue
        starts.append((line_no, sid, anchor_id))

    starts.sort(key=lambda x: x[0])
    for i, (line_no, sid, anchor_id) in enumerate(starts):
        end_line = len(lines) if i == len(starts) - 1 else starts[i + 1][0] - 1
        out.append(
            {
                "section_id": sid,
                "anchor": f"#{anchor_id}",
                "start_line": line_no,
                "end_line": end_line,
            }
        )
    return out, warnings


def unsatisfied_targets(
    action: Optional[str], candidate_targets: List[Any], target_exists: Callable[[str], bool]
) -> List[str]:
    """Return the candidate paths that violate the target requirement for this
    integration_action (the #7 routing contract — resolution is by PATH):

      enrich-*  -> the target page must EXIST; missing paths are unsatisfied.
      create-*  -> the target must NOT exist yet; existing paths are unsatisfied
                   (a collision with the prefer-enrich rule, flagged for review).
      otherwise -> source_only / flag-for-review / unset impose no path
                   requirement, so nothing is unsatisfied.
    """
    act = str(action or "").strip().lower()
    paths = [p for p in candidate_targets if isinstance(p, str)]
    if act.startswith("enrich"):
        return [p for p in paths if not target_exists(p)]
    if act.startswith("create"):
        return [p for p in paths if target_exists(p)]
    return []


def compile_index(
    pages: List[Page],
    *,
    target_exists: Callable[[str], bool],
    today: Optional[date] = None,
) -> BuildResult:
    """Compile Pages into a BuildResult. Pure: no clock, no filesystem — the two
    impure facts it needs are injected. `target_exists` answers "does this
    candidate target page exist on disk?"; `today` is the clock the
    contradiction-aging rule ages against (None disables aging). The per-page and
    cross-page processing order mirrors the original build so the emitted ledgers
    and rows are position-stable."""
    result = BuildResult()

    id_to_page: Dict[str, Page] = {}
    duplicate_ids = set()
    raw_edges: List[Dict[str, Any]] = []
    term_docs: List[Tuple[str, str]] = []

    for page in pages:
        fm = page.frontmatter
        if fm.get("_yaml_error"):
            result.critical.append({"path": page.rel_path, "error": "invalid_yaml_frontmatter"})
            continue

        if not fm:
            result.warnings.append({"path": page.rel_path, "warning": "missing_frontmatter"})
            continue

        page_id = fm.get("id")
        if not page_id and fm.get("type") == "source" and fm.get("source_id"):
            page_id = normalize_source_id(str(fm.get("source_id")))
            result.warnings.append({"path": page.rel_path, "warning": f"derived_source_id:{page_id}"})

        if fm.get("type") == "source" and not fm.get("retrieval_status"):
            source_status = str(fm.get("status", "")).strip()
            fm["retrieval_status"] = "usable" if source_status in {"ingested", "reviewed"} else "limited"
            result.warnings.append(
                {"path": page.rel_path, "warning": f"derived_retrieval_status:{fm['retrieval_status']}"}
            )

        ptype = str(fm.get("type", "")).strip()
        ctx = RuleCtx(rel_path=page.rel_path, fm=fm, page_id=page_id, ptype=ptype, today=today)
        for issue in run_rules(ctx):
            if issue.severity == "critical":
                result.critical.append({"path": page.rel_path, "error": issue.code})
            else:
                result.warnings.append({"path": page.rel_path, "warning": issue.code})

        if page_id:
            if page_id in id_to_page:
                duplicate_ids.add(page_id)
            else:
                id_to_page[page_id] = page

        sections = fm.get("sections", [])
        if not sections:
            result.warnings.append({"path": page.rel_path, "warning": "missing_sections"})
        elif isinstance(sections, list):
            ranges, sec_warn = section_line_ranges(page.body, sections)
            for w in sec_warn:
                result.critical.append({"path": page.rel_path, "error": f"section_error:{w}"})
            for sec in ranges:
                result.section_rows.append(
                    {
                        "page_id": page_id,
                        "section_id": sec["section_id"],
                        "path": page.rel_path,
                        "start_line": sec["start_line"],
                        "end_line": sec["end_line"],
                    }
                )
        else:
            result.critical.append({"path": page.rel_path, "error": "sections_not_list"})

        row = {
            "id": page_id,
            "type": ptype,
            "title": fm.get("title"),
            "path": page.rel_path,
            "lifecycle_stage": fm.get("lifecycle_stage", []),
            "primary_topics": fm.get("primary_topics", []),
            "retrieval_status": fm.get("retrieval_status"),
            # ADR-0001 classification axes: always present (null when undeclared)
            # so the ranker can read promotion_stage and filter by tier.
            "promotion_stage": fm.get("promotion_stage"),
            "implementation_tier": fm.get("implementation_tier"),
        }
        # cross_cutting_topics (ADR-0003) is optional: surface it only when the
        # page declares it, so rows stay clean for the pages that don't.
        if "cross_cutting_topics" in fm:
            row["cross_cutting_topics"] = fm.get("cross_cutting_topics")
        if ptype == "source":
            row["primary_context"] = fm.get("primary_context")
            row["urban_applicability"] = fm.get("urban_applicability")
            row["urban_adaptation_scope"] = fm.get("urban_adaptation_scope")
            row["institutional_credibility"] = fm.get("institutional_credibility")
            row["evidence_quality"] = fm.get("evidence_quality")
            row["composite_authority"] = fm.get("composite_authority")
            row["comparison_readiness"] = fm.get("comparison_readiness")
        result.page_rows.append(row)
        if page_id:
            term_docs.append((page_id, f"{fm.get('title') or ''}\n{page.body}"))

        if ptype == "source":
            for finding in fm.get("findings", []) or []:
                if not isinstance(finding, dict):
                    continue
                candidate_targets = finding.get("candidate_target_pages", []) or []
                result.evidence_rows.append(
                    {
                        "source_id": page_id,
                        "finding_id": finding.get("finding_id"),
                        "finding": finding.get("finding"),
                        "finding_type": finding.get("finding_type"),
                        "knowledge_layer": finding.get("knowledge_layer"),
                        "lifecycle_stage": finding.get("lifecycle_stage"),
                        "source_pages": finding.get("source_pages", []),
                        "candidate_target_pages": candidate_targets,
                        "integration_action": finding.get("integration_action"),
                        "field_query_trigger": finding.get("field_query_trigger"),
                        "status": finding.get("status"),
                        "human_review_required": finding.get("human_review_required"),
                    }
                )

                status_val = str(finding.get("status", "")).strip().lower()
                unsatisfied = unsatisfied_targets(
                    finding.get("integration_action"), candidate_targets, target_exists
                )
                if status_val not in TERMINAL_FINDING_STATUS or unsatisfied:
                    result.routing_pending.append(
                        {
                            "source_id": page_id,
                            "finding_id": finding.get("finding_id"),
                            "status": finding.get("status"),
                            "integration_action": finding.get("integration_action"),
                            "human_review_required": finding.get("human_review_required"),
                            "candidate_target_pages": candidate_targets,
                            "unsatisfied_target_pages": unsatisfied,
                        }
                    )

        for field_name, relation in REL_FIELDS.items():
            for t in edge_targets(field_name, fm.get(field_name)):
                raw_edges.append(
                    {"from": page_id, "relation": relation, "to": t, "source_file": page.rel_path}
                )

    inbound_counts: Dict[str, int] = {pid: 0 for pid in id_to_page.keys()}

    for edge in raw_edges:
        target = edge["to"]
        if target in id_to_page:
            result.valid_edges.append(
                {"from": edge["from"], "relation": edge["relation"], "to": target, "status": "valid"}
            )
            inbound_counts[target] = inbound_counts.get(target, 0) + 1
        else:
            result.unresolved_edges.append(
                {
                    "from": edge["from"],
                    "relation": edge["relation"],
                    "to": target,
                    "status": "unresolved",
                    "reason": "target_id_not_found",
                    "severity": "high",
                    "source_file": edge["source_file"],
                }
            )

    result.inbound_degree = inbound_counts

    # Cross-page validation runs through the graph rule registry (lint_rules.py),
    # peer to the per-page registry. Issues carry their own path.
    graph_ctx = GraphCtx(
        id_to_page=id_to_page,
        inbound_counts=inbound_counts,
        valid_edges=result.valid_edges,
        unresolved_edges=result.unresolved_edges,
        duplicate_ids=duplicate_ids,
    )
    for issue in run_graph_rules(graph_ctx):
        if issue.severity == "critical":
            result.critical.append({"path": issue.path, "error": issue.code})
        else:
            result.warnings.append({"path": issue.path, "warning": issue.code})

    # cited_sources in_wiki resolution needs the full id set, so it runs last.
    for row in result.page_rows:
        if row.get("type") == "source":
            page_obj = id_to_page.get(row["id"])
            if page_obj:
                raw_cited = page_obj.frontmatter.get("cited_sources", []) or []
                cited_out = []
                for entry in raw_cited:
                    if not isinstance(entry, dict):
                        continue
                    wiki_id = entry.get("wiki_id")
                    cited_out.append(
                        {
                            "raw_citation": entry.get("raw_citation"),
                            "wiki_id": wiki_id,
                            "in_wiki": bool(wiki_id and wiki_id in id_to_page),
                        }
                    )
                row["cited_sources"] = cited_out

    result.term_index = build_term_index(term_docs)

    return result
