---
type: memory-governance
status: active
updated: 2026-05-06
---

# Memory Rules

Simple rules for what belongs in vault memory.

## The 10 Compliance Rules

See [[vault-compliance-rules]] for full details.

### Quick Reference

| Rule | What To Do |
|------|------------|
| 1. Cite sources | Every claim needs a source |
| 2. Link decisions | Decisions → evidence |
| 3. Claim types | Use ✅ 🔹 🎯 💡 ❓ |
| 4. Contradictions | Put in unresolved/contradictions/ |
| 5. Update index | After every content add |
| 6. Append-only log | Only add, never overwrite |
| 7. Don't overwrite | Raw sources are sacred |
| 8. Supersede | Mark old as superseded |
| 9. Review status | draft → reviewed → validated → stale |
| 10. Verify | Wiki for navigation, sources for truth |

## What Stays in Vault

| Category | stale_after_days | What It Is |
|----------|------------------|------------|
| infrastructure | 14 | Server configs, IPs, Docker |
| decisions | 90 | Architectural choices |
| procedures | 30 | Verified procedures |
| outcomes | 180 | Lessons learned |
| unresolved | 30 | Gaps, contradictions |

**What NOT stored here:** user preferences, session history, task context.

## Claim Type Required

Every entry must specify:

```yaml
claim_type: fact | inference | decision | hypothesis | unresolved
```

## Review Status Required

Every entry must specify:

```yaml
status: draft | reviewed | validated | stale
```

## Supersession Pattern

```markdown
### Superseded
- date: YYYY-MM-DD
- superseded_by: [link]
- reason: [why]
```

## What Agents Should Do

- Read: workflows, prompts, tools, procedures, decisions
- Write: task outcomes with claim types, discovered gaps, architectural decisions
- Don't write: user preferences, session state, task context
- Always: cite sources, use claim types, use review status