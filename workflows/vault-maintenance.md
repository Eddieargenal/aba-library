---
type: workflow
scope: vault-maintenance
status: active
updated: 2026-05-06
---

# Workflow: Vault Self-Maintenance

Use this workflow to keep the vault healthy, accurate, and self-improving.

## Purpose

The vault should evolve based on agent experience. This workflow defines how agents identify gaps, log issues, and improve the vault structure.

## When to Run

- After completing any non-trivial task (>10 minutes)
- When encountering a gap in documentation
- When a workflow produces unexpected results
- During session cleanup (end of significant session)

## Steps

### 1. Log Task Outcome

If the session involved meaningful work, log to `memory/runtime/logs/log.md`:
- What was attempted
- What succeeded/failed
- Any gaps discovered

### 2. Identify Documentation Gaps

Ask: "Did I need information that wasn't in the vault?"
- Missing workflow? → log to `memory/categories/unresolved` with `gap` tag
- Missing tool? → log to unresolved
- Stale information? → note in unresolved

### 2b. Check section index freshness

For each section folder in `_system/urban-drr-aba-wiki/wiki/`:
- Open `00_index.md`
- Compare its stated file count against the actual folder contents
- If the count is wrong, a significant file is unmentioned, or the characterization no longer fits, update the index
- Log any updated indexes to `memory/runtime/logs/log.md` with entry: `## [YYYY-MM-DD] maintenance | section index updated: [section-name]`

### 3. Review Unresolved

Check `memory/categories/unresolved.md`:
- Any gaps that can be filled now?
- Any contradictions that can be resolved?

### 4. Update Context and Handoff

Update both files before closing the session:
- `memory/context.md` — refresh Current Focus, Active Decisions, Key Infrastructure, First Action (keep under 400 tokens)
- `memory/current-handoff.md` — longer transition note: current state, what still needs attention, vault improvements needed

### 5. Suggest Improvements

If significant gap found, create a proposal in `memory/categories/unresolved`:

```
### vault-gap-[DATE]-[TOPIC]
- type: documentation-gap
- status: proposed
- source: agent-observed
- updated: YYYY-MM-DD
- gap: [what was missing]
- impact: [how it affected the task]
- suggested_fix: [how to fill it]
```

## Self-Improvement Patterns

| Pattern | Action | Log To |
|---------|--------|--------|
| Missing workflow | Create draft in unresolved | unresolved.md |
| Stale information | Flag in unresolved | unresolved.md |
| Workflow failure | Document in task-log | log.md |
| Useful discovery | Add to relevant category | appropriate category file |
| Tool gap | Log to unresolved | unresolved.md |

## Model Tier

- Review and logging → use `cheap` mode
- Creating new content → use appropriate tier for content type

## Linked Files

- [[../memory/runtime/logs/log]]
- [[../memory/categories/pending]]
- [[../memory/categories/unresolved]]
- [[../memory/categories/outcomes]]
- [[../memory/current-handoff]]
- [[../archive/CHANGELOG]]
- [[../memory/context]]

## Agent Rule

**Do not actively modify vault structure without user confirmation.** Log proposals to unresolved and let the user approve changes. This prevents the vault from drifting based on agent assumptions.