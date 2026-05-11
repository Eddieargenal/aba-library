---
type: audit-catalog
scope: wiki-master
status: validated
updated: 2026-05-08
title: Wiki Index
sources: ['wiki/index.md']
tags: ['wiki', 'index', 'governance']
---

# Wiki Index

**Audit use only.** Agents doing work navigate via section `00_index.md` files. Use this file during ingest (to register new pages) and vault-maintenance (to check for orphans and staleness).

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

## Operations (`governance/workflows/`)

Use [[../indexes/workflows]] if you need a workflow router before selecting a specific runbook.

| Page | Summary |
|------|---------|
| [[../governance/workflows/ingest]] | Add a source document and update the wiki |
| [[../governance/workflows/query]] | Answer a question from the wiki with citations |
| [[../governance/workflows/lint]] | Health-check the wiki for stale pages and contradictions |
| [[../governance/workflows/vault-initialization]] | Load vault context at session start |
| [[../governance/workflows/vault-maintenance]] | Keep the vault healthy and self-improving |
| [[../governance/workflows/model-routing]] | Select the right model/mode for a task |
| [[../governance/workflows/coding-tasks]] | Write, edit, debug, or refactor code |
| [[../governance/workflows/document-extraction]] | Extract content from PDFs, images, spreadsheets |
| [[../governance/workflows/odoo-accounting]] | Odoo tasks, accounting reports, chart of accounts |
| [[../governance/workflows/memory-recall]] | Recall previous decisions, facts, or session history |

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
| [[../agents/Hermes]] | Hermes: model-routing and task-execution agent (placeholder) |
| [[../agents/OpenClaw]] | OpenClaw: gateway agent for server-side and external integrations (placeholder) |

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

## Governance (`wiki/`)

| Page | Summary |
|------|---------|
| [[../governance/compliance-rules]] | The 10 non-negotiable vault governance rules — canonical reference |
| [[../governance/workflows/lint-plan]] | Self-contained lint routine: checks, output template, log destination |

---

## Diagnosis & Audit (`wiki/diagnosis/`)

| Page | Summary |
|------|---------|
| [[diagnosis/karpathy-vault-quality-diagnosis-2026-05-08]] | 2026-05-08 vault quality diagnosis — findings and action plan |
| [[diagnosis/karpathy-vault-audit-2026-05-09]] | 2026-05-09 first-pass audit — issues found and remediation backlog |

---

## Urban DRR + ABA Knowledge Wiki (`wiki/aba/`)

A separate, fully structured LLM wiki for urban disaster risk reduction and area-based emergency response. Entry point is its own index file.

| Resource            | Path                                         |
| ------------------- | -------------------------------------------- |
| **Wiki index**      | [[aba/index]]                                |
| **Quick answers**   | [[aba/wiki/00-overview/qa-common-questions]] |
| **Operating rules** | [[aba/CLAUDE]]                               |

---

## How to Use This Index

- **On query:** Scan the table headers to find the relevant section, then open the 1-3 most relevant pages.
- **On ingest:** After updating wiki pages, add any new rows here and update summaries that changed.
- **On lint:** Pages marked `stale` in their frontmatter should be flagged in the summary column: `⚠️ stale`.

*This file does not catalog `sources/` — raw documents are not wiki pages.*
