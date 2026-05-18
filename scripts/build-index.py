#!/usr/bin/env python3
"""
build-index.py — v2.6 index compiler

Compiles markdown/frontmatter into deterministic JSONL indexes.
Publishes atomically to indexes/current only when critical lint errors are zero.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

VAULT = Path(__file__).resolve().parents[1]
WIKI_ROOT = VAULT / "wiki" / "aba"
INDEXES_DIR = VAULT / "indexes"
BUILDS_DIR = INDEXES_DIR / "builds"
CURRENT_DIR = INDEXES_DIR / "current"

REL_FIELDS = {
    "related_concepts": "related_concept",
    "related_frameworks": "related_framework",
    "related_tools": "related_tool",
    "related_risks": "related_risk",
    "source_basis": "source_basis",
    "known_tensions": "known_tension",
    "contradicts": "contradicts",
    "used_by_playbooks": "used_by_playbook",
    "output_templates": "output_template",
    "requires_concepts": "requires_concept",
    "parent_frameworks": "parent_framework",
    "required_inputs": "requires_input",
    "compatible_instruments": "compatible_instrument",
    "mitigated_by": "mitigated_by",
    "risk_applies_to": "risk_applies_to",
    "escalation_triggers": "escalation_trigger",
}

STRICT_REQUIRED = ["id", "type", "title", "retrieval_status"]
LIFECYCLE_REQUIRED_TYPES = {
    "source",
    "concept",
    "framework",
    "tool",
    "field-instrument",
    "risk",
    "advisory-playbook",
    "decision-protocol",
    "output-template",
}


@dataclass
class Page:
    path: Path
    rel_path: str
    frontmatter: Dict[str, Any]
    body: str


def now_build_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")


def scan_pages() -> List[Page]:
    pages: List[Page] = []
    for path in sorted(WIKI_ROOT.rglob("*.md")):
        rel = path.relative_to(WIKI_ROOT).as_posix()
        if rel.startswith("01-sources/raw-content/") or rel.startswith("01-sources/raw/"):
            continue
        if path.name.startswith("00_"):
            continue
        text = path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
        if not m:
            pages.append(Page(path=path, rel_path=rel, frontmatter={}, body=text))
            continue
        try:
            fm = parse_yaml(m.group(1))
        except Exception:
            fm = {"_yaml_error": True}
        body = text[m.end() :]
        pages.append(Page(path=path, rel_path=rel, frontmatter=fm, body=body))
    return pages


def parse_yaml(text: str) -> Dict[str, Any]:
    """
    Parse YAML frontmatter without Python third-party dependencies.
    Uses Ruby stdlib YAML + JSON bridge available by default on macOS.
    """
    cmd = [
        "ruby",
        "-rdate",
        "-ryaml",
        "-rjson",
        "-e",
        "obj = YAML.safe_load(STDIN.read, permitted_classes: [Date, Time], aliases: true); puts(JSON.generate(obj || {}))",
    ]
    proc = subprocess.run(
        cmd,
        input=text,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise ValueError(proc.stderr.strip() or "YAML parse failed")
    parsed = json.loads(proc.stdout or "{}")
    if not isinstance(parsed, dict):
        return {}
    return parsed


def normalize_source_id(source_id: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9-]+", "-", source_id).strip("-")
    return f"S-{slug}"


def section_line_ranges(body: str, sections: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[str]]:
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


def edge_targets(field: str, value: Any) -> List[str]:
    if value is None:
        return []
    if field == "source_basis":
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


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: List[Dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Fail build publication when warnings exist")
    args = parser.parse_args()

    build_id = now_build_id()
    build_dir = BUILDS_DIR / build_id
    build_dir.mkdir(parents=True, exist_ok=True)

    pages = scan_pages()
    critical: List[Dict[str, Any]] = []
    warnings: List[Dict[str, Any]] = []

    page_rows: List[Dict[str, Any]] = []
    section_rows: List[Dict[str, Any]] = []
    evidence_rows: List[Dict[str, Any]] = []
    raw_edges: List[Dict[str, Any]] = []

    id_to_page: Dict[str, Page] = {}
    duplicate_ids = set()

    for page in pages:
        fm = page.frontmatter
        if fm.get("_yaml_error"):
            critical.append({"path": page.rel_path, "error": "invalid_yaml_frontmatter"})
            continue

        if not fm:
            warnings.append({"path": page.rel_path, "warning": "missing_frontmatter"})
            continue

        page_id = fm.get("id")
        if not page_id and fm.get("type") == "source" and fm.get("source_id"):
            page_id = normalize_source_id(str(fm.get("source_id")))
            warnings.append({"path": page.rel_path, "warning": f"derived_source_id:{page_id}"})

        if fm.get("type") == "source" and not fm.get("retrieval_status"):
            source_status = str(fm.get("status", "")).strip()
            fm["retrieval_status"] = "usable" if source_status in {"ingested", "reviewed"} else "limited"
            warnings.append(
                {
                    "path": page.rel_path,
                    "warning": f"derived_retrieval_status:{fm['retrieval_status']}",
                }
            )

        for field in STRICT_REQUIRED:
            if field == "id":
                if not page_id:
                    critical.append({"path": page.rel_path, "error": "missing_id"})
                continue
            if fm.get(field) in (None, "", []):
                critical.append({"path": page.rel_path, "error": f"missing_{field}"})

        ptype = str(fm.get("type", "")).strip()
        if ptype in LIFECYCLE_REQUIRED_TYPES and not fm.get("lifecycle_stage"):
            critical.append({"path": page.rel_path, "error": "missing_lifecycle_stage"})

        if page_id:
            if page_id in id_to_page:
                duplicate_ids.add(page_id)
            else:
                id_to_page[page_id] = page

        sections = fm.get("sections", [])
        if not sections:
            warnings.append({"path": page.rel_path, "warning": "missing_sections"})
        elif isinstance(sections, list):
            ranges, sec_warn = section_line_ranges(page.body, sections)
            for w in sec_warn:
                critical.append({"path": page.rel_path, "error": f"section_error:{w}"})
            for sec in ranges:
                section_rows.append(
                    {
                        "page_id": page_id,
                        "section_id": sec["section_id"],
                        "path": page.rel_path,
                        "start_line": sec["start_line"],
                        "end_line": sec["end_line"],
                    }
                )
        else:
            critical.append({"path": page.rel_path, "error": "sections_not_list"})

        row = {
            "id": page_id,
            "type": ptype,
            "title": fm.get("title"),
            "path": page.rel_path,
            "lifecycle_stage": fm.get("lifecycle_stage", []),
            "primary_topics": fm.get("primary_topics", []),
            "retrieval_status": fm.get("retrieval_status"),
        }
        page_rows.append(row)

        if ptype == "source":
            for finding in fm.get("findings", []) or []:
                if not isinstance(finding, dict):
                    continue
                evidence_rows.append(
                    {
                        "source_id": page_id,
                        "finding_id": finding.get("finding_id"),
                        "finding": finding.get("finding"),
                        "finding_type": finding.get("finding_type"),
                        "lifecycle_stage": finding.get("lifecycle_stage"),
                        "source_pages": finding.get("source_pages", []),
                        "candidate_target_pages": finding.get("candidate_target_pages", []),
                        "integration_action": finding.get("integration_action"),
                        "status": finding.get("status"),
                    }
                )

        for field, relation in REL_FIELDS.items():
            targets = edge_targets(field, fm.get(field))
            for t in targets:
                raw_edges.append({"from": page_id, "relation": relation, "to": t, "source_file": page.rel_path})

    for dup in sorted(duplicate_ids):
        critical.append({"path": id_to_page[dup].rel_path, "error": f"duplicate_id:{dup}"})

    valid_edges: List[Dict[str, Any]] = []
    unresolved_edges: List[Dict[str, Any]] = []
    inbound_counts: Dict[str, int] = {pid: 0 for pid in id_to_page.keys()}

    for edge in raw_edges:
        target = edge["to"]
        if target in id_to_page:
            valid_edges.append({"from": edge["from"], "relation": edge["relation"], "to": target, "status": "valid"})
            inbound_counts[target] = inbound_counts.get(target, 0) + 1
        else:
            unresolved_edges.append(
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

    for pid, count in inbound_counts.items():
        if count == 0:
            p = id_to_page.get(pid)
            if p:
                warnings.append({"path": p.rel_path, "warning": f"orphan_page:{pid}"})

    if unresolved_edges:
        for edge in unresolved_edges:
            critical.append({"path": edge["source_file"], "error": f"unresolved_edge:{edge['to']}"})

    status = "valid"
    if critical:
        status = "invalid"
    elif warnings:
        status = "valid_with_warnings"

    manifest = {
        "build_id": build_id,
        "build_status": status,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "page_count": len(page_rows),
        "edge_count": len(valid_edges),
        "unresolved_edge_count": len(unresolved_edges),
        "critical_error_count": len(critical),
        "warning_count": len(warnings),
        "active": False,
    }

    lint_report = {
        "build_id": build_id,
        "critical_errors": critical,
        "warnings": warnings,
    }

    write_json(build_dir / "manifest.json", manifest)
    write_jsonl(build_dir / "agent-index.jsonl", page_rows)
    write_jsonl(build_dir / "graph-edges.jsonl", valid_edges)
    write_jsonl(build_dir / "unresolved-edges.jsonl", unresolved_edges)
    write_jsonl(build_dir / "section-index.jsonl", section_rows)
    write_jsonl(build_dir / "source-evidence-index.jsonl", evidence_rows)
    write_json(build_dir / "lint-report.json", lint_report)

    publish_allowed = len(critical) == 0 and (not args.strict or len(warnings) == 0)
    if publish_allowed:
        temp_current = INDEXES_DIR / f".current-{build_id}"
        temp_current.mkdir(parents=True, exist_ok=True)
        for name in [
            "manifest.json",
            "agent-index.jsonl",
            "graph-edges.jsonl",
            "unresolved-edges.jsonl",
            "section-index.jsonl",
            "source-evidence-index.jsonl",
            "lint-report.json",
        ]:
            shutil.copy2(build_dir / name, temp_current / name)

        if CURRENT_DIR.exists():
            shutil.rmtree(CURRENT_DIR)
        os.replace(temp_current, CURRENT_DIR)

        manifest["active"] = True
        write_json(build_dir / "manifest.json", manifest)
        write_json(CURRENT_DIR / "manifest.json", manifest)

    print(json.dumps({
        "build_id": build_id,
        "status": status,
        "published": publish_allowed,
        "critical_error_count": len(critical),
        "warning_count": len(warnings),
    }))
    return 0 if publish_allowed else 2


if __name__ == "__main__":
    raise SystemExit(main())
