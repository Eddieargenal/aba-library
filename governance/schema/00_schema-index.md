---
type: section-index
status: active
updated: 2026-05-12
---
# Schema — Section Index

All schema definitions for the vault. Read the relevant file before performing the operation it governs. All schema changes must be logged in `changelog.md` before taking effect.

| Document | Purpose | When to Read | When NOT to Read |
|---|---|---|---|
| [[frontmatter-schema]] | Required YAML frontmatter fields for canonical page types plus `source_raw_extract` mirror files in `01-sources/raw-content/` | Before creating or validating any wiki page or syncing raw-content metadata | When you only need to read existing pages |
| [[lint-rules]] | 16 lint checks + hard lint rule for tool pages | Before running a lint pass; when determining if a page passes quality review | During ingest or query operations |
| [[ingest-rules]] | Canonical ingest sequence including `raw/` PDF placement, `raw-content/` extraction, and metadata sync script usage | Before ingesting a new source document | During query or lint operations |
| [[query-rules]] | Three-layer query rule; step-by-step query procedure; tool response requirements | Before answering any domain question | During ingest; when operating on raw sources |
| [[citation-rules]] | Citation format; multi-source rules; confidence levels; minimum evidence per tool domain | When writing or reviewing factual claims in wiki pages | For non-factual content (indexes, templates) |
| [[naming-conventions]] | File naming for raw sources and wiki pages; ID conventions (source_id, tool_id, instrument_id) | Before creating any new file or ID | When reading existing files |
| [[page-types]] | Definitions for canonical wiki page types plus the non-canonical `source_raw_extract` operational mirror type | When creating a new page type or verifying page classification | For operational queries |
| [[tool-quality-standard]] | 10-point minimum requirements for tool pages; 5 failure conditions; stub exception rules | Before writing or reviewing a tool page | For non-tool page types |
| [[changelog]] | Audit log of all schema changes | Before making any schema change; when auditing schema history | For regular reading operations |
