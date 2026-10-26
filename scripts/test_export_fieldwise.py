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
import re
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


def text(body):
    """A note body without its link lines."""
    return "\n".join(l for l in body.splitlines()
                     if not l.startswith(("Same page: ", "Tensions: ", "Sources: ", "Related: "))).strip()


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


class VaultFields(unittest.TestCase):
    def test_each_note_carries_its_pages_promotion_and_lifecycle_stages_limited_to_and_sectors(self):
        pages = [page(retrieval_status="limited", limited_to="urban flood contexts in informal settlements",
                      sectors=["shelter", "wash"], lifecycle_stage=["area-selection", "neighbourhood-diagnosis"]),
                 page("C-scales", title="Neighbourhood scales")]
        notes, _, _ = export(pages)
        by_title = {fm["title"]: fm for fm, _ in notes.values()}
        fm = by_title["Neighbourliness — Field Use"]
        self.assertEqual((fm["promotion_stage"], fm["lifecycle_stage"]),
                         ("concept", "area-selection, neighbourhood-diagnosis"))
        self.assertEqual((fm["limited_to"], fm["sectors"]), ("urban flood contexts in informal settlements",
                                                             "shelter, wash"))
        usable = by_title["Neighbourhood scales — Definition"]
        self.assertNotIn("limited_to", usable)
        self.assertNotIn("sectors", usable, "an empty field is left out")

    def test_source_notes_are_at_the_finding_stage_and_a_finding_keeps_its_own_lifecycle_stages(self):
        body = SOURCE_BODY + """
<a id="findings"></a>
## Findings

**F-001** — There is no consensus definition.

**F-002** — A working definition combines three lenses.
"""
        meta = [{"finding_id": "F-001", "finding_type": "concept-definition", "lifecycle_stage": ["monitoring-learning"]},
                {"finding_id": "F-002", "finding_type": "framework-component", "lifecycle_stage": []}]
        notes, _, _ = export([source(body=body, findings=meta,
                                     lifecycle_stage=["area-selection", "coordination-design"])])
        by_section = {fm["aba_section"]: fm for fm, _ in notes.values()}
        self.assertEqual({fm["promotion_stage"] for fm in by_section.values()}, {"finding"})
        self.assertEqual(by_section["summary"]["lifecycle_stage"], "area-selection, coordination-design")
        self.assertEqual(by_section["finding-f-001"]["lifecycle_stage"], "monitoring-learning")
        self.assertEqual(by_section["finding-f-002"]["lifecycle_stage"], "area-selection, coordination-design",
                         "a finding with no stages of its own has its source's")

    def test_the_bundle_flag_is_carried_only_when_the_page_sets_it(self):
        pages = [page(bundle=True), page("C-scales", title="Neighbourhood scales", bundle=False),
                 page("C-unit", title="Neighbourhood unit")]
        notes, _, _ = export(pages)
        bundled = {fm["aba_id"] for fm, _ in notes.values() if fm.get("bundle") == "true"}
        self.assertEqual(bundled, {"C-neighbourliness"})
        self.assertFalse(any("bundle" in fm for fm, _ in notes.values() if fm["aba_id"] != "C-neighbourliness"))


class HeldBack(unittest.TestCase):
    def test_a_page_nobody_reviewed_or_accepted_is_held_back_and_reported(self):
        pages = [page(), page("C-unreviewed", title="Unreviewed", last_reviewed=None),
                 page("C-orphan", title="No author", accepted_by=None)]
        notes, plan, _ = export(pages)
        self.assertEqual({fm["aba_id"] for fm, _ in notes.values()}, {"C-neighbourliness"})
        self.assertEqual(plan.report["held_back"], [
            {"aba_id": "C-unreviewed", "path": "02-concepts/C-unreviewed.md", "reason": "no last_reviewed"},
            {"aba_id": "C-orphan", "path": "02-concepts/C-orphan.md", "reason": "no accepted_by"}])


