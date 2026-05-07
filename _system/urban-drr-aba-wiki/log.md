# Wiki Change Log

Append-only. Do not edit existing entries.

---

## [2026-05-07] structure | Wiki initialization

- Created Urban DRR + ABA LLM wiki root at _system/urban-drr-aba-wiki/
- Created all subdirectories: raw/, schema/, wiki/, outputs/, scripts/
- Copied 21 non-empty PDFs from Downloads/urban_tools/ to raw/pdf/
- Flagged 1 empty PDF: 2020-iasc-meeting-humanitarian-challenges-urban-areas-strategy.pdf (0 bytes)
- Copied 2 v2 duplicate PDFs (same SHA256 as primary versions)
- Copied spreadsheet urban_ABA_DRR_matrix_UPDATED.xlsx to raw/spreadsheets/
- Copied source_metadata.csv to raw/spreadsheets/
- Created source catalog from 46-row spreadsheet
- Created core files: README.md, CLAUDE.md, AGENTS.md, index.md, log.md
- Created 8 schema files
- Created 3 overview pages
- Created 9 agent prompt pages
- Created 4 script placeholders
- Preserved all existing vault content (no modifications outside _system/)
- Git status: vault is existing repo on main branch
- Note: PDF text extraction skipped — mark all raw/extracted/ as TODO
- Open issues: 2020-iasc PDF is empty; extraction needed for all 21 PDFs

---

## [2026-05-07] content | Source pages created (WU-2)

- Created 18 source pages in wiki/01-sources/ — one per document from source_metadata.csv
- Flagged 2020-iasc source page status as `not-started` (PDF is 0 bytes)
- Source pages include: title, year, authors, PDF path, source URL, lifecycle stages covered, key themes, status

---

## [2026-05-07] content | Concept pages and framework pages created (WU-3)

- Created 18 concept pages in wiki/02-concepts/ — stub format with purpose and TODO[agent] markers
- Created 9 framework pages in wiki/03-frameworks/ — stub format
- Concepts include: area-based-approach, resilience, urban-systems-thinking, hevc, service-functionality, etc.
- Frameworks include: ABA decision framework, area selection, coordination, integrated strategy, etc.

---

## [2026-05-07] content | Tool #01 fully populated (WU-3)

- Created wiki/04-tools/01-aba-feasibility-and-necessity-assessment-tool.md — FULLY POPULATED
- 9 modules: context-scoping, preliminary-risk-profile, population-analysis, service-systems-mapping, coordination-landscape, community-engagement-readiness, feasibility-stress-test, synthesis-scoring, decision-recommendation
- Scoring model: 0–2 scale per module, total 0–18, decision thresholds defined
- 12 output documents defined
- Field instruments: all 12 instruments for Tool #01 fully populated (separate pages)
- Instruments: rapid-area-observation-form, 6x KII guides, hevc-matrix, service-functionality-mapping-sheet, stakeholder-5w-mapping-form, household-mini-survey, operational-feasibility-checklist

---

## [2026-05-07] content | Remaining tool stubs, sector, coordination pages created (WU-4)

- Created 16 tool stubs: wiki/04-tools/02 through wiki/04-tools/17
- Created 2 additional field instrument stubs: participatory-mapping-guide, duplication-gap-analysis-matrix
- Created 11 lifecycle pages in wiki/06-lifecycle/
- Created 11 sector application pages in wiki/07-sector-applications/
- Created 10 coordination pages in wiki/08-coordination/
- All pages include: frontmatter, purpose section, decision questions/core questions, TODO[agent] markers for all content sections, source foundation links

---

## [2026-05-07] content | MEL, transition, and risks pages created (WU-4 finalization)

