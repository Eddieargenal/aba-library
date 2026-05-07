---
type: memory-category
scope: decisions
status: active
updated: 2026-05-06
---

# Decisions — Architectural Choices

Stores deliberate architectural decisions. Must link to evidence.

## Claim Types

| Type | When to Use |
|------|-------------|
| 🎯 Decision | Deliberate architectural choice |
| ✅ Fact | Verified technical requirement |
| 💡 Hypothesis | Assumption being tested |

## Format

```markdown
### [decision-title]
- type: decision
- status: draft | reviewed | validated | stale
- claim_type: decision | fact | hypothesis
- source: [documentation, discussion, requirement]
- evidence: [links to why this decision was made]
- updated: YYYY-MM-DD

## Decision
[What was decided]

## Rationale
[Why this decision was made]

## Evidence
- [link 1]
- [link 2]

## Alternatives Considered
- [alternative 1]: [why rejected]
- [alternative 2]: [why rejected]
```

## Examples

### Decision Example

```markdown
### odoo-postgres-decision
- type: decision
- status: validated
- claim_type: decision
- source: Odoo 17 documentation requirements
- evidence: 
  - https://www.odoo.com/documentation/17.0/administration/setup/deploy.html#postgresql
- updated: 2026-05-06

## Decision
Use PostgreSQL as the Odoo database backend.

## Rationale
Odoo 17 requires PostgreSQL for multi-company and advanced accounting features.

## Evidence
- Odoo docs require PostgreSQL 12+
- Multi-company module needs transactional integrity

## Alternatives Considered
- SQLite: Rejected — doesn't support multi-company
- MySQL: Rejected — not supported by Odoo
```

## Superseding Decisions

When a decision changes, mark old as superseded:

```markdown
### Superseded
- date: YYYY-MM-DD
- superseded_by: [new decision link]
- reason: [why it changed]
- impact: [what needs updating because of this change]
```