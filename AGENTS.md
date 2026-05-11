---
type: vault-entry
status: active
created: 2026-05-11
updated: 2026-05-11
---

# Vault AGENTS.md

A governed markdown knowledge base for local AI agents — workflows, domain knowledge, tools, decisions, and memory in a navigable structure.

## Design Philosophy
- Obsidian-compatible markdown with `[[wikilinks]]`
- Agent-navigable: every section has a `00_index.md`; load only what you need
- Human-readable: open in Obsidian or any text editor
- Governed memory: truth states, source tags, contradiction handling built in

## Intended Users
Hermes (task-execution), OpenClaw (gateway agent), human operators. No secrets, API keys, or credentials stored here. No fabricated memory.

## Vault Structure
```
obsidian-vault/
├── AGENTS.md              ← vault entry point (this file)
├── governance/            ← ALL operational rules, schemas, workflows, ABA ops docs
│   ├── 00_index.md        ← start here for any governance question
│   ├── schema/00_index.md ← frontmatter, lint, ingest, citation, naming rules
│   ├── workflows/00_index.md ← ingest, query, lint, model-routing, maintenance
│   └── aba/00_index.md    ← ABA agent contract, prompts, operating model
├── wiki/index.md          ← master catalog of all wiki pages
├── wiki/aba/              ← Urban DRR + ABA domain knowledge (13 sections)
├── sources/               ← raw source documents (read-only)
├── memory/                ← runtime: context, categories, logs, handoffs
└── archive/               ← append-only history
```

## Agent Navigation
1. Read `[[governance/00_index]]` — find governance sub-section
2. Read the section `00_index.md` — find the right file
3. Open file — execute
4. Log to `memory/runtime/logs/log.md`

## Quick Routing

| Task | File |
|------|------|
| Session start | `[[memory/context]]` |
| Any governance / rule question | `[[governance/00_index]]` |
| Ingest a source | `[[governance/workflows/ingest]]` |
| Query the wiki | `[[wiki/index]]` → `[[wiki/aba/00-overview/00_index]]` |
| Lint / health check | `[[governance/workflows/lint]]` |
| Model selection | `[[governance/workflows/model-routing]]` |
| ABA agent prompts | `[[governance/aba/00_index]]` |
| Memory recall | `[[memory/MEMORY]]` |
| Session end | `[[governance/workflows/vault-maintenance]]` |

## ABA Wiki — Section Index
`wiki/aba/` — 13 sections, each with a `00_index.md`. Start at `[[wiki/aba/00-overview/00_index]]`.

Sections: 00 Overview · 01 Sources · 02 Concepts · 03 Frameworks · 04 Tools · 05 Field Instruments · 06 Lifecycle · 07 Sector Applications · 08 Coordination · 09 Monitoring & Learning · 10 Transition & Scale · 11 Patterns · 12 Risks & Contradictions · 13 Agent Prompts → `[[governance/aba/00_index]]`

## Memory & Truth States

Load `[[memory/context]]` every session. Categories: `[[memory/categories/infrastructure]]` · `[[memory/categories/decisions]]` · `[[memory/categories/unresolved]]` · `[[memory/categories/outcomes]]`. Full index: `[[memory/MEMORY]]`.

Truth states: `validated` (user-confirmed) · `proposed` (agent-inferred, needs confirmation) · `disputed` (contradiction found) · `unresolved` (logged, pending)

## Special Files

| File | Purpose |
|------|---------|
| `governance/00_index.md` | Governance entry point |
| `wiki/index.md` | Master wiki catalog — read first on any query |
| `wiki/aba/CLAUDE.md` | ABA stub → full content at `governance/aba/CLAUDE.md` |
| `memory/runtime/logs/log.md` | Append-only operation log |
