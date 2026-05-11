---
type: index
scope: workflows
updated: 2026-05-06
status: active
---

# Workflow Index

Open a workflow only when routed here from [[../AGENTS]].

## Workflows

| Workflow | Use When | Linked Prompt |
|---|---|---|
| [[../governance/workflows/ingest]] | Adding a new source document to the wiki | none — follow steps directly |
| [[../governance/workflows/query]] | Answering a question from the wiki with citations | none — navigate wiki/index.md first |
| [[../governance/workflows/lint]] | Health-checking the wiki for stale pages and contradictions | none — produces repair list |
| [[../governance/workflows/model-routing]] | Selecting the right model/mode for a task | [[../prompts/cheap-summary]], [[../prompts/fix-code]], [[../prompts/code-debug]], [[../prompts/plan-architecture]] |
| [[../governance/workflows/vault-initialization]] | Loading vault context on session start | none — read files directly |
| [[../governance/workflows/vault-maintenance]] | Keeping the vault healthy and self-improving | [[../memory/categories/unresolved]] |
| [[../governance/workflows/coding-tasks]] | Writing, editing, debugging, or refactoring code | [[../prompts/code-debug]], [[../prompts/fix-code]] |
| [[../governance/workflows/document-extraction]] | Extracting content from PDFs, images, spreadsheets | [[../prompts/cheap-summary]] |
| [[../governance/workflows/odoo-accounting]] | Odoo tasks, accounting reports, chart of accounts | [[../prompts/plan-architecture]] |
| [[../governance/workflows/memory-recall]] | Recalling previous decisions, facts, or session history | none — navigate memory directly |

## Notes

- Open only the workflow relevant to the current task.
- If a workflow seems wrong, return here and re-route.
- If no workflow fits, escalate to plan mode and log the gap.

## Related

- [[../wiki/index]] — master wiki catalog
- [[../indexes/prompts]] — prompt router
- [[../indexes/tools]] — tool router
