---
type: schema
created: 2026-05-07
updated: 2026-05-12
status: active
---
# Wiki Page Types

Canonical page types used by frontmatter queries and index generation:

## `source`
- Directory: `wiki/aba/01-sources/extracted/`
- Purpose: structured extraction page per raw source document
- Schema authority: `frontmatter-schema.md` Source Page block

## `concept`
- Directory: `wiki/aba/02-concepts/`
- Purpose: synthesis concepts promoted from source evidence

## `framework`
- Directory: `wiki/aba/03-frameworks/`
- Purpose: decision frameworks (Tier 1 operational + Tier 2 reference)

## `tool`
- Directory: `wiki/aba/04-tools/`
- Purpose: operational tools with explicit evidence collection/decision logic

## `field-instrument`
- Directory: `wiki/aba/05-field-instruments/`
- Purpose: forms/checklists/guides used by tools for field data collection

## `synthesis`
- Directory: `wiki/aba/outputs/internal/` (and approved output locations)
- Purpose: filed analytical outputs and reusable internal syntheses

---

## Extension Section Types (Operational Content Sections)

These sections are active content zones and may use canonical page types above while section-specific schemas continue to evolve:
- `wiki/aba/06-lifecycle/`
- `wiki/aba/07-sector-applications/`
- `wiki/aba/08-coordination/`
- `wiki/aba/09-monitoring-learning/`
- `wiki/aba/10-transition-scale/`
- `wiki/aba/11-patterns/`
- `wiki/aba/12-risks-contradictions/`

Agents should follow existing frontmatter in-section and `frontmatter-schema.md` constraints for shared critical fields (`lifecycle_stage`, `contradicts`, etc.).

---

## Operational Mirror Type (Non-Canonical Answer Layer)

## `source_raw_extract`
- Directory: `wiki/aba/01-sources/raw-content/`
- Purpose: markdown text mirror of raw PDFs for ingestion/review workflows
- Population method:
  - body text generated from raw PDF extraction
  - selected frontmatter fields synced from `01-sources/extracted/` using `scripts/sync_extracted_frontmatter_to_raw_content.py`
- Query rule:
  - do not use as primary answer source for domain questions
  - use extracted/synthesis layers for answers; use raw-content for ingestion support and auditability
