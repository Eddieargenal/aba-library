---
type: agent-context
status: reviewed
updated: 2026-05-08
---

# Agent Context

Load this file first on every session start. Keep it under 400 tokens. Update it at session end.

---

## Current Focus

Consolidating two knowledge bases into one vault: personal agent infrastructure + urban DRR/ABA humanitarian wiki.

## Active Decisions

- 🎯 vault structure: ABA wiki moved from `_system/` to `wiki/aba/` — unified single vault, no path duplication
- 🎯 navigation: JSONL indexes removed — agents use `wiki/index.md` + `indexes/*.md` routing tables
- 🎯 sources/: kept empty — ingest workflow documented, ready for first document
- 🎯 compliance: claim types (✅🔹🎯💡❓) + review status required on all memory category entries

## Key Infrastructure

- ✅ Vault path: `/Users/eddieargenal/Documents/obsidian-vault`
- ✅ Git-tracked: vault is under version control
- ✅ ABA wiki: `wiki/aba/` — 210 .md files, 13 sections, humanitarian domain knowledge

## First Action

- If session is vault work: read [[../SCHEMA]] first, then [[wiki/index]]
- If session is ABA/DRR work: read `wiki/aba/CLAUDE.md` for operating rules
- If general task: check [[memory/categories/infrastructure]] for server coordinates

## Blockers

- `sources/` has no content documents — first ingest needed when user provides a source
- `procedures.md` is a template with zero records — populate when procedures are verified
- ABA `wiki/aba/wiki/11-patterns/` section is empty

---

*Update this file at the end of every session. If it grows past 400 tokens, move the excess to [[current-handoff]] and trim.*