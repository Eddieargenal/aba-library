---
type: schema-changelog
status: active
created: 2026-05-11
updated: 2026-05-11
---
# Schema Changelog

All schema changes must be logged here before taking effect. No exceptions.

| date | author | change | files affected | migration |
|---|---|---|---|---|
| 2026-05-07 | system | Initial schema creation — 8 schema files established | frontmatter-schema, lint-rules, ingest-rules, query-rules, citation-rules, naming-conventions, page-types, tool-quality-standard | n/a (initial creation) |
| 2026-05-11 | consolidation | schema/ moved to governance/schema/ as part of governance consolidation | all 8 schema files | update all references from `schema/` to `governance/schema/` |
| 2026-05-11 | vault-upgrade | Created scripts/build-index.py; created indexes/agent-index.md; created .claude/commands/librarian.md; rewrote AGENTS.md to ABA architecture model; updated ingest-new-source.md step 12; updated log.md format section | scripts/build-index.py, indexes/agent-index.md, AGENTS.md, .claude/commands/librarian.md, governance/aba/prompts/ingest-new-source.md, memory/runtime/logs/log.md | No migration required — additive changes only |
| 2026-05-11 | librarian-skill | Created /librarian Claude Code skill at ~/.claude/skills/librarian/SKILL.md — 14 operations: open, close, query, ingest, extract, lint, build-index, build-concept, build-framework, build-tool, build-instrument, crosslink, review-tool, promote | ~/.claude/skills/librarian/SKILL.md | No migration — new capability |
