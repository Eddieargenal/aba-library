---
type: workflow
status: validated
updated: 2026-05-07
---

# Query Workflow

Answer a question from the wiki, with citations.

## When to Use

When a user or agent asks a factual question that should be answerable from the knowledge base.

---

## Steps

### 1. Read wiki/index.md

Open `wiki/index.md`. Scan the table for the 1–3 pages most likely to contain the answer.

Do not open pages speculatively. Match the question to the catalog before opening files.

### 2. Read relevant pages

Open the pages identified in step 1. Read fully — do not skim.

If a page links to another page that seems more relevant, follow the link.

### 3. Synthesize the answer

Compose the answer with:

- Claim type prefix on every statement (✅🔹🎯💡❓)
- Source citation on every factual claim: `[source: page-name or sources/file]`
- Clear indication when the answer is incomplete or uncertain

If the wiki does not have the answer:
- Say so explicitly — do not fabricate
- Log the gap to `memory/categories/unresolved.md` with type `gap`
- Suggest a source that would fill it

### 4. Optionally file the answer

If the synthesized answer contains knowledge worth retaining — and it is not already captured in a wiki page — file it:

- Create or update the appropriate `memory/categories/` page
- Update `wiki/index.md` if a new page was created
- Append to log:

```markdown
## [YYYY-MM-DD] query | [question summary]
- Pages consulted: [list]
- New page filed: [yes + link, or "no"]
```

---

## Notes

- The wiki is for navigation and synthesis. For accuracy-critical claims in the main vault, verify against the raw source in `sources/`.
- **Exception — sub-wikis with a synthesis layer:** If the query routes into a sub-wiki that maintains its own `wiki/` synthesis (e.g. `wiki/aba/`), that wiki's `wiki/` pages are the answer source. Do not go to that wiki's `raw/` directory to verify. The sub-wiki's index.md will say this explicitly.
- If two wiki pages contradict each other, do not pick one — log the contradiction to `memory/categories/unresolved.md` and surface it in your answer.
- Do not update wiki pages during a query unless you are explicitly filing a new answer (step 4). Keep query and ingest separate.

## Related

- [[../SCHEMA.md]] — Full operation definitions
- [[../wiki/index.md]] — Master catalog (start here)
- [[../memory/categories/unresolved]] — Log gaps and contradictions here
- [[../workflows/ingest]] — Use when you have a new source to process
