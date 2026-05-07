---
type: lint-report
created: 2026-05-07
status: complete
---

# Wiki Lint Report
**Generated:** 2026-05-07  
**Total pages scanned:** 176  
**Wiki root:** `/Users/eddieargenal/Documents/obsidian-vault/_system/urban-drr-aba-wiki`

---

## Summary

| Issue type | Count |
|---|---:|
| Missing frontmatter | 0 |
| No source_foundation field | 49 |
| Tools with empty field_instruments | 14 |
| Zero-byte source PDFs | 1 |
| Pages with 5+ TODO-only sections | 37 |
| Stubs needing population | 34 |

**Overall wiki health:** Structure complete; source text extraction pending; tool stubs require population.

---

## CRITICAL: Zero-byte source PDFs

These PDFs must be re-downloaded before content can be extracted:

- `raw/pdf/2020-iasc-meeting-humanitarian-challenges-urban-areas-strategy.pdf` — **0 bytes, empty file**

---

## Tools with empty field_instruments field

These tools have `field_instruments: []` — instruments not yet linked:

- `wiki/04-tools/02-area-selection-matrix.md`
- `wiki/04-tools/03-settlement-neighborhood-boundary-definition-tool.md`
- `wiki/04-tools/04-urban-systems-diagnosis-tool.md`
- `wiki/04-tools/07-community-engagement-platform-tool.md`
- `wiki/04-tools/08-joint-risk-needs-prioritization-matrix.md`
- `wiki/04-tools/09-response-option-comparison-matrix.md`
- `wiki/04-tools/10-integrated-area-strategy-builder.md`
- `wiki/04-tools/11-sector-technical-design-checklist.md`
- `wiki/04-tools/12-implementation-sequencing-dependency-map.md`
- `wiki/04-tools/13-area-coordination-dashboard.md`
- `wiki/04-tools/14-accountability-feedback-tracker.md`
- `wiki/04-tools/15-referral-pathway-tracker.md`
- `wiki/04-tools/16-area-based-mel-adaptation-framework.md`
- `wiki/04-tools/17-handover-scale-up-checklist.md`

---

## Pages with missing frontmatter

- None — all pages have frontmatter ✅

---

## Stubs requiring population (selected high-priority)

The following pages have 5+ TODO sections and require agent population from source documents:

### Tools (prioritized by lifecycle order)
- tool: 02-area-selection-matrix.md (11 TODOs)
- tool: 03-settlement-neighborhood-boundary-definition-tool.md (11 TODOs)
- tool: 04-urban-systems-diagnosis-tool.md (11 TODOs)
- tool: 05-hevc-risk-mapping-tool.md (10 TODOs)
- tool: 06-stakeholder-coordination-mapping-tool.md (10 TODOs)
- tool: 07-community-engagement-platform-tool.md (13 TODOs)
- tool: 08-joint-risk-needs-prioritization-matrix.md (13 TODOs)
- tool: 09-response-option-comparison-matrix.md (13 TODOs)
- tool: 10-integrated-area-strategy-builder.md (13 TODOs)
- tool: 11-sector-technical-design-checklist.md (13 TODOs)

### Concepts (prioritized by cross-reference frequency)
- concept: area-based-approach.md (5 TODOs)
- concept: area-based-coordination.md (5 TODOs)
- concept: build-back-better.md (5 TODOs)
- concept: geographic-targeting.md (5 TODOs)
- concept: hazard-exposure-vulnerability-capacity.md (5 TODOs)
- concept: implementation-sequencing.md (5 TODOs)
- concept: local-resource-leverage.md (5 TODOs)
- concept: multi-sector-response-analysis.md (5 TODOs)
- concept: municipal-risk-governance.md (5 TODOs)
- concept: neighborhood-boundaries.md (5 TODOs)

---

## Quality assessment: Tool #01

**Tool #01 (ABA Feasibility and Necessity Assessment):** PASSES quality standard  
- ✅ 9 modules, all decision questions answered  
- ✅ Evidence required defined per domain  
- ✅ Field data points specified  
- ✅ Collection methods specified  
- ✅ Respondents/data sources specified  
- ✅ Field instruments linked  
- ✅ Analysis method per domain  
- ✅ Scoring rule (0-4) per domain  
- ✅ Decision rule per domain  
- ✅ Risk flags per domain  
- ✅ Source foundation per domain  

All other tools (02-17): **FAIL** — stubs only, do not use as operational guidance.

---

## Quality assessment: Field instruments

**Fully populated (16 instruments):** PASS — complete questions/fields, enumerator guidance, data quality checks, analysis use, risks/safeguards

| Instrument | Status |
|---|---|
| rapid-area-observation-form | ✅ PASS |
| transect-walk-observation-form | ✅ PASS |
| household-mini-survey | ✅ PASS |
| kii-guide-municipality | ✅ PASS |
| kii-guide-service-provider | ✅ PASS |
| kii-guide-community-leaders | ✅ PASS |
| kii-guide-ngos-cbos | ✅ PASS |
| kii-guide-market-actors | ✅ PASS |
| kii-guide-protection-actors | ✅ PASS |
| service-functionality-mapping-sheet | ✅ PASS |
| stakeholder-5w-mapping-form | ✅ PASS |
| local-resource-inventory | ✅ PASS |
| hazard-exposure-vulnerability-capacity-matrix | ✅ PASS |
| participation-feasibility-checklist | ✅ PASS |
| operational-feasibility-checklist | ✅ PASS |
| decision-memo-template | ✅ PASS |
| participatory-mapping-guide | ⚠️ structured stub |
| duplication-gap-analysis-matrix | ⚠️ structured stub |

---

## Incomplete source text extraction

**All source pages**: PDF text extraction has NOT been performed. Source pages contain metadata stubs only.  
Impact: Concept pages, frameworks, and tool stubs cannot be populated until source extraction is complete.  
**Recommended next step**: Run PDF extraction on all 21 non-empty PDFs in `raw/pdf/` then run ingest agent.

---

## Overlapping topic coverage (pages with similar scope)

The following page pairs were created by parallel agents and may have overlapping content:
- `07-sector-applications/health.md` and `health-service-access.md`
- `07-sector-applications/shelter-nfi.md` and `shelter-settlements.md`
- `07-sector-applications/livelihoods-markets.md` and `livelihoods.md`
- `07-sector-applications/protection.md` and `protection-mainstreaming.md`
- `07-sector-applications/urban-land-tenure.md` and `tenure-eviction-risk.md`
- `08-coordination/referral-pathway-design.md` and `referral-pathways.md`
- `08-coordination/municipal-engagement.md` and `municipal-alignment.md`

**Recommended action**: Merge overlapping pairs when populating from source documents.

---

## Recommended population sequence

When source text becomes available, populate in this order:

1. **Concept pages** (18 stubs) — from Parker & Maynard 2015, Sanderson & Sitko 2017, Campbell 2016
2. **Tool #02** (area selection matrix) — from Sanderson & Sitko 2017, GSC/USWG 2019
3. **Tool #05** (HEVC risk mapping) — from Sendai Framework, Twigg 2007
4. **Tool #07** (community engagement platform) — from Sanderson & Sitko 2017
5. **Lifecycle pages** (11 stubs) — cross-cutting population from all primary sources
6. **Frameworks** (8 stubs) — populate after tools are complete
7. **Tools #03-04, #06, #08-17** — follow Tool #01 quality standard

---
*Lint report generated by WU-4 agent. Report is a point-in-time snapshot — re-run after each ingest cycle.*