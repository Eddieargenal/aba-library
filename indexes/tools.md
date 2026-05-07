---
type: index
scope: tools
updated: 2026-05-06
---

# Tools Index

Reference cards for tools used by agents. Open only the tool file you need.

## Tools

| Tool | Use For | Risk |
|---|---|---|
| [[../tools/openrouter]] | Routing model calls to multiple LLM providers | medium — cost and rate limits |
| [[../tools/hermes]] | Local model-routing and task-execution agent | low — local only |
| [[../tools/openclaw]] | Gateway-style local agent, server workflows, external services | medium — external service access |
| [[../tools/obsidian]] | Viewing and editing this wiki as a knowledge base | low — read-only unless plugins enabled |
| [[../tools/n8n]] | Workflow automation, scheduled jobs, webhook triggers | high — can trigger external actions |
| [[../tools/tailscale]] | Secure private network access between devices | medium — network access |

## Safety Notes

- Do not store credentials in any tool file.
- High-risk tools require explicit user authorization before use.
- Log tool invocations in [[../memory/runtime/logs/task-log]] when consequential.
