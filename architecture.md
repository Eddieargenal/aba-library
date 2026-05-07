---
type: documentation
scope: architecture
updated: 2026-05-07
---

# Vault Architecture

Visual overview of the AI Agent Wiki structure and navigation flows.

## Three-Layer Architecture (Karpathy LLM Wiki Pattern)

```mermaid
graph TD
    S[sources/] -->|read-only input| W
    W[Wiki Layer<br/>memory/ workflows/ tools/ agents/ prompts/] -->|governed by| SC
    SC[Schema Layer<br/>SCHEMA.md + vault-compliance-rules.md]
    WI[wiki/index.md<br/>master catalog] --> W
    LOG[memory/runtime/logs/log.md<br/>append-only] --> W
```

## Folder Structure

```mermaid
graph TD
    A[obsidian-vault/] --> SC[SCHEMA.md]
    A --> B[00_Start_Here.md]
    A --> C[README.md]
    A --> D[QUICK.md]
    A --> SRC[sources/]
    A --> WI[wiki/index.md]
    A --> E[indexes/]
    A --> F[workflows/]
    A --> G[prompts/]
    A --> H[tools/]
    A --> I[agents/]
    A --> J[memory/]
    A --> K[templates/]

    F --> F1[ingest.md]
    F --> F2[query.md]
    F --> F3[lint.md]
    F --> F4[...domain workflows]

    E --> E1[workflows.md]
    E --> E2[prompts.md]
    E --> E3[tools.md]
    E --> E4[memory.md]

    J --> J1[categories/]
    J --> J2[runtime/logs/]
    J --> J3[indexes/]
    J --> J4[MEMORY.md]
```

## Agent Navigation Flow

```mermaid
flowchart LR
    A[User Request] --> SC[SCHEMA.md]
    SC --> B[00_Start_Here.md]
    B --> WI[wiki/index.md]
    WI --> D[indexes/]
    D --> E[workflows/]
    E --> F[prompts/ or tools/]
    F --> G[Execute Task]
    G --> H[memory/runtime/logs/log.md]
```

## Three Operations Flow

```mermaid
flowchart TD
    SRC[sources/YYYY-MM-DD_slug.md] -->|Ingest| WP[wiki pages updated]
    WP --> IDX[wiki/index.md updated]
    IDX --> LOG[log.md appended]

    Q[User Question] -->|Query| IDX2[wiki/index.md read first]
    IDX2 --> PG[relevant pages opened]
    PG --> ANS[synthesized answer with citations]

    LINT[Lint trigger] --> SCAN[scan all wiki pages]
    SCAN --> UR[memory/categories/unresolved.md]
    SCAN --> LOG2[log.md appended]
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