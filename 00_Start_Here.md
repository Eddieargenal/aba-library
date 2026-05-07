---
type: entry
status: active
updated: 2026-05-07
---

# Start Here

The vault provides **structured processes** — workflows, prompts, and tools. It does NOT replace Hermes memory.

> **New agents:** Read [[SCHEMA]] first. It defines the three layers (sources/wiki/schema), the three operations (ingest/query/lint), and all content conventions in one place.

## The 10 Rules (Must Read)

1. **Cite raw sources** — Every claim needs a source
2. **Link decisions to evidence** — Decisions must reference why
3. **Distinguish claim types** — Use ✅ 🔹 🎯 💡 ❓
4. **Contradictions → unresolved** — Never hide conflicts
5. **wiki/index.md updated after ingest** — Keep the master catalog current
6. **log.md append-only** — Never overwrite
7. **Don't overwrite raw sources** — Create derived pages
8. **Supersede don't delete** — Mark old as superseded
9. **Review status** — draft → reviewed → validated → stale
10. **Verify against sources** — Wiki for navigation, sources for accuracy

See [[memory/vault-compliance-rules]] for full rules.

## What The Vault Provides

| Folder/File | Use For |
|-------------|---------|
| [[SCHEMA]] | LLM instruction doc — architecture, operations, conventions |
| [[wiki/index]] | Master catalog — find any wiki page fast |
| [[sources/README]] | Raw source documents — read-only layer |
| [[workflows/]] | Step-by-step task guides |
| [[prompts/]] | Prompt templates by tier |
| [[tools/]] | Tool reference cards |
| [[indexes/]] | Finding the right workflow/prompt/tool |

## Claim Types

| Symbol | Meaning |
|--------|---------|
| ✅ Fact | Verified externally |
| 🔹 Inference | Agent-derived from facts |
| 🎯 Decision | Deliberate choice |
| 💡 Hypothesis | Unverified assumption |
| ❓ Unresolved | Open question |

## Review Status

| Status | Meaning |
|--------|---------|
| draft | In progress |
| reviewed | Agent verified |
| validated | User confirmed |
| stale | Needs re-verification |

## Navigation (For Agents)

1. Read [[SCHEMA]] — understand the vault structure and operations
2. Read [[memory/context]] — compressed current state, load first
3. Read [[wiki/index]] — find relevant wiki pages for the task
4. Open `indexes/workflows.md` → find the right workflow
5. Follow steps → use linked prompts
6. Log to `memory/runtime/logs/log.md`
7. Mark claims with correct type
8. Cite sources for all facts

## Quick Routing

| Task | Workflow |
|------|----------|
| Session start — load context | [[workflows/vault-initialization]] |
| Add a source document | [[workflows/ingest]] |
| Answer a question from the wiki | [[workflows/query]] |
| Health-check the wiki | [[workflows/lint]] |
| Model selection | [[workflows/model-routing]] |
| Coding/debugging | [[workflows/coding-tasks]] |
| Document/PDF extraction | [[workflows/document-extraction]] |
| Odoo accounting | [[workflows/odoo-accounting]] |
| Memory recall | [[workflows/memory-recall]] |
| Session end — update vault | [[workflows/vault-maintenance]] |

## Memory (Only Permanent Things)

| Category | Stores |
|----------|--------|
| [[memory/context]] | Compressed current state — load every session |
| [[memory/vault-compliance-rules]] | The 10 rules (read first) |
| [[memory/governance]] | Quick reference |
| [[memory/memory-rules]] | Memory system rules |
| [[memory/runtime/logs/log]] | Append-only log |
| [[memory/categories/infrastructure]] | Servers, IPs, Docker |
| [[memory/categories/decisions]] | Architectural choices |
| [[memory/categories/procedures]] | Verified guides |
| [[memory/categories/unresolved]] | Gaps & contradictions |
| [[memory/categories/outcomes]] | Lessons learned |

## Rules

- Don't duplicate what Hermes already handles
- Vault = permanent, cross-session knowledge
- Session = temporary, use Hermes directly
- Always cite sources
- Always use claim types
- Always use review status