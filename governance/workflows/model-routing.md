---
type: workflow
scope: model-routing
status: active
updated: 2026-05-11
---

# Workflow: Model Routing

Use this workflow when the task is to select the right model mode before executing.

## Routing Table

| Mode | Use For | Prompt |
|---|---|---|
| cheap | summaries, rewriting, simple questions, lookups | [[../../prompts/cheap-summary]] |
| fix | small code or UI changes, one-liner patches | [[../../prompts/fix-code]] |
| code | debugging, implementation, refactoring, multi-file changes | [[../../prompts/code-debug]] |
| plan | architecture, specs, complex multi-step reasoning | [[../../prompts/plan-architecture]] |

## Decision Rule

Use the cheapest model that can safely complete the task. Escalate only when needed.

## Steps

1. Read the user request.
2. Identify the primary action: summarize / change / debug / design.
3. Match to the mode table above.
4. If the task spans multiple modes (e.g., plan then code), start with plan.
5. Open the linked prompt.
6. Execute.
7. If the model fails or produces low-quality output, escalate one tier and retry.
8. Log the escalation in [[../../memory/runtime/logs/task-log]] if it happens more than once.

## Escalation Triggers

- Output is incomplete or logically wrong → escalate one tier.
- Task involves irreversible actions (file deletion, deployment, data write) → use plan minimum.
- User explicitly requests higher-quality reasoning → use plan.

## Linked Files

- [[../../agents/Hermes]]
- [[../../indexes/prompts]]
- [[../../memory/runtime/logs/task-log]]
