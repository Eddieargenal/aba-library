---
type: task-log-template
updated: YYYY-MM-DD
---

# Task Log Entry Template

Use this template when adding an entry to [[../memory/runtime/logs/task-log]].

## Template

```markdown
### [DATE] [TASK-SUMMARY]
- agent: hermes | openclaw | user
- mode: cheap | fix | code | plan | review
- action: [what was done — one sentence]
- result: success | partial | failed
- files_changed:
  - [file path and what changed]
- notes: [anything notable — failures, escalations, follow-up needed]
```

## When to Log

Log when:
- A task failed or produced unexpected output
- A consequential action was taken (file deleted, service restarted, data written to production)
- A model tier escalation occurred
- A tool was invoked with external effects (API call, deployment, data write)
- A procedure was executed and its outcome should be recorded

Do not log:
- Routine read operations
- Summarization tasks with no side effects
- Failed tool calls that were immediately retried successfully

## Example Entry

```markdown
### 2026-05-06 Restarted Odoo staging container after module update
- agent: hermes
- mode: fix
- action: SSH to VPS, ran docker restart odoo-staging
- result: success
- files_changed: none
- notes: Module custom_account_hn was updated; restart required for new Python methods to register.
```
