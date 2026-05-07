---
type: index
scope: workflows
updated: 2026-05-06
---

# Workflow Index

Open a workflow only when routed here from [[../00_Start_Here]].

## Workflows

| Workflow | Use When | Linked Prompt |
|---|---|---|
| [[../workflows/ingest]] | Adding a new source document to the wiki | none — follow steps directly |
| [[../workflows/query]] | Answering a question from the wiki with citations | none — navigate wiki/index.md first |
| [[../workflows/lint]] | Health-checking the wiki for stale pages and contradictions | none — produces repair list |
| [[../workflows/model-routing]] | Selecting the right model/mode for a task | [[../prompts/cheap-summary]], [[../prompts/fix-code]], [[../prompts/code-debug]], [[../prompts/plan-architecture]] |
| [[../workflows/vault-initialization]] | Loading vault context on session start | none — read files directly |
| [[../workflows/vault-maintenance]] | Keeping the vault healthy and self-improving | [[../memory/categories/unresolved]] |
| [[../workflows/coding-tasks]] | Writing, editing, debugging, or refactoring code | [[../prompts/code-debug]], [[../prompts/fix-code]] |
| [[../workflows/document-extraction]] | Extracting content from PDFs, images, spreadsheets | [[../prompts/cheap-summary]] |
| [[../workflows/odoo-accounting]] | Odoo tasks, accounting reports, chart of accounts | [[../prompts/plan-architecture]] |
| [[../workflows/memory-recall]] | Recalling previous decisions, facts, or session history | none — navigate memory directly |

## Notes

- Open only the workflow relevant to the current task.
- If a workflow seems wrong, return here and re-route.
- If no workflow fits, escalate to plan mode and log the gap.

## Related

- [[../wiki/index]] — master wiki catalog
- [[../indexes/prompts]] — prompt router
- [[../indexes/tools]] — tool router
