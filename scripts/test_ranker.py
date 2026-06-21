#!/usr/bin/env python3
"""
test_ranker.py — behavior tests for the retrieval ranker (ranker.py)

Zero dependencies. Run:  python3 scripts/test_ranker.py

Exercises rank() through its public interface: a structured query + an in-memory
index -> a RankResult. No filesystem. Pipeline + contract per ADR-0002/0004.
"""

import unittest
from pathlib import Path

import ranker
from bm25 import build_term_index
from ranker import rank


def row(rid, type="concept", title="", promotion_stage=None, implementation_tier=None,
        lifecycle_stage=None, retrieval_status="usable", path=None):
    return {
        "id": rid, "type": type, "title": title, "path": path or f"{rid}.md",
        "promotion_stage": promotion_stage, "implementation_tier": implementation_tier,
        "lifecycle_stage": lifecycle_stage or [], "retrieval_status": retrieval_status,
    }


def index(pages, term_index=None, degree=None, edges=None):
    return {
        "pages": pages,
        "term_index": term_index or build_term_index([]),
        "degree": degree or {},
        "edges": edges or [],
    }


def ids(result):
    return {c["id"] for c in result.candidates}


class CandidateUniverseAndGate(unittest.TestCase):
    def test_only_ladder_pages_that_pass_the_gate(self):
        pages = [
            row("F-1", "framework", promotion_stage="framework", retrieval_status="usable"),
            row("C-ok", "concept", promotion_stage="concept", retrieval_status="limited"),
            row("S-1", "source", promotion_stage=None, retrieval_status="usable"),       # no stage
            row("C-dep", "concept", promotion_stage="concept", retrieval_status="deprecated"),
            row("C-draft", "concept", promotion_stage="concept", retrieval_status="draft"),
        ]
        result = rank({}, index(pages))
        self.assertEqual(ids(result), {"F-1", "C-ok"})


class FacetFilter(unittest.TestCase):
    def setUp(self):
        self.pages = [
            row("C-a", promotion_stage="concept", lifecycle_stage=["area-selection"], implementation_tier="synthesis"),
            row("C-b", promotion_stage="concept", lifecycle_stage=["monitoring-learning"], implementation_tier="design"),
            row("C-c", promotion_stage="concept", lifecycle_stage=["area-selection", "monitoring-learning"], implementation_tier="all"),
        ]

    def test_no_facets_returns_all(self):
        self.assertEqual(ids(rank({}, index(self.pages))), {"C-a", "C-b", "C-c"})

    def test_lifecycle_intersection(self):
        r = rank({"lifecycle_stage": "area-selection"}, index(self.pages))
        self.assertEqual(ids(r), {"C-a", "C-c"})

    def test_tier_all_matches_any_requested_tier(self):
        r = rank({"implementation_tier": "synthesis"}, index(self.pages))
        self.assertEqual(ids(r), {"C-a", "C-c"})  # C-c is 'all'

    def test_facets_are_anded(self):
        r = rank({"lifecycle_stage": "area-selection", "implementation_tier": "design"}, index(self.pages))
        self.assertEqual(ids(r), {"C-c"})  # area-selection AND (design or all)


def order(result):
    return [c["id"] for c in result.candidates]


class Ordering(unittest.TestCase):
    def test_promotion_stage_is_primary_desc(self):
        pages = [
            row("C-fi", promotion_stage="finding"),
            row("T-to", promotion_stage="tool"),
            row("C-co", promotion_stage="concept"),
            row("F-fr", promotion_stage="framework"),
        ]
        self.assertEqual(order(rank({}, index(pages))), ["T-to", "F-fr", "C-co", "C-fi"])

    def test_bm25_breaks_ties_within_a_stage(self):
        pages = [row("C-1", promotion_stage="concept"), row("C-2", promotion_stage="concept")]
        ti = build_term_index([("C-1", "flood flood"), ("C-2", "drought")])
        r = rank({"text": "flood"}, index(pages, term_index=ti))
        self.assertEqual(order(r)[0], "C-1")
        self.assertGreater(r.candidates[0]["bm25_score"], 0)

    def test_degree_is_final_tiebreaker(self):
        pages = [row("C-a", promotion_stage="concept"), row("C-b", promotion_stage="concept")]
        r = rank({}, index(pages, degree={"C-a": 5, "C-b": 1}))
        self.assertEqual(order(r), ["C-a", "C-b"])


class TopK(unittest.TestCase):
    def setUp(self):
        self.pages = [row(f"C-{i}", promotion_stage="concept") for i in range(1, 6)]
        self.deg = {f"C-{i}": 6 - i for i in range(1, 6)}  # C-1 highest degree

    def test_k_limits_results(self):
        r = rank({"k": 2}, index(self.pages, degree=self.deg))
        self.assertEqual(order(r), ["C-1", "C-2"])

    def test_omitted_k_returns_all(self):
        self.assertEqual(len(rank({}, index(self.pages, degree=self.deg)).candidates), 5)


class Expansion(unittest.TestCase):
    def test_expands_contradicts_and_known_tension_with_provenance(self):
        pages = [
            row("C-x", promotion_stage="concept", title="X"),
            row("C-y", promotion_stage="concept", title="Why"),
        ]
        edges = [
            {"from": "C-x", "relation": "contradicts", "to": "C-y"},
            {"from": "C-x", "relation": "known_tension", "to": "C-y"},
            {"from": "C-x", "relation": "related_concept", "to": "C-y"},  # not an expansion relation
        ]
        exp = rank({}, index(pages, edges=edges)).expansion
        self.assertEqual(
            exp,
            [
                {"from": "C-x", "relation": "contradicts", "to": "C-y", "to_title": "Why"},
                {"from": "C-x", "relation": "known_tension", "to": "C-y", "to_title": "Why"},
            ],
        )

    def test_no_expansion_for_filtered_out_pages(self):
        pages = [row("C-dep", promotion_stage="concept", retrieval_status="deprecated", title="Dep")]
        edges = [{"from": "C-dep", "relation": "contradicts", "to": "C-y"}]
        self.assertEqual(rank({}, index(pages, edges=edges)).expansion, [])


class LoadIndex(unittest.TestCase):
    IDX = Path(__file__).resolve().parents[1] / "indexes" / "current"

    def test_loads_published_index_into_the_rank_shape(self):
        idx = ranker.load_index(self.IDX)
        self.assertIsInstance(idx["pages"], list)
        self.assertTrue(idx["pages"])
        self.assertIn("doc_count", idx["term_index"])
        self.assertTrue(all(isinstance(v, int) for v in idx["degree"].values()))
        self.assertIsInstance(idx["edges"], list)

    def test_rank_runs_end_to_end_on_published_index(self):
        r = rank({}, ranker.load_index(self.IDX))
        self.assertIsInstance(r.candidates, list)  # may be empty, must not error


if __name__ == "__main__":
    unittest.main(verbosity=2)
