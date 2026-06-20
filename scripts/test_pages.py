#!/usr/bin/env python3
"""
test_pages.py — tests for read_pages (pages.py), the filesystem -> Page seam.

Uses a throwaway temp vault and exercises the real frontmatter parser (ruby),
so this is the one place the scan/parse path is covered end to end. Run:
    python3 scripts/test_pages.py
"""

import tempfile
import unittest
from pathlib import Path

from pages import read_pages


class ReadPages(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def test_parses_frontmatter_and_body(self):
        self.write("c.md", "---\nid: C-x\ntype: concept\n---\n\nBody here\n")
        pages = read_pages(self.root)
        self.assertEqual(len(pages), 1)
        self.assertEqual(pages[0].frontmatter["id"], "C-x")
        self.assertEqual(pages[0].rel_path, "c.md")
        self.assertIn("Body here", pages[0].body)

    def test_no_frontmatter_is_empty_dict(self):
        self.write("plain.md", "no frontmatter at all\n")
        pages = read_pages(self.root)
        self.assertEqual(pages[0].frontmatter, {})

    def test_malformed_yaml_flags_error(self):
        self.write("bad.md", "---\nfoo: [1, 2\n---\nbody\n")
        pages = read_pages(self.root)
        self.assertEqual(pages[0].frontmatter, {"_yaml_error": True})

    def test_skips_raw_layers_and_numeric_prefix(self):
        self.write("01-sources/raw/x.md", "---\nid: S-x\n---\nbody")
        self.write("01-sources/raw-content/y.md", "---\nid: S-y\n---\nbody")
        self.write("00_index.md", "---\nid: ignore\n---\nbody")
        self.write("keep.md", "---\nid: C-keep\n---\nbody")
        rels = [p.rel_path for p in read_pages(self.root)]
        self.assertEqual(rels, ["keep.md"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
