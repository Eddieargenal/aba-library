#!/usr/bin/env python3
"""
test_export_fieldwise.py — behavior tests for the FieldWise vault export (export_fieldwise.py)

Zero dependencies. Run:  python3 scripts/test_export_fieldwise.py

A clean build becomes one zip that FieldWise imports: each anchored section of a usable or limited synthesis page
becomes one note with simple `key: value` front matter, and a manifest pins the build (FieldWise PRD #30, issue #50).
Tests go through plan_export (in-memory Pages and their compiled build in, a plan out) and write_package (plan in,
zip on disk out), and read the zip back as FieldWise would.
"""

import hashlib
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from compile_index import Page, compile_index
from export_fieldwise import NotClean, StaleBuild, export_from_disk, plan_export, write_package
from pages import pages_digest, read_pages

BODY = """
<a id="definition"></a>
## Definition

Neighbourliness is friendliness, helpfulness and respect for privacy (p. 15).

<a id="field-use"></a>
## Field Use

Read it as a progress indicator of social cohesion (p. 15).
"""


def page(page_id="C-neighbourliness", ptype="concept", body=BODY, rel=None, **fm):
    front = {"id": page_id, "type": ptype, "title": "Neighbourliness", "retrieval_status": "usable",
             "last_reviewed": "2026-10-25", "accepted_by": "Ed", "lifecycle_stage": ["neighbourhood-diagnosis"],
             "promotion_stage": "concept", "implementation_tier": "all",
             "source_basis": [{"source_id": "S-youngfoundation2010", "object_id": "S-youngfoundation2010-MEASURE-001"}],
             "sections": [{"id": "definition", "anchor": "#definition"}, {"id": "field-use", "anchor": "#field-use"}]}
    front.update(fm)
    front = {k: v for k, v in front.items() if v is not None}
    rel = rel or f"02-concepts/{page_id}.md"
    return Page(path=Path(rel), rel_path=rel, frontmatter=front, body=body)


def export(pages, build_id="2026-10-25T120000Z"):
    """Plan and write the package; return {file name: (front matter dict, body)} and the plan."""
    result = compile_index(pages, target_exists=lambda p: True)
    plan = plan_export(pages, result, build_id=build_id)
    tmp = Path(tempfile.mkdtemp())
    out = tmp / "fieldwise.zip"
    write_package(plan, out)
    notes = {}
    with zipfile.ZipFile(out) as z:
        for name in z.namelist():
            if name.endswith(".md"):
                text = z.read(name).decode("utf-8")
                head, body = text.split("\n---\n", 1)
                fm = dict(line.split(": ", 1) for line in head.removeprefix("---\n").splitlines())
                notes[name] = (fm, body)
    return notes, plan, out


class Tracer(unittest.TestCase):
    def test_each_anchored_section_of_a_reviewed_concept_becomes_one_note(self):
        notes, _, _ = export([page()])
        self.assertEqual(len(notes), 2)
        by_title = {fm["title"]: (fm, body) for fm, body in notes.values()}
        self.assertEqual(set(by_title), {"Neighbourliness — Definition", "Neighbourliness — Field Use"})
        fm, body = by_title["Neighbourliness — Field Use"]
        self.assertEqual(fm["kind"], "synthesis")
        self.assertEqual((fm["aba_id"], fm["aba_section"]), ("C-neighbourliness", "field-use"))
        self.assertEqual(fm["authority"], "FieldWise ABA library")
        self.assertEqual(fm["author"], "Ed")
        self.assertEqual(fm["valid_until"], "2027-10-25")
        self.assertEqual(fm["retrieval_status"], "usable")
        self.assertEqual(fm["build_id"], "2026-10-25T120000Z")
        self.assertIn("progress indicator of social cohesion (p. 15)", body)
        self.assertNotIn("friendliness, helpfulness", body, "one section per note")


