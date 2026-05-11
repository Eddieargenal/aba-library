---
type: workflow
status: validated
updated: 2026-05-11
---

# Ingest Workflow

Add a new source document to the vault and update the wiki.

## When to Use

When you have a new document, article, spec, or note to add to the knowledge base.

## Pre-conditions

- You have a raw document (markdown, plain text, or PDF-to-markdown export)
- The document has not been added to `sources/` before

---

## Steps

### 1. Save the source

Save the raw document to `sources/` without modification:

```
sources/YYYY-MM-DD_slug.md
```

Example: `sources/2026-05-07_karpathy-llm-wiki-spec.md`

Do not edit the file after saving. It is now immutable.

### 2. Read and extract

Read the source document completely. Extract:

- **Key facts** — verifiable claims about systems, people, decisions
- **Decisions** — choices made and their rationale
- **Entities** — infrastructure, tools, projects referenced
- **Open questions** — gaps, contradictions, things to verify

Note which existing wiki pages are affected.

### 3. Update wiki pages

For each affected wiki page in `memory/categories/`:

- Add new entries with the correct claim type (✅🔹🎯💡❓)
- Cite the source on every claim: `[source: sources/YYYY-MM-DD_slug.md]`
- Update the `updated:` date in frontmatter
- Change `status: stale` → `status: reviewed` if you've verified the content

If no appropriate page exists, create one in `memory/categories/` using the template at `templates/memory-record-template.md`.

Contradictions found during ingest → log to `memory/categories/unresolved.md`.

### 3b. Update section 00_index.md

For each section folder where a new page was added or an existing page significantly changed:
- Open that section's `00_index.md`
- Update the file count if it changed
- If the new page is significant (fully populated, not a stub), mention it in the index
- Keep the index to ≤3 sentences — revise the characterization only if the section's purpose has meaningfully changed

### 4. Update wiki/index.md

Open `wiki/index.md` and:

- Add a row for any new wiki pages created
- Update the summary of any pages whose content changed significantly

This file is the audit registration — every wiki page must appear here. If the new page is not listed, add it now.

### 5. Append to log

Open `memory/runtime/logs/log.md` and append:

```markdown
## [YYYY-MM-DD] ingest | [source title]
- Source: sources/YYYY-MM-DD_slug.md
- Updated pages: [comma-separated list]
- New pages: [comma-separated list, or "none"]
- Open questions logged: [yes/no]
```

---

## Notes

- Do not create a wiki page for every source — only when the knowledge is worth retaining long-term.
- Do not copy raw text into wiki pages. Summarize and extract.
- If the source is large, process it section by section before writing wiki entries.
- Sources are immutable ground truth. If something in a source is wrong, log it to `memory/categories/unresolved.md` rather than editing the source.

## Related

- [[../../AGENTS]] — Vault entry point and routing
- [[../../sources/README]] — What belongs in sources/
- [[../../wiki/index]] — Master catalog to update after ingest
- [[../../memory/runtime/logs/log]] — Append-only log
