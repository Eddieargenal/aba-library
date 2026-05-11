---
type: memory-record-template
updated: YYYY-MM-DD
status: reference
---

# Memory Record Template

Use this template when adding a record to any category file.

## Standard Record Fields

```
### [RECORD-KEY]
- [category-specific-fields]: [value]
- status: proposed | observed | validated | disputed | superseded | archived
- source: user-stated | user-confirmed | agent-inferred | tool-output | compaction | consolidation
- updated: YYYY-MM-DD
```

## Category-Specific Fields

### Behavioral
```
- type: correction-rule | session-directive | explicit-preference | project-specific-rule | assistant-commitment | inferred-preference
- rule: [the behavior rule]
- context: [when does this apply?]
- supersedes: [prior key, if any]
```

### Decisions
```
- decision: [what was decided]
- rationale: [why]
- supersedes: [prior key, if any]
- related: [other keys]
```

### Procedures
```
- purpose: [what it accomplishes]
- prerequisites: [list]
- steps: [numbered list]
- verification: [how to confirm success]
- last_executed: YYYY-MM-DD
- failure_notes: [gotchas]
```

### Infrastructure
```
- host: [hostname or IP]
- observation: [what was observed]
- last_observed: YYYY-MM-DD
```

### Outcomes
```
- decision_key: [related key]
- action_taken: [what was done]
- result: [what happened]
- observed_at: YYYY-MM-DD
- impact: [what changed]
- lesson: [takeaway]
- applied_to: [project or system]
- source_session: [session ID or date]
```

## Truth State Guidance

| State | When to Use |
|---|---|
| proposed | Default for new agent-inferred or unreviewed records |
| observed | Directly observed this session — include last_observed date |
| validated | User has explicitly confirmed this fact |
| disputed | Contradicts another record — route to unresolved |
| superseded | Replaced by a newer record — keep for history |
| archived | No longer relevant |
