---
type: section-index
status: active
updated: 2026-05-11
---

# ABA Wiki — Operational Governance

This section contains all operational documents governing the ABA/DRR wiki: agent behavioral contract, operating rules, access guide, and agent prompts. Domain content (concepts, frameworks, tools, sources) lives in `wiki/aba/`.

Agents working in the ABA wiki read `wiki/aba/AGENTS.md` first (stub that redirects here). For the full behavioral contract, read `agent-contract.md`. For task-specific prompts, read `prompts/00_index.md`.

---

## Core Operational Docs

| Document | Purpose | When to Read | When NOT to Read |
|---|---|---|---|
| `AGENTS.md` | ABA domain agent entry point — routing table for wiki operations | First read when entering the ABA wiki from outside | If already in the wiki mid-task |
| `CLAUDE.md` | ABA agent operating rules — layer discipline, ingest update chain, query procedure, lint checks, tool quality standard | Before any ingest, query, lint, or tool-building operation | If already familiar with the rules in this session |
| `agent-contract.md` | Authoritative behavioral contract — rule precedence, layer discipline (hard rule), domain query workflow, prohibited behaviors, quality obligations | When uncertain about how agents must behave; when a rule conflict arises | For routine tasks where rules are already loaded |
| `agent-operating-model.md` | What agents are permitted to do in this wiki — 6 capabilities and 6 operating rules | When setting up a new agent session or onboarding a new agent type | Mid-task when operating model is already established |
| `how-to-use-this-wiki.md` | Access guide for AI agents (5-step nav flow) and human users (5-step workflow) | When orienting a new agent or user to the wiki | When agent is already operational in the wiki |

---

## Agent Prompts (`prompts/`)

Read `prompts/00_index.md` for the full index. Quick reference:

| Prompt File | Task It Runs | When to Use |
|---|---|---|
| `ingest-new-source.md` | Add a new source PDF through extraction, source page creation, and wiki updates | Whenever a new source document is available for ingestion |
| `extract-source-from-pdf.md` | Convert a raw PDF into a complete extracted source page | Before running ingest-new-source; for any PDF in `01-sources/raw/` |
| `query-wiki.md` | Answer a domain question using wiki content with citations | Any domain question about urban DRR, ABA, field tools, or response design |
| `lint-wiki.md` | Run quality check — orphan pages, missing citations, stubs, evidence gaps | Periodically or after a major ingestion pass |
| `run-manual-lint-checklist.md` | Command-based fallback lint when automated script unavailable | When `scripts/lint_wiki.py` is not implemented |
| `build-framework-from-sources.md` | Write a Karpathy-style operational decision framework | When a lifecycle decision point lacks a framework |
| `build-concept-pages-from-sources.md` | Build or rewrite concept pages bottom-up from extracted sources | After a significant ingestion pass |
| `build-new-tool-from-sources.md` | Construct a new tool page with decision domains and scoring thresholds | When a decision question needs a structured analytical tool |
| `review-tool-quality.md` | Audit a tool page against the 10-field quality standard | When developing a tool page or after new source ingestion |
| `generate-field-instrument.md` | Create a new data collection form, checklist, or interview guide | When a tool page identifies a data need without an existing instrument |
| `create-decision-memo.md` | Produce a structured decision memo after a tool assessment | After any Tool 01 assessment |
| `detect-duplication-and-gaps.md` | Identify activity overlap and uncovered needs before finalizing area strategy | Before finalizing the integrated area strategy |
| `update-crosslinks.md` | Update cross-references after adding new pages or completing ingestion | After any new page creation |
