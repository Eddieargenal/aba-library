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
    rule_contradiction_disclosure,
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
    rule_schema_version,
    rule_source_basis_resolves,
    rule_gate_state,
    source_ids_in_section_index,
    rule_tool_related_risks,
    run_graph_rules,
    run_rules,
)
from schema import SCHEMA_VERSION


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


def ctx(fm=None, page_id="C-x", ptype="concept", rel_path="p.md", today=None,
        known_source_ids=None):
    return RuleCtx(rel_path=rel_path, fm=fm or {}, page_id=page_id, ptype=ptype,
                   today=today, known_source_ids=known_source_ids)


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

    def test_companion_target_allowed_when_primary_canonical(self):
        # multi-target: primary matches the action's type, secondary is a
        # cross-type companion page -> allowed (guard checks the primary only).
        f = {"finding_id": "F-1", "integration_action": "create-concept",
             "candidate_target_pages": ["wiki/aba/02-concepts/x.md",
                                        "wiki/aba/04-tools/x-process.md"]}
        self.assertEqual(codes(rule_finding_target_folder(src_ctx([f]))), [])

    def test_flagged_when_no_target_matches_action_type(self):
        f = {"finding_id": "F-1", "integration_action": "create-risk",
             "candidate_target_pages": ["wiki/aba/07-known-tensions/x.md"]}
        self.assertIn("finding_target_folder:F-1:07-known-tensions->06-risks",
                      codes(rule_finding_target_folder(src_ctx([f]))))

    def test_known_tension_action_maps_to_known_tensions_folder(self):
        ok = {"finding_id": "F-1", "integration_action": "create-known-tension",
              "candidate_target_pages": ["wiki/aba/07-known-tensions/x.md"]}
        self.assertEqual(codes(rule_finding_target_folder(src_ctx([ok]))), [])
        bad = {"finding_id": "F-2", "integration_action": "create-known-tension",
               "candidate_target_pages": ["wiki/aba/06-risks/x.md"]}
        self.assertIn("finding_target_folder:F-2:06-risks->07-known-tensions",
                      codes(rule_finding_target_folder(src_ctx([bad]))))

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


class SchemaVersion(unittest.TestCase):
    def test_divergent_declared_version_warns(self):
        c = ctx(fm={"schema_version": "9.9"})
        self.assertEqual(codes(rule_schema_version(c)), ["schema_version_mismatch:9.9"])

    def test_matching_declared_version_is_clean(self):
        self.assertEqual(rule_schema_version(ctx(fm={"schema_version": SCHEMA_VERSION})), [])

    def test_absent_version_is_clean(self):
        # most pages omit schema_version; absence is never flagged
        self.assertEqual(rule_schema_version(ctx(fm={})), [])

    def test_v_prefix_is_tolerated(self):
        # the historical drift used "v2.7"/"v3.0" notation; a cosmetic v prefix
        # on the active generation is not a mismatch
        self.assertEqual(rule_schema_version(ctx(fm={"schema_version": "v" + SCHEMA_VERSION})), [])

    def test_v_prefixed_mismatch_reports_normalized(self):
        c = ctx(fm={"schema_version": "v3.0"})
        self.assertEqual(codes(rule_schema_version(c)), ["schema_version_mismatch:3.0"])


class SourceBasisResolves(unittest.TestCase):
    KNOWN = {"S-2009-twigg-ucl-disaster-resilient-community"}

    def test_dangling_source_id_warns(self):
        c = ctx(fm={"source_basis": [{"source_id": "S-ghost"}]},
                known_source_ids=self.KNOWN)
        self.assertEqual(codes(rule_source_basis_resolves(c)),
                         ["source_basis_unresolved:S-ghost"])

    def test_resolvable_source_id_is_clean(self):
        c = ctx(fm={"source_basis": [{"source_id": "S-2009-twigg-ucl-disaster-resilient-community"}]},
                known_source_ids=self.KNOWN)
        self.assertEqual(rule_source_basis_resolves(c), [])

    def test_no_index_skips(self):
        # index unavailable: skip rather than flag every reference as dangling
        c = ctx(fm={"source_basis": [{"source_id": "S-ghost"}]}, known_source_ids=None)
        self.assertEqual(rule_source_basis_resolves(c), [])

    def test_empty_source_basis_is_clean(self):
        # source pages carry source_basis: [] ; absence is fine too
        self.assertEqual(rule_source_basis_resolves(
            ctx(fm={"source_basis": []}, known_source_ids=self.KNOWN)), [])
        self.assertEqual(rule_source_basis_resolves(
            ctx(fm={}, known_source_ids=self.KNOWN)), [])

    def test_mixed_entries_report_only_danglers(self):
        c = ctx(fm={"source_basis": [
            {"source_id": "S-2009-twigg-ucl-disaster-resilient-community"},  # resolvable
            {"source_id": "S-ghost-a"},
            {"source_id": "S-ghost-b"},
        ]}, known_source_ids=self.KNOWN)
        self.assertEqual(codes(rule_source_basis_resolves(c)),
                         ["source_basis_unresolved:S-ghost-a", "source_basis_unresolved:S-ghost-b"])

    def test_malformed_entries_skipped_gracefully(self):
        # a bare string and a dict with no source_id are malformed shapes other
        # rules own; this rule skips them rather than crash or emit ":None"
        c = ctx(fm={"source_basis": ["S-bare-string", {"finding_ids": ["F-1"]}]},
                known_source_ids=self.KNOWN)
        self.assertEqual(rule_source_basis_resolves(c), [])

    def test_source_ids_in_section_index_extracts_page_ids(self):
        rows = [
            {"page_id": "S-a", "section_id": "summary"},
            {"page_id": "S-a", "section_id": "findings"},   # deduped
            {"page_id": "S-b", "section_id": "summary"},
        ]
        self.assertEqual(source_ids_in_section_index(rows), {"S-a", "S-b"})


