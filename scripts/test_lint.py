#!/usr/bin/env python3
"""
test_lint.py — unit tests for the per-page lint rules (lint_rules.py)

Zero dependencies. Run:  python3 scripts/test_lint.py
The rule registry is the test surface this exists to exercise — each rule is
checked in isolation with a tiny in-memory page.
"""

import unittest
from datetime import date

from lint_rules import (
    GraphCtx,
    RuleCtx,
    rule_deprecated_target_linked,
    rule_duplicate_ids,
    rule_finding_target_folder,
    rule_ghost_nodes,
    rule_id_prefix,
    rule_lifecycle_required,
    rule_lifecycle_vocab,
    rule_orphan_pages,
    rule_primary_topics,
    rule_cross_cutting_topics_vocab,
    rule_promotion_stage,
    rule_implementation_tier,
    rule_contradiction_aging,
    rule_required_fields,
    rule_retrieval_status_vocab,
    rule_source_basis_usable,
    rule_tool_related_risks,
    run_graph_rules,
    run_rules,
)


class FakePage:
    """Duck-typed stand-in for compile_index.Page — graph rules only read
    .rel_path and .frontmatter, so tests avoid the real Page (and a circular
    import)."""

    def __init__(self, rel_path, fm=None):
        self.rel_path = rel_path
        self.frontmatter = fm or {}


def gctx(id_to_page=None, inbound_counts=None, valid_edges=None,
         unresolved_edges=None, duplicate_ids=None):
    return GraphCtx(
        id_to_page=id_to_page or {},
        inbound_counts=inbound_counts or {},
        valid_edges=valid_edges or [],
        unresolved_edges=unresolved_edges or [],
        duplicate_ids=duplicate_ids or set(),
    )


def ctx(fm=None, page_id="C-x", ptype="concept", rel_path="p.md", today=None):
    return RuleCtx(rel_path=rel_path, fm=fm or {}, page_id=page_id, ptype=ptype, today=today)


def codes(issues):
    return [i.code for i in issues]


def src_ctx(findings):
    return ctx(fm={"findings": findings}, page_id="S-x", ptype="source", rel_path="01-sources/extracted/s.md")


class FindingTargetFolder(unittest.TestCase):
    def test_noncanonical_folder_is_flagged(self):
        f = {"finding_id": "F-1", "integration_action": "create-tool",
             "candidate_target_pages": ["wiki/aba/03-tasks/x.md"]}
        self.assertIn("finding_target_folder:F-1:03-tasks->04-tools",
                      codes(rule_finding_target_folder(src_ctx([f]))))

    def test_canonical_folder_is_clean(self):
        f = {"finding_id": "F-1", "integration_action": "create-tool",
             "candidate_target_pages": ["wiki/aba/04-tools/x.md"]}
        self.assertEqual(codes(rule_finding_target_folder(src_ctx([f]))), [])

    def test_decision_rule_maps_to_decision_protocols(self):
        f = {"finding_id": "F-2", "integration_action": "create-decision-rule",
             "candidate_target_pages": ["wiki/aba/04-decision-rules/x.md"]}
        self.assertIn("finding_target_folder:F-2:04-decision-rules->09-decision-protocols",
                      codes(rule_finding_target_folder(src_ctx([f]))))

    def test_source_only_imposes_no_folder(self):
        f = {"finding_id": "F-3", "integration_action": "source_only",
             "candidate_target_pages": ["source_only"]}
        self.assertEqual(codes(rule_finding_target_folder(src_ctx([f]))), [])

    def test_non_source_page_is_ignored(self):
        f = {"finding_id": "F-4", "integration_action": "create-tool",
             "candidate_target_pages": ["wiki/aba/03-tasks/x.md"]}
        self.assertEqual(codes(rule_finding_target_folder(ctx(fm={"findings": [f]}, ptype="concept"))), [])


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


class GraphDuplicate(unittest.TestCase):
    def test_duplicate_id_is_critical_with_path(self):
        ctx = gctx(id_to_page={"C-x": FakePage("a.md")}, duplicate_ids={"C-x"})
        issues = rule_duplicate_ids(ctx)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, "critical")
        self.assertEqual(issues[0].code, "duplicate_id:C-x")
        self.assertEqual(issues[0].path, "a.md")

    def test_no_duplicates_is_clean(self):
        self.assertEqual(rule_duplicate_ids(gctx(id_to_page={"C-x": FakePage("a.md")})), [])


class GraphOrphan(unittest.TestCase):
    def test_zero_inbound_is_orphan_warning(self):
        ctx = gctx(id_to_page={"C-x": FakePage("x.md")}, inbound_counts={"C-x": 0})
        issues = rule_orphan_pages(ctx)
        self.assertEqual(codes(issues), ["orphan_page:C-x"])
        self.assertEqual(issues[0].path, "x.md")

    def test_inbound_present_is_clean(self):
        ctx = gctx(id_to_page={"C-x": FakePage("x.md")}, inbound_counts={"C-x": 2})
        self.assertEqual(rule_orphan_pages(ctx), [])


class GraphGhost(unittest.TestCase):
    def test_unresolved_edge_is_ghost_warning(self):
        ctx = gctx(unresolved_edges=[{"to": "C-z", "source_file": "src.md"}])
        issues = rule_ghost_nodes(ctx)
        self.assertEqual(codes(issues), ["ghost_node:C-z"])
        self.assertEqual(issues[0].path, "src.md")


