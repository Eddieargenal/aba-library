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

- [[./00-overview/urban-drr-aba-knowledge-map]] — Knowledge architecture and navigation guide
- [[./00-overview/how-to-use-this-wiki]] — Instructions for agents and human users
- [[./00-overview/agent-operating-model]] — How agents interact with this wiki
- [[./00-overview/agent-contract]] — Canonical operating contract and conflict-resolution order
- [[./00-overview/source-catalog-from-matrix]] — Full 46-row source catalog from spreadsheet

---

## Source Pages (./01-sources/extracted/) — 18 pages

Primary literature underpinning all wiki content. Each page links to its raw PDF and extracted text (when available).

- [[2009_twigg_characteristics-disaster-resilient-community]]
- [[./01-sources/extracted/2010_iasc_meeting-humanitarian-challenges-urban-areas-strategy]]
- [[./01-sources/extracted/2013_worldbank-gfdrr_building-urban-resilience-principles-tools-practice-handbook]]
- [[./01-sources/extracted/2015_parker-maynard_humanitarian-response-urban-crises-aba-review]] ✅ INGESTED — text extracted, source page fully populated, concept/lifecycle/risk pages updated
- [[./01-sources/extracted/2015_undrr_sendai-framework-drr-2015-2030-framework]]
- [[./01-sources/extracted/2016_campbell_stepping-back-understanding-cities-systems-guide]]
- [[./01-sources/extracted/2017_ifrc_building-urban-resilience-guide]]
- [[./01-sources/extracted/2017_irc_urban-context-analysis-toolkit-guidance-note]]
- [[./01-sources/extracted/2017_mohiddin-smith-phelps_urban-response-analysis-framework]]
- [[./01-sources/extracted/2017_sanderson-sitko_urban-area-based-approaches-post-disaster-guide]]
- [[./01-sources/extracted/2017_undrr_how-to-make-cities-more-resilient-handbook]]
- [[./01-sources/extracted/2019_alnap_barrio-mio-katye-neighbourhood-approach-cities-case-study]]
- [[./01-sources/extracted/2019_alnap_global-practice-review-urban-humanitarian-response]]
- [[./01-sources/extracted/2019_gsc-uswg_area-based-approaches-urban-settings-compendium]]
- [[./01-sources/extracted/2019_reach-unhcr_area-based-assessment-key-informants-practical-guide]]
- [[./01-sources/extracted/2020_iasc_meeting-humanitarian-challenges-urban-areas-strategy]] ⚠️ SOURCE FILE IS 0 BYTES
- [[./01-sources/extracted/2026_iasc_standard-terms-reference-area-based-coordination]]
- [[./01-sources/extracted/0000_stronger-cities-consortium_umvat-guidance-note]]

---

## Concept Pages (./02-concepts/) — 19 pages

Core concepts that appear across multiple tools, frameworks, and lifecycle stages.

- [[./02-concepts/aba-definition-one-pager]] — Quick-reference summary: what ABA is, what it isn't, how to push back on misuse
- [[./02-concepts/area-based-approach]]
- [[./02-concepts/area-based-coordination]]
- [[./02-concepts/build-back-better]]
- [[./02-concepts/geographic-targeting]]
- [[./02-concepts/hazard-exposure-vulnerability-capacity]]
- [[./02-concepts/implementation-sequencing]]
- [[./02-concepts/local-resource-leverage]]
- [[./02-concepts/multi-sector-response-analysis]]
- [[./02-concepts/municipal-risk-governance]]
- [[./02-concepts/neighborhood-boundaries]]
- [[./02-concepts/participation-in-urban-response]]
- [[./02-concepts/protection-do-no-harm]]
- [[./02-concepts/resilience]]
- [[./02-concepts/service-functionality]]
- [[./02-concepts/stakeholder-power-mapping]]
- [[./02-concepts/urban-displacement-vulnerability]]
- [[./02-concepts/urban-risk]]
- [[./02-concepts/urban-systems-thinking]]

---

## Framework Pages (./03-frameworks/) — 9 pages

Analytical frameworks that structure decision-making across the ABA/DRR lifecycle.

- [[./03-frameworks/aba-appropriateness-decision-framework]]
- [[./03-frameworks/area-based-coordination-framework]]
- [[./03-frameworks/area-selection-framework]]
- [[./03-frameworks/implementation-adaptation-framework]]
- [[./03-frameworks/integrated-area-strategy-framework]]
- [[./03-frameworks/joint-prioritization-framework]]
- [[./03-frameworks/neighborhood-diagnosis-framework]]
- [[./03-frameworks/transition-handover-framework]]
- [[./03-frameworks/urban-drr-response-design-framework]]

---

## Tool Pages (./04-tools/) — 17 pages

Operational tools for evidence collection, analysis, and decision-making. Tool #01 is fully populated. Tools #02–17 are stubs.

