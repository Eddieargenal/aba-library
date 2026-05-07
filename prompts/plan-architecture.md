---
type: prompt
mode: plan
status: active
updated: 2026-05-06
---

# Prompt: Plan Architecture

## Purpose

Design a system, produce a spec, or reason through a complex multi-step problem before any implementation begins.

## Use When

- Designing a new system or significant feature
- Writing a technical specification
- Evaluating tradeoffs between approaches
- Planning a multi-step implementation before coding
- Any task involving irreversible actions that require careful pre-validation

## Prompt Text

```
You are a senior software architect. Produce a clear plan before any implementation.

Rules:
- Do not write implementation code in this response.
- Identify all major components and their responsibilities.
- Identify all dependencies and integration points.
- List known risks, constraints, and open questions.
- Propose a step-by-step implementation order.
- Flag anything that requires user confirmation before proceeding.
- Ask clarifying questions if the requirements are ambiguous.

Goal:
[DESCRIBE THE SYSTEM OR FEATURE TO BE BUILT]

Constraints:
[LIST KNOWN CONSTRAINTS: technology, performance, cost, security, compatibility]

Context:
[DESCRIBE EXISTING SYSTEM, RELEVANT FILES, CURRENT STATE]

Open questions (if any):
[LIST UNKNOWNS OR AMBIGUITIES]
```

## Expected Output

- System overview: components and responsibilities.
- Dependency map or integration diagram (as text/table).
- Risk list with mitigations.
- Ordered implementation steps.
- List of questions requiring user confirmation.

## Quality Checklist

- [ ] No implementation code written before plan is confirmed.
- [ ] All major components are identified.
- [ ] Risks are named and mitigation strategies proposed.
- [ ] Implementation steps are in a safe execution order.
- [ ] Ambiguities are listed as questions, not assumptions.
- [ ] Plan is complete enough that a separate agent could implement it.
