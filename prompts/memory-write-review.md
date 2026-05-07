---
type: prompt
mode: review
status: active
updated: 2026-05-06
---

# Prompt: Memory Write Review

## Purpose

Review a proposed memory write before it is committed to a category file. Prevent fabricated, duplicated, or incorrectly classified memory from entering the system.

## Use When

- Before writing any new record to a memory category file
- Before updating an existing validated record
- Before promoting a `proposed` fact to `validated`
- Any time an agent-inferred fact is about to be stored

## Prompt Text

```
You are a memory governance reviewer. Evaluate the proposed memory write before it is committed.

Rules:
- Agent-inferred facts cannot become validated without user confirmation.
- Compaction records stay proposed until reviewed.
- Live observations need an expiration or last-observed date.
- No secrets or credentials may be stored.
- No raw LLM summaries become validated facts.
- If this write contradicts an existing validated record, route to unresolved instead.

Proposed write:
[PASTE THE PROPOSED MEMORY RECORD]

Existing record (if updating):
[PASTE EXISTING RECORD OR "none"]

Review criteria:
- Source: is the source tag correct? (user-stated / user-confirmed / agent-inferred / tool-output / compaction / consolidation)
- Truth state: is the proposed truth state appropriate? (proposed / observed / validated / disputed / superseded / archived)
- Contradiction: does this conflict with any existing validated record?
- Secrets: does this contain any credentials, tokens, or keys?
- Fabrication: is any part of this invented rather than observed?
- Category: is this in the correct category file?
```

## Expected Output

| Criterion | Result | Notes |
|---|---|---|
| Source tag | correct / incorrect | ... |
| Truth state | appropriate / escalate | ... |
| Contradiction | none / route to unresolved | ... |
| Secrets | none / block | ... |
| Fabrication | none / flag | ... |
| Category | correct / wrong file | ... |

Followed by: commit / revise / block / route-to-unresolved.

## Quality Checklist

- [ ] Source tag matches actual provenance.
- [ ] Truth state is not escalated beyond what the source warrants.
- [ ] No contradiction with validated records (or routed to unresolved).
- [ ] No credentials or sensitive data present.
- [ ] Correct category file identified.
