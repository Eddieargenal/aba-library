#!/usr/bin/env python3
"""
test_compile.py — behavior tests for the index compiler (compile_index.py)

Zero dependencies. Run:  python3 scripts/test_compile.py

These exercise compile_index through its public interface: a list of in-memory
Pages plus an injected target_exists predicate, in -> a BuildResult out. No
filesystem, no JSON read-back. The seam that build-index.py's main() lacked.
"""

import unittest
from pathlib import Path

from datetime import date

from compile_index import BuildResult, Page, compile_index, index_health


def page(page_id=None, ptype="concept", body="", **fm):
    """Build an in-memory Page. fm keys become frontmatter; id/type are set
    from the named args unless overridden in fm."""
    front = {"type": ptype}
    if page_id is not None:
        front["id"] = page_id
    front.update(fm)
    rel = f"{(page_id or 'nofm')}.md"
    return Page(path=Path(rel), rel_path=rel, frontmatter=front, body=body)


def warning_codes(result):
    return [w["warning"] for w in result.warnings]


def critical_codes(result):
    return [c["error"] for c in result.critical]


def compile(pages, target_exists=lambda p: True):
    return compile_index(pages, target_exists=target_exists)


class EdgeResolution(unittest.TestCase):
    def test_edge_to_present_target_is_valid(self):
        pages = [
            page("C-x", related_concepts=["C-y"], title="X", retrieval_status="draft"),
            page("C-y", title="Y", retrieval_status="draft"),
        ]
        result = compile(pages)
        self.assertIn(
            {"from": "C-x", "relation": "related_concept", "to": "C-y", "status": "valid"},
            result.valid_edges,
        )
        self.assertEqual(result.unresolved_edges, [])

    def test_edge_to_absent_target_is_unresolved_and_ghosts(self):
        pages = [page("C-x", related_concepts=["C-z"], title="X", retrieval_status="draft")]
        result = compile(pages)
        self.assertEqual(len(result.unresolved_edges), 1)
        edge = result.unresolved_edges[0]
        self.assertEqual(edge["to"], "C-z")
        self.assertEqual(edge["reason"], "target_id_not_found")
        self.assertEqual(edge["severity"], "high")
        self.assertEqual(result.valid_edges, [])
        self.assertIn("ghost_node:C-z", warning_codes(result))


class RoutingQueue(unittest.TestCase):
    def _source(self, finding):
        return page("S-x", ptype="source", title="S", retrieval_status="usable", findings=[finding])

    def test_nonterminal_status_is_pending(self):
        src = self._source({"finding_id": "f1", "status": "open", "candidate_target_pages": []})
        result = compile([src])
        self.assertEqual(len(result.routing_pending), 1)
        self.assertEqual(result.routing_pending[0]["finding_id"], "f1")
        self.assertEqual(result.routing_pending[0]["unsatisfied_target_pages"], [])

    def test_terminal_enrich_with_target_present_is_not_pending(self):
        src = self._source(
            {"finding_id": "f1", "status": "integrated", "integration_action": "enrich-concept",
             "candidate_target_pages": ["wiki/x.md"]}
        )
        result = compile([src], target_exists=lambda p: p == "wiki/x.md")
        self.assertEqual(result.routing_pending, [])

    def test_terminal_enrich_with_missing_target_is_pending(self):
        src = self._source(
            {"finding_id": "f1", "status": "integrated", "integration_action": "enrich-concept",
             "candidate_target_pages": ["wiki/gone.md"]}
        )
        result = compile([src], target_exists=lambda p: False)
        self.assertEqual(len(result.routing_pending), 1)
        self.assertEqual(result.routing_pending[0]["unsatisfied_target_pages"], ["wiki/gone.md"])


class TargetResolution(unittest.TestCase):
    """The #7 contract: candidate_target_pages resolve by PATH, and whether a
    target is 'satisfied' branches on integration_action — enrich-* needs the
    page to exist; create-* needs it to NOT exist yet."""

    def _source(self, finding):
        return page("S-x", ptype="source", title="S", retrieval_status="usable", findings=[finding])

    def test_create_action_not_pending_when_target_absent(self):
        src = self._source({
            "finding_id": "f1", "status": "integrated",
            "integration_action": "create-concept",
            "candidate_target_pages": ["wiki/aba/03-frameworks/new.md"],
        })
        result = compile([src], target_exists=lambda p: False)
        self.assertEqual(result.routing_pending, [])

    def test_create_action_pending_when_target_already_exists(self):
        # Collision with the prefer-enrich rule: a create-* target that already
        # exists is an anomaly -> flagged (pending, listed as unsatisfied).
        src = self._source({
            "finding_id": "f1", "status": "integrated",
            "integration_action": "create-concept",
            "candidate_target_pages": ["wiki/aba/02-concepts/exists.md"],
        })
        result = compile([src], target_exists=lambda p: True)
        self.assertEqual(len(result.routing_pending), 1)
        self.assertEqual(
            result.routing_pending[0]["unsatisfied_target_pages"],
            ["wiki/aba/02-concepts/exists.md"],
        )

    def test_source_only_imposes_no_target_requirement(self):
        src = self._source({
            "finding_id": "f1", "status": "integrated",
            "integration_action": "source_only",
            "candidate_target_pages": ["source_only"],
        })
        result = compile([src], target_exists=lambda p: False)
        self.assertEqual(result.routing_pending, [])


