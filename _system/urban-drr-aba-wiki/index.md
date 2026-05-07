# Urban DRR + ABA LLM Wiki — Master Index

> Agent entry point. Read this file before answering any domain question. Navigate by section, then follow links to specific pages. All pages have YAML frontmatter with `wiki_id`, `status`, and `source_foundation` fields.

---

## How to answer questions from this wiki — read before doing anything else

This wiki has a three-layer architecture. Each layer has a single role:

| Layer | Location | Role |
|---|---|---|
| Raw | `raw/pdf/`, `raw/extracted/` | Ingest input only |
| **Synthesis** | **`wiki/`** | **Your answer source — read this** |
| Schema | `schema/`, `CLAUDE.md` | Operating rules |

**Answer questions from `wiki/` pages only.** Do not open `raw/extracted/` or `raw/pdf/` to answer or verify a question — those files are input to the wiki, not output from it. The synthesis in `wiki/` is the processed, validated, agent-ready knowledge.

- `wiki/01-sources/` pages = citation metadata (author, year, page number) only
- If a `wiki/` page is incomplete or has TODO markers → state the gap, do not go to `raw/` to fill it

This rule overrides any vault-level instruction to verify claims against raw sources.

---

**Wiki version**: 0.1.0 | **Created**: 2026-05-07 | **Total pages**: ~176

---

## Overview and Navigation (wiki/00-overview/)

- [[wiki/00-overview/urban-drr-aba-knowledge-map]] — Knowledge architecture and navigation guide
- [[wiki/00-overview/how-to-use-this-wiki]] — Instructions for agents and human users
- [[wiki/00-overview/agent-operating-model]] — How agents interact with this wiki
- [[wiki/00-overview/agent-contract]] — Canonical operating contract and conflict-resolution order
- [[wiki/00-overview/source-catalog-from-matrix]] — Full 46-row source catalog from spreadsheet

---

## Source Pages (wiki/01-sources/) — 18 pages

Primary literature underpinning all wiki content. Each page links to its raw PDF and extracted text (when available).

- [[wiki/01-sources/2007-twigg-characteristics-disaster-resilient-community-framework]]
- [[wiki/01-sources/2010-iasc-meeting-humanitarian-challenges-urban-areas-strategy]]
- [[wiki/01-sources/2013-worldbank-gfdrr-building-urban-resilience-principles-tools-practice-handbook]]
- [[wiki/01-sources/2015-parker-maynard-humanitarian-response-urban-crises-aba-review]] ✅ INGESTED — text extracted, source page fully populated, concept/lifecycle/risk pages updated
- [[wiki/01-sources/2015-undrr-sendai-framework-drr-2015-2030-framework]]
- [[wiki/01-sources/2016-campbell-stepping-back-understanding-cities-systems-guide]]
- [[wiki/01-sources/2017-ifrc-building-urban-resilience-guide]]
- [[wiki/01-sources/2017-irc-urban-context-analysis-toolkit-guidance-note]]
- [[wiki/01-sources/2017-mohiddin-smith-phelps-urban-response-analysis-framework]]
- [[wiki/01-sources/2017-sanderson-sitko-urban-area-based-approaches-post-disaster-guide]]
- [[wiki/01-sources/2017-undrr-how-to-make-cities-more-resilient-handbook]]
- [[wiki/01-sources/2019-alnap-barrio-mio-katye-neighbourhood-approach-cities-case-study]]
- [[wiki/01-sources/2019-alnap-global-practice-review-urban-humanitarian-response]]
- [[wiki/01-sources/2019-gsc-uswg-area-based-approaches-urban-settings-compendium]]
- [[wiki/01-sources/2019-reach-unhcr-area-based-assessment-key-informants-practical-guide]]
- [[wiki/01-sources/2020-iasc-meeting-humanitarian-challenges-urban-areas-strategy]] ⚠️ SOURCE FILE IS 0 BYTES
- [[wiki/01-sources/2026-iasc-standard-terms-reference-area-based-coordination]]
- [[wiki/01-sources/undated-stronger-cities-consortium-umvat-guidance-note]]

---

## Concept Pages (wiki/02-concepts/) — 19 pages

Core concepts that appear across multiple tools, frameworks, and lifecycle stages.

