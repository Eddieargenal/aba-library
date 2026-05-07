---
type: index
scope: wiki-master
status: validated
updated: 2026-05-07
---

# Wiki Index

**Read this file first on every query.** It is the master catalog of all wiki pages. Find the relevant pages here, then open them.

After every ingest: add new pages, update summaries that changed. After every lint: mark stale pages.

---

## Knowledge Base (`memory/categories/`)

| Page | Summary |
|------|---------|
| [[../memory/categories/infrastructure]] | Servers, IPs, Docker networks, VPS config, SSH access |
| [[../memory/categories/decisions]] | Architectural and product decisions with rationale |
| [[../memory/categories/procedures]] | Verified step-by-step technical guides |
| [[../memory/categories/outcomes]] | Lessons learned and post-task retrospectives |
| [[../memory/categories/unresolved]] | Open questions, contradictions, documentation gaps |

---

## Operations (`workflows/`)

| Page | Summary |
|------|---------|
| [[../workflows/ingest]] | Add a source document and update the wiki |
| [[../workflows/query]] | Answer a question from the wiki with citations |
| [[../workflows/lint]] | Health-check the wiki for stale pages and contradictions |
| [[../workflows/vault-initialization]] | Load vault context at session start |
| [[../workflows/vault-maintenance]] | Keep the vault healthy and self-improving |
| [[../workflows/model-routing]] | Select the right model/mode for a task |
| [[../workflows/coding-tasks]] | Write, edit, debug, or refactor code |
| [[../workflows/document-extraction]] | Extract content from PDFs, images, spreadsheets |
| [[../workflows/odoo-accounting]] | Odoo tasks, accounting reports, chart of accounts |
| [[../workflows/memory-recall]] | Recall previous decisions, facts, or session history |

---

## Tools (`tools/`)

| Page | Summary |
|------|---------|
| [[../tools/hermes]] | Hermes tool capabilities and configuration reference |
| [[../tools/openclaw]] | OpenClaw tool capabilities and configuration reference |
| [[../tools/obsidian]] | Obsidian — markdown wiki and vault management |
| [[../tools/openrouter]] | OpenRouter — model API routing and cost management |
| [[../tools/tailscale]] | Tailscale — zero-config VPN for remote access |
| [[../tools/n8n]] | n8n — workflow automation and webhook orchestration |

---

## Agents (`agents/`)

| Page | Summary |
|------|---------|
| [[../agents/Hermes]] | Hermes: model-routing and task-execution agent |
| [[../agents/OpenClaw]] | OpenClaw: gateway agent for server-side and external integrations |

---

## Prompts (`prompts/`)

| Page | Summary |
|------|---------|
| [[../prompts/cheap-summary]] | Cheap-mode prompt for summaries and simple lookups |
| [[../prompts/fix-code]] | Fix-mode prompt for small code patches and one-liners |
| [[../prompts/code-debug]] | Code-mode prompt for debugging and implementation |
| [[../prompts/plan-architecture]] | Plan-mode prompt for architecture and complex reasoning |
| [[../prompts/review-output]] | Review prompt for validating agent output |
| [[../prompts/memory-write-review]] | Review prompt before writing to memory |

---

## How to Use This Index

- **On query:** Scan the table headers to find the relevant section, then open the 1-3 most relevant pages.
- **On ingest:** After updating wiki pages, add any new rows here and update summaries that changed.
- **On lint:** Pages marked `stale` in their frontmatter should be flagged in the summary column: `⚠️ stale`.

*This file does not catalog `sources/` — raw documents are not wiki pages.*
