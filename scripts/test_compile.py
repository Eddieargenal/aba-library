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

from compile_index import BuildResult, Page, compile_index


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
        self.assertEqual(result.routing_pending[0]["missing_target_pages"], [])

    def test_terminal_with_all_targets_present_is_not_pending(self):
        src = self._source(
            {"finding_id": "f1", "status": "integrated", "candidate_target_pages": ["wiki/x.md"]}
        )
        result = compile([src], target_exists=lambda p: p == "wiki/x.md")
        self.assertEqual(result.routing_pending, [])

    def test_terminal_but_missing_target_is_pending(self):
        src = self._source(
            {"finding_id": "f1", "status": "integrated", "candidate_target_pages": ["wiki/gone.md"]}
        )
        result = compile([src], target_exists=lambda p: False)
        self.assertEqual(len(result.routing_pending), 1)
        self.assertEqual(result.routing_pending[0]["missing_target_pages"], ["wiki/gone.md"])


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


if __name__ == "__main__":
    unittest.main(verbosity=2)