class DuplicateId(unittest.TestCase):
    def test_two_pages_same_id_is_critical(self):
        pages = [
            page("C-dup", title="A", retrieval_status="draft"),
            page("C-dup", title="B", retrieval_status="draft"),
        ]
        result = compile(pages)
        self.assertEqual(critical_codes(result).count("duplicate_id:C-dup"), 1)

    def test_distinct_ids_no_duplicate_critical(self):
        pages = [
            page("C-a", title="A", retrieval_status="draft"),
            page("C-b", title="B", retrieval_status="draft"),
        ]
        result = compile(pages)
        self.assertNotIn("duplicate_id:C-a", critical_codes(result))
        self.assertNotIn("duplicate_id:C-b", critical_codes(result))


class OrphanPage(unittest.TestCase):
    def test_page_with_no_inbound_edges_is_orphan(self):
        pages = [
            page("C-x", related_concepts=["C-y"], title="X", retrieval_status="draft"),
            page("C-y", title="Y", retrieval_status="draft"),
        ]
        result = compile(pages)
        # C-x points at C-y but nothing points at C-x
        self.assertIn("orphan_page:C-x", warning_codes(result))
        self.assertNotIn("orphan_page:C-y", warning_codes(result))


class IndexHealth(unittest.TestCase):
    def test_percentages_from_counts(self):
        h = index_health(page_count=4, orphan_count=1, edge_count=3,
                         unresolved_edge_count=1, stale_count=2)
        self.assertEqual(h["orphan_pct"], 25.0)            # 1/4
        self.assertEqual(h["ghost_pct"], 25.0)             # 1/(3+1) edges
        self.assertEqual(h["stale_pct"], 50.0)             # 2/4

    def test_empty_index_is_zero_not_divide_error(self):
        h = index_health(page_count=0, orphan_count=0, edge_count=0,
                         unresolved_edge_count=0, stale_count=0)
        self.assertEqual((h["orphan_pct"], h["ghost_pct"], h["stale_pct"]), (0.0, 0.0, 0.0))

    def test_compile_populates_health_with_orphans(self):
        # C-x -> C-y; nothing points at C-x, so 1 of 2 pages is an orphan
        pages = [
            page("C-x", related_concepts=["C-y"], title="X", retrieval_status="draft"),
            page("C-y", title="Y", retrieval_status="draft"),
        ]
        h = compile(pages).health
        self.assertEqual(h["page_count"], 2)
        self.assertEqual(h["orphan_count"], 1)
        self.assertEqual(h["orphan_pct"], 50.0)
        self.assertEqual(h["ghost_pct"], 0.0)

    def test_compile_health_reflects_ghost_edges(self):
        # C-x points at C-z which does not exist: 1 of 1 edges is a ghost
        pages = [page("C-x", related_concepts=["C-z"], title="X", retrieval_status="draft")]
        h = compile(pages).health
        self.assertEqual(h["ghost_edge_count"], 1)
        self.assertEqual(h["ghost_pct"], 100.0)

    def test_compile_health_counts_stale_pages(self):
        # last_reviewed older than the staleness threshold counts as stale;
        # recent and never-reviewed pages do not.
        TODAY = date(2026, 6, 21)
        pages = [
            page("C-old", title="Old", retrieval_status="draft", last_reviewed="2025-01-01"),
            page("C-new", title="New", retrieval_status="draft", last_reviewed="2026-06-01"),
            page("C-none", title="None", retrieval_status="draft"),
        ]
        h = compile_index(pages, target_exists=lambda p: True, today=TODAY).health
        self.assertEqual(h["page_count"], 3)
        self.assertEqual(h["stale_count"], 1)
        self.assertEqual(h["stale_pct"], 33.3)

    def test_compile_health_stale_needs_clock(self):
        # no injected clock -> staleness can't be computed, so nothing is stale
        pages = [page("C-old", title="Old", retrieval_status="draft", last_reviewed="2000-01-01")]
        h = compile_index(pages, target_exists=lambda p: True, today=None).health
        self.assertEqual(h["stale_count"], 0)


class Status(unittest.TestCase):
    def test_critical_makes_invalid(self):
        self.assertEqual(BuildResult(critical=[{"error": "x"}]).status, "invalid")

    def test_critical_wins_over_warnings(self):
        r = BuildResult(critical=[{"error": "x"}], warnings=[{"warning": "w"}])
        self.assertEqual(r.status, "invalid")

    def test_warnings_only_is_valid_with_warnings(self):
        self.assertEqual(BuildResult(warnings=[{"warning": "w"}]).status, "valid_with_warnings")

    def test_clean_is_valid(self):
        self.assertEqual(BuildResult().status, "valid")

    def test_duplicate_id_drives_invalid_through_compile(self):
        pages = [
            page("C-dup", title="A", retrieval_status="draft"),
            page("C-dup", title="B", retrieval_status="draft"),
        ]
        self.assertEqual(compile(pages).status, "invalid")


