# Urban DRR + ABA LLM Wiki — Master Index

> Audit catalog. Agents answering domain questions use section `00_index.md` files for navigation. Use this file during ingest and lint to verify page registration and completeness. All pages have YAML frontmatter with `wiki_id`, `status`, and `source_foundation` fields.

---

## How to answer questions from this wiki — read before doing anything else

**Audit use only for navigation.** Agents answering domain questions use `00_index.md` files in each section folder for navigation. Use this file during ingest (to register new pages) and lint (to check completeness and orphans).

This wiki has a three-layer architecture. Each layer has a single role:

| Layer | Location | Role |
|---|---|---|
| Raw | `../raw/pdf/`, `../raw/extracted/` | Ingest input only |
| **Synthesis** | **`wiki/`** | **Your answer source — read this** |
| Schema | `schema/`, `CLAUDE.md` | Operating rules |

**Answer questions from `wiki/` pages only.** Do not open `../raw/extracted/` or `../raw/pdf/` to answer or verify a question — those files are input to the wiki, not output from it. The synthesis in `wiki/` is the processed, validated, agent-ready knowledge.

- `./01sources/` pages = citation metadata (author, year, page number) only
- If a `wiki/` page is incomplete or has TODO markers → state the gap, do not go to `../raw/` to fill it

This rule overrides any vault-level instruction to verify claims against raw sources.

---

**Wiki version**: 0.1.0 | **Created**: 2026-05-07 | **Total pages**: ~176

---

## Overview and Navigation (./00overview/)

- [[./00overview/urban-drr-aba-knowledge-map]] — Knowledge architecture and navigation guide
- [[./00overview/how-to-use-this-wiki]] — Instructions for agents and human users
- [[./00overview/agent-operating-model]] — How agents interact with this wiki
- [[./00overview/agent-contract]] — Canonical operating contract and conflict-resolution order
- [[./00overview/source-catalog-from-matrix]] — Full 46-row source catalog from spreadsheet

---

## Source Pages (./01sources/) — 18 pages

Primary literature underpinning all wiki content. Each page links to its raw PDF and extracted text (when available).

- [[./01sources/2007-twigg-characteristics-disaster-resilient-community-framework]]
- [[./01sources/2010-iasc-meeting-humanitarian-challenges-urban-areas-strategy]]
- [[./01sources/2013-worldbank-gfdrr-building-urban-resilience-principles-tools-practice-handbook]]
- [[./01sources/2015-parker-maynard-humanitarian-response-urban-crises-aba-review]] ✅ INGESTED — text extracted, source page fully populated, concept/lifecycle/risk pages updated
- [[./01sources/2015-undrr-sendai-framework-drr-2015-2030-framework]]
- [[./01sources/2016-campbell-stepping-back-understanding-cities-systems-guide]]
- [[./01sources/2017-ifrc-building-urban-resilience-guide]]
- [[./01sources/2017-irc-urban-context-analysis-toolkit-guidance-note]]
- [[./01sources/2017-mohiddin-smith-phelps-urban-response-analysis-framework]]
- [[./01sources/2017-sanderson-sitko-urban-area-based-approaches-post-disaster-guide]]
- [[./01sources/2017-undrr-how-to-make-cities-more-resilient-handbook]]
- [[./01sources/2019-alnap-barrio-mio-katye-neighbourhood-approach-cities-case-study]]
- [[./01sources/2019-alnap-global-practice-review-urban-humanitarian-response]]
- [[./01sources/2019-gsc-uswg-area-based-approaches-urban-settings-compendium]]
- [[./01sources/2019-reach-unhcr-area-based-assessment-key-informants-practical-guide]]
- [[./01sources/2020-iasc-meeting-humanitarian-challenges-urban-areas-strategy]] ⚠️ SOURCE FILE IS 0 BYTES
- [[./01sources/2026-iasc-standard-terms-reference-area-based-coordination]]
- [[./01sources/undated-stronger-cities-consortium-umvat-guidance-note]]

---

## Concept Pages (./02concepts/) — 19 pages

Core concepts that appear across multiple tools, frameworks, and lifecycle stages.

