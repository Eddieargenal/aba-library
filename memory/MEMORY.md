---
type: memory-index
status: active
updated: 2026-05-06
---

# Memory Index

This is the top-level index for vault memory. **Not all memory belongs here.**

## Vault Memory vs Hermes Memory

| Store In Vault | Store In Hermes |
|----------------|-----------------|
| Infrastructure (servers, networks) | User preferences |
| Architectural decisions | Session history |
| Verified procedures | Current task context |
| Documentation gaps | Project state |
| Lessons learned | Task outcomes |

**Rule:** If Hermes already tracks it, don't duplicate in the vault.

## What Vault Memory Provides

|| Category | File | Use For |
|---|---|---|---|
| ✓ | Infrastructure | [[categories/infrastructure]] | Server configs, IPs, networks, paths |
| ✓ | Decisions | [[categories/decisions]] | Architectural choices that persist |
| ✓ | Procedures | [[categories/procedures]] | Verified step-by-step guides |
| ✓ | Unresolved | [[categories/unresolved]] | Documentation gaps, contradictions |
| ✓ | Outcomes | [[categories/outcomes]] | Lessons learned from tasks |
| ✗ | Behavioral | (removed) | Use Hermes user profile |
| ✗ | Projects | (temporary — delete) | Use session context |
| ✗ | Pending | (temporary — delete) | Use session context |
| ✗ | Tools | (removed) | Use Hermes tool system |

## Session Files (Lightweight)

|| File | Purpose |
|---|---|---|
| [[current-handoff]] | Brief context for next session (2-3 sentences max) |
| [[next-session]] | What the previous session planned |
| [[runtime/logs/task-log]] | Task outcomes (not session logs) |

## Core Rules

- Do not duplicate what Hermes already handles
- Vault memory = persistent, cross-session knowledge
- Session memory = temporary, use Hermes directly
- Log gaps to unresolved — don't try to fix mid-session