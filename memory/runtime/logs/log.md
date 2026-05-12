---
type: vault-log
status: active
updated: 2026-05-06
---

# Vault Log (Append-Only)

This file is **append-only**. Never overwrite. Never delete entries.

## Format

```markdown
## [YYYY-MM-DD] type | brief description
- key action 1
- key action 2
- files changed: [list]
```

Where `type` is one of: `ingest` · `query` · `lint` · `schema` · `maintenance`

## Rules

- Only append new entries
- Never modify or delete existing entries
- Include timestamps
- Link to related pages when applicable

---

## 2026-05-06
- Initialized vault with 10 compliance rules
- Added vault-compliance-rules.md
- Added governance.md

## 2026-05-08
- [vault-quality-monitor] Deployed guardrail skill for vault quality verification
- [vault-quality-monitor] Preflight check: PASS - governance/vault-quality-remediation/SKILL.md exists
- [vault-quality-monitor] Preflight check: PASS - governance/vault-quality-remediation/RUNBOOK.md exists
- [vault-quality-monitor] Post-deploy check: PASS - wiki/index.md exists
- [vault-quality-monitor] Post-deploy check: PASS - wiki/vault-compliance-rules.md exists
- [vault-quality-monitor] Post-deploy check: PASS - memory/runtime/logs/log.md exists
- [vault-quality-monitor] Status: ALL CHECKS PASSED
- Updated infrastructure.md with claim types
- Updated decisions.md with claim types
- Updated unresolved.md with claim types
- Created contradictions subfolder
- Created append-only log.md

## 2026-05-07
- Created memory/context.md — compressed agent context file, load first on every session start
- Wired context.md into vault-initialization.md as step 1 (before handoff and entry point)
- Added context.md to navigation table and memory index in 00_Start_Here.md
- Fixed duplicate Step 3 in vault-initialization.md — renumbered steps 1–7
- Added context.md update to session-end steps in vault-initialization.md and vault-maintenance.md
- Resolved contradiction destination ambiguity: unresolved.md is single-file, no subfolder
- Added `gap` type to unresolved.md and aligned vault-compliance-rules.md Rule 4 to match
- Added wikilinks to 5 unlinked memory category entries in 00_Start_Here.md
- Expanded Quick Routing in 00_Start_Here.md from 2 to 7 workflows
- Removed non-existent indexes/templates.md reference from QUICK.md
- Appended 2026-05-07 entry to archive/CHANGELOG.md

## 2026-05-07
- Created agents/ folder with Hermes.md and OpenClaw.md (placeholders)
- Created archive/README.md (CHANGELOG.md already existed)
- Fixed outcomes.md: removed pending.md reference
- Updated wiki/index.md: agents section now links to existing files
- Added archive/ to SCHEMA.md Wiki Folder Map
- Added agents/ and archive/ to 00_Start_Here.md What The Vault Provides table
- Created memory/indexes/README.md explaining JSONL indexes (undecided purpose)
- Updated QUICK.md folder structure with archive/ contents note


- Added stale thresholds table to vault-compliance-rules.md (was referenced from memory-rules.md but missing)
- Added summary card to vault-compliance-rules.md
- Fixed broken task-log → log references in: vault-initialization.md, vault-maintenance.md, QUICK.md, architecture.md
- Removed non-existent indexes/templates.md reference from QUICK.md
## [2026-05-08] lint | vault-wide audit — karpathy governance remediation
- Broken wikilinks: 65 — relative-path wikilinks flagged; many resolve correctly in Obsidian (e.g. `_system/urban-drr-aba-wiki/`, `memory/categories/`, `../indexes/`). Manual verification recommended for: `../archive/CHANGELOG`, `../memory/governance`, `../memory/context`, `../memory/current-handoff`, `../memory/memory-rules`, `../memory/indexes/*.jsonl`, `../memory/categories/behavioral`, `../memory/categories/pending`, `../memory/categories/projects`, `../memory/categories/tools`
- Orphan pages: 0 — all wiki/ and memory/categories/ pages are linked
- Missing frontmatter fields (type/status/updated): 2 — memory/categories/outcomes.md, memory/categories/procedures.md
- Stale pages (updated before 2026-02-07): 0
- Issues found: 3 categories (65 potential broken links for manual review, 2 missing frontmatter)
- Logged to unresolved: no
- Remediation files changed: wiki/index.md, wiki/vault-compliance-rules.md, wiki/workflows/lint-plan.md, SCHEMA.md, wiki/diagnosis/karpathy-vault-quality-diagnosis-2026-05-08.md

## [2026-05-11] query | ABA characteristics according to Parker & Maynard (2015)
- question: top three characteristics of area-based approach according to Maynard
- pages read: 2015-parker-maynard-aba-review, area-based-approach concept
- answer: geographic targeting + participatory + multi-sectoral — all three required simultaneously
- tensions flagged: stricter than DFID/IRC/ALNAP (2015), GSC (2019), Sanderson & Sitko (2017) definitions

## [2026-05-11] query | ABA characteristics — cross-corpus synthesis
- question: characteristics of area-based approaches (all sources)
- navigation: index grep → concept page (cached) → 3x sed Key Concepts extracts
- pages read: grep on index, sed on 3 source files; concept page from prior session context
- answer: 3 consensus characteristics (geographic, participatory, multi-sector); source-by-source additions mapped; simultaneity requirement contested
- sources: parker-maynard-2015, dfid-irc-alnap-2015, sanderson-sitko-2017, globalcluster-2019