- [[./02concepts/aba-definition-one-pager]] — Quick-reference summary: what ABA is, what it isn't, how to push back on misuse
- [[./02concepts/area-based-approach]]
- [[./02concepts/area-based-coordination]]
- [[./02concepts/build-back-better]]
- [[./02concepts/geographic-targeting]]
- [[./02concepts/hazard-exposure-vulnerability-capacity]]
- [[./02concepts/implementation-sequencing]]
- [[./02concepts/local-resource-leverage]]
- [[./02concepts/multi-sector-response-analysis]]
- [[./02concepts/municipal-risk-governance]]
- [[./02concepts/neighborhood-boundaries]]
- [[./02concepts/participation-in-urban-response]]
- [[./02concepts/protection-do-no-harm]]
- [[./02concepts/resilience]]
- [[./02concepts/service-functionality]]
- [[./02concepts/stakeholder-power-mapping]]
- [[./02concepts/urban-displacement-vulnerability]]
- [[./02concepts/urban-risk]]
- [[./02concepts/urban-systems-thinking]]

---

## Framework Pages (./03frameworks/) — 9 pages

Analytical frameworks that structure decision-making across the ABA/DRR lifecycle.

- [[./03frameworks/aba-appropriateness-decision-framework]]
- [[./03frameworks/area-based-coordination-framework]]
- [[./03frameworks/area-selection-framework]]
- [[./03frameworks/implementation-adaptation-framework]]
- [[./03frameworks/integrated-area-strategy-framework]]
- [[./03frameworks/joint-prioritization-framework]]
- [[./03frameworks/neighborhood-diagnosis-framework]]
- [[./03frameworks/transition-handover-framework]]
- [[./03frameworks/urban-drr-response-design-framework]]

---

## Tool Pages (./04tools/) — 17 pages

Operational tools for evidence collection, analysis, and decision-making. Tool #01 is fully populated. Tools #02–17 are stubs.

- [[./04tools/01-aba-feasibility-and-necessity-assessment-tool]] ✅ FULLY POPULATED — 9 modules, scoring model, 12 outputs
- [[./04tools/02-area-selection-matrix]] — stub
- [[./04tools/03-settlement-neighborhood-boundary-definition-tool]] — stub
- [[./04tools/04-urban-systems-diagnosis-tool]] — stub
- [[./04tools/05-hevc-risk-mapping-tool]] — stub
- [[./04tools/06-stakeholder-coordination-mapping-tool]] — stub
- [[./04tools/07-community-engagement-platform-tool]] — stub
- [[./04tools/08-joint-risk-needs-prioritization-matrix]] — stub
- [[./04tools/09-response-option-comparison-matrix]] — stub
- [[./04tools/10-integrated-area-strategy-builder]] — stub
- [[./04tools/11-sector-technical-design-checklist]] — stub
- [[./04tools/12-implementation-sequencing-dependency-map]] — stub
- [[./04tools/13-area-coordination-dashboard]] — stub
- [[./04tools/14-accountability-feedback-tracker]] — stub
- [[./04tools/15-referral-pathway-tracker]] — stub
- [[./04tools/16-area-based-mel-adaptation-framework]] — stub
- [[./04tools/17-handover-scale-up-checklist]] — stub

---

## Field Instrument Pages (./05field-instruments/) — 18 pages

Data collection instruments and templates. Instruments for Tool #01 are fully populated. Others are stubs.

**Fully populated instruments (16):**
- [[./05field-instruments/rapid-area-observation-form]] ✅
- [[./05field-instruments/transect-walk-observation-form]] ✅
- [[./05field-instruments/household-mini-survey]] ✅
- [[./05field-instruments/kii-guide-municipality]] ✅
- [[./05field-instruments/kii-guide-service-provider]] ✅
- [[./05field-instruments/kii-guide-community-leaders]] ✅
- [[./05field-instruments/kii-guide-ngos-cbos]] ✅
- [[./05field-instruments/kii-guide-market-actors]] ✅
- [[./05field-instruments/kii-guide-protection-actors]] ✅
- [[./05field-instruments/service-functionality-mapping-sheet]] ✅
- [[./05field-instruments/stakeholder-5w-mapping-form]] ✅
- [[./05field-instruments/local-resource-inventory]] ✅
- [[./05field-instruments/hazard-exposure-vulnerability-capacity-matrix]] ✅
- [[./05field-instruments/participation-feasibility-checklist]] ✅
- [[./05field-instruments/operational-feasibility-checklist]] ✅
- [[./05field-instruments/decision-memo-template]] ✅ (required ABA decision output)

