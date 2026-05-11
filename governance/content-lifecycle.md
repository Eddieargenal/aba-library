---
type: governance
status: active
created: 2026-05-11
updated: 2026-05-11
---

# Content Lifecycle & Maintenance

*Part of the Knowledge Library Governance Framework v2.0. See [[00_index]] for all governance sub-documents.*

---

## Content Lifecycle & States

Every file carries a `status` field. Transitions are governed and logged.

```
draft → under_review → approved → active → superseded → archived
```

### Source Metadata (`01-sources/`)

```yaml
status: active | superseded | archived | under_review
review_cycle: quarterly | annual | event_triggered
last_reviewed: YYYY-MM-DD
next_review: YYYY-MM-DD
supersedes:
superseded_by:
foundational: true | false
```

The 2007–2026 date range is not a problem if each source is clearly marked as `foundational`, `still_valid`, `partially_superseded`, or `historical`. Age alone does not determine relevance.

---

## Schema Change Control

Every change to `governance/schema/` follows this mandatory sequence:[cite:23]

```
1. Change proposed (any role) + rationale documented
2. Impact assessed via lint check against existing files
3. Sample migration tested on 3–5 representative files
4. Library Steward approves
5. Technical Maintainer applies change
6. All affected 00_index.md files updated by LLM agent
7. Lint rules updated
8. Change logged in governance/schema/changelog.md
   [date | author | change description | files affected | migration applied]
```

**No agent silently rewrites schema rules. Ever.**

---

## Pattern Governance (`11-patterns/`)

Without discipline, `11-patterns/` becomes a graveyard of interesting observations. Every pattern requires the following frontmatter:[cite:23]

```yaml
pattern_status: candidate | under_review | validated | promoted | rejected | archived
promotion_target: concept | framework | tool | risk_register | none
evidence_count:
contexts_observed: []
review_by:
review_date:
contradictions_checked: true | false
applicability:
```

Promotion requires: observation in ≥2 contexts (or strong validation in one critical context), contradiction check passed, applicability boundaries defined, existing concepts/frameworks checked for duplication, and Domain Steward approval.[cite:24]

---

## Linting: Proactive LLM Health Checks

Linting is **not a static audit** — it is a regular LLM-run diagnostic that produces a `lint-report-YYYY-MM-DD.md` filed into `outputs/internal/` and fed back into the wiki as an internal output. This converts the contradiction register from a static log into a **living diagnostic layer**.[cite:32]

### Lint Checks Include

- Files missing required frontmatter fields (status, review date, tags, source links)
- `00_index.md` entries that are stale, vague, or missing
- Patterns in `candidate` status older than 90 days with no review activity
- Outputs past their `valid_until` date with no supersession record
- Concepts or frameworks referenced in outputs but not linked in indexes
- Contradictions discovered during query activity not yet logged in `12-risks-contradictions/`
- New article candidates based on emerging gaps or cross-document connections
- Schema drift (naming inconsistencies, non-standard tags, duplicate concepts)

### Lint Failure Levels

| Level | Condition | Action |
|---|---|---|
| **Critical** | Unlogged schema change; agent navigation broken | Block publication; escalate to Steward immediately |
| **High** | Missing frontmatter on active files; stale outputs in circulation | Flag in lint report; 7-day resolution target |
| **Medium** | Patterns past review date; vague index entries | Flag in lint report; quarterly resolution |
| **Low** | New article candidates; connection suggestions | Log for Governance Council review |
