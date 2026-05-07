---
type: prompt
mode: review
status: active
updated: 2026-05-06
---

# Prompt: Review Output

## Purpose

Review any agent output for quality, correctness, completeness, and safety before it is accepted or committed.

## Use When

- Before accepting a code change from an agent
- Before committing a memory write
- Before sending an agent-produced document to a user
- Before executing an agent-proposed plan
- Any time output quality is uncertain

## Prompt Text

```
You are a careful reviewer. Evaluate the provided output against the original request and the quality criteria below.

Rules:
- Do not assume the output is correct.
- Check for fabricated content, missing steps, and logical errors.
- Check that the output matches the requested format and scope.
- Flag any irreversible actions that have not been confirmed.
- Produce a structured review: pass / warn / fail for each criterion.

Original request:
[PASTE THE ORIGINAL USER REQUEST OR TASK]

Agent output to review:
[PASTE THE OUTPUT]

Review criteria:
- Correctness: does the output answer the request accurately?
- Completeness: are all required parts present?
- Scope: did the agent stay within the requested scope?
- Safety: are any irreversible or high-risk actions proposed without confirmation?
- Fabrication: is any content invented rather than derived from the source?
```

## Expected Output

A structured review table:

| Criterion | Result | Notes |
|---|---|---|
| Correctness | pass / warn / fail | ... |
| Completeness | pass / warn / fail | ... |
| Scope | pass / warn / fail | ... |
| Safety | pass / warn / fail | ... |
| Fabrication | pass / warn / fail | ... |

Followed by a summary: accept / revise / reject.

## Quality Checklist

- [ ] Every criterion is explicitly evaluated.
- [ ] Fabricated content is identified if present.
- [ ] Irreversible actions are flagged.
- [ ] A clear accept/revise/reject recommendation is given.
- [ ] Notes are specific enough to act on.
