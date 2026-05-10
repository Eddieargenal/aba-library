---
type: overview
status: draft
created: 2026-05-07
updated: 2026-05-07
---
# Agent Operating Model

## What agents can do with this wiki

### Answer domain questions
Agents read relevant pages and produce practical guidance for technical teams. All answers must be grounded in the source pages.

### Ingest new sources
Use the prompt at [[../13-agent-prompts/ingest-new-source.md]]. Follow ingest-rules.md.

### Generate tools from sources
Use the prompt at [[../13-agent-prompts/build-new-tool-from-sources.md]].

### Generate field instruments
Use the prompt at [[../13-agent-prompts/generate-field-instrument.md]].

### Create decision memos
Use the template at [[../13-agent-prompts/create-decision-memo.md]].

### Lint the wiki
Use the prompt at [[../13-agent-prompts/lint-wiki.md]]. Check against [[../schema/lint-rules.md]].

## Agent rules
- Always read index.md before answering
- Always cite source pages
- Never fabricate evidence
- Flag uncertainty explicitly
- File reusable synthesis back into the wiki
- Append actions to log.md
