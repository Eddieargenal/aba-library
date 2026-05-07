---
type: index
status: placeholder
updated: 2026-05-07
---

# Memory Indexes

This folder contains machine-readable indexes for programmatic lookup.

## Contents

| File | Purpose | Status |
|------|---------|--------|
| `key-index.jsonl` | Key-value index | placeholder |
| `keyword-index.jsonl` | Keyword lookup | placeholder |
| `relations.jsonl` | Page relationships | placeholder |

## Purpose (Undecided)

These indexes were created for potential programmatic lookup by agents. Currently unused.

Options:
1. **Keep** — populate as the vault grows for faster search
2. **Remove** — wikilinks and wiki/index.md are sufficient
3. **Repurpose** — use for something else (suggestions welcome)

## Usage

If used, each line is valid JSONL:
```json
{"key": "workflow:ingest", "path": "workflows/ingest.md", "tags": ["workflow", "operations"]}
```

## Related

- [[../wiki/index]] — Human-readable master catalog
- [[../indexes/workflows]] — Workflow routing table