---
type: index
scope: prompts
updated: 2026-05-06
---

# Prompt Index

Use this index to find the right prompt for a task. Open only the prompt you need.

## Prompts

| Prompt | Use When | Model Tier |
|---|---|---|
| [[../prompts/cheap-summary]] | Summarizing, rewriting, simple Q&A, extraction | cheap |
| [[../prompts/fix-code]] | Small targeted code changes, UI tweaks, one-liner fixes | fix |
| [[../prompts/code-debug]] | Debugging, implementation, multi-file refactors | code |
| [[../prompts/plan-architecture]] | Architecture decisions, specs, complex multi-step reasoning | plan |
| [[../prompts/review-output]] | Reviewing any agent output for quality or correctness | review |
| [[../prompts/memory-write-review]] | Reviewing a proposed memory write before committing it | review |

## Model Tier Reference

| Tier | Intended Cost | When to Use |
|---|---|---|
| cheap | lowest | summaries, rewrites, simple lookups |
| fix | low | small contained code changes |
| code | medium | debugging, implementation, refactoring |
| plan | high | architecture, specs, complex reasoning |
| review | medium | output validation, memory governance |

Use the cheapest model that can safely complete the task. Escalate only when needed.
