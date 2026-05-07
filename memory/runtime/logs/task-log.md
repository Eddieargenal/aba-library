---
type: runtime-log
scope: task-log
status: active
---

# Task Log

Log important task results here. Routine, ephemeral output does not need to be logged. Log when:

- a task failed or produced unexpected output
- a consequential action was taken (file deleted, service restarted, data written)
- an escalation occurred (model tier bumped up)
- a tool was invoked with external effects

## Log Format

```
### [DATE] [TASK-SUMMARY]
- agent: hermes | openclaw | user
- mode: cheap | fix | code | plan | review
- action: [what was done]
- result: success | partial | failed
- files_changed: [list of files, if any]
- notes: [anything notable — failures, surprises, follow-up needed]
```

## Log Entries

<!-- Add entries below, newest first. -->
