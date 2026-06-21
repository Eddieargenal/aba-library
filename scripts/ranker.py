"""
ranker.py — retrieval ranker for the synthesis tier (ADR-0002 / ADR-0004)

Pure core `rank(query, index) -> RankResult` plus a thin `load_index(dir)` loader
(mirrors the compiler: pure logic, I/O at the edge). Deterministic, zero-pip,
works in every runtime mode.

Pipeline: filter (lifecycle_stage ∩ implementation_tier) -> gate
(retrieval_status ∈ {usable, limited}) -> order (promotion_stage -> BM25 ->
graph-degree) -> expand (contradicts/known_tension) -> candidate + expansion sets.
"""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List

from schema import PROMOTION_STAGE_ORDER
from bm25 import bm25_score, tokenize

GATE = {"usable", "limited"}
EXPANSION_RELATIONS = {"contradicts", "known_tension"}


@dataclass
class RankResult:
    candidates: List[Dict[str, Any]] = field(default_factory=list)
    expansion: List[Dict[str, Any]] = field(default_factory=list)


def _read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_index(index_dir) -> Dict[str, Any]:
    """Load a published index directory into the in-memory shape rank() expects.
    The I/O edge of the ranker; rank() itself stays pure."""
    d = Path(index_dir)
    term_path = d / "term-index.json"
    term_index = json.loads(term_path.read_text(encoding="utf-8")) if term_path.exists() else {}
    degree = {r["id"]: r["inbound_degree"] for r in _read_jsonl(d / "graph-degree.jsonl")}
    return {
        "pages": _read_jsonl(d / "agent-index.jsonl"),
        "term_index": term_index,
        "degree": degree,
        "edges": _read_jsonl(d / "graph-edges.jsonl"),
    }


def rank(query: Dict[str, Any], index: Dict[str, Any]) -> RankResult:
    pages = index.get("pages", [])

    # Candidate universe: ladder pages (have a promotion_stage) that pass the gate.
    candidates = [
        p for p in pages
        if p.get("promotion_stage") and p.get("retrieval_status") in GATE
    ]

    # Facet filters (omitted facet imposes no constraint).
    q_life = query.get("lifecycle_stage")
    if q_life:
        wanted = {q_life} if isinstance(q_life, str) else set(q_life)
        candidates = [p for p in candidates if wanted & set(p.get("lifecycle_stage") or [])]

    q_tier = query.get("implementation_tier")
    if q_tier:
        candidates = [
            p for p in candidates
            if p.get("implementation_tier") == q_tier or p.get("implementation_tier") == "all"
        ]

    # Score: promotion_stage ordinal (primary), BM25 (tiebreaker), degree (final).
    term_index = index.get("term_index", {})
    degree = index.get("degree", {})
    q_terms = tokenize(query.get("text", "")) if query.get("text") else []

    scored = []
    for p in candidates:
        pid = p.get("id")
        stage = p.get("promotion_stage")
        ordinal = PROMOTION_STAGE_ORDER.index(stage) if stage in PROMOTION_STAGE_ORDER else -1
        b = bm25_score(term_index, q_terms, pid) if q_terms else 0.0
        d = degree.get(pid, 0)
        scored.append((ordinal, b, d, p))

    scored.sort(key=lambda t: (t[0], t[1], t[2]), reverse=True)

    k = query.get("k")
    if k:
        scored = scored[:k]

    result = RankResult()
    for ordinal, b, d, p in scored:
        result.candidates.append(
            {
                "id": p.get("id"),
                "title": p.get("title"),
                "type": p.get("type"),
                "path": p.get("path"),
                "promotion_stage": p.get("promotion_stage"),
                "bm25_score": b,
                "inbound_degree": d,
            }
        )

    # Expansion: follow contradicts/known_tension edges out of each ranked
    # candidate (in candidate order), carrying provenance + the target's title.
    title_by_id = {p.get("id"): p.get("title") for p in pages}
    edges = index.get("edges", [])
    for cand in result.candidates:
        for edge in edges:
            if edge.get("from") == cand["id"] and edge.get("relation") in EXPANSION_RELATIONS:
                result.expansion.append(
                    {
                        "from": edge["from"],
                        "relation": edge["relation"],
                        "to": edge.get("to"),
                        "to_title": title_by_id.get(edge.get("to")),
                    }
                )

    return result
