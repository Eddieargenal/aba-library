---
type: index
scope: templates
---

# Templates Index

Scaffold files for creating new vault content. Use these as starting points for workflows, prompts, tools, and memory records.

## Available Templates

| Template | Use For | Link |
|----------|---------|------|
| [[../templates/workflow-template]] | Creating new task workflows | [[../workflows/model-routing]] as example |
| [[../templates/tool-template]] | Adding new tool references | [[../tools/hermes]] as example |
| [[../templates/prompt-template]] | Creating reusable prompt templates | [[../prompts/code-debug]] as example |
| [[../templates/task-log-template]] | Logging task execution results | [[../memory/runtime/logs/task-log]] as example |
| [[../templates/memory-record-template]] | Adding new memory entries | [[../memory/categories/behavioral]] as example |

## How to Use

1. Copy the template file to the appropriate folder
2. Replace placeholder values (in brackets `[]`)
3. Add frontmatter with `type`, appropriate `scope`, and `status: active`
4. Link from the relevant index file

## Template Naming Convention

- Workflows: `workflows/[name].md`
- Tools: `tools/[name].md`
- Prompts: `prompts/[name].md`
- Memory records: `memory/categories/[category].md`

## Related

- [[../indexes/workflows]]
- [[../indexes/tools]]
- [[../indexes/prompts]]
- [[../indexes/memory]]