class GraphDeprecated(unittest.TestCase):
    def _ctx(self, linker_type):
        return gctx(
            id_to_page={
                "P-x": FakePage("p.md", {"type": linker_type, "retrieval_status": "usable"}),
                "C-dep": FakePage("c.md", {"type": "concept", "retrieval_status": "deprecated"}),
            },
            valid_edges=[{"from": "P-x", "relation": "related_concept", "to": "C-dep"}],
        )

    def test_active_playbook_to_deprecated_warns(self):
        issues = rule_deprecated_target_linked(self._ctx("advisory-playbook"))
        self.assertEqual(codes(issues), ["deprecated_target_linked:C-dep"])
        self.assertEqual(issues[0].path, "p.md")

    def test_non_linker_type_is_silent(self):
        self.assertEqual(rule_deprecated_target_linked(self._ctx("concept")), [])


class PromotionStage(unittest.TestCase):
    def test_missing_on_ladder_type_is_critical(self):
        self.assertIn("missing_promotion_stage", codes(rule_promotion_stage(ctx(fm={"type": "concept"}, ptype="concept"))))

    def test_invalid_value_is_critical(self):
        c = ctx(fm={"promotion_stage": "gold"}, ptype="concept")
        self.assertEqual(codes(rule_promotion_stage(c)), ["invalid_promotion_stage:gold"])

    def test_valid_value_clean(self):
        self.assertEqual(rule_promotion_stage(ctx(fm={"promotion_stage": "framework"}, ptype="concept")), [])

    def test_source_is_exempt(self):
        self.assertEqual(rule_promotion_stage(ctx(fm={"type": "source"}, ptype="source", page_id="S-x")), [])


class ImplementationTier(unittest.TestCase):
    def test_missing_on_ladder_type_is_critical(self):
        self.assertIn("missing_implementation_tier", codes(rule_implementation_tier(ctx(fm={"type": "tool"}, ptype="tool"))))

    def test_invalid_value_is_critical(self):
        c = ctx(fm={"implementation_tier": "ops"}, ptype="tool")
        self.assertEqual(codes(rule_implementation_tier(c)), ["invalid_implementation_tier:ops"])

    def test_all_is_valid(self):
        self.assertEqual(rule_implementation_tier(ctx(fm={"implementation_tier": "all"}, ptype="tool")), [])

    def test_source_is_exempt(self):
        self.assertEqual(rule_implementation_tier(ctx(fm={"type": "source"}, ptype="source", page_id="S-x")), [])


class CrossCuttingTopicsVocab(unittest.TestCase):
    def test_absent_is_clean(self):
        self.assertEqual(rule_cross_cutting_topics_vocab(ctx(fm={})), [])  # absence never flagged

    def test_free_text_primary_topics_not_validated(self):
        # primary_topics stays free-text keywords; the vocab rule ignores it
        self.assertEqual(rule_cross_cutting_topics_vocab(ctx(fm={"primary_topics": ["anything-goes"]})), [])

    def test_present_valid_is_clean(self):
        self.assertEqual(rule_cross_cutting_topics_vocab(ctx(fm={"cross_cutting_topics": ["relational-trust"]})), [])

    def test_present_invalid_warns(self):
        c = ctx(fm={"cross_cutting_topics": ["relational-trust", "made-up-topic"]})
        self.assertEqual(codes(rule_cross_cutting_topics_vocab(c)), ["invalid_cross_cutting_topic:made-up-topic"])


class ContradictionAging(unittest.TestCase):
    TODAY = date(2026, 6, 20)

    def test_no_contradicts_is_clean(self):
        c = ctx(fm={"last_reviewed": "2020-01-01"}, today=self.TODAY)  # ancient but no contradicts
        self.assertEqual(rule_contradiction_aging(c), [])

    def test_contradicts_without_last_reviewed_warns(self):
        c = ctx(fm={"contradicts": ["C-y"]}, today=self.TODAY)
        self.assertEqual(codes(rule_contradiction_aging(c)), ["contradicts_without_last_reviewed"])

    def test_aging_over_30_days_warns(self):
        c = ctx(fm={"contradicts": ["C-y"], "last_reviewed": "2026-05-01"}, today=self.TODAY)  # 50d
        self.assertEqual(len(rule_contradiction_aging(c)), 1)
        self.assertEqual(rule_contradiction_aging(c)[0].severity, "warning")
        self.assertTrue(codes(rule_contradiction_aging(c))[0].startswith("contradiction_aging:"))

    def test_stale_over_90_days_is_critical(self):
        c = ctx(fm={"contradicts": ["C-y"], "last_reviewed": "2026-01-01"}, today=self.TODAY)  # 170d
        issues = rule_contradiction_aging(c)
        self.assertEqual(issues[0].severity, "critical")
        self.assertTrue(issues[0].code.startswith("contradiction_stale_block:"))

    def test_recent_review_is_clean(self):
        c = ctx(fm={"contradicts": ["C-y"], "last_reviewed": "2026-06-20"}, today=self.TODAY)
        self.assertEqual(rule_contradiction_aging(c), [])

    def test_no_clock_skips(self):
        c = ctx(fm={"contradicts": ["C-y"], "last_reviewed": "2026-01-01"}, today=None)
        self.assertEqual(rule_contradiction_aging(c), [])


class GraphRegistry(unittest.TestCase):
    def test_run_graph_rules_orders_critical_then_warnings(self):
        ctx = gctx(
            id_to_page={"C-x": FakePage("x.md")},
            inbound_counts={"C-x": 0},
            duplicate_ids={"C-x"},
            unresolved_edges=[{"to": "C-z", "source_file": "x.md"}],
        )
        got = codes(run_graph_rules(ctx))
        # duplicate (critical) precedes orphan then ghost (warnings)
        self.assertEqual(got, ["duplicate_id:C-x", "orphan_page:C-x", "ghost_node:C-z"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
