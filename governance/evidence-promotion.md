---
type: governance
status: active
created: 2026-05-11
updated: 2026-05-11
---

# Field Evidence Promotion Path

*Part of the Knowledge Library Governance Framework v2.0. See [[governance/00_governance-index]] for all governance sub-documents.*

---

The highest-risk pathway in the architecture. Field findings **never feed directly** into `02-concepts/`, `03-frameworks/`, or `04-tools/`. They enter a gated review queue — the **pending-findings queue** (open findings tracked in `indexes/current/routing-report.json` and counted by `manifest.pending_finding_count`).[cite:24]

```
Field Instrument Finding
        ↓
LLM logs as a finding record in the extracted source page frontmatter
[status: pending — appears as a pending finding in routing-report.json]
        ↓
Evidence Reviewer validates source, context, method, protection risks
[promotion_stage: finding]
        ↓
Promotion candidate — repeated across ≥2 contexts or critically validated
[candidate_target_pages set to the canonical destination folder]
        ↓
Domain Steward reviews + contradiction check against 07-known-tensions/ (and 06-risks/)
        ↓
Concept / Framework / Tool / Risk / Known-tension update drafted by LLM agent
[promotion_stage advances along the ladder: finding → concept → framework → tool → validated]
        ↓
Library Steward approves
        ↓
Knowledge Layer updated + all affected 00_index.md files refreshed + indexes rebuilt
[status: integrated]
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
# On the finding record (in the extracted source page frontmatter):
finding_id: F-001
finding_type: concept-definition | decision-rule | risk-identification | ...
status: pending | integrated        # pending = unrouted; integrated/done/complete/resolved/source_only = terminal
candidate_target_pages: []          # canonical destination page(s) for this finding
lifecycle_stage: []
# On the destination page once the finding is promoted:
promotion_stage: finding | concept | framework | tool | validated   # epistemic ladder (ADR-0001)
confidence: low | medium | high
```