SOURCE_BODY = """
<a id="summary"></a>
## Summary

The guide defines neighbourhoods through three lenses (p. 9).
"""


def source(page_id="S-youngfoundation2010", body=SOURCE_BODY, **fm):
    front = {"id": page_id, "type": "source", "title": "How can neighbourhoods be defined?",
             "retrieval_status": "usable", "last_reviewed": "2026-10-25", "accepted_by": "Ed",
             "institution": "The Young Foundation", "author": "The Young Foundation", "status": "extracted",
             "lifecycle_stage": ["area-selection"], "findings": []}
    front.update(fm)
    front = {k: v for k, v in front.items() if v is not None}
    return Page(path=Path(f"01-sources/extracted/{page_id}.md"), rel_path=f"01-sources/extracted/{page_id}.md",
                frontmatter=front, body=body)


class SourcePages(unittest.TestCase):
    def test_the_summary_of_a_reviewed_source_becomes_a_standard_note_with_the_publisher_as_authority(self):
        notes, _, _ = export([source()])
        self.assertEqual(len(notes), 1)
        fm, body = next(iter(notes.values()))
        self.assertEqual(fm["title"], "How can neighbourhoods be defined? — Summary")
        self.assertEqual(fm["kind"], "standard")
        self.assertEqual((fm["aba_id"], fm["aba_section"]), ("S-youngfoundation2010", "summary"))
        self.assertEqual(fm["authority"], "The Young Foundation")
        self.assertEqual((fm["author"], fm["valid_until"]), ("Ed", "2027-10-25"))
        self.assertIn("three lenses (p. 9)", body)

    def test_only_the_fixed_guidance_sections_leave_the_library(self):
        workflow = ["lifecycle-coverage", "findings", "task-seeds", "integration-map", "step-13-internal-structures",
                    "step-16-source-level-synthesis-for-later-agents", "gate-a-review-queue"]
        guidance = ["summary", "key-concepts", "methods-and-tools", "known-tensions", "decision-logic"]
        body = "".join(f'\n<a id="{a}"></a>\n## {a.replace("-", " ").title()}\n\nText of {a}.\n'
                       for a in guidance[:2] + workflow + guidance[2:])
        notes, _, _ = export([source(body=body)])
        self.assertEqual(sorted(fm["aba_section"] for fm, _ in notes.values()), sorted(guidance))
        self.assertFalse(any("Text of task-seeds" in b or "Text of gate-a" in b for _, b in notes.values()))

    def test_each_finding_becomes_one_note_with_its_pages_and_lifecycle_stages(self):
        body = SOURCE_BODY + """
<a id="findings"></a>
## Findings

**Group 1: Neighbourhood definition**

**F-001** — There is no consensus definition of "neighbourhood". → see S-youngfoundation2010-CONCEPT-001
*Routing rationale:* Core definitional problem; routes to neighbourhood-concept.

**F-002** — A working definition combines three lenses. → see S-youngfoundation2010-FRAMEWORK-001
*Routing rationale:* Routes to a new framework page.

**Group 6: Task seeds**

**F-016** — Task seed: How to define the neighbourhood unit?
*Routing rationale:* Core ABA design question.
"""
        findings = [
            {"finding_id": "F-001", "finding_type": "concept-definition", "source_pages": ["p. 9"],
             "lifecycle_stage": ["area-selection", "neighbourhood-diagnosis"]},
            {"finding_id": "F-002", "finding_type": "framework-component", "source_pages": ["p. 9–10", "p. 14"],
             "lifecycle_stage": ["area-selection"]},
            {"finding_id": "F-016", "finding_type": "task-seed", "source_pages": [], "lifecycle_stage": []}]
        notes, _, _ = export([source(body=body, findings=findings)])
        by_section = {fm["aba_section"]: (fm, b) for fm, b in notes.values()}
        self.assertEqual(set(by_section), {"summary", "finding-f-001", "finding-f-002"}, "task seeds never leave")
        fm, b = by_section["finding-f-002"]
        self.assertEqual(fm["title"], "How can neighbourhoods be defined? — Finding F-002")
        self.assertEqual((fm["kind"], fm["authority"]), ("standard", "The Young Foundation"))
        self.assertEqual(fm["lifecycle_stage"], "area-selection")
        self.assertEqual(by_section["finding-f-001"][0]["lifecycle_stage"], "area-selection, neighbourhood-diagnosis")
        self.assertIn("A working definition combines three lenses.", b)
        self.assertIn("Pages: p. 9–10, p. 14", b)
        self.assertNotIn("Routing rationale", b)
        self.assertNotIn("consensus", b, "one finding per note")

    def test_findings_written_as_a_table_also_become_one_note_each(self):
        body = SOURCE_BODY + """
<a id="findings"></a>
## Findings

| Finding ID | Finding | Finding type | Knowledge layer | Lifecycle stage | Source pages | status |
|---|---|---|---|---|---|---|
| F-001 | Resilience is the capacity to absorb shocks. → see S-twigg-CONCEPT-001 | concept-definition | conceptual | assessment | p. 8 | integrated |
| F-013 | Task seed: How to assess resilience? → see S-twigg-SEED-001 | task-seed | operational | assessment | throughout | pending |
"""
        findings = [{"finding_id": "F-001", "finding_type": "concept-definition", "source_pages": ["p. 8"],
                     "lifecycle_stage": ["assessment"]},
                    {"finding_id": "F-013", "finding_type": "task-seed", "source_pages": [], "lifecycle_stage": []}]
        notes, _, _ = export([source(body=body, findings=findings)])
        by_section = {fm["aba_section"]: (fm, b) for fm, b in notes.values()}
        self.assertEqual(set(by_section), {"summary", "finding-f-001"})
        fm, b = by_section["finding-f-001"]
        self.assertEqual(fm["lifecycle_stage"], "assessment")
        self.assertEqual(text(b), "Resilience is the capacity to absorb shocks.\n\nPages: p. 8")

    def test_each_known_tensions_row_becomes_one_tension_note_and_the_rest_stays_in_the_section(self):
        body = SOURCE_BODY + """
<a id="known-tensions"></a>
## Known Tensions

| Tension ID | First position | Source location | Conflicting position | Source location | Type | Why it matters | Related objects |
|---|---|---|---|---|---|---|---|
| S-youngfoundation2010-TNS-001 | Boundaries should reflect lived experience. | p. 9–10 | Administrative geography leaves no one out. | p. 10–11 | conceptual | Validity against completeness. | S-youngfoundation2010-FRAMEWORK-001 |
| S-youngfoundation2010-TNS-002 | Self-defined units are more cohesive. | p. 10 | Self-defined units reinforce social divides. | p. 12 | normative |  | S-youngfoundation2010-RISK-001 |

**Urban applicability gaps:**
- Informal settlement dynamics assumed absent
"""
        notes, _, _ = export([source(body=body)])
        by_section = {fm["aba_section"]: (fm, b) for fm, b in notes.values()}
        self.assertEqual(set(by_section), {"summary", "known-tensions", "tns-001", "tns-002"})
        fm, b = by_section["tns-001"]
        self.assertEqual(fm["title"], "How can neighbourhoods be defined? — Tension TNS-001")
        self.assertEqual((fm["role"], fm["kind"], fm["authority"]), ("tension", "standard", "The Young Foundation"))
        self.assertEqual(text(b).splitlines(), [
            "Position A: Boundaries should reflect lived experience. (p. 9–10)",
            "Position B: Administrative geography leaves no one out. (p. 10–11)",
            "Why it matters: Validity against completeness."])
        self.assertNotIn("Why it matters", by_section["tns-002"][1], "the line is optional")
        section = by_section["known-tensions"][1]
        self.assertIn("Informal settlement dynamics assumed absent", section)
        self.assertNotIn("lived experience", section, "each tension is in one note only")

    def test_a_section_over_about_600_words_is_split_at_its_subheadings(self):
        words = " ".join(["word"] * 250)
        body = f"""
<a id="summary"></a>
## Summary

{words} {words} {words}

<a id="methods-and-tools"></a>
## Methods and Tools

The guide gives two methods and one tool.

### Methods

#### Desk Review Method

Desk review {words}

#### Key Informant Interview (KII) Method

KII {words}

### Tools

#### Tool 1 — Workplan Template

Workplan {words}

<a id="decision-logic"></a>
## Decision Logic

### Short rule

Use the proximity scale.
"""
        notes, _, _ = export([source(body=body)])
        by_section = {fm["aba_section"]: (fm, b) for fm, b in notes.values()}
        self.assertEqual(set(by_section), {
            "summary", "decision-logic", "methods-and-tools",
            "methods-and-tools--desk-review-method", "methods-and-tools--key-informant-interview-kii-method",
            "methods-and-tools--tool-1-workplan-template"}, "no subheadings or under 600 words: one note")
        fm, b = by_section["methods-and-tools--key-informant-interview-kii-method"]
        self.assertEqual(fm["title"], "How can neighbourhoods be defined? — Methods and Tools: "
                                      "Key Informant Interview (KII) Method")
        self.assertTrue(b.startswith("#### Key Informant Interview (KII) Method"))
        self.assertNotIn("Desk review", b)
        self.assertIn("two methods and one tool", by_section["methods-and-tools"][1])

    def test_a_source_in_the_old_format_is_held_back_and_reported(self):
        old = """
<a id="summary"></a>
# Summary

The strategy sets six objectives.

# Key concepts

Urban vulnerability.

# Quality Checklist (must pass before finishing)

- [x] Pages cited
"""
        notes, plan, _ = export([source(), source("S-iasc2010", body=old)])
        self.assertEqual({fm["aba_id"] for fm, _ in notes.values()}, {"S-youngfoundation2010"})
        self.assertEqual(plan.report["held_back"], [{"aba_id": "S-iasc2010",
                                                     "path": "01-sources/extracted/S-iasc2010.md",
                                                     "reason": "old source format"}])

    def test_the_author_is_the_publisher_when_there_is_no_institution_and_no_publisher_holds_the_page_back(self):
        pages = [source("S-worldbank2013", institution=None, author="The World Bank"),
                 source("S-anon", institution=None, author=None)]
        notes, plan, _ = export(pages)
        self.assertEqual([fm["authority"] for fm, _ in notes.values()], ["The World Bank"])
        self.assertEqual(plan.report["held_back"], [{"aba_id": "S-anon", "path": "01-sources/extracted/S-anon.md",
                                                     "reason": "no publisher"}])


