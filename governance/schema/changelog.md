---
type: schema-changelog
status: active
created: 2026-05-11
updated: 2026-05-11
---
# Schema Changelog

All schema changes must be logged here before taking effect. No exceptions.

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
| 2026-05-07 | system | Initial schema creation — 8 schema files established | frontmatter-schema, lint-rules, ingest-rules, query-rules, citation-rules, naming-conventions, page-types, tool-quality-standard | n/a (initial creation) |
| 2026-05-11 | consolidation | schema/ moved to governance/schema/ as part of governance consolidation | all 8 schema files | update all references from `schema/` to `governance/schema/` |
| 2026-05-11 | vault-upgrade | Created scripts/build-index.py; created indexes/agent-index.md; created .claude/commands/librarian.md; rewrote AGENTS.md to ABA architecture model; updated ingest-new-source.md step 12; updated log.md format section | scripts/build-index.py, indexes/agent-index.md, AGENTS.md, .claude/commands/librarian.md, governance/aba/prompts/ingest-new-source.md, memory/runtime/logs/log.md | No migration required — additive changes only |
| 2026-05-11 | librarian-skill | Created /librarian Claude Code skill at ~/.claude/skills/librarian/SKILL.md — 14 operations: open, close, query, ingest, extract, lint, build-index, build-concept, build-framework, build-tool, build-instrument, crosslink, review-tool, promote | ~/.claude/skills/librarian/SKILL.md | No migration — new capability |