- Created 6 MEL pages in wiki/09-monitoring-learning/: area-based-mel-framework, community-resilience-indicators, area-based-reassessment-tool, outcome-harvesting-case-study-template, sendai-municipal-drr-progress-review, adaptive-management-triggers
- Created 4 transition/scale pages in wiki/10-transition-scale/: handover-readiness-checklist, municipal-integration-plan, replication-scale-up-learning-note, build-back-better-recovery-alignment-tool
- Created 7 risks/contradictions pages in wiki/12-risks-contradictions/: known-contradictions, weak-evidence-claims, unresolved-questions, stale-guidance-watchlist, common-aba-misuse, protection-and-do-no-harm-risks, evidence-gaps-to-fill
- evidence-gaps-to-fill.md includes CRITICAL entry for 0-byte 2020-iasc PDF and all duplicate source pairs

---

## [2026-05-07] quality | Lint report generated

- Created outputs/wiki-lint-report.md — manual lint pass
- 1 CRITICAL: 0-byte PDF (2020-iasc)
- 8 WARNINGs: PDF extraction not done; agent completion pending for WU-2/3; stubs for most content
- 14 INFOs: Stub pages with all sections as TODO (expected at this scope)
- 80% structural pass estimated

---

## [2026-05-07] navigation | index.md updated to comprehensive catalog

- Updated index.md with full navigable catalog of all ~176 pages
- Sections: overview, sources, concepts, frameworks, tools, field instruments, lifecycle, sectors, coordination, MEL, transition, risks, agent prompts, schema
- Critical flags section added for agents: 0-byte PDF, no extraction, stub pages, contradictions, tool quality

---

## [2026-05-07] summary | Wiki v0.1.0 creation complete

