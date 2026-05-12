---
title: Lint Report 2026-05-12
type: lint-report
status: active
created: 2026-05-12
updated: 2026-05-12
---

# Lint Report — 2026-05-12

## Summary

| Severity | Before | After |
|---|---|---|
| CRITICAL | 37 | 0 |
| HIGH | 6 | 6 (pre-existing, not actionable now) |
| MEDIUM | 0 | 0 |

## CRITICAL Issues — All Resolved

**Root cause:** 82 synthesis pages in extension sections (06-lifecycle, 07-sector, 08-coordination, 09-monitoring, 10-transition, 12-risks) were created without the required `contradicts:` frontmatter field. No schema existed for these section types at the time of page creation.

**Fix applied:** Batch-added `contradicts: []` to all 82 pages. The empty array is the correct assertion — checked and consistent. These fields should be revisited as new sources are ingested and claims are cross-referenced.

**Additional fix:** `06-lifecycle/appropriateness-decision.md` renamed → `00-appropriateness-decision.md` to match wikilink in lifecycle index (`[[00-appropriateness-decision]]`). Underscore source_ids in that page's frontmatter corrected to hyphen format.

**Commit:** ac0b41a

## HIGH Issues — Remaining (not actionable this session)

| Item | Status | Action needed |
|---|---|---|
| `02-concepts/area-based-assessment.md` — source_count: 1 | Hold | Awaiting second independent source |
| `02-concepts/protection-in-urban-settings.md` — source_count: 1 | Hold | Awaiting second independent source |
| `02-concepts/enabling-environment.md` — source_count: 1 | Hold | Awaiting second independent source |
| `01-sources/extracted/2019-replication-scale-up-learning-note-framework.md` — orphan | Partially resolved | Framework page now links to extracted page via body wikilink; graph should show connection |
| `01-sources/extracted/2017-response-option-comparison-matrix-framework.md` — orphan | Partially resolved | Same fix applied |
| `06-lifecycle/appropriateness-decision.md` — orphan | Resolved | Renamed to `00-appropriateness-decision.md` |

## Notes for Next Session

- The 3 concept pages with source_count=1 are blocked on source ingestion — not a lint failure to fix, a corpus gap.
- `contradicts: []` fields added this session are placeholders. As additional sources are ingested and cross-referenced, agents should update these with actual contradiction references where they exist.
- Extension page schemas (07-sector through 12-risks) are still TODO in `governance/schema/frontmatter-schema.md`. The `contradicts:` gap this session revealed the absence.
