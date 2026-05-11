# Agent Operating Instructions

This file tells AI agents how to work with the Urban DRR + ABA LLM Wiki.

## Entry Points
- For any domain question: read [[index.md]] first
- Read canonical behavior contract: [[agent-contract]]
- For tool use: read [[../../wiki/aba/04-tools/00_index]] + linked field instruments
- For new source ingestion: follow [[prompts/ingest-new-source]]
- For quality check: run [[prompts/lint-wiki]]
- If automation is unavailable: run [[prompts/run-manual-lint-checklist]]

## Page Types
See [[../schema/page-types]] for definitions and templates.

## Naming Conventions
See [[../schema/naming-conventions]].

## Quality Standard
See [[../schema/tool-quality-standard]].

A response that cites a tool but omits evidence collection and analysis instructions has failed quality.