- [[./04-tools/01-aba-feasibility-and-necessity-assessment-tool]] ✅ FULLY POPULATED — 9 modules, scoring model, 12 outputs
- [[./04-tools/02-area-selection-matrix]] — stub
- [[./04-tools/03-settlement-neighborhood-boundary-definition-tool]] — stub
- [[./04-tools/04-urban-systems-diagnosis-tool]] — stub
- [[./04-tools/05-hevc-risk-mapping-tool]] — stub
- [[./04-tools/06-stakeholder-coordination-mapping-tool]] — stub
- [[./04-tools/07-community-engagement-platform-tool]] — stub
- [[./04-tools/08-joint-risk-needs-prioritization-matrix]] — stub
- [[./04-tools/09-response-option-comparison-matrix]] — stub
- [[./04-tools/10-integrated-area-strategy-builder]] — stub
- [[./04-tools/11-sector-technical-design-checklist]] — stub
- [[./04-tools/12-implementation-sequencing-dependency-map]] — stub
- [[./04-tools/13-area-coordination-dashboard]] — stub
- [[./04-tools/14-accountability-feedback-tracker]] — stub
- [[./04-tools/15-referral-pathway-tracker]] — stub
- [[./04-tools/16-area-based-mel-adaptation-framework]] — stub
- [[./04-tools/17-handover-scale-up-checklist]] — stub

---

## Field Instrument Pages (./05-field-instruments/) — 18 pages

Data collection instruments and templates. Instruments for Tool #01 are fully populated. Others are stubs.

**Fully populated instruments (16):**
- [[./05-field-instruments/rapid-area-observation-form]] ✅
- [[./05-field-instruments/transect-walk-observation-form]] ✅
- [[./05-field-instruments/household-mini-survey]] ✅
- [[./05-field-instruments/kii-guide-municipality]] ✅
- [[./05-field-instruments/kii-guide-service-provider]] ✅
- [[./05-field-instruments/kii-guide-community-leaders]] ✅
- [[./05-field-instruments/kii-guide-ngos-cbos]] ✅
- [[./05-field-instruments/kii-guide-market-actors]] ✅
- [[./05-field-instruments/kii-guide-protection-actors]] ✅
- [[./05-field-instruments/service-functionality-mapping-sheet]] ✅
- [[./05-field-instruments/stakeholder-5w-mapping-form]] ✅
- [[./05-field-instruments/local-resource-inventory]] ✅
- [[./05-field-instruments/hazard-exposure-vulnerability-capacity-matrix]] ✅
- [[./05-field-instruments/participation-feasibility-checklist]] ✅
- [[./05-field-instruments/operational-feasibility-checklist]] ✅
- [[./05-field-instruments/decision-memo-template]] ✅ (required ABA decision output)

**Structured stubs (2):**
- [[./05-field-instruments/participatory-mapping-guide]] — structured stub
- [[./05-field-instruments/duplication-gap-analysis-matrix]] — structured stub

---

## Lifecycle Pages (./06-lifecycle/) — 11 pages

Programme phases from appropriateness decision through transition and handover.

- [[./06-lifecycle/00-appropriateness-decision]] — Stage 0: Is ABA appropriate?
- [[./06-lifecycle/01-area-selection-boundary-definition]] — Stage 1: Select target area
- [[./06-lifecycle/02-area-profile-systems-diagnosis]] — Stage 2: Diagnose area systems
- [[./06-lifecycle/03-community-stakeholder-engagement]] — Stage 3: Engage community and stakeholders
- [[./06-lifecycle/04-joint-risk-needs-prioritization]] — Stage 4: Prioritise risks and needs
- [[./06-lifecycle/05-integrated-area-strategy]] — Stage 5: Develop integrated strategy
- [[./06-lifecycle/06-program-design-modality-selection]] — Stage 6: Design programme and select modalities
- [[./06-lifecycle/07-detailed-technical-design]] — Stage 7: Technical design
- [[./06-lifecycle/08-area-based-implementation]] — Stage 8: Implement
- [[./06-lifecycle/09-monitoring-learning-adaptation]] — Stage 9: Monitor, learn, adapt
- [[./06-lifecycle/10-transition-handover-scaling]] — Stage 10: Transition, hand over, or scale

---

## Sector Application Pages (./07sector-applications/) — 11 pages (core)

How ABA/DRR principles apply within specific humanitarian and development sectors.

- [[./07-sector-applications/shelter-settlements]]
- [[./07-sector-applications/wash]]
- [[./07-sector-applications/health]]
- [[./07-sector-applications/livelihoods-markets]]
- [[./07-sector-applications/protection-mainstreaming]]
- [[./07-sector-applications/education]]
- [[./07-sector-applications/food-and-fsl]]
- [[./07-sector-applications/urban-governance]]
- [[./07-sector-applications/drainage-flood-risk]]
- [[./07-sector-applications/solid-waste]]
- [[./07-sector-applications/preparedness-early-warning]]

