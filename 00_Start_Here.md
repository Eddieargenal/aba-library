---
type: entry
status: active
updated: 2026-05-06
---

# Start Here

The vault provides **structured processes** — workflows, prompts, and tools. It does NOT replace Hermes memory.

## The 10 Rules (Must Read)

1. **Cite raw sources** — Every claim needs a source
2. **Link decisions to evidence** — Decisions must reference why
3. **Distinguish claim types** — Use ✅ 🔹 🎯 💡 ❓
4. **Contradictions → unresolved** — Never hide conflicts
5. **index.md updated after ingest** — Keep indexes current
6. **log.md append-only** — Never overwrite
7. **Don't overwrite raw sources** — Create derived pages
8. **Supersede don't delete** — Mark old as superseded
9. **Review status** — draft → reviewed → validated → stale
10. **Verify against sources** — Wiki for navigation, sources for accuracy

See [[memory/vault-compliance-rules]] for full rules.

## What The Vault Provides

| Folder | Use For |
|--------|---------|
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

1. Read [[memory/context]] — compressed current state, load first
2. Read [[memory/vault-compliance-rules]] — only if unfamiliar with the rules
3. Open `indexes/workflows.md` → find workflow
4. Follow steps → use linked prompts
5. Log to `memory/runtime/logs/log.md`
6. Mark claims with correct type
7. Cite sources for all facts

## Quick Routing

| Task | Workflow |
|------|----------|
| Session start — load context | [[workflows/vault-initialization]] |
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