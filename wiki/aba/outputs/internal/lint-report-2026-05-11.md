---
type: lint-report
status: complete
generated: 2026-05-11
method: manual-checks
---

# Wiki Lint Report

Generated: 2026-05-11
Wiki root: `/Users/eddieargenal/Documents/obsidian-vault/wiki/aba`
Pages scanned: 224
Method: Manual bash checks (lint_wiki.py not present — see governance/aba/prompts/lint-wiki.md for procedure)

## Summary

| Issue type | Count | Change vs 2026-05-09 |
|---|---:|---:|
| Orphan pages (no inbound links) | 0 | -41 |
| Tool pages missing field instruments | 14 | 0 |
| Tool pages without scoring rules | 0 | 0 |
| Field instruments without data-quality checks | 0 | -1 |
| Files missing required frontmatter (status/type) | 0 | -75 |
| Empty placeholder pages | 0 | 0 |
| **Total issues** | **14** | **-42** |

## Orphan Pages

None detected. All 41 framework files (9 Tier 1 + 32 Tier 2) are linked from `03-frameworks/00_index.md`. Frontmatter added to all 32 Tier 2 frameworks on 2026-05-11.

## Tool Pages Missing Field Instruments (14)

These tools have `field_instruments: []` (empty). This is finding H-3 — deferred; requires domain expert input.

- `04-tools/02-area-selection-matrix.md`
- `04-tools/03-settlement-neighborhood-boundary-definition-tool.md`
- `04-tools/04-urban-systems-diagnosis-tool.md`
- `04-tools/07-community-engagement-platform-tool.md`
- `04-tools/08-joint-risk-needs-prioritization-matrix.md`
- `04-tools/09-response-option-comparison-matrix.md`
- `04-tools/10-integrated-area-strategy-builder.md`
- `04-tools/11-sector-technical-design-checklist.md`
- `04-tools/12-implementation-sequencing-dependency-map.md`
- `04-tools/13-area-coordination-dashboard.md`
- `04-tools/14-accountability-feedback-tracker.md`
- `04-tools/15-referral-pathway-tracker.md`
- `04-tools/16-area-based-mel-adaptation-framework.md`
- `04-tools/17-handover-scale-up-checklist.md`

## Tool Pages Without Scoring Rules

None

## Field Instruments Without Data-Quality Checks

None. `duplication-gap-analysis-matrix.md` received `## Data Quality Checks` section on 2026-05-11 (finding L-3 closed). All other 17 instruments already had data quality content embedded in their body.

## Files Missing Required Frontmatter

None. 75 files received `status:` field during audit remediation sprint on 2026-05-11:
- 32 Tier 2 frameworks received full frontmatter block (type, tier, status, created, updated)
- 18 field instruments received `status: draft`
- 9 Tier 1 frameworks received `used_by_outputs: []`
- 17 governance/indexes/templates/sources files received `status:`

## Empty Placeholder Pages

None

## Open Findings (Deferred)

| Finding | Description | Blocker |
|---|---|---|
| H-3 | 14 tool pages missing field instruments | Requires domain expert input |
| M-1 | `11-patterns/` empty — no pattern candidates filed | Requires field evidence and domain judgment |