> Note: Additional sector pages exist in this folder (shelter-nfi, cva-market-based-response, drr-integration, health-service-access, livelihoods, protection, roads-access-mobility, social-cohesion, tenure-eviction-risk, urban-land-tenure) — created by parallel agents.

---

## Coordination Pages (./08-coordination/) — 10 pages (core)

Structures, tools, and protocols for multi-actor area-based coordination.

- [[./08-coordination/area-based-coordination-model]]
- [[./08-coordination/area-platform-setup]]
- [[./08-coordination/cluster-vs-area-coordination]]
- [[./08-coordination/municipal-engagement]]
- [[./08-coordination/cbo-local-actor-engagement]]
- [[./08-coordination/information-management]]
- [[./08-coordination/4w-5w-management]]
- [[./08-coordination/coordination-meeting-brief-template]] ✅ template with actual content
- [[./08-coordination/decision-log-template]] ✅ template with actual content
- [[./08-coordination/actor-responsibility-matrix]] ✅ template with actual content

> Note: Additional coordination pages exist in this folder — created by parallel agents.

---

## Monitoring, Evaluation and Learning Pages (./09-monitoring-learning/) — 6 pages (core)

MEL frameworks, indicator sets, and adaptive management tools.

- [[./09-monitoring-learning/area-based-mel-framework]]
- [[./09-monitoring-learning/community-resilience-indicators]]
- [[./09-monitoring-learning/area-based-reassessment-tool]]
- [[./09-monitoring-learning/outcome-harvesting-case-study-template]]
- [[./09-monitoring-learning/sendai-municipal-drr-progress-review]]
- [[./09-monitoring-learning/adaptive-management-triggers]]

> Note: Additional MEL pages exist in this folder — created by parallel agents.

---

## Transition and Scale Pages (./10transition-scale/) — 4 pages (core)

Tools and protocols for programme exit, handover, and scale-up.

- [[./10-transition-scale/handover-readiness-checklist]]
- [[./10-transition-scale/municipal-integration-plan]]
- [[./10-transition-scale/replication-scale-up-learning-note]]
- [[./10-transition-scale/build-back-better-recovery-alignment-tool]]

> Note: Additional transition pages exist in this folder — created by parallel agents.

---

## Risks and Contradictions (./12-risks-contradictions/) — 7 pages (core)

Critical analysis layer. Agents must consult before making claims.

- [[./12-risks-contradictions/known-contradictions]] — Conflicting recommendations across sources
- [[./12-risks-contradictions/weak-evidence-claims]] — Widely-cited claims with thin evidence
- [[./12-risks-contradictions/unresolved-questions]] — Open questions the literature has not settled
- [[./12-risks-contradictions/stale-guidance-watchlist]] — Potentially outdated guidance
- [[./12-risks-contradictions/common-aba-misuse]] — Recurring misapplication patterns
- [[./12-risks-contradictions/protection-and-do-no-harm-risks]] — Protection risks specific to ABA
- [[./12-risks-contradictions/evidence-gaps-to-fill]] ⚠️ READ THIS — 0-byte PDF, missing sources, TODO items

> Note: Additional risk pages exist in this folder — created by parallel agents.

---

## Agent Prompt Pages (./13-agent-prompts/) — 10 pages

Reusable operational prompts for AI agents working with this wiki.

- [[./13-agent-prompts/ingest-new-source]] — How to ingest a new source document
- [[./13-agent-prompts/query-wiki]] — How to answer a domain question using the wiki
- [[./13-agent-prompts/lint-wiki]] — How to run a wiki quality check
- [[./13-agent-prompts/run-manual-lint-checklist]] — Command-based fallback lint workflow
- [[./13-agent-prompts/build-new-tool-from-sources]] — How to build a new tool page from source material
- [[./13-agent-prompts/generate-field-instrument]] — How to create a field instrument for a tool
- [[./13-agent-prompts/create-decision-memo]] — How to create a decision memo for a field team
- [[./13-agent-prompts/detect-duplication-and-gaps]] — How to identify coverage gaps and response duplication
- [[./13-agent-prompts/review-tool-quality]] — How to validate a tool page against quality standard
- [[./13-agent-prompts/update-crosslinks]] — How to update cross-references across wiki pages

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

1. **0-byte PDF**: `2020-iasc` source file is empty — do not cite it. See [[./12-risks-contradictions/evidence-gaps-to-fill]].
2. **Partial ingestion state**: Some source pages are still metadata-first, while selected pages are ingested. Verify page-level status before relying on narrative synthesis.
3. **Stub pages**: Tools #02–17 and many concept/framework/coordination pages are still stubs — do not present stub content as vetted guidance.
4. **Contradictions**: Check [[./12-risks-contradictions/known-contradictions]] before generating recommendations.
5. **Tool #01 only**: Only Tool #01 meets the tool quality standard. Use it as the reference for what a complete tool page looks like.
