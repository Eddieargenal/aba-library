---
type: workflow
scope: coding-tasks
status: active
updated: 2026-05-06
---

# Workflow: Coding Tasks

Use this workflow for writing, editing, debugging, or refactoring code.

## Steps

1. **Understand the requested change.**
   - Read the user request fully before touching any file.
   - Clarify ambiguity before acting if the request is unclear.

2. **Inspect relevant files before editing.**
   - Read the target file(s) and any directly imported dependencies.
   - Do not assume file contents — read them.

3. **Avoid changing unrelated code.**
   - Scope changes to only what the task requires.
   - Do not refactor, rename, or clean up code not mentioned in the task.

4. **Back up important files before risky changes.**
   - If a change is hard to reverse, copy the file to `archive/` with a timestamp before editing.
   - Note the backup path in your response.

5. **Make minimal changes.**
   - Prefer the smallest diff that correctly solves the problem.
   - Do not introduce abstractions for hypothetical future needs.

6. **Test or validate.**
   - Run tests if available.
   - If tests are not available, describe how you verified correctness.
   - State clearly if you could not test the change.

7. **Summarize exact files changed.**
   - List every file modified, created, or deleted.
   - Include line ranges for significant edits.

8. **Log known failures.**
   - If a test fails or validation is partial, log it in [[../memory/runtime/logs/task-log]].
   - Do not claim success when uncertainty exists.

## Model Tier

- Small targeted fix → fix mode → [[../prompts/fix-code]]
- Debugging or implementation → code mode → [[../prompts/code-debug]]
- Architecture or major refactor → plan mode first → [[../prompts/plan-architecture]]

## Linked Files

- [[../prompts/fix-code]]
- [[../prompts/code-debug]]
- [[../prompts/plan-architecture]]
- [[../memory/runtime/logs/task-log]]