**Structured stubs (2):**
- [[./05field-instruments/participatory-mapping-guide]] — structured stub
- [[./05field-instruments/duplication-gap-analysis-matrix]] — structured stub

---

## Lifecycle Pages (./06lifecycle/) — 11 pages

Programme phases from appropriateness decision through transition and handover.

- [[./06lifecycle/00-appropriateness-decision]] — Stage 0: Is ABA appropriate?
- [[./06lifecycle/01-area-selection-boundary-definition]] — Stage 1: Select target area
- [[./06lifecycle/02-area-profile-systems-diagnosis]] — Stage 2: Diagnose area systems
- [[./06lifecycle/03-community-stakeholder-engagement]] — Stage 3: Engage community and stakeholders
- [[./06lifecycle/04-joint-risk-needs-prioritization]] — Stage 4: Prioritise risks and needs
- [[./06lifecycle/05-integrated-area-strategy]] — Stage 5: Develop integrated strategy
- [[./06lifecycle/06-program-design-modality-selection]] — Stage 6: Design programme and select modalities
- [[./06lifecycle/07-detailed-technical-design]] — Stage 7: Technical design
- [[./06lifecycle/08-area-based-implementation]] — Stage 8: Implement
- [[./06lifecycle/09-monitoring-learning-adaptation]] — Stage 9: Monitor, learn, adapt
- [[./06lifecycle/10-transition-handover-scaling]] — Stage 10: Transition, hand over, or scale

---

## Sector Application Pages (./07sector-applications/) — 11 pages (core)

How ABA/DRR principles apply within specific humanitarian and development sectors.

- [[./07sector-applications/shelter-settlements]]
- [[./07sector-applications/wash]]
- [[./07sector-applications/health]]
- [[./07sector-applications/livelihoods-markets]]
- [[./07sector-applications/protection-mainstreaming]]
- [[./07sector-applications/education]]
- [[./07sector-applications/food-and-fsl]]
- [[./07sector-applications/urban-governance]]
- [[./07sector-applications/drainage-flood-risk]]
- [[./07sector-applications/solid-waste]]
- [[./07sector-applications/preparedness-early-warning]]

> Note: Additional sector pages exist in this folder (shelter-nfi, cva-market-based-response, drr-integration, health-service-access, livelihoods, protection, roads-access-mobility, social-cohesion, tenure-eviction-risk, urban-land-tenure) — created by parallel agents.

---

## Coordination Pages (./08coordination/) — 10 pages (core)

Structures, tools, and protocols for multi-actor area-based coordination.

- [[./08coordination/area-based-coordination-model]]
- [[./08coordination/area-platform-setup]]
- [[./08coordination/cluster-vs-area-coordination]]
- [[./08coordination/municipal-engagement]]
- [[./08coordination/cbo-local-actor-engagement]]
- [[./08coordination/information-management]]
- [[./08coordination/4w-5w-management]]
- [[./08coordination/coordination-meeting-brief-template]] ✅ template with actual content
- [[./08coordination/decision-log-template]] ✅ template with actual content
- [[./08coordination/actor-responsibility-matrix]] ✅ template with actual content

> Note: Additional coordination pages exist in this folder — created by parallel agents.

---

## Monitoring, Evaluation and Learning Pages (./09monitoring-learning/) — 6 pages (core)

MEL frameworks, indicator sets, and adaptive management tools.

- [[./09monitoring-learning/area-based-mel-framework]]
- [[./09monitoring-learning/community-resilience-indicators]]
- [[./09monitoring-learning/area-based-reassessment-tool]]
- [[./09monitoring-learning/outcome-harvesting-case-study-template]]
- [[./09monitoring-learning/sendai-municipal-drr-progress-review]]
- [[./09monitoring-learning/adaptive-management-triggers]]

> Note: Additional MEL pages exist in this folder — created by parallel agents.

