---
type: tool
tool: hermes
status: active
updated: 2026-05-06
---

# Tool: Hermes

## Purpose

Hermes is the local model-routing and task-execution agent. It is the primary interface for running tasks through this wiki system.

## Used For

- Receiving user requests and routing them to the correct model and workflow
- Executing tasks using the cheap / fix / code / plan mode system
- Navigating this wiki as external memory
- Logging results to `memory/runtime/logs/task-log.md`

## Safety Rules

- Do not store large knowledge blobs inside Hermes config — use this wiki instead.
- Hermes config lives at `~/.hermes/config.yaml`. Do not modify it from within this wiki.
- Do not use Hermes to run irreversible external actions without user confirmation.

## Related Workflows

- [[../governance/workflows/model-routing]]
- [[../agents/Hermes]]
- [[../indexes/workflows]]

## Notes

- Hermes navigates via: `AGENTS.md → routing table → index → workflow → prompt/tool/memory only if needed → log result`
- To point Hermes at this wiki, set the wiki path in `~/.hermes/config.yaml` under the wiki or knowledge-base key (consult Hermes docs for exact key name).