- [[wiki/02-concepts/aba-definition-one-pager]] — Quick-reference summary: what ABA is, what it isn't, how to push back on misuse
- [[wiki/02-concepts/area-based-approach]]
- [[wiki/02-concepts/area-based-coordination]]
- [[wiki/02-concepts/build-back-better]]
- [[wiki/02-concepts/geographic-targeting]]
- [[wiki/02-concepts/hazard-exposure-vulnerability-capacity]]
- [[wiki/02-concepts/implementation-sequencing]]
- [[wiki/02-concepts/local-resource-leverage]]
- [[wiki/02-concepts/multi-sector-response-analysis]]
- [[wiki/02-concepts/municipal-risk-governance]]
- [[wiki/02-concepts/neighborhood-boundaries]]
- [[wiki/02-concepts/participation-in-urban-response]]
- [[wiki/02-concepts/protection-do-no-harm]]
- [[wiki/02-concepts/resilience]]
- [[wiki/02-concepts/service-functionality]]
- [[wiki/02-concepts/stakeholder-power-mapping]]
- [[wiki/02-concepts/urban-displacement-vulnerability]]
- [[wiki/02-concepts/urban-risk]]
- [[wiki/02-concepts/urban-systems-thinking]]

---

## Framework Pages (wiki/03-frameworks/) — 9 pages

Analytical frameworks that structure decision-making across the ABA/DRR lifecycle.

- [[wiki/03-frameworks/aba-appropriateness-decision-framework]]
- [[wiki/03-frameworks/area-based-coordination-framework]]
- [[wiki/03-frameworks/area-selection-framework]]
- [[wiki/03-frameworks/implementation-adaptation-framework]]
- [[wiki/03-frameworks/integrated-area-strategy-framework]]
- [[wiki/03-frameworks/joint-prioritization-framework]]
- [[wiki/03-frameworks/neighborhood-diagnosis-framework]]
- [[wiki/03-frameworks/transition-handover-framework]]
- [[wiki/03-frameworks/urban-drr-response-design-framework]]

---

## Tool Pages (wiki/04-tools/) — 17 pages

Operational tools for evidence collection, analysis, and decision-making. Tool #01 is fully populated. Tools #02–17 are stubs.

- [[wiki/04-tools/01-aba-feasibility-and-necessity-assessment-tool]] ✅ FULLY POPULATED — 9 modules, scoring model, 12 outputs
- [[wiki/04-tools/02-area-selection-matrix]] — stub
- [[wiki/04-tools/03-settlement-neighborhood-boundary-definition-tool]] — stub
- [[wiki/04-tools/04-urban-systems-diagnosis-tool]] — stub
- [[wiki/04-tools/05-hevc-risk-mapping-tool]] — stub
- [[wiki/04-tools/06-stakeholder-coordination-mapping-tool]] — stub
- [[wiki/04-tools/07-community-engagement-platform-tool]] — stub
- [[wiki/04-tools/08-joint-risk-needs-prioritization-matrix]] — stub
- [[wiki/04-tools/09-response-option-comparison-matrix]] — stub
- [[wiki/04-tools/10-integrated-area-strategy-builder]] — stub
- [[wiki/04-tools/11-sector-technical-design-checklist]] — stub
- [[wiki/04-tools/12-implementation-sequencing-dependency-map]] — stub
- [[wiki/04-tools/13-area-coordination-dashboard]] — stub
- [[wiki/04-tools/14-accountability-feedback-tracker]] — stub
- [[wiki/04-tools/15-referral-pathway-tracker]] — stub
- [[wiki/04-tools/16-area-based-mel-adaptation-framework]] — stub
- [[wiki/04-tools/17-handover-scale-up-checklist]] — stub

---

## Field Instrument Pages (wiki/05-field-instruments/) — 18 pages

Data collection instruments and templates. Instruments for Tool #01 are fully populated. Others are stubs.