---

## Transition and Scale Pages (./10transition-scale/) — 4 pages (core)

Tools and protocols for programme exit, handover, and scale-up.

- [[./10transition-scale/handover-readiness-checklist]]
- [[./10transition-scale/municipal-integration-plan]]
- [[./10transition-scale/replication-scale-up-learning-note]]
- [[./10transition-scale/build-back-better-recovery-alignment-tool]]

> Note: Additional transition pages exist in this folder — created by parallel agents.

---

## Risks and Contradictions (./12risks-contradictions/) — 7 pages (core)

Critical analysis layer. Agents must consult before making claims.

- [[./12risks-contradictions/known-contradictions]] — Conflicting recommendations across sources
- [[./12risks-contradictions/weak-evidence-claims]] — Widely-cited claims with thin evidence
- [[./12risks-contradictions/unresolved-questions]] — Open questions the literature has not settled
- [[./12risks-contradictions/stale-guidance-watchlist]] — Potentially outdated guidance
- [[./12risks-contradictions/common-aba-misuse]] — Recurring misapplication patterns
- [[./12risks-contradictions/protection-and-do-no-harm-risks]] — Protection risks specific to ABA
- [[./12risks-contradictions/evidence-gaps-to-fill]] ⚠️ READ THIS — 0-byte PDF, missing sources, TODO items

> Note: Additional risk pages exist in this folder — created by parallel agents.

---

## Agent Prompt Pages (./13agent-prompts/) — 10 pages

Reusable operational prompts for AI agents working with this wiki.

- [[./13agent-prompts/ingest-new-source]] — How to ingest a new source document
- [[./13agent-prompts/query-wiki]] — How to answer a domain question using the wiki
- [[./13agent-prompts/lint-wiki]] — How to run a wiki quality check
- [[./13agent-prompts/run-manual-lint-checklist]] — Command-based fallback lint workflow
- [[./13agent-prompts/build-new-tool-from-sources]] — How to build a new tool page from source material
- [[./13agent-prompts/generate-field-instrument]] — How to create a field instrument for a tool
- [[./13agent-prompts/create-decision-memo]] — How to create a decision memo for a field team
- [[./13agent-prompts/detect-duplication-and-gaps]] — How to identify coverage gaps and response duplication
- [[./13agent-prompts/review-tool-quality]] — How to validate a tool page against quality standard
- [[./13agent-prompts/update-crosslinks]] — How to update cross-references across wiki pages

---

## Schema Files (schema/) — 8 files

Operating rules for the wiki. Agents must follow these rules when reading, writing, or updating wiki content.

- [[schema/page-types]] — Defined page types and required fields
- [[schema/ingest-rules]] — Rules for adding new source documents
- [[schema/query-rules]] — Rules for answering questions from the wiki
- [[schema/lint-rules]] — Quality rules for wiki validation
- [[schema/citation-rules]] — How to cite sources in wiki pages
- [[schema/naming-conventions]] — File naming rules
- [[schema/frontmatter-schema]] — Required YAML frontmatter fields by page type
- [[schema/tool-quality-standard]] — Evidence-to-decision standard for tool pages

---

## Key Documents

| File | Purpose |
|------|---------|
| [[README]] | Human-readable orientation |
| [[CLAUDE.md]] | Instructions for Claude agents |
| [[AGENTS.md]] | Multi-agent operating model |
| [[log]] | Creation and update history |
| [[outputs/wiki-lint-report]] | Quality assurance report |

---

## Critical Flags for Agents

1. **0-byte PDF**: `2020-iasc` source file is empty — do not cite it. See [[./12risks-contradictions/evidence-gaps-to-fill]].
2. **Partial ingestion state**: Some source pages are still metadata-first, while selected pages are ingested. Verify page-level status before relying on narrative synthesis.
3. **Stub pages**: Tools #02–17 and many concept/framework/coordination pages are still stubs — do not present stub content as vetted guidance.
4. **Contradictions**: Check [[./12risks-contradictions/known-contradictions]] before generating recommendations.
5. **Tool #01 only**: Only Tool #01 meets the tool quality standard. Use it as the reference for what a complete tool page looks like.
