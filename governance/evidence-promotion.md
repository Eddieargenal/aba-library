---
type: governance
status: active
created: 2026-05-11
updated: 2026-05-11
---

# Field Evidence Promotion Path

*Part of the Knowledge Library Governance Framework v2.0. See [[governance/00_governance-index]] for all governance sub-documents.*

---

The highest-risk pathway in the architecture. Field findings **never feed directly** into `02-concepts/`, `03-frameworks/`, or `04-tools/`. They enter a gated review queue.[cite:24]

```
Field Instrument Finding
        ↓
LLM logs as Finding Note in 11-patterns/
[evidence_status: raw_finding]
        ↓
Evidence Reviewer validates source, context, method, protection risks
[evidence_status: reviewed_finding]
        ↓
Pattern candidate — repeated across ≥2 contexts or critically validated
[pattern_status: candidate]
        ↓
Domain Steward reviews + contradiction check against 12-risks-contradictions/
[pattern_status: under_review]
        ↓
Concept / Framework / Tool update drafted by LLM agent
        ↓
Library Steward approves
        ↓
Knowledge Layer updated + all affected 00_index.md files refreshed
[pattern_status: promoted]
```

## Evidence Eligibility Criteria (all must be met)

- Source is known and context is described
- Method is documented
- Finding is not a one-off anecdote
- Protection/do-no-harm risks checked
- Contradictory evidence considered
- Applicability limits stated
- Human Evidence Reviewer has approved

## Evidence Frontmatter

```yaml
evidence_status: raw_finding | reviewed_finding | candidate_pattern | validated_pattern | promoted
confidence: low | medium | high
reviewed_by:
review_date:
applicability:
limits:
protection_check: passed | flagged | pending
```
