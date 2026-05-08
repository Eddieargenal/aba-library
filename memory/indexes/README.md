---
type: index
status: removed
updated: 2026-05-08
---

# Memory Indexes

JSONL indexes were removed — workflows navigate via `wiki/index.md` and `indexes/*.md` instead.
Programmatic lookup is unnecessary: agents use text-based wikilink navigation.

## What Changed

- `key-index.jsonl` → removed (placeholder, never populated)
- `keyword-index.jsonl` → removed (placeholder, never populated)
- `relations.jsonl` → removed (never created)

## How Agents Navigate Now

- Discover pages: `wiki/index.md` (master catalog)
- Route workflows: `indexes/workflows.md`
- Route prompts: `indexes/prompts.md`
- Route tools: `indexes/tools.md`
