"""
lint_rules.py — per-page validation rules over the data model (schema.py)

Each rule is a pure function `rule(ctx: RuleCtx) -> list[Issue]`. `build-index.py`
runs `run_rules()` for every page and routes the issues into its critical/warning
lists. Because the rules are pure and importable, each one is a unit-test surface
(see test_lint.py) — the internal seam this module exists to provide.

Scope: per-page validation only. Cross-page checks (duplicate id, orphan pages,
ghost-node edges, deprecated-target links) need the full page set and stay in
build-index.py; modelling them as per-page rules would force a fake interface.
"""

from dataclasses import dataclass
from typing import Callable, List, Optional

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
