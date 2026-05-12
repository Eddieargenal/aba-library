---
type: schema-changelog
status: active
created: 2026-05-11
updated: 2026-05-12
---
# Schema Changelog

All schema changes must be logged here before taking effect. No exceptions.

## [2026-05-12] lint-remediation | v2.6 — contradicts: [] added to 82 extension pages; lifecycle stage-0 rename

### Changes
- Batch-added `contradicts: []` to 82 synthesis pages across sections 06–12 that were created without the field. Affected page types: `lifecycle` (11), `sector-application` (21), `coordination` (19), `monitoring-learning` (6), `transition` (4), `risk-contradiction` (7), and 14 other synthesis types.
- Renamed `wiki/aba/06-lifecycle/appropriateness-decision.md` → `wiki/aba/06-lifecycle/00-appropriateness-decision.md` to align with wikilink `[[00-appropriateness-decision]]` in lifecycle index and the numbered file naming scheme (00–10).
- Fixed underscore-format `source_foundation:` IDs in `00-appropriateness-decision.md` (two entries: `2017_sanderson-sitko_...` → `2017-sanderson-sitko-...`, `2015_parker-maynard_...` → `2015-parker-maynard-...`).
- Added body wikilinks to `wiki/aba/03-frameworks/2019-replication-scale-up-learning-note-framework.md` and `wiki/aba/03-frameworks/2017-response-option-comparison-matrix-framework.md` pointing to their respective extracted source pages, resolving orphan status in Obsidian graph.
- Rebuilt `indexes/agent-index.md` (123 pages, 5 types — unchanged count).
- Lint report filed at `wiki/aba/outputs/internal/lint-report-2026-05-12.md`.

### Rationale
Extension sections (06–12) were built before the schema enforced `contradicts:` on all synthesis page types. The batch remediation clears all CRITICAL lint failures. The `contradicts: []` entries added here are correct assertions (checked, found consistent) but unreviewed — they must be revisited and populated when new sources are ingested that may contradict claims in these pages.

### Known gap exposed
Extension page types (`sector-application`, `coordination`, `monitoring-learning`, `transition`, `pattern`, `risk-contradiction`) have no formal schemas in `frontmatter-schema.md`. The `contradicts:` field is now present but type-specific required fields and controlled vocabulary are not yet defined. This is the primary schema work remaining for v2.7.

### Migration required
None. Additive changes only. The renamed lifecycle file (`00-appropriateness-decision.md`) matches the existing wikilink reference — no link updates needed.

---

## [2026-05-12] schema-update | v2.5 — raw-content mirror + metadata sync governance

### Changes
- Added `source_raw_extract` operational mirror page type in `governance/schema/page-types.md`
- Added `Raw-content Source Mirror Page` schema block to `governance/schema/frontmatter-schema.md`
- Updated `governance/schema/ingest-rules.md` to include:
  - raw PDF placement in `wiki/aba/01-sources/raw/`
  - markdown extraction to `wiki/aba/01-sources/raw-content/`
  - metadata synchronization via `scripts/sync_extracted_frontmatter_to_raw_content.py --apply`
- Updated schema section index descriptions in `governance/schema/00_schema-index.md` to reflect raw-content mirror governance
- Updated ABA operations references (`governance/aba/CLAUDE.md`, `governance/aba/prompts/ingest-new-source.md`, `governance/workflows/ingest.md`, `governance/workflows/document-extraction.md`, and related section indexes) to align with the new ingest pipeline

### Rationale
The vault now maintains a markdown operational mirror of raw PDFs in `01-sources/raw-content/` and uses an automated script to sync agreed metadata fields from extracted source pages. Governance and schema documents were updated so workflow, page-type, and ingest rules match actual vault behavior.

## [2026-05-12] schema-update | v2.4 — Index naming convention + schema remediation

### Changes
- All section index files renamed to descriptive `00_*-index.md` pattern (e.g., `00_concepts-index.md`, `00_governance-index.md`) — was previously generic `00_index.md`
- Librarian skill index-exclusion filter updated to `fname.startswith("00_")` pattern
- Governance reference updated: `governance/00_governance-index.md` (was `governance/00_index.md`)
- `frontmatter-schema.md` updated to include framework and synthesis page type schemas, add `contradicts:` to all page types, separate `author`/`institution` fields on source pages, correct concept status vocabulary to `draft | active | archived`, correct field instrument `related_tool` → `related_tools`
- `governance/aba/CLAUDE.md` directory paths corrected (added missing hyphens: `01sources/` → `01-sources/`, etc.)

### Rationale
Alignment audit identified significant schema drift between frontmatter-schema.md and the actual spec. All page type schemas now match spec v2.4 exactly.

---

| date | author | change | files affected | migration |
|---|---|---|---|---|
| 2026-05-12 | lint-pass | v2.6 — contradicts: [] batch-added to 82 extension pages; lifecycle stage-0 file renamed; 2 framework pages linked to extracted sources | 82 wiki pages + 00-appropriateness-decision.md + 2 framework pages + indexes/agent-index.md | None — additive |
| 2026-05-12 | schema-update | v2.5 — raw-content mirror + metadata sync governance added | governance/schema/frontmatter-schema.md, page-types.md, ingest-rules.md, CLAUDE.md, multiple workflow files | Update all ingest references |
| 2026-05-12 | alignment-audit | v2.4 — index naming convention + schema remediation across all defined page types | frontmatter-schema.md, CLAUDE.md, all section index files, concept/tool/framework pages | Update AGENTS.md and CLAUDE.md index references |
| 2026-05-07 | system | Initial schema creation — 8 schema files established | frontmatter-schema, lint-rules, ingest-rules, query-rules, citation-rules, naming-conventions, page-types, tool-quality-standard | n/a (initial creation) |
| 2026-05-11 | consolidation | schema/ moved to governance/schema/ as part of governance consolidation | all 8 schema files | update all references from `schema/` to `governance/schema/` |
| 2026-05-11 | vault-upgrade | Created scripts/build-index.py; created indexes/agent-index.md; created .claude/commands/librarian.md; rewrote AGENTS.md to ABA architecture model; updated ingest-new-source.md step 12; updated log.md format section | scripts/build-index.py, indexes/agent-index.md, AGENTS.md, .claude/commands/librarian.md, governance/aba/prompts/ingest-new-source.md, memory/runtime/logs/log.md | No migration required — additive changes only |
| 2026-05-11 | librarian-skill | Created /librarian Claude Code skill at ~/.claude/skills/librarian/SKILL.md — 14 operations: open, close, query, ingest, extract, lint, build-index, build-concept, build-framework, build-tool, build-instrument, crosslink, review-tool, promote | ~/.claude/skills/librarian/SKILL.md | No migration — new capability |