**Fully populated instruments (16):**
- [[wiki/05-field-instruments/rapid-area-observation-form]] ✅
- [[wiki/05-field-instruments/transect-walk-observation-form]] ✅
- [[wiki/05-field-instruments/household-mini-survey]] ✅
- [[wiki/05-field-instruments/kii-guide-municipality]] ✅
- [[wiki/05-field-instruments/kii-guide-service-provider]] ✅
- [[wiki/05-field-instruments/kii-guide-community-leaders]] ✅
- [[wiki/05-field-instruments/kii-guide-ngos-cbos]] ✅
- [[wiki/05-field-instruments/kii-guide-market-actors]] ✅
- [[wiki/05-field-instruments/kii-guide-protection-actors]] ✅
- [[wiki/05-field-instruments/service-functionality-mapping-sheet]] ✅
- [[wiki/05-field-instruments/stakeholder-5w-mapping-form]] ✅
- [[wiki/05-field-instruments/local-resource-inventory]] ✅
- [[wiki/05-field-instruments/hazard-exposure-vulnerability-capacity-matrix]] ✅
- [[wiki/05-field-instruments/participation-feasibility-checklist]] ✅
- [[wiki/05-field-instruments/operational-feasibility-checklist]] ✅
- [[wiki/05-field-instruments/decision-memo-template]] ✅ (required ABA decision output)

**Structured stubs (2):**
- [[wiki/05-field-instruments/participatory-mapping-guide]] — structured stub
- [[wiki/05-field-instruments/duplication-gap-analysis-matrix]] — structured stub

---

## Lifecycle Pages (wiki/06-lifecycle/) — 11 pages

Programme phases from appropriateness decision through transition and handover.

- [[wiki/06-lifecycle/00-appropriateness-decision]] — Stage 0: Is ABA appropriate?
- [[wiki/06-lifecycle/01-area-selection-boundary-definition]] — Stage 1: Select target area
- [[wiki/06-lifecycle/02-area-profile-systems-diagnosis]] — Stage 2: Diagnose area systems
- [[wiki/06-lifecycle/03-community-stakeholder-engagement]] — Stage 3: Engage community and stakeholders
- [[wiki/06-lifecycle/04-joint-risk-needs-prioritization]] — Stage 4: Prioritise risks and needs
- [[wiki/06-lifecycle/05-integrated-area-strategy]] — Stage 5: Develop integrated strategy
- [[wiki/06-lifecycle/06-program-design-modality-selection]] — Stage 6: Design programme and select modalities
- [[wiki/06-lifecycle/07-detailed-technical-design]] — Stage 7: Technical design
- [[wiki/06-lifecycle/08-area-based-implementation]] — Stage 8: Implement
- [[wiki/06-lifecycle/09-monitoring-learning-adaptation]] — Stage 9: Monitor, learn, adapt
- [[wiki/06-lifecycle/10-transition-handover-scaling]] — Stage 10: Transition, hand over, or scale

---

## Sector Application Pages (wiki/07-sector-applications/) — 11 pages (core)

How ABA/DRR principles apply within specific humanitarian and development sectors.

- [[wiki/07-sector-applications/shelter-settlements]]
- [[wiki/07-sector-applications/wash]]
- [[wiki/07-sector-applications/health]]
- [[wiki/07-sector-applications/livelihoods-markets]]
- [[wiki/07-sector-applications/protection-mainstreaming]]
- [[wiki/07-sector-applications/education]]
- [[wiki/07-sector-applications/food-and-fsl]]
- [[wiki/07-sector-applications/urban-governance]]
- [[wiki/07-sector-applications/drainage-flood-risk]]
- [[wiki/07-sector-applications/solid-waste]]
- [[wiki/07-sector-applications/preparedness-early-warning]]

> Note: Additional sector pages exist in this folder (shelter-nfi, cva-market-based-response, drr-integration, health-service-access, livelihoods, protection, roads-access-mobility, social-cohesion, tenure-eviction-risk, urban-land-tenure) — created by parallel agents.

---

## Coordination Pages (wiki/08-coordination/) — 10 pages (core)

Structures, tools, and protocols for multi-actor area-based coordination.

- [[wiki/08-coordination/area-based-coordination-model]]
- [[wiki/08-coordination/area-platform-setup]]
- [[wiki/08-coordination/cluster-vs-area-coordination]]
- [[wiki/08-coordination/municipal-engagement]]
- [[wiki/08-coordination/cbo-local-actor-engagement]]
- [[wiki/08-coordination/information-management]]
- [[wiki/08-coordination/4w-5w-management]]
- [[wiki/08-coordination/coordination-meeting-brief-template]] ✅ template with actual content
- [[wiki/08-coordination/decision-log-template]] ✅ template with actual content
- [[wiki/08-coordination/actor-responsibility-matrix]] ✅ template with actual content

