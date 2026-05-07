---
type: memory-category
scope: unresolved
status: active
updated: 2026-05-06
---

# Unresolved — Documentation Gaps & Contradictions

This category stores:
- Documentation gaps (missing info)
- Open questions
- Contradictions found during work

## Claim Types Used Here

| Type | When to Use |
|------|-------------|
| ❓ Unresolved | Open question that needs answering |
| ⚠️ Contradiction | Conflicting information found in two sources |
| 🕳️ Gap | Information needed but not found in the vault |

## Format

All entries go inline in this file. Do not create separate contradiction files.

```markdown
### [title]
- type: unresolved | contradiction | gap
- status: proposed | confirmed
- source: [where the gap/contradiction was found]
- updated: YYYY-MM-DD
- question: [the open question or contradiction details]
- evidence: [links to sources that conflict or are missing]
- suggested_fix: [how to resolve]
```

## Examples

### Documentation Gap Example

```markdown
### vault-gap-odoo-modules
- type: unresolved
- status: proposed
- source: agent working on Odoo deployment
- updated: 2026-05-06
- question: What custom modules exist for Honduras accounting?
- evidence: No module list found in vault
- suggested_fix: Add module list to projects/odoo-honduras.md
```

### Contradiction Example

```markdown
### network-contradiction-001
- type: contradiction
- status: confirmed
- source: comparing infrastructure.md vs VPS shell
- updated: 2026-05-06
- question: Is port 8069 open on VPS?
- evidence: 
  - infrastructure.md says "ports: 22, 80, 443"
  - VPS has 8069 open for Odoo
- resolution: [pending]
```

## Rules

- Never hide contradictions — they go here
- Log gaps when you can't find information
- Don't try to resolve mid-session — log for review
- Use "superseded" pattern when resolving