---
type: tool
tool: openclaw
status: active
updated: 2026-05-06
---

# Tool: OpenClaw

## Purpose

OpenClaw is a gateway-style local agent for server-hosted workflows, external service access, and scheduled automation.

## Used For

- Executing workflows on a server or VPS
- Accessing external APIs and services on behalf of agents
- Running scheduled or triggered jobs
- Bridging local agent sessions to remote systems via Tailscale or SSH

## Safety Rules

- Do not store credentials or API keys in this wiki or in OpenClaw config within this wiki.
- High-risk operations (data writes, deployments, deletions) require explicit user authorization.
- All consequential actions must be logged in [[../memory/runtime/logs/task-log]].
- Do not create a separate memory truth store — use this wiki's memory system.

## Related Workflows

- [[../agents/OpenClaw]]
- [[../tools/tailscale]]
- [[../tools/n8n]]
- [[../indexes/workflows]]

## Notes

- OpenClaw should be pointed at this wiki as its shared knowledge base.
- Consult OpenClaw documentation for how to set the wiki path in its config.
