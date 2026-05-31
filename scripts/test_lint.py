#!/usr/bin/env python3
"""
test_lint.py — unit tests for the per-page lint rules (lint_rules.py)

Zero dependencies. Run:  python3 scripts/test_lint.py
The rule registry is the test surface this exists to exercise — each rule is
checked in isolation with a tiny in-memory page.
"""

import unittest

from lint_rules import (
    RuleCtx,
    rule_id_prefix,
    rule_lifecycle_required,
    rule_lifecycle_vocab,
    rule_primary_topics,
    rule_required_fields,
    rule_retrieval_status_vocab,
    rule_source_basis_usable,
    rule_tool_related_risks,
    run_rules,
)


def ctx(fm=None, page_id="C-x", ptype="concept", rel_path="p.md"):
    return RuleCtx(rel_path=rel_path, fm=fm or {}, page_id=page_id, ptype=ptype)


def codes(issues):
    return [i.code for i in issues]


class RequiredFields(unittest.TestCase):
    def test_missing_id(self):
        self.assertIn("missing_id", codes(rule_required_fields(ctx(page_id=None))))

    def test_missing_title(self):
        c = ctx(fm={"type": "concept", "retrieval_status": "usable"})  # no title
        self.assertIn("missing_title", codes(rule_required_fields(c)))

    def test_complete_is_clean(self):
        c = ctx(fm={"type": "concept", "title": "T", "retrieval_status": "usable"})
        self.assertEqual(codes(rule_required_fields(c)), [])


class Vocab(unittest.TestCase):
    def test_invalid_retrieval_status(self):
        c = ctx(fm={"retrieval_status": "usabel"})
        self.assertEqual(codes(rule_retrieval_status_vocab(c)), ["invalid_retrieval_status:usabel"])

    def test_valid_retrieval_status(self):
        self.assertEqual(rule_retrieval_status_vocab(ctx(fm={"retrieval_status": "draft"})), [])

    def test_invalid_lifecycle_value(self):
        c = ctx(fm={"lifecycle_stage": ["neighbourhood-diagnosis", "response-design"]})
        self.assertEqual(codes(rule_lifecycle_vocab(c)), ["invalid_lifecycle_stage:response-design"])

    def test_lifecycle_required_missing(self):
        c = ctx(fm={"type": "concept"}, ptype="concept")
        self.assertEqual(codes(rule_lifecycle_required(c)), ["missing_lifecycle_stage"])


class SourceBasis(unittest.TestCase):
    def test_usable_concept_without_basis_is_critical(self):
        c = ctx(fm={"retrieval_status": "usable", "source_basis": []}, ptype="concept")
        self.assertEqual(codes(rule_source_basis_usable(c)), ["missing_source_basis_usable"])

    def test_usable_concept_with_basis_is_clean(self):
        c = ctx(fm={"retrieval_status": "usable", "source_basis": ["S-x"]}, ptype="concept")
        self.assertEqual(rule_source_basis_usable(c), [])

    def test_source_page_is_exempt(self):
        # sources provide evidence; they are not "technical" pages and need no source_basis
        c = ctx(fm={"retrieval_status": "usable", "source_basis": []}, ptype="source", page_id="S-x")
        self.assertEqual(rule_source_basis_usable(c), [])

    def test_draft_concept_is_exempt(self):
        c = ctx(fm={"retrieval_status": "draft", "source_basis": []}, ptype="concept")
        self.assertEqual(rule_source_basis_usable(c), [])


class Prefix(unittest.TestCase):
    def test_mismatch(self):
        c = ctx(page_id="T-foo", ptype="concept")
        self.assertEqual(len(rule_id_prefix(c)), 1)

    def test_match(self):
        self.assertEqual(rule_id_prefix(ctx(page_id="C-foo", ptype="concept")), [])


class ToolRisksAndTopics(unittest.TestCase):
    def test_usable_tool_without_risks(self):
        c = ctx(fm={"retrieval_status": "usable", "related_risks": []}, ptype="tool", page_id="T-x")
        self.assertEqual(codes(rule_tool_related_risks(c)), ["tool_missing_related_risks"])

    def test_tool_with_risks_clean(self):
        c = ctx(fm={"retrieval_status": "usable", "related_risks": ["R-x"]}, ptype="tool", page_id="T-x")
        self.assertEqual(rule_tool_related_risks(c), [])

    def test_excessive_topics(self):
        c = ctx(fm={"primary_topics": list("abcdefg")})  # 7 > 6
        self.assertEqual(codes(rule_primary_topics(c)), ["excessive_primary_topics:7"])

    def test_topics_at_limit_clean(self):
        c = ctx(fm={"primary_topics": list("abcdef")})  # 6
        self.assertEqual(rule_primary_topics(c), [])


class Registry(unittest.TestCase):
    def test_run_rules_aggregates(self):
        # a usable concept missing title, lifecycle, and source_basis trips three criticals
        c = ctx(fm={"type": "concept", "retrieval_status": "usable", "source_basis": []},
                ptype="concept", page_id="C-x")
        got = codes(run_rules(c))
        for expected in ("missing_title", "missing_lifecycle_stage", "missing_source_basis_usable"):
            self.assertIn(expected, got)


if __name__ == "__main__":
    unittest.main(verbosity=2)
