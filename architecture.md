---
type: documentation
scope: architecture
---

# Vault Architecture

Visual overview of the AI Agent Wiki structure and navigation flows.

## Folder Structure

```mermaid
graph TD
    A[obsidian-vault/] --> B[00_Start_Here.md]
    A --> C[README.md]
    A --> D[QUICK.md]
    A --> E[indexes/]
    A --> F[workflows/]
    A --> G[prompts/]
    A --> H[tools/]
    A --> I[agents/]
    A --> J[memory/]
    A --> K[templates/]

    E --> E1[workflows.md]
    E --> E2[prompts.md]
    E --> E3[tools.md]
    E --> E4[memory.md]
    E --> E5[templates.md]

    J --> J1[categories/]
    J --> J2[runtime/]
    J --> J3[indexes/]
    J --> J4[MEMORY.md]
    J --> J5[memory-rules.md]
```

## Agent Navigation Flow

```mermaid
flowchart LR
    A[User Request] --> B[00_Start_Here.md]
    B --> C{Routing Table}
    C --> D[indexes/]
    D --> E[workflows/]
    E --> F[prompts/ or tools/]
    F --> G[Execute Task]
    G --> H[memory/runtime/logs/log.md]
```

## Memory System Architecture

```mermaid
flowchart TB
    A[User Request] --> B{Hermes Agent}
    B --> C[Category Files<br/>Source of Truth]
    B --> D[Index Files<br/>Derived Lookup]
    B --> E[Runtime Files<br/>Logs & Recovery]

    C --> C1[behavioral.md]
    C --> C2[infrastructure.md]
    C --> C3[decisions.md]
    C --> C4[procedures.md]
    C --> C5[tools.md]
    C --> C6[projects.md]
    C --> C7[pending.md]
    C --> C8[unresolved.md]
    C --> C9[outcomes.md]

    D --> D1[key-index.jsonl]
    D --> D2[keyword-index.jsonl]
    D --> D3[relations.jsonl]

    E --> E1[log.md]
    E --> E2[recovery/]
```

## Truth State Transitions

```mermaid
stateDiagram-v2
    [*] --> proposed: agent-inferred
    proposed --> validated: user-confirmed
    proposed --> disputed: contradiction found
    disputed --> resolved: user resolves
    resolved --> validated: correct fact
    validated --> superseded: new decision
    superseded --> archived
```

## File Type Legend

| Prefix | Type | Purpose |
|--------|------|---------|
| `00_` | Entry point | Agent/human starting point |
| `indexes/` | Cross-reference | Navigation tables |
| `workflows/` | Task guides | Step-by-step procedures |
| `prompts/` | Templates | Reusable prompt patterns |
| `tools/` | Reference | Tool capability cards |
| `agents/` | Profiles | Agent definitions |
| `memory/` | Knowledge | Governed truth store |
| `templates/` | Scaffolds | File creation templates |

## Navigation Quick Reference

| From | To | When |
|------|-----|------|
| 00_Start_Here.md | indexes/workflows.md | Need a task workflow |
| indexes/workflows.md | workflows/*.md | Select specific workflow |
| workflow | prompts/*.md | Get prompt template |
| Any | memory/*.md | Recall facts |
| Any | tools/*.md | Understand tool capabilities |
| Any | agents/*.md | Understand agent roles |

## Index Dependencies

```mermaid
graph LR
    A[indexes/workflows.md] --> F1[workflows/model-routing.md]
    A --> F2[workflows/coding-tasks.md]
    A --> F3[workflows/document-extraction.md]

    B[indexes/prompts.md] --> P1[prompts/cheap-summary.md]
    B --> P2[prompts/fix-code.md]
    B --> P3[prompts/code-debug.md]
    B --> P4[prompts/plan-architecture.md]

    C[indexes/tools.md] --> T1[tools/hermes.md]
    C --> T2[tools/openclaw.md]
    C --> T3[tools/openrouter.md]
```

## Related Documentation

- [[README]] — Full vault documentation
- [[QUICK]] — Quick reference guide
- [[00_Start_Here]] — Entry point
- [[memory/memory-rules]] — Memory governance rules
- [[archive/CHANGELOG]] — Vault version history