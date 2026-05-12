---
type: governance
status: active
created: 2026-05-11
updated: 2026-05-11
---

# Vault Compliance Rules

*Authoritative single copy. All other copies of these rules are superseded. See [[governance/00_governance-index]] for all governance sub-documents.*

These 10 rules govern all content in the vault. No exceptions.

---

## Rule 1: Cite Raw Sources

Every wiki page must cite raw sources. Every factual claim needs a source.

```markdown
## Claim
The VPS runs Odoo 17. [source: VPS shell access, verified 2026-05-06]
```

## Rule 2: Link Decisions to Evidence

Every claim that affects decisions must link back to evidence.

```markdown
## Decision
Use PostgreSQL for the accounting database. [evidence: Odoo requires PostgreSQL for multi-company]
```

## Rule 3: Distinguish Claim Types

Every piece of content must be labeled as one of:

| Type | Symbol | Meaning |
|------|--------|---------|
| fact | ✅ | Verified externally |
| inference | 🔹 | Agent-derived from facts |
| decision | 🎯 | Deliberate choice |
| hypothesis | 💡 | Unverified assumption |
| unresolved | ❓ | Open question |

```markdown
✅ Fact: Odoo 17 runs on PostgreSQL
🔹 Inference: The Honduras module extends account_account
🎯 Decision: Use production VPS for Odoo deployment
💡 Hypothesis: Tailscale allows remote access without port forwarding
❓ Unresolved: Which Odoo version for long-term support?
```

## Rule 4: Contradictions → Unresolved

Contradictions go inline in `memory/categories/unresolved.md`. Never hide conflicts, never create separate files.

Use `type: contradiction` and reference both conflicting sources:

```markdown
### [title]
- type: contradiction
- status: proposed
- source: [where the conflict was found]
- updated: YYYY-MM-DD
- question: [what conflicts]
- evidence:
  - [source A says X]
  - [source B says Y]
- suggested_fix: [how to resolve]
```

## Rule 5: index.md Updated After Ingest

Every time new content is added, `indexes/` files must be updated.

## Rule 6: log.md Is Append-Only

`memory/runtime/logs/log.md` only appends. Never overwrite.

```markdown
## 2026-05-06
- Added infrastructure record for VPS
- Updated workflow index
```

## Rule 7: Don't Overwrite Raw Sources

Never edit raw source files. Create derived pages instead.

- Raw: `tools/hermes.md` (tool definition)
- Derived: Use the tool, don't modify it

## Rule 8: Supersede, Don't Delete

To update a claim, create a new entry and mark old as superseded. Never silently delete.

```markdown
### Superseded by [NEW-CLAIM]
- date: 2026-05-06
- superseded_by: odoo17-deployment
```

## Rule 9: Review Status

Important pages need review status:

```yaml
status: draft      # In progress
status: reviewed   # Agent verified
status: validated  # User confirmed
status: stale      # Needs re-verification
```

## Rule 10: Verify Against Sources

For accuracy-critical queries:
1. Start from wiki for navigation
2. Verify against raw sources when accuracy matters
3. Cite the verification in your output

---

## Stale Thresholds (Rule 9 Reference)

Entries past their threshold revert to `stale` status and must be re-verified before use.

| Category | stale_after_days | Rationale |
|----------|-----------------|-----------|
| infrastructure | 14 | Servers and configs change frequently |
| decisions | 90 | Decisions are more stable |
| procedures | 30 | Procedures drift with system changes |
| outcomes | 180 | Historical record, rarely stale |
| unresolved | 30 | Should be resolved or deferred |

---

## Summary Card

```
✅ Cite sources         🔹 Label inferences      🎯 Justify decisions
❓ Log contradictions   📋 Update indexes        📝 Append-only log
🚫 Don't overwrite      ♻️ Supersede not delete  🔄 Use review status
🔍 Verify at source
```

---

## Enforcement

These rules apply to:
- All new content created by agents
- All modifications to existing content
- All memory category entries

The vault is the source of navigation and structure, but raw sources (tool docs, API specs, config files) are the source of truth.

---

## Optional Governance Signals

*Carried forward from on-wiki reference — recommended but not mandatory.*

- **Provenance markers** for multi-source syntheses: append source references inline in the text body.
- **Append-only change history** for major sections: log what changed and when at the bottom of high-stakes pages.
- **Automated frontmatter validation** prior to publishing: run lint check to confirm required fields are present before any output is released.
