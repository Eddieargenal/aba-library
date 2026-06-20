"""
lint_rules.py — per-page validation rules over the data model (schema.py)

Each rule is a pure function `rule(ctx: RuleCtx) -> list[Issue]`. `build-index.py`
runs `run_rules()` for every page and routes the issues into its critical/warning
lists. Because the rules are pure and importable, each one is a unit-test surface
(see test_lint.py) — the internal seam this module exists to provide.

Two registries, two contexts:
  - per-page  : rule(RuleCtx)  -> [Issue]   run via run_rules()
  - cross-page: rule(GraphCtx) -> [Issue]   run via run_graph_rules()

Graph rules (duplicate id, orphan pages, ghost-node edges, deprecated-target
links) need the full page set and the resolved edges, so they take a GraphCtx
rather than being bent into the per-page shape. compile_index.py builds both
contexts and routes the Issues into its critical/warning ledgers.
"""

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Set

from schema import (
    ID_PREFIX_BY_TYPE,
    LIFECYCLE_REQUIRED_TYPES,
    LIFECYCLE_VOCAB,
    MAX_PRIMARY_TOPICS,
    RETRIEVAL_STATUS_VOCAB,
    STRICT_REQUIRED,
    TECHNICAL_TYPES,
)

CRITICAL = "critical"
WARNING = "warning"


@dataclass
class Issue:
    severity: str  # CRITICAL | WARNING
    code: str
    # Per-page rules leave path None (build attaches the page's path); graph
    # rules set it, because each cross-page issue names a different page.
    path: Optional[str] = None


@dataclass
class RuleCtx:
    """Everything a per-page rule needs. `fm` is post-derivation frontmatter
    (page_id and source retrieval_status already resolved by build-index.py)."""
    rel_path: str
    fm: dict
    page_id: Optional[str]
    ptype: str

    @property
    def rs_val(self) -> str:
        rs = self.fm.get("retrieval_status")
        return str(rs).strip() if rs is not None else ""


def rule_required_fields(ctx: RuleCtx) -> List[Issue]:
    issues: List[Issue] = []
    for field in STRICT_REQUIRED:
        if field == "id":
            if not ctx.page_id:
                issues.append(Issue(CRITICAL, "missing_id"))
            continue
        if ctx.fm.get(field) in (None, "", []):
            issues.append(Issue(CRITICAL, f"missing_{field}"))
    return issues


def rule_lifecycle_required(ctx: RuleCtx) -> List[Issue]:
    if ctx.ptype in LIFECYCLE_REQUIRED_TYPES and not ctx.fm.get("lifecycle_stage"):
        return [Issue(CRITICAL, "missing_lifecycle_stage")]
    return []


def rule_retrieval_status_vocab(ctx: RuleCtx) -> List[Issue]:
    if ctx.rs_val and ctx.rs_val not in RETRIEVAL_STATUS_VOCAB:
        return [Issue(CRITICAL, f"invalid_retrieval_status:{ctx.rs_val}")]
    return []


def rule_source_basis_usable(ctx: RuleCtx) -> List[Issue]:
    if ctx.ptype in TECHNICAL_TYPES and ctx.rs_val == "usable" and not ctx.fm.get("source_basis"):
        return [Issue(CRITICAL, "missing_source_basis_usable")]
    return []


def rule_lifecycle_vocab(ctx: RuleCtx) -> List[Issue]:
    issues: List[Issue] = []
    ls = ctx.fm.get("lifecycle_stage") or []
    if isinstance(ls, list):
        for v in ls:
            vv = str(v).strip()
            if vv and vv not in LIFECYCLE_VOCAB:
                issues.append(Issue(WARNING, f"invalid_lifecycle_stage:{vv}"))
    return issues


def rule_id_prefix(ctx: RuleCtx) -> List[Issue]:
    expected = ID_PREFIX_BY_TYPE.get(ctx.ptype)
    if ctx.page_id and expected and not str(ctx.page_id).startswith(expected):
        return [Issue(WARNING, f"id_prefix_mismatch:{ctx.page_id}:expected:{expected}")]
    return []