def lines(body, label):
    """The wikilink targets on a note's labelled link line, in order; [] when the line is absent."""
    for line in body.splitlines():
        if line.startswith(f"{label}: "):
            return re.findall(r"\[\[([^\]]+)\]\]", line)
    return []


class LinkLines(unittest.TestCase):
    def test_a_related_page_is_linked_by_the_title_of_its_first_section(self):
        pages = [page(related_concepts=["C-scales"]), page("C-scales", title="Neighbourhood scales")]
        notes, _, _ = export(pages)
        by_title = {fm["title"]: b for fm, b in notes.values()}
        self.assertEqual(lines(by_title["Neighbourliness — Field Use"], "Related"),
                         ["Neighbourhood scales — Definition"])
        self.assertEqual(lines(by_title["Neighbourhood scales — Field Use"], "Related"), [])

    def test_same_page_lists_the_other_notes_of_the_page(self):
        notes, _, _ = export([page()])
        by_title = {fm["title"]: b for fm, b in notes.values()}
        self.assertEqual(lines(by_title["Neighbourliness — Definition"], "Same page"), ["Neighbourliness — Field Use"])
        self.assertEqual(lines(by_title["Neighbourliness — Field Use"], "Same page"), ["Neighbourliness — Definition"])

    def test_sources_link_each_evidence_object_to_its_finding_note(self):
        findings_body = SOURCE_BODY + """
<a id="findings"></a>
## Findings

**F-001** — There is no consensus definition. → see S-youngfoundation2010-CONCEPT-001

**F-002** — A working definition combines three lenses. → see S-youngfoundation2010-FRAMEWORK-001
"""
        meta = [{"finding_id": "F-001", "finding_type": "concept-definition"},
                {"finding_id": "F-002", "finding_type": "framework-component"}]
        pages = [source(body=findings_body, findings=meta),
                 page(source_basis=[{"source_id": "S-youngfoundation2010",
                                     "object_id": "S-youngfoundation2010-FRAMEWORK-001"}]),
                 page("C-scales", title="Neighbourhood scales",
                      source_basis=[{"source_id": "S-youngfoundation2010", "finding_ids": ["F-001"]}])]
        notes, _, _ = export(pages)
        by_title = {fm["title"]: b for fm, b in notes.values()}
        b = by_title["Neighbourliness — Field Use"]
        self.assertEqual(lines(b, "Sources"), ["How can neighbourhoods be defined? — Finding F-002"])
        self.assertEqual(lines(b, "Related"), [], "a source is not a related page")
        self.assertEqual(lines(by_title["Neighbourhood scales — Definition"], "Sources"),
                         ["How can neighbourhoods be defined? — Finding F-001"])

    def test_sources_fall_back_to_the_summary_when_no_exported_finding_matches(self):
        body = SOURCE_BODY + """
<a id="findings"></a>
## Findings

**F-016** — Task seed: How to define the unit? → see S-youngfoundation2010-SEED-001
"""
        pages = [source(body=body, findings=[{"finding_id": "F-016", "finding_type": "task-seed"}]),
                 page(source_basis=[{"source_id": "S-youngfoundation2010",
                                     "object_id": "S-youngfoundation2010-SEED-001"}]),
                 page("C-scales", title="Neighbourhood scales",
                      source_basis=[{"source_id": "S-youngfoundation2010", "pages": [9, 10]}])]
        notes, _, _ = export(pages)
        by_title = {fm["title"]: b for fm, b in notes.values()}
        summary = "How can neighbourhoods be defined? — Summary"
        self.assertEqual(lines(by_title["Neighbourliness — Definition"], "Sources"), [summary])
        self.assertEqual(lines(by_title["Neighbourhood scales — Definition"], "Sources"), [summary])

    def test_tensions_come_from_known_tension_and_contradicts_edges(self):
        pages = [page(known_tensions=["KTN-boundary"], contradicts=["C-scales"], related_concepts=["C-scales"]),
                 page("KTN-boundary", ptype="known-tension", rel="07-known-tensions/KTN-boundary.md",
                      title="Boundary tension"),
                 page("C-scales", title="Neighbourhood scales")]
        notes, _, _ = export(pages)
        b = {fm["title"]: b for fm, b in notes.values()}["Neighbourliness — Field Use"]
        self.assertEqual(lines(b, "Tensions"), ["Boundary tension — Definition", "Neighbourhood scales — Definition"])
        self.assertEqual(lines(b, "Related"), ["Neighbourhood scales — Definition"])
        self.assertEqual([l.split(":")[0] for l in b.splitlines() if l.startswith(("Same page:", "Tensions:", "Related:"))],
                         ["Same page", "Tensions", "Related"], "FieldWise reads the lines in this order")

    def test_a_tension_row_is_linked_from_the_findings_and_pages_that_rest_on_its_related_objects(self):
        body = SOURCE_BODY + """
<a id="known-tensions"></a>
## Known Tensions

| Tension ID | First position | Source location | Conflicting position | Source location | Type | Why it matters | Related objects |
|---|---|---|---|---|---|---|---|
| S-youngfoundation2010-TNS-001 | Lived experience. | p. 9 | Administrative geography. | p. 10 | conceptual | Validity. | S-youngfoundation2010-FRAMEWORK-001, S-youngfoundation2010-TYPOLOGY-001 |

<a id="findings"></a>
## Findings

**F-001** — There is no consensus definition. → see S-youngfoundation2010-CONCEPT-001

**F-002** — A working definition combines three lenses. → see S-youngfoundation2010-FRAMEWORK-001
"""
        meta = [{"finding_id": "F-001", "finding_type": "concept-definition"},
                {"finding_id": "F-002", "finding_type": "framework-component"}]
        pages = [source(body=body, findings=meta),
                 page(source_basis=[{"source_id": "S-youngfoundation2010",
                                     "object_id": "S-youngfoundation2010-FRAMEWORK-001"}]),
                 page("C-scales", title="Neighbourhood scales",
                      source_basis=[{"source_id": "S-youngfoundation2010", "finding_ids": ["F-001"]}])]
        notes, _, _ = export(pages)
        by_title = {fm["title"]: b for fm, b in notes.values()}
        tension = "How can neighbourhoods be defined? — Tension TNS-001"
        self.assertEqual(lines(by_title["How can neighbourhoods be defined? — Finding F-002"], "Tensions"), [tension])
        self.assertEqual(lines(by_title["Neighbourliness — Field Use"], "Tensions"), [tension])
        self.assertEqual(lines(by_title["How can neighbourhoods be defined? — Finding F-001"], "Tensions"), [])
        self.assertEqual(lines(by_title["Neighbourhood scales — Definition"], "Tensions"), [])

    def test_links_to_missing_or_unexported_pages_are_dropped_and_reported(self):
        pages = [page(related_concepts=["C-scales", "C-draft", "C-ghost"]),
                 page("C-scales", title="Neighbourhood scales"),
                 page("C-draft", title="Draft idea", retrieval_status="draft", related_concepts=["C-ghost-2"])]
        notes, plan, _ = export(pages)
        b = {fm["title"]: b for fm, b in notes.values()}["Neighbourliness — Definition"]
        self.assertEqual(lines(b, "Related"), ["Neighbourhood scales — Definition"])
        self.assertEqual([d for d in plan.report["dropped_links"] if d["relation"] == "related_concept"], [
            {"from": "C-neighbourliness", "relation": "related_concept", "to": "C-draft", "reason": "not exported"},
            {"from": "C-neighbourliness", "relation": "related_concept", "to": "C-ghost", "reason": "unresolved"}])

    def test_a_body_link_is_rewritten_only_when_it_matches_a_valid_edge(self):
        body = """
<a id="definition"></a>
## Definition

It builds on [[neighbourhood-scales]] and [the scale rule](../09-decision-protocols/D-scale-rule.md).
It is not [[community-resilience-characteristics]] nor [a draft](../02-concepts/C-draft.md).

<a id="field-use"></a>
## Field Use

Read it as a progress indicator.
"""
        pages = [page(body=body, related_concepts=["C-scales"], related_tools=["D-scale-rule"]),
                 page("C-scales", rel="02-concepts/neighbourhood-scales.md", title="Neighbourhood scales"),
                 page("D-scale-rule", ptype="decision-protocol", rel="09-decision-protocols/D-scale-rule.md",
                      title="Scale rule"),
                 page("C-draft", title="Draft idea", retrieval_status="draft")]
        notes, plan, _ = export(pages)
        b = text({fm["title"]: b for fm, b in notes.values()}["Neighbourliness — Definition"])
        self.assertIn("It builds on [[Neighbourhood scales — Definition]] and "
                      "[[Scale rule — Definition|the scale rule]].", b)
        self.assertIn("It is not community resilience characteristics nor a draft.", b)
        self.assertEqual([d for d in plan.report["dropped_links"] if d["relation"] == "body"], [
            {"from": "C-neighbourliness", "relation": "body", "to": "community-resilience-characteristics",
             "reason": "no valid edge"},
            {"from": "C-neighbourliness", "relation": "body", "to": "../02-concepts/C-draft.md",
             "reason": "no valid edge"}])


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
