---
type: workflow
scope: vault-initialization
status: active
updated: 2026-05-11
---

# Workflow: Vault Initialization

Use this workflow when an agent starts a new session and needs to load context from the vault.

## Purpose

Initialize agent context from the obsidian-vault on session start. This ensures continuity and up-to-date knowledge.

## Prerequisites

- Vault path: `/Users/eddieargenal/Documents/obsidian-vault`
- Skill loaded: `obsidian-vault`

## Steps

### 1. Load Agent Context
Read `memory/context.md` first. This is the compressed current state — under 400 tokens.
- Apply Current Focus and First Action immediately to the session.
- If context.md is empty or stale, fall back to step 2.

### 2. Read Entry Point
Open `AGENTS.md` at vault root only if you need routing or rules not covered by context.md.

### 3. Check Session Handoff
Read `memory/current-handoff.md` to get:
- Current focus
- Active tasks
- Blockers
- Next actions

If `current-handoff.md` has content, apply it to the session context.

### 4. Check Next Session Prep
Read `memory/next-session.md` to see:
- What the previous session planned
- Pending work
- Suggested first action

### 5. Verify Memory Freshness
Check `governance/memory-rules.md` for current `stale_after_days` thresholds.

When reading any memory record:
- Compare `updated:` date to threshold
- If stale, note it but still use unless contradicted

### 6. Load Relevant Index
Based on hints from handoff or user request:
- `indexes/workflows.md` — task workflows
- `indexes/prompts.md` — prompt templates
- `indexes/tools.md` — tool references
- `indexes/memory.md` — memory categories

### 7. Update Context and Handoff at Session End
At the end of this session, update both:
- `memory/context.md` — refresh Current Focus, Active Decisions, Key Infrastructure, First Action
- `memory/current-handoff.md` — longer transition note: what was worked on, what's pending, blockers, next actions

## Model Tier

- This is a lookup/reading task → use `cheap` mode

## Linked Files

- [[../../AGENTS]]
- [[../../memory/current-handoff]]
- [[../../memory/next-session]]
- [[../../memory/MEMORY]]
- [[../../governance/memory-rules]]
- [[../../indexes/workflows]]
- [[../../indexes/tools]]
- [[../../indexes/memory]]
- [[../../memory/context]]
- [[../../memory/runtime/logs/log]]
