# Quick Reference

Single-page summary for fast navigation. See [[README]] for full documentation.

## Folder Structure

```
obsidian-vault/
├── SCHEMA.md            ← LLM instruction doc (read first)
├── 00_Start_Here.md     ← Agent entry point
├── README.md            ← Full documentation
├── QUICK.md             ← This file
├── sources/             ← Raw documents (read-only)
├── wiki/
│   └── index.md         ← Master catalog of all wiki pages
├── indexes/             ← Domain cross-reference tables
│   ├── workflows.md
│   ├── prompts.md
│   ├── tools.md
│   ├── memory.md
├── workflows/           ← Task guides (ingest, query, lint + domain)
├── prompts/             ← Prompt templates
├── tools/               ← Tool reference cards
├── agents/              ← Agent profiles
├── memory/              ← Governed wiki knowledge base
│   ├── categories/      ← Long-term knowledge pages
│   └── runtime/logs/    ← Append-only log
├── templates/           ← File scaffolds
└── archive/             ← Sessions, changelogs (contains CHANGELOG.md)
```

## Agent Navigation

```
User Request → SCHEMA.md → 00_Start_Here.md → wiki/index.md → workflow → execute → log
```

## Workflow Routing

| Task | Workflow |
|------|----------|
| Add a source document | [[workflows/ingest]] |
| Answer from the wiki | [[workflows/query]] |
| Health-check the wiki | [[workflows/lint]] |
| Model selection | [[workflows/model-routing]] |
| Coding/debugging | [[workflows/coding-tasks]] |
| Document extraction | [[workflows/document-extraction]] |
| Odoo accounting | [[workflows/odoo-accounting]] |
| Memory recall | [[workflows/memory-recall]] |

## Model Modes (for Hermes)

| Mode | Use For | Cost |
|------|---------|------|
| cheap | Summaries, rewrites, simple lookups | lowest |
| fix | Small code changes, one-liners | low |
| code | Debugging, implementation, refactors | medium |
| plan | Architecture, specs, complex reasoning | high |

## Memory Truth States

| State | Meaning |
|-------|---------|
| validated | Confirmed by user |
| proposed | Agent-inferred, needs confirmation |
| disputed | Contradiction pending resolution |
| unresolved | Contradictions stored here |

## Key Rules

- **No secrets** — never store API keys or passwords
- **No fabricated memory** — if it's not recorded, it doesn't exist
- **Agent-inferred = proposed** — requires user confirmation to validate
- **Contradictions go to unresolved** — never overwrite validated facts

## Links

- [[agents/Hermes]] — Hermes agent profile
- [[agents/OpenClaw]] — OpenClaw agent profile
- [[memory/memory-rules]] — Full memory governance rules
- [[memory/runtime/logs/log]] — Vault append-only log
- [[archive/CHANGELOG]] — Vault version history