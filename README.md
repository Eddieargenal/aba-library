# AI Agent Wiki

This folder is an Obsidian-compatible markdown wiki designed for local AI agents (Hermes, OpenClaw, and others).

## What This Is

A structured knowledge base and lightweight governed memory system. It stores workflows, reusable prompts, tool references, decisions, and memory in a navigable folder hierarchy.

## How Agents Should Use It

1. Start at `00_Start_Here.md` — always.
2. Use the routing table to find the right index file.
3. Open only the workflow relevant to the task.
4. Open linked prompts, tools, or memory only when the workflow requires it.
5. Log results to `memory/runtime/logs/task-log.md`.

Do not scan the whole vault. Do not fabricate memory.

## Design Philosophy

- Obsidian-compatible: all files are standard markdown with `[[wikilinks]]`.
- Agent-navigable: each file links explicitly to the next relevant file.
- Human-readable: any person can open this folder in Obsidian or any text editor.
- Governed memory: truth states, source tags, and contradiction handling are built in.

## What Is Not Here

- No secrets, API keys, or credentials.
- No Obsidian plugin configuration.
- No automated scripts (intentionally deferred).
- No Hermes config changes (edit `~/.hermes/config.yaml` separately).

## Intended Users

- Hermes (model-routing and task-execution agent)
- OpenClaw (gateway-style local agent)
- Human operators reviewing agent decisions

## Structure Overview

```
SCHEMA.md              ← LLM instruction doc: layers, operations, conventions
00_Start_Here.md       ← agent entry point and routing table
README.md              ← this file (human-readable)
QUICK.md               ← condensed quick reference
architecture.md        ← visual structure diagrams
sources/               ← raw source documents (read-only)
wiki/
  index.md             ← master catalog of all wiki pages
workflows/             ← step-by-step task guides (ingest, query, lint + domain workflows)
agents/                ← agent profiles
prompts/               ← reusable prompt templates
tools/                 ← tool reference cards
memory/                ← governed wiki knowledge base
  categories/          ← long-term knowledge pages
  runtime/logs/        ← append-only log and task log
indexes/               ← domain-specific cross-reference tables (workflows, prompts, tools)
templates/             ← file scaffolds
archive/               ← sessions, changelogs, postmortems
```

## Three Operations (Karpathy LLM Wiki Pattern)

| Operation | Workflow | Summary |
|-----------|----------|---------|
| Ingest | [[workflows/ingest]] | Add source → update wiki pages → update index → log |
| Query | [[workflows/query]] | Read index → open pages → synthesize with citations |
| Lint | [[workflows/lint]] | Scan for stale/orphan/contradictions → log repair list |

See [[SCHEMA]] for the full architecture.

## Heavy Automation Is Intentionally Delayed

Hooks, indexing pipelines, and audit automation are future upgrades. This version focuses on structure, navigation, and content correctness first.
