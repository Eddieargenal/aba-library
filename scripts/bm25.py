"""
bm25.py — lexical retrieval primitives (pure stdlib, no pip)

The index build precomputes a term index (build_term_index); the retrieval
ranker (ADR-0002) scores candidate pages against a query with bm25_score. BM25 is
an intra-tier tiebreaker, so this stays small and deterministic, and works in
every runtime mode including no_llm.
"""

import math
import re
from typing import Any, Dict, Iterable, List, Tuple

_TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> List[str]:
    """Lowercase, split on non-alphanumeric, drop single-character tokens."""
    return [t for t in _TOKEN_RE.findall((text or "").lower()) if len(t) > 1]


def build_term_index(docs: Iterable[Tuple[str, str]]) -> Dict[str, Any]:
    """Compile (doc_id, text) pairs into a deterministic BM25 term index:
    per-doc lengths, the corpus average length, and postings (term -> {doc_id:
    term_frequency}). Document frequency per term is len(postings[term])."""
    doc_length: Dict[str, int] = {}
    postings: Dict[str, Dict[str, int]] = {}

    for doc_id, text in docs:
        toks = tokenize(text)
        doc_length[doc_id] = len(toks)
        for tok in toks:
            postings.setdefault(tok, {})
            postings[tok][doc_id] = postings[tok].get(doc_id, 0) + 1

    doc_count = len(doc_length)
    total = sum(doc_length.values())
    avg = total / doc_count if doc_count else 0
    # sort for deterministic serialization
    postings = {t: dict(sorted(postings[t].items())) for t in sorted(postings)}
    return {
        "doc_count": doc_count,
        "avg_doc_length": avg,
        "doc_length": dict(sorted(doc_length.items())),
        "postings": postings,
    }


def bm25_score(
    term_index: Dict[str, Any],
    query_terms: List[str],
    doc_id: str,
    k1: float = 1.5,
    b: float = 0.75,
) -> float:
    """Okapi BM25 score of doc_id against query_terms, using a precomputed
    term_index. Terms absent from the index (or the doc) contribute nothing;
    rarer terms (lower document frequency) weigh more via IDF."""
    n = term_index.get("doc_count", 0)
    avgdl = term_index.get("avg_doc_length", 0)
    if not n or not avgdl:
        return 0.0
    postings = term_index.get("postings", {})
    dl = term_index.get("doc_length", {}).get(doc_id, 0)

    score = 0.0
    for term in query_terms:
        plist = postings.get(str(term).strip().lower())
        if not plist:
            continue
        tf = plist.get(doc_id, 0)
        if not tf:
            continue
        df = len(plist)
        idf = math.log(1 + (n - df + 0.5) / (df + 0.5))
        denom = tf + k1 * (1 - b + b * dl / avgdl)
        score += idf * (tf * (k1 + 1)) / denom
    return score