class Scope(unittest.TestCase):
    def test_only_usable_and_limited_synthesis_pages_leave_the_library(self):
        pages = [
            page(),
            page("R-capture", ptype="risk", rel="06-risks/R-capture.md", title="Governance capture",
                 retrieval_status="limited", limited_to="contested informal settlements"),
            page("C-draft", title="Draft idea", retrieval_status="draft"),
            page("T-old", ptype="tool", rel="04-tools/T-old.md", title="Old tool", retrieval_status="deprecated"),
            page("O-brief", ptype="output-template", rel="10-output-templates/O-brief.md", title="Brief"),
            page("SS-slice", ptype="slice-spec", rel="11-slice-specs/SS-slice.md", title="Slice"),
            page("C-map", rel="00-overview/C-map.md", title="Scaffold map"),
        ]
        notes, _, _ = export(pages)
        self.assertEqual({fm["aba_id"] for fm, _ in notes.values()}, {"C-neighbourliness", "R-capture"})
        limited = next(fm for fm, _ in notes.values() if fm["aba_id"] == "R-capture")
        self.assertEqual(limited["retrieval_status"], "limited")


class HeldBack(unittest.TestCase):
    def test_a_page_nobody_reviewed_or_accepted_is_held_back_and_reported(self):
        pages = [page(), page("C-unreviewed", title="Unreviewed", last_reviewed=None),
                 page("C-orphan", title="No author", accepted_by=None)]
        notes, plan, _ = export(pages)
        self.assertEqual({fm["aba_id"] for fm, _ in notes.values()}, {"C-neighbourliness"})
        self.assertEqual(plan.report["held_back"], [
            {"aba_id": "C-unreviewed", "path": "02-concepts/C-unreviewed.md", "reason": "no last_reviewed"},
            {"aba_id": "C-orphan", "path": "02-concepts/C-orphan.md", "reason": "no accepted_by"}])


class Manifest(unittest.TestCase):
    def test_the_manifest_pins_the_build_and_holds_a_digest_of_every_note(self):
        notes, plan, out = export([page(), page("C-unreviewed", title="Unreviewed", last_reviewed=None)])
        with zipfile.ZipFile(out) as z:
            m = json.loads(z.read("manifest.json"))
            files = {n: z.read(n) for n in z.namelist() if n.endswith(".md")}
        self.assertEqual((m["format"], m["build_id"], m["critical_error_count"]),
                         ("fieldwise-vault/1", "2026-10-25T120000Z", 0))
        self.assertRegex(m["exported_at"], r"^\d{4}-\d{2}-\d{2}T")
        self.assertEqual({n["file"]: n["sha256"] for n in m["notes"]},
                         {name: hashlib.sha256(data).hexdigest() for name, data in files.items()})
        self.assertEqual(m["report"]["held_back"][0]["aba_id"], "C-unreviewed")


class Refusals(unittest.TestCase):
    def test_a_build_with_a_critical_error_writes_no_package(self):
        broken = page("C-broken", retrieval_status="public")   # not in the vocabulary: a critical lint error
        result = compile_index([page(), broken], target_exists=lambda p: True)
        self.assertTrue(result.critical)
        with self.assertRaises(NotClean) as e:
            plan_export([page(), broken], result, build_id="b1")
        self.assertIn("critical", str(e.exception))


    def test_the_command_refuses_when_pages_changed_after_the_current_build(self):
        root = Path(tempfile.mkdtemp())
        wiki = root / "wiki" / "aba"
        p = page()
        f = wiki / p.rel_path
        f.parent.mkdir(parents=True)
        fm_lines = "\n".join(f"{k}: {json.dumps(v)}" for k, v in p.frontmatter.items())
        f.write_text(f"---\n{fm_lines}\n---\n{BODY}", encoding="utf-8")
        current = root / "indexes" / "current"
        current.mkdir(parents=True)
        (current / "manifest.json").write_text(json.dumps(
            {"build_id": "2026-10-25T120000Z", "critical_error_count": 0, "content_digest": pages_digest(read_pages(wiki))}))
        out = export_from_disk(root, root / "exports")
        self.assertEqual(out.name, "fieldwise-2026-10-25T120000Z.zip")
        with zipfile.ZipFile(out) as z:
            self.assertEqual(len([n for n in z.namelist() if n.endswith(".md")]), 2)
        f.write_text(f.read_text(encoding="utf-8").replace("progress indicator", "soft indicator"), encoding="utf-8")
        with self.assertRaises(StaleBuild) as e:
            export_from_disk(root, root / "exports")
        self.assertIn("rebuild", str(e.exception))


if __name__ == "__main__":
    unittest.main()
