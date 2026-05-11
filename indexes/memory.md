---
type: index
scope: memory
updated: 2026-05-06
status: active
---

# Memory Index

This index explains how the memory system is organized.

## Memory Categories (Vault-Specific)

These are the ONLY memory categories stored in the vault:

|| Category | File | Stores |
|---|---|---|---|
| ✓ | Infrastructure | [[../memory/categories/infrastructure]] | Server configs, IPs, Docker, paths |
| ✓ | Decisions | [[../memory/categories/decisions]] | Architectural decisions |
| ✓ | Procedures | [[../memory/categories/procedures]] | Verified step-by-step procedures |
| ✓ | Unresolved | [[../memory/categories/unresolved]] | Gaps, contradictions |
| ✓ | Outcomes | [[../memory/categories/outcomes]] | Lessons learned |

**What NOT to store here:**
- User preferences → Hermes user profile
- Session history → Hermes sessions
- Task context → session context
- Active projects → session context

## Memory Files

|| File | Purpose |
|---|---|---|
| [[../governance/compliance-rules]] | The 10 non-negotiable rules |
| [[../governance/governance-model]] | Governance model quick reference |
| [[../governance/memory-rules]] | Memory system rules |
| [[current-handoff]] | Brief context for next session |
| [[next-session]] | What previous session planned |
| [[runtime/logs/log]] | Append-only vault log |

## Category Files (Source of Truth)

The memory system has layers:

1. **Category files** — source of truth (see above)
2. **Index files** — derived lookup structures (JSONL)
3. **Runtime files** — logs and recovery

## Key Rules

- **No duplication** — if Hermes tracks it, don't store here
- **Vault = persistent** — cross-session knowledge
- **Session = temporary** — use Hermes directly
- **Log gaps** — when you discover missing docs, add to unresolved