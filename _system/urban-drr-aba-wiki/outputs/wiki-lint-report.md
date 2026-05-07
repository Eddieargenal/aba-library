---
type: lint-report
created: 2026-05-07
status: complete
method: manual-checklist
---

# Wiki Lint Report
**Generated:** 2026-05-07  
**Mode:** Manual checklist (`wiki/13-agent-prompts/run-manual-lint-checklist`)  
**Wiki root:** `/Users/eddieargenal/Documents/obsidian-vault/_system/urban-drr-aba-wiki`  
**Total `wiki/*.md` pages scanned:** 181

---

## Summary

| Issue type | Count |
|---|---:|
| Zero-byte source PDFs | 1 |
| Orphan pages (no inbound links) | 32 |
| Source pages not linked from concept/tool/lifecycle | 4 |
| Tool pages with `field_instruments: []` | 14 |
| Tool pages missing scoring keywords | 0 |
| Field instruments lacking data quality keywords | 1 |
| Coordination pages lacking duplication/gap keywords | 10 |
| Pages with `status: draft` | 111 |
| Total `TODO[agent]` markers | 794 |
| Pages with 5+ `TODO[agent]` markers | 74 |
| Draft pages that still contain TODO markers | 103 |

**Overall wiki health:** Governance structure is strong and now more coherent (agent contract + manual lint fallback added), but content readiness remains low across most draft pages.

---

## Critical Findings

1. **Zero-byte source PDF remains unresolved**
- `raw/pdf/2020-iasc-meeting-humanitarian-challenges-urban-areas-strategy.pdf`
- Impact: blocks ingestion and citation of this source.

---

## High Findings

1. **14 tool pages still missing linked field instruments**
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

2. **32 orphan pages**
- Concentrated in additional sector/coordinator/MEL/transition/risk pages created by parallel agents.
- These pages are not discoverable from the current navigation graph.

3. **10 coordination pages still lack explicit duplication/gap logic language**
- `wiki/08-coordination/area-platform-setup.md`
- `wiki/08-coordination/cluster-vs-area-coordination.md`
- `wiki/08-coordination/cluster-sector-interface.md`
- `wiki/08-coordination/coordination-architecture.md`
- `wiki/08-coordination/coordination-data-sharing.md`
- `wiki/08-coordination/referral-pathway-design.md`
- `wiki/08-coordination/municipal-engagement.md`
- `wiki/08-coordination/municipal-alignment.md`
- `wiki/08-coordination/decision-log-template.md`
- `wiki/08-coordination/referral-pathways.md`

---

## Medium Findings

1. **1 field instrument missing explicit data-quality language**
- `wiki/05-field-instruments/duplication-gap-analysis-matrix.md`

2. **4 source pages not referenced from concept/tool/lifecycle pages**
- `2010-iasc-meeting-humanitarian-challenges-urban-areas-strategy`
- `2019-alnap-barrio-mio-katye-neighbourhood-approach-cities-case-study`
- `2020-iasc-meeting-humanitarian-challenges-urban-areas-strategy`
- `undated-stronger-cities-consortium-umvat-guidance-note`

---

## Informational Findings

1. **Scoring keyword presence check passed for tools**
- No tool page is missing scoring/threshold keywords.
- Note: most stubs still contain TODO scoring placeholders and do not yet pass full quality review.

2. **Stub density remains high**
- `status: draft` pages: 111
- `TODO[agent]` markers: 794
- Pages with 5+ TODO markers: 74

---

## Prioritized Next Actions

1. Replace and re-ingest the zero-byte 2020 IASC PDF.
2. Link field instruments into tools #02-#17 (minimum frontmatter completion first).
3. Resolve orphan pages by either merging duplicate variants or adding inbound links from index/hubs.
4. Add explicit duplication/gap logic sections to the 10 flagged coordination pages.
5. Populate `duplication-gap-analysis-matrix` with data-quality checks.

---

## Notes on Method

- This report was produced with command-based checks from `wiki/13-agent-prompts/run-manual-lint-checklist.md`.
- Pattern checks are heuristic; final content quality must still be reviewed against `schema/tool-quality-standard.md`.