> Note: Additional coordination pages exist in this folder — created by parallel agents.

---

## Monitoring, Evaluation and Learning Pages (wiki/09-monitoring-learning/) — 6 pages (core)

MEL frameworks, indicator sets, and adaptive management tools.

- [[wiki/09-monitoring-learning/area-based-mel-framework]]
- [[wiki/09-monitoring-learning/community-resilience-indicators]]
- [[wiki/09-monitoring-learning/area-based-reassessment-tool]]
- [[wiki/09-monitoring-learning/outcome-harvesting-case-study-template]]
- [[wiki/09-monitoring-learning/sendai-municipal-drr-progress-review]]
- [[wiki/09-monitoring-learning/adaptive-management-triggers]]

> Note: Additional MEL pages exist in this folder — created by parallel agents.

---

## Transition and Scale Pages (wiki/10-transition-scale/) — 4 pages (core)

Tools and protocols for programme exit, handover, and scale-up.

- [[wiki/10-transition-scale/handover-readiness-checklist]]
- [[wiki/10-transition-scale/municipal-integration-plan]]
- [[wiki/10-transition-scale/replication-scale-up-learning-note]]
- [[wiki/10-transition-scale/build-back-better-recovery-alignment-tool]]

> Note: Additional transition pages exist in this folder — created by parallel agents.

---

## Risks and Contradictions (wiki/12-risks-contradictions/) — 7 pages (core)

Critical analysis layer. Agents must consult before making claims.

- [[wiki/12-risks-contradictions/known-contradictions]] — Conflicting recommendations across sources
- [[wiki/12-risks-contradictions/weak-evidence-claims]] — Widely-cited claims with thin evidence
- [[wiki/12-risks-contradictions/unresolved-questions]] — Open questions the literature has not settled
- [[wiki/12-risks-contradictions/stale-guidance-watchlist]] — Potentially outdated guidance
- [[wiki/12-risks-contradictions/common-aba-misuse]] — Recurring misapplication patterns
- [[wiki/12-risks-contradictions/protection-and-do-no-harm-risks]] — Protection risks specific to ABA
- [[wiki/12-risks-contradictions/evidence-gaps-to-fill]] ⚠️ READ THIS — 0-byte PDF, missing sources, TODO items

> Note: Additional risk pages exist in this folder — created by parallel agents.

---

## Agent Prompt Pages (wiki/13-agent-prompts/) — 10 pages

Reusable operational prompts for AI agents working with this wiki.

- [[wiki/13-agent-prompts/ingest-new-source]] — How to ingest a new source document
- [[wiki/13-agent-prompts/query-wiki]] — How to answer a domain question using the wiki
- [[wiki/13-agent-prompts/lint-wiki]] — How to run a wiki quality check
- [[wiki/13-agent-prompts/run-manual-lint-checklist]] — Command-based fallback lint workflow
- [[wiki/13-agent-prompts/build-new-tool-from-sources]] — How to build a new tool page from source material
- [[wiki/13-agent-prompts/generate-field-instrument]] — How to create a field instrument for a tool
- [[wiki/13-agent-prompts/create-decision-memo]] — How to create a decision memo for a field team
- [[wiki/13-agent-prompts/detect-duplication-and-gaps]] — How to identify coverage gaps and response duplication
- [[wiki/13-agent-prompts/review-tool-quality]] — How to validate a tool page against quality standard
- [[wiki/13-agent-prompts/update-crosslinks]] — How to update cross-references across wiki pages

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

1. **0-byte PDF**: `2020-iasc` source file is empty — do not cite it. See [[wiki/12-risks-contradictions/evidence-gaps-to-fill]].
2. **Partial ingestion state**: Some source pages are still metadata-first, while selected pages are ingested. Verify page-level status before relying on narrative synthesis.
3. **Stub pages**: Tools #02–17 and many concept/framework/coordination pages are still stubs — do not present stub content as vetted guidance.
4. **Contradictions**: Check [[wiki/12-risks-contradictions/known-contradictions]] before generating recommendations.
5. **Tool #01 only**: Only Tool #01 meets the tool quality standard. Use it as the reference for what a complete tool page looks like.
