---
type: documentation
updated: 2026-05-07
---

# Sources

This folder holds raw, immutable source documents. The LLM reads these during ingest but never modifies them.

## Rules

- **Read-only** — Never edit files in this folder. Create derived wiki pages instead.
- **Add freely** — Drop any document here: articles, PDF-to-markdown exports, meeting notes, specs, transcripts.
- **One source per file** — Do not concatenate multiple documents into one file.
- **Filename convention** — `YYYY-MM-DD_slug.md` (e.g., `2026-05-07_karpathy-llm-wiki-spec.md`)
- **After adding a source** — Run the Ingest workflow: [[../governance/workflows/ingest]]

## What Goes Here

- Web-clipped articles (Obsidian Web Clipper output)
- PDF extracts converted to markdown
- Meeting notes and transcripts
- External specs and documentation snapshots
- Research papers and references
- Raw data exports

## What Does NOT Go Here

- Synthesized wiki pages → `memory/categories/`
- Workflows or procedures → `workflows/`
- Tool documentation you wrote → `tools/`
- Anything that is agent-generated or derived

## Relationship to the Wiki

Sources are the ground truth. Wiki pages are derived summaries.

```
sources/YYYY-MM-DD_article.md  ← raw, immutable
    ↓ ingest
memory/categories/decisions.md  ← wiki page, cites source
```

See [[../AGENTS.md]] for the full vault structure and [[../governance/governance-model]] for the three-layer architecture.
