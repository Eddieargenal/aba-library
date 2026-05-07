# Changelog

All notable changes to the AI Agent Wiki vault.

## [2026-05-07] — Navigation & Consistency Fixes

### Fixed
- `vault-initialization.md` — duplicate Step 3 header corrected, steps renumbered 1–7
- `vault-initialization.md`, `vault-maintenance.md` — added `context.md` to session-end update steps
- `memory/categories/unresolved.md` — removed conflicting subfolder instruction; added `gap` as a third entry type
- `memory/vault-compliance-rules.md` Rule 4 — aligned to single-file pattern, removed `contradictions/` subfolder reference
- `00_Start_Here.md` — added wikilinks to 5 unlinked memory category entries
- `00_Start_Here.md` — expanded Quick Routing from 2 to all 7 workflows
- `vault-maintenance.md` — removed reference to `pending.md` (out of vault scope per v3 decision)

### Added
- `memory/context.md` — compressed agent context file (~400 tokens), loaded first on every session start

---

## [2026-05-06] — Vault Compliance (v3)

### Added
- **10 Compliance Rules** — Implemented all 10 rules from day one:
  - Rule 1: Source citation required
  - Rule 2: Decisions linked to evidence
  - Rule 3: Claim types (✅ 🔹 🎯 💡 ❓)
  - Rule 4: Contradictions folder
  - Rule 5: index.md updated after ingest
  - Rule 6: Append-only log.md
  - Rule 7: Raw sources protected
  - Rule 8: Supersession pattern
  - Rule 9: Review status (draft/validated/stale)
  - Rule 10: Verify against sources

- `memory/vault-compliance-rules.md` — Full 10 rules reference
- `memory/governance.md` — Governance quick reference
- `memory/categories/unresolved/contradictions/` — Contradictions subfolder
- `memory/runtime/logs/log.md` — Append-only vault log
- Updated all category templates with claim types and review status

### Changed
- **Simplified vault scope** — now focuses only on workflows, prompts, tools
- **Removed duplicate memory categories** — deleted behavioral, projects, pending, tools (duplicates Hermes)
- **Simplified handoff files** — now brief notes, not a memory system
- **Updated skill** — now explicitly tells Hermes what NOT to store in vault
- **Removed knowledge_base from config** — not needed with simpler design

### What Stays
- Workflows (step-by-step guides)
- Prompts (templates by tier)
- Tools (reference cards)
- Indexes (routing tables)
- Infrastructure (server configs)
- Decisions (architectural)
- Procedures (verified guides)
- Unresolved (gaps)
- Outcomes (lessons)

### What Was Removed
- Behavioral memory (duplicates Hermes user profile)
- Projects memory (temporary, session-specific)
- Pending memory (temporary, session-specific)
- Tools memory (Hermes has tool definitions)

---

## [2026-05-06] — Initial Vault Improvements (v1)

### Added
- `00_Start_Here.md` — Missing entry point for agent and human navigation
- `QUICK.md` — Single-page quick reference for fast lookup
- `architecture.md` — Visual documentation with Mermaid diagrams
- `indexes/templates.md` — Template index with links to usage examples
- **Timestamps** — Added `updated: YYYY-MM-DD` to all content files
- **Stale content guidelines** — Added `stale_after_days` table to memory-rules.md
- **Vault integration**:
  - `workflows/vault-initialization.md` — How agents should load vault context
  - `workflows/vault-maintenance.md` — How the vault self-improves
  - Skill: `~/.hermes/skills/obsidian-vault/SKILL.md`

### Fixed
- Broken wikilinks to non-existent `00_Start_Here.md`
- Empty memory category files populated
- Missing human-accessible quick reference