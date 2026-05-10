# Agent Operating Instructions

This file tells AI agents how to work with the Urban DRR + ABA LLM Wiki.

## Entry Points
- For any domain question: read [[index.md]] first
- Read canonical behavior contract: [[./00-overview/agent-contract]]
- For tool use: read [[./04-tools/]] + linked field instruments
- For new source ingestion: follow [[./13-agent-prompts/ingest-new-source]]
- For quality check: run [[./13-agent-prompts/lint-wiki]]
- If automation is unavailable: run [[./13-agent-prompts/run-manual-lint-checklist]]

## Page Types
See [[schema/page-types.md]] for definitions and templates.

## Naming Conventions
See [[schema/naming-conventions.md]].

## Quality Standard
See [[schema/tool-quality-standard.md]].

A response that cites a tool but omits evidence collection and analysis instructions has failed quality.
