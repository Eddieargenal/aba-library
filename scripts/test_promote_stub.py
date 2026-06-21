#!/usr/bin/env python3
"""
test_promote_stub.py — behavior tests for the Gate-D promotion helper.

Zero dependencies. Run:  python3 scripts/test_promote_stub.py

Exercises the pure transform that turns a PU- proposed-update stub into a
publishable wiki page: set retrieval_status + the ladder axes, strip the PU
note, and resolve the canonical target path.
"""

import unittest

from promote_stub import promote, target_path, strip_pu_note


STUB_FM = {
    "id": "C-resilience-framework",
    "type": "concept",
    "title": "Disaster-resilient community (aspirational model)",
    "slug": "resilience-framework",
    "retrieval_status": "draft",
    "source_basis": [{"source_id": "S-2009-twigg-ucl-disaster-resilient-community"}],
    "sections": [{"id": "definition", "anchor": "#definition", "purpose": "x"}],
}

STUB_BODY = """> **Proposed library update (PU)** — drafted by the routing pass.
> Status: draft — pending Gate B review. Not yet part of the wiki.

<a id="definition"></a>
## Definition
Real content here.
"""


class Promote(unittest.TestCase):
    def test_sets_status_and_ladder_axes(self):
        fm, _ = promote(dict(STUB_FM), STUB_BODY,
                        status="limited", promotion_stage="concept",
                        implementation_tier="synthesis")
        self.assertEqual(fm["retrieval_status"], "limited")
        self.assertEqual(fm["promotion_stage"], "concept")
        self.assertEqual(fm["implementation_tier"], "synthesis")

    def test_strips_the_pu_note(self):
        _, body = promote(dict(STUB_FM), STUB_BODY, status="limited",
                          promotion_stage="concept", implementation_tier="synthesis")
        self.assertNotIn("Proposed library update", body)
        self.assertTrue(body.startswith('<a id="definition"></a>'))
        self.assertIn("Real content here.", body)

    def test_invalid_promotion_stage_raises(self):
        with self.assertRaises(ValueError):
            promote(dict(STUB_FM), STUB_BODY, status="limited",
                    promotion_stage="gold", implementation_tier="synthesis")

    def test_invalid_status_raises(self):
        with self.assertRaises(ValueError):
            promote(dict(STUB_FM), STUB_BODY, status="published",
                    promotion_stage="concept", implementation_tier="synthesis")


class TargetPath(unittest.TestCase):
    def test_maps_type_and_slug_to_canonical_folder(self):
        self.assertEqual(
            target_path({"type": "concept", "slug": "resilience-framework"}),
            "wiki/aba/02-concepts/resilience-framework.md")
        self.assertEqual(
            target_path({"type": "tool", "slug": "measure-resilience-progress"}),
            "wiki/aba/04-tools/measure-resilience-progress.md")


class StripPuNote(unittest.TestCase):
    def test_leading_blockquote_removed_but_inner_preserved(self):
        body = "> note line\n> more note\n\n## Heading\nbody\n> a real quote\n"
        out = strip_pu_note(body)
        self.assertTrue(out.startswith("## Heading"))
        self.assertIn("> a real quote", out)  # non-leading blockquote untouched


if __name__ == "__main__":
    unittest.main(verbosity=2)
