---
type: index
scope: templates
status: active
---

# Templates Index

Scaffold files for creating new vault content. Use these as starting points for workflows, prompts, tools, and memory records.

## Available Templates

| Template | Use For | Link |
|----------|---------|------|
| [[workflow-template]] | Creating new task workflows | [[../governance/workflows/model-routing]] as example |
| [[tool-template]] | Adding new tool references | [[../tools/hermes]] as example |
| [[prompt-template]] | Creating reusable prompt templates | [[../prompts/code-debug]] as example |
| [[task-log-template]] | Logging task execution results | [[../memory/runtime/logs/task-log]] as example |
| [[memory-record-template]] | Adding new memory entries | [[../memory/categories/infrastructure]] as example |

## How to Use

1. Copy the template file to the appropriate folder
2. Replace placeholder values (in brackets `[]`)
3. Add frontmatter with `type`, appropriate `scope`, and `status: active`
4. Link from the relevant index file

## Template Naming Convention

- Workflows: `governance/workflows/[name].md`
- Tools: `tools/[name].md`
- Prompts: `prompts/[name].md`
- Memory records: `memory/categories/[category].md`

## Related

- [[../indexes/workflows]]
- [[../indexes/tools]]
- [[../indexes/prompts]]
- [[../indexes/memory]]