class GateState(unittest.TestCase):
    def test_pending_gate_is_critical_blocking(self):
        issues = rule_gate_state(ctx(fm={"gate_state": "awaiting-gate-b"}))
        self.assertEqual(codes(issues), ["gate_pending:awaiting-gate-b"])
        self.assertEqual(issues[0].severity, "critical")

    def test_cleared_is_clean(self):
        self.assertEqual(rule_gate_state(ctx(fm={"gate_state": "cleared"})), [])

    def test_absent_is_clean(self):
        # unannotated pages keep the review-process model; no constraint imposed
        self.assertEqual(rule_gate_state(ctx(fm={})), [])

    def test_unrecognized_value_is_critical_invalid(self):
        issues = rule_gate_state(ctx(fm={"gate_state": "bogus"}))
        self.assertEqual(codes(issues), ["invalid_gate_state:bogus"])
        self.assertEqual(issues[0].severity, "critical")


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

    def test_run_rules_includes_schema_version(self):
        c = ctx(fm={"schema_version": "9.9"}, ptype="concept", page_id="C-x")
        self.assertIn("schema_version_mismatch:9.9", codes(run_rules(c)))

    def test_run_rules_includes_gate_state(self):
        c = ctx(fm={"gate_state": "awaiting-gate-b"}, ptype="concept", page_id="C-x")
        self.assertIn("gate_pending:awaiting-gate-b", codes(run_rules(c)))

    def test_run_rules_includes_source_basis_resolution(self):
        c = ctx(fm={"source_basis": [{"source_id": "S-ghost"}]},
                ptype="concept", page_id="C-x",
                known_source_ids={"S-real"})
        self.assertIn("source_basis_unresolved:S-ghost", codes(run_rules(c)))


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


class GraphContradictionDisclosure(unittest.TestCase):
    def _ctx(self, edges):
        return gctx(
            id_to_page={"C-a": FakePage("a.md"), "C-b": FakePage("b.md")},
            valid_edges=edges,
        )

    def test_asymmetric_contradicts_flags_the_silent_side(self):
        # C-a discloses a contradiction with C-b; C-b does not reciprocate
        issues = rule_contradiction_disclosure(
            self._ctx([{"from": "C-a", "relation": "contradicts", "to": "C-b"}]))
        self.assertEqual(codes(issues), ["undisclosed_contradiction:C-b:C-a"])
        self.assertEqual(issues[0].severity, "warning")
        self.assertEqual(issues[0].path, "b.md")

    def test_mutual_contradiction_is_clean(self):
        issues = rule_contradiction_disclosure(self._ctx([
            {"from": "C-a", "relation": "contradicts", "to": "C-b"},
            {"from": "C-b", "relation": "contradicts", "to": "C-a"},
        ]))
        self.assertEqual(issues, [])

    def test_non_contradicts_relation_is_ignored(self):
        # a one-sided related_concept edge is not a contradiction to disclose
        issues = rule_contradiction_disclosure(self._ctx([
            {"from": "C-a", "relation": "related_concept", "to": "C-b"},
        ]))
        self.assertEqual(issues, [])


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

    def test_run_graph_rules_includes_contradiction_disclosure(self):
        ctx = gctx(
            id_to_page={"C-a": FakePage("a.md"), "C-b": FakePage("b.md")},
            valid_edges=[{"from": "C-a", "relation": "contradicts", "to": "C-b"}],
        )
        self.assertIn("undisclosed_contradiction:C-b:C-a", codes(run_graph_rules(ctx)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