SECTION_BODY = """intro line
<a id="s1"></a>
## Section one
more
<a id="s2"></a>
## Section two
end"""


class SectionRanges(unittest.TestCase):
    def test_anchors_yield_correct_line_ranges(self):
        p = page(
            "C-x",
            title="X",
            retrieval_status="draft",
            body=SECTION_BODY,
            sections=[{"id": "SEC-1", "anchor": "#s1"}, {"id": "SEC-2", "anchor": "#s2"}],
        )
        result = compile([p])
        rows = {r["section_id"]: r for r in result.section_rows}
        self.assertEqual((rows["SEC-1"]["start_line"], rows["SEC-1"]["end_line"]), (2, 4))
        self.assertEqual((rows["SEC-2"]["start_line"], rows["SEC-2"]["end_line"]), (5, 7))
        self.assertEqual(rows["SEC-1"]["page_id"], "C-x")

    def test_missing_anchor_is_critical_section_error(self):
        p = page(
            "C-x",
            title="X",
            retrieval_status="draft",
            body="no anchors here",
            sections=[{"id": "SEC-9", "anchor": "#nope"}],
        )
        result = compile([p])
        self.assertIn("section_error:missing_anchor:nope", critical_codes(result))

    def test_no_sections_warns(self):
        p = page("C-x", title="X", retrieval_status="draft", body="body")
        result = compile([p])
        self.assertIn("missing_sections", warning_codes(result))


class DegreeCentrality(unittest.TestCase):
    def test_inbound_degree_counts_inbound_edges(self):
        pages = [
            page("C-x", related_concepts=["C-y"], title="X", retrieval_status="draft"),
            page("C-y", title="Y", retrieval_status="draft"),
        ]
        self.assertEqual(compile(pages).inbound_degree, {"C-x": 0, "C-y": 1})


class TermIndex(unittest.TestCase):
    def test_term_index_built_from_title_and_body(self):
        p = page("C-x", title="Resilience", retrieval_status="draft", body="flood risk flood")
        idx = compile([p]).term_index
        self.assertEqual(idx["doc_count"], 1)
        self.assertEqual(idx["postings"]["flood"]["C-x"], 2)
        self.assertIn("resilience", idx["postings"])  # title is indexed too


class DeprecatedTargetLinked(unittest.TestCase):
    def test_active_playbook_linking_deprecated_page_warns(self):
        pages = [
            page("P-x", ptype="advisory-playbook", title="P", retrieval_status="usable",
                 related_concepts=["C-dep"]),
            page("C-dep", title="Dep", retrieval_status="deprecated"),
        ]
        result = compile(pages)
        self.assertIn("deprecated_target_linked:C-dep", warning_codes(result))

    def test_non_linker_type_linking_deprecated_page_is_silent(self):
        pages = [
            page("C-y", title="Y", retrieval_status="draft", related_concepts=["C-dep"]),
            page("C-dep", title="Dep", retrieval_status="deprecated"),
        ]
        result = compile(pages)
        self.assertNotIn("deprecated_target_linked:C-dep", warning_codes(result))


class ClassificationAxes(unittest.TestCase):
    def _row(self, result, page_id):
        return next(r for r in result.page_rows if r["id"] == page_id)

    def test_row_carries_declared_promotion_stage_and_tier(self):
        p = page("F-x", ptype="framework", title="X", retrieval_status="usable",
                 promotion_stage="framework", implementation_tier="synthesis")
        row = self._row(compile([p]), "F-x")
        self.assertEqual(row["promotion_stage"], "framework")
        self.assertEqual(row["implementation_tier"], "synthesis")

    def test_row_axes_default_to_none_when_undeclared(self):
        p = page("C-x", title="X", retrieval_status="draft")
        row = self._row(compile([p]), "C-x")
        self.assertIn("promotion_stage", row)
        self.assertIn("implementation_tier", row)
        self.assertIsNone(row["promotion_stage"])
        self.assertIsNone(row["implementation_tier"])

    def test_row_includes_cross_cutting_topics_when_declared(self):
        p = page("F-x", ptype="framework", title="X", retrieval_status="usable",
                 cross_cutting_topics=["relational-trust", "co-design"])
        row = self._row(compile([p]), "F-x")
        self.assertEqual(row["cross_cutting_topics"], ["relational-trust", "co-design"])

    def test_row_omits_cross_cutting_topics_when_absent(self):
        p = page("C-x", title="X", retrieval_status="draft")
        row = self._row(compile([p]), "C-x")
        self.assertNotIn("cross_cutting_topics", row)


if __name__ == "__main__":
    unittest.main(verbosity=2)
