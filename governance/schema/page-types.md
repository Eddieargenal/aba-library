---
type: schema
created: 2026-05-07
updated: 2026-05-18
status: active
version: 2.7
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

## `risk`
- Directory: `wiki/aba/06-risks/`
- Purpose: identified operational or contextual risks with mitigation links

## `known-tension`
- Directory: `wiki/aba/07-known-tensions/`
- Purpose: documented tensions between concepts, frameworks, or field practices

## `advisory-playbook`
- Directory: `wiki/aba/08-advisory-playbooks/`
- Purpose: multi-step guidance sequences for specific decision domains

## `decision-protocol`
- Directory: `wiki/aba/09-decision-protocols/`
- Purpose: structured decision logic for high-stakes operational choices

## `output-template`
- Directory: `wiki/aba/10-output-templates/`
- Purpose: reusable output formats for field advice, evidence packets, reports

## `slice-spec`
- Directory: `wiki/aba/11-slice-specs/`
- Purpose: packaging specifications for field-deployable knowledge slices

## `synthesis`
- Directory: `wiki/aba/12-synthesis/`
- Purpose: cross-cutting synthesis pages integrating evidence across multiple source pages

---

## Operational Mirror Type (Non-Canonical Answer Layer)

## `source_raw_extract`
- Directory: `wiki/aba/01-sources/raw-content/`
- Purpose: markdown text mirror of raw PDFs for ingestion/review workflows
- Population method: body text generated from raw PDF extraction
- Query rule: do not use as primary answer source for domain questions; use extracted/synthesis layers for answers; use raw-content for ingestion support and auditability
