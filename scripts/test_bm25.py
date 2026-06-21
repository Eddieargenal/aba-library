#!/usr/bin/env python3
"""
test_bm25.py — unit tests for the BM25 retrieval primitives (bm25.py)

Zero dependencies. Run:  python3 scripts/test_bm25.py

These are the lexical primitives the index build precomputes (term index) and the
retrieval ranker (ADR-0002) scores against. Pure stdlib, deterministic.
"""

import unittest

from bm25 import tokenize, build_term_index, bm25_score


class Tokenize(unittest.TestCase):
    def test_lowercases_and_splits_on_nonalnum(self):
        self.assertEqual(tokenize("Hello, World! DRR-2009"), ["hello", "world", "drr", "2009"])

    def test_drops_length_one_tokens(self):
        self.assertEqual(tokenize("a big I/O job"), ["big", "job"])

    def test_empty(self):
        self.assertEqual(tokenize(""), [])


CORPUS = [("A", "the cat sat"), ("B", "the dog ran fast"), ("C", "cat cat dog")]


class BuildTermIndex(unittest.TestCase):
    def setUp(self):
        self.idx = build_term_index(CORPUS)

    def test_doc_count_and_lengths(self):
        self.assertEqual(self.idx["doc_count"], 3)
        self.assertEqual(self.idx["doc_length"], {"A": 3, "B": 4, "C": 3})

    def test_avg_doc_length(self):
        self.assertAlmostEqual(self.idx["avg_doc_length"], 10 / 3)

    def test_postings_count_term_frequency(self):
        self.assertEqual(self.idx["postings"]["cat"], {"A": 1, "C": 2})
        self.assertEqual(self.idx["postings"]["the"], {"A": 1, "B": 1})

    def test_empty_corpus(self):
        idx = build_term_index([])
        self.assertEqual(idx["doc_count"], 0)
        self.assertEqual(idx["avg_doc_length"], 0)
        self.assertEqual(idx["postings"], {})


class Bm25Score(unittest.TestCase):
    def setUp(self):
        self.idx = build_term_index(CORPUS)

    def test_absent_term_scores_zero(self):
        self.assertEqual(bm25_score(self.idx, ["zebra"], "A"), 0.0)

    def test_absent_doc_scores_zero(self):
        self.assertEqual(bm25_score(self.idx, ["cat"], "Z"), 0.0)

    def test_matching_doc_outscores_non_matching(self):
        self.assertGreater(bm25_score(self.idx, ["cat"], "A"), bm25_score(self.idx, ["cat"], "B"))
        self.assertEqual(bm25_score(self.idx, ["cat"], "B"), 0.0)

    def test_more_query_matches_score_higher(self):
        q = ["cat", "dog"]  # C has both, A only cat, B only dog
        self.assertGreater(bm25_score(self.idx, q, "C"), bm25_score(self.idx, q, "A"))
        self.assertGreater(bm25_score(self.idx, q, "C"), bm25_score(self.idx, q, "B"))

    def test_rarer_term_weighs_more(self):
        # in doc B: "fast" (df=1) should outweigh "the" (df=2), same tf and doc length
        self.assertGreater(bm25_score(self.idx, ["fast"], "B"), bm25_score(self.idx, ["the"], "B"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