def rule_tool_related_risks(ctx: RuleCtx) -> List[Issue]:
    if ctx.ptype == "tool" and ctx.rs_val == "usable" and not ctx.fm.get("related_risks"):
        return [Issue(WARNING, "tool_missing_related_risks")]
    return []


def rule_primary_topics(ctx: RuleCtx) -> List[Issue]:
    pt = ctx.fm.get("primary_topics") or []
    if isinstance(pt, list) and len(pt) > MAX_PRIMARY_TOPICS:
        return [Issue(WARNING, f"excessive_primary_topics:{len(pt)}")]
    return []


# --- Cross-page (graph) rules ------------------------------------------------


@dataclass
class GraphCtx:
    """Everything a cross-page rule needs: the resolved id set, inbound-edge
    counts, the valid/unresolved edges, and the ids seen more than once. Pages
    are duck-typed (.rel_path, .frontmatter) to avoid importing compile_index."""
    id_to_page: Dict[str, Any]
    inbound_counts: Dict[str, int]
    valid_edges: List[dict]
    unresolved_edges: List[dict]
    duplicate_ids: Set[str]


ACTIVE_LINKER_TYPES = {"advisory-playbook", "decision-protocol"}


def rule_duplicate_ids(ctx: GraphCtx) -> List[Issue]:
    return [
        Issue(CRITICAL, f"duplicate_id:{dup}", path=ctx.id_to_page[dup].rel_path)
        for dup in sorted(ctx.duplicate_ids)
    ]


def rule_orphan_pages(ctx: GraphCtx) -> List[Issue]:
    issues: List[Issue] = []
    for pid, count in ctx.inbound_counts.items():
        if count == 0:
            page = ctx.id_to_page.get(pid)
            if page:
                issues.append(Issue(WARNING, f"orphan_page:{pid}", path=page.rel_path))
    return issues


def rule_ghost_nodes(ctx: GraphCtx) -> List[Issue]:
    return [
        Issue(WARNING, f"ghost_node:{edge['to']}", path=edge["source_file"])
        for edge in ctx.unresolved_edges
    ]


def rule_deprecated_target_linked(ctx: GraphCtx) -> List[Issue]:
    deprecated_ids = {
        pid
        for pid, pg in ctx.id_to_page.items()
        if str(pg.frontmatter.get("retrieval_status", "")).strip() == "deprecated"
    }
    issues: List[Issue] = []
    for edge in ctx.valid_edges:
        if edge["to"] in deprecated_ids:
            from_pg = ctx.id_to_page.get(edge["from"])
            if from_pg:
                ftype = str(from_pg.frontmatter.get("type", "")).strip()
                fstatus = str(from_pg.frontmatter.get("retrieval_status", "")).strip()
                if ftype in ACTIVE_LINKER_TYPES and fstatus != "deprecated":
                    issues.append(
                        Issue(WARNING, f"deprecated_target_linked:{edge['to']}", path=from_pg.rel_path)
                    )
    return issues


# Order matters: criticals (duplicate) then warnings (orphan, ghost, deprecated)
# so the routed ledgers stay position-stable against the original build.
GRAPH_RULES: List[Callable[[GraphCtx], List[Issue]]] = [
    rule_duplicate_ids,
    rule_orphan_pages,
    rule_ghost_nodes,
    rule_deprecated_target_linked,
]


def run_graph_rules(ctx: GraphCtx) -> List[Issue]:
    out: List[Issue] = []
    for rule in GRAPH_RULES:
        out.extend(rule(ctx))
    return out


RULES: List[Callable[[RuleCtx], List[Issue]]] = [
    rule_required_fields,
    rule_lifecycle_required,
    rule_retrieval_status_vocab,
    rule_source_basis_usable,
    rule_lifecycle_vocab,
    rule_id_prefix,
    rule_tool_related_risks,
    rule_primary_topics,
]


def run_rules(ctx: RuleCtx) -> List[Issue]:
    out: List[Issue] = []
    for rule in RULES:
        out.extend(rule(ctx))
    return out
