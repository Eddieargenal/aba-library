---
type: tool
tool: n8n
status: active
updated: 2026-05-06
---

# Tool: n8n

## Purpose

n8n is a workflow automation platform used for scheduled jobs, webhook triggers, and multi-service orchestration.

## Used For

- Triggering agent tasks on a schedule (cron)
- Receiving webhooks from external services and routing them to agent workflows
- Connecting agents to external APIs (email, databases, HTTP endpoints)
- Multi-step automation that spans more than one service

## Safety Rules

- **High risk tool.** n8n can trigger external actions that modify data, send messages, or deploy services.
- All n8n workflows that write data or call external APIs require explicit user authorization before first run.
- Do not store credentials in n8n workflow nodes that are exported to this wiki.
- Test workflows in a sandboxed or staging environment before running on production data.
- Log all n8n-triggered consequential actions in [[../memory/runtime/logs/task-log]].

## Related Files

- [[../agents/OpenClaw]]
- [[../tools/openclaw]]
- [[../memory/runtime/logs/task-log]]

## Notes

- n8n can be self-hosted on the VPS — consult [[../memory/categories/infrastructure]] for deployment details.
- Webhook URLs should be protected (authentication, IP allowlist) before exposing externally.
- n8n credential store is separate from this wiki — do not cross-populate.