Total pages created: ~176
- 4 overview pages
- 18 source pages
- 18 concept pages (stubs)
- 9 framework pages (stubs)
- 17 tool pages (Tool #01 fully populated; 02–17 stubs)
- 18 field instrument pages (Tool #01 instruments fully populated; others stubs)
- 11 lifecycle pages (stubs)
- 21 sector application pages (11 core + 10 additional from parallel agents)
- 19 coordination pages (10 core + 9 additional from parallel agents)
- 11 MEL pages (6 core + 5 additional from parallel agents)
- 8 transition pages (4 core + 4 additional from parallel agents)
- 13 risks/contradictions pages (7 core + 6 additional from parallel agents)
- 9 agent prompt pages (fully operational)
- 8 schema files
- 5 root files (README, CLAUDE, AGENTS, index, log)

Known gaps:
- 2020-iasc PDF is 0 bytes (CRITICAL)
- PDF text extraction not performed for any source
- All source pages remain status: not-started pending extraction
- Tools #02–17 are stubs pending further population
- scripts/ are placeholders — lint_wiki.py, extract_text.py, rebuild_index.py not built

Next steps:
1. Replace 0-byte IASC 2020 PDF
2. Build and run extraction script
3. Populate priority tools (#02–05 most referenced)
4. Run automated lint after scripts built

---

## [2026-05-07] efficiency | Cold-agent navigation layer added

Added three quick-reference files to reduce token cost for cold agents answering common questions:
- wiki/00-overview/qa-common-questions.md — 10 pre-answered common field questions (1-file read → complete answer)
- wiki/00-overview/aba-definition-one-pager.md — self-contained ABA definition, misuse table, pushback questions
- wiki/00-overview/tool-01-quick-reference.md — compact scoring model, 5 screening questions, decision table (~60 lines)
- wiki/index.md (vault root) — added Urban DRR + ABA section surfacing these entry points

Trigger: fresh agent required 4-step navigation and 749-line tool read to answer "we work in one neighborhood, so we're area-based" — now answered in qa-common-questions.md Q2 directly.

---

## [2026-05-07] ingest | Parker & Maynard 2015 — first full source extraction

Source: Humanitarian Response to Urban Crises: A Review of Area-Based Approaches (IIED, 2015)

Actions:
- raw/extracted/2015-parker-maynard-humanitarian-response-urban-crises-aba-review.md — 28-page PDF extracted via PyMuPDF (105K characters)
- wiki/01-sources/2015-parker-maynard-...: status changed copied → ingested
- All TODO[agent] sections populated: 3 ABA criteria with page refs, Box 2/3/4/5/6 content, 5 case studies (Kabul/Port-au-Prince x2/Baghdad/Tacloban), 8 good-practice principles, positive/negative consequences, coordination and DRR implications, limitations, citable claims with page numbers, concept and tool links

Status: source page fully ingested. Concept/lifecycle pages not yet updated from this source (pending).

---

## [2026-05-07] schema | Enforce .md-only file format rule

- All vault files must use .md extension — Obsidian does not render .txt
- raw/extracted/ file renamed from .txt → .md
- schema/ingest-rules.md step 5 and status definitions updated to specify .md explicitly
- CLAUDE.md: file format rule added at top of operating instructions
- wiki/01-sources/...: extracted_text pointer updated to .md path

---

## [2026-05-07] ingest | Parker & Maynard 2015 — downstream pages updated (ingest steps 7-13)

Completed remaining ingest steps for Parker & Maynard (2015):

**Concept pages updated (draft → active):**
- wiki/02-concepts/area-based-approach — full evidence base, practical implications, ABA vs alternatives, 8 good-practice principles, common mistakes, known risks
- wiki/02-concepts/geographic-targeting — boundary types (administrative/physical), scale, field data requirements, common mistakes
- wiki/02-concepts/participation-in-urban-response — community-driven vs. informed distinction, PASSA reference, timeline requirements, inclusion requirements
- wiki/02-concepts/urban-displacement-vulnerability — IDP/host community inclusive targeting evidence (NRC Baghdad)
- wiki/02-concepts/stakeholder-power-mapping — multi-level facilitation model, humanitarian facilitator role

**Lifecycle pages updated (draft → active):**
- wiki/06-lifecycle/00-appropriateness-decision — key decisions, required evidence table, minimum outputs, quality checks, 5 failure modes

**Risk pages updated (stub → active):**
- wiki/12-risks-contradictions/common-aba-misuse — 6 patterns with detection and corrective action
- wiki/12-risks-contradictions/protection-and-do-no-harm-risks — 6 risk categories with evidence, populations, warnings, mitigation, halt criteria

**Index updated:** Parker & Maynard 2015 marked ✅ INGESTED

Remaining not yet updated from this source (pending other source ingests):
- wiki/02-concepts/multi-sector-response-analysis (Parker & Maynard is secondary source here)
- wiki/03-frameworks/ pages (framework stubs not yet populated)
- wiki/05-field-instruments/ (no new instruments implied by this source beyond existing Tool #01 set)

---

## [2026-05-07] schema | Enforce wiki synthesis as source of truth

**Problem identified via agent test:** Cold agent navigated to raw/extracted/ to get "definitive answer" on boundary types, bypassing wiki/02-concepts/geographic-targeting.md which already contained the synthesised answer. Root cause: query-rules.md step 4 ("use source pages for citation support") was ambiguous — agents interpreted it as permission to read raw extracted text.

**Fix:**
- CLAUDE.md: added explicit layer discipline section at top — raw/ is ingest input only, never queried; wiki/ is canonical answer source; wiki/01-sources/ is citation metadata only
- schema/query-rules.md: added three-layer rule table; rewrote answer steps 1-5 to be unambiguous; explicit prohibition on going to raw/ to fill wiki gaps

**Rule:** If wiki/ content is insufficient, flag the gap — do not bypass the synthesis layer.

---

## [2026-05-07] schema | Fix agent read path — layer discipline in index.md and query workflow

**Problem:** Rules in CLAUDE.md and schema/ files are never in the actual agent read chain. Cold agents follow: 00_Start_Here.md → workflows/query.md → wiki/index.md. The vault-level workflows/query.md explicitly told agents to verify accuracy-critical claims against raw sources — causing agents to bypass the wiki synthesis layer.

**Fix:**
- _system/urban-drr-aba-wiki/index.md: layer discipline rule added at the very top as a mandatory pre-read. Agents see this the moment they enter the wiki. Explicitly overrides vault-level "verify against raw" instruction.
- workflows/query.md: sub-wiki exception added to the Notes section — when a sub-wiki maintains its own wiki/ synthesis layer, that wiki/ is the answer source.

**Principle:** Rules only work if they're in the path agents actually walk. Schema files document; index.md enforces.
