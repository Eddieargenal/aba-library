---
type: entry
status: active
updated: 2026-05-07
---

# Start Here

The vault provides **structured processes** — workflows, prompts, and tools. It does NOT replace Hermes memory.

> **New agents:** Read [[SCHEMA]] first. It defines the three layers (sources/wiki/schema), the three operations (ingest/query/lint), and all content conventions in one place.

## The 10 Rules (Must Read)

1. **Cite raw sources** — Every claim needs a source
2. **Link decisions to evidence** — Decisions must reference why
3. **Distinguish claim types** — Use ✅ 🔹 🎯 💡 ❓
4. **Contradictions → unresolved** — Never hide conflicts
5. **wiki/index.md updated after ingest** — Keep the master catalog current
6. **log.md append-only** — Never overwrite
7. **Don't overwrite raw sources** — Create derived pages
8. **Supersede don't delete** — Mark old as superseded
9. **Review status** — draft → reviewed → validated → stale
10. **Verify against sources** — Wiki for navigation, sources for accuracy

See [[memory/vault-compliance-rules]] for full rules.

## What The Vault Provides

| Folder/File                       | Use For                                                     |
| --------------------------------- | ----------------------------------------------------------- |
| [[SCHEMA]]                        | LLM instruction doc — architecture, operations, conventions |
| [[wiki/index]]                    | Master catalog — find any wiki page fast                    |
| [[sources/README]]                | Raw source documents — read-only layer                      |
| [[wiki/aba/00-overview/00_index]] | Urban DRR + ABA wiki — humanitarian domain knowledge        |
| [[workflows/]]                    | Step-by-step task guides (vault + domain workflows)         |
| [[indexes/workflows]]             | Workflow router (choose the right workflow first)           |
| [[prompts/]]                      | Prompt templates by tier                                    |
| [[tools/]]                        | Tool reference cards                                        |
| [[agents/]]                       | Agent profiles                                              |
| [[indexes/]]                      | Finding the right workflow/prompt/tool                      |
| [[archive/]]                      | Historical records                                          |
| [[architecture]]                  | Visual architecture and navigation diagrams                 |

## Vault Directory

| Section | What's here | Index |
|---|---|---|
| [[wiki/aba/00-overview/00_index]] | Urban DRR + ABA wiki — overview, operating rules, quick ref | (ABA wiki root: `wiki/aba/`) |
| [[indexes/workflows]] | Workflow router | (see [[workflows/]]) |
| [[indexes/templates]] | Prompt/template router by tier | (see [[prompts/]]) |
| [[indexes/tools]] | Tool reference cards | (see [[tools/]]) |
| [[memory/MEMORY]] | Long-term knowledge base | (see `memory/categories/`) |

## Urban DRR + ABA Wiki (`wiki/aba/`)

An **Area-Based Approach (ABA)** uses a defined geography — such as a neighborhood, district, or urban area — as the organizing frame for humanitarian, disaster risk reduction, and recovery action. Rather than planning by sector or population category alone, it brings humanitarian actors, local authorities, communities, and markets together to assess needs, capacities, and risks within the same territory. This wiki encodes the evidence base, operational tools, field instruments, and decision frameworks for implementing ABA in urban contexts.

**Progressive discovery:** Pick the section that matches your question, then use its `00_index.md` to find the right page. Each section index shows every file with a one-line summary.

| Section | Jump | What's here |
|---|---|---|
| 00 — Overview | [[wiki/aba/00-overview/00_index]] | Navigation, agent rules, quick Q&A, knowledge map. Start here if unsure. |
| 01 — Sources | [[wiki/aba/01-sources/extracted/00_index]] | Primary literature references — author, year, summary, ingestion status. (Raw index: [[wiki/aba/01-sources/raw/00_index]]) |
| 02 — Concepts | [[wiki/aba/02-concepts/00_index]] | Core definitions: ABA, geographic targeting, participation, resilience, urban risk. |
| 03 — Frameworks | [[wiki/aba/03-frameworks/00_index]] | Decision frameworks: appropriateness, area selection, transition, diagnosis. |
| 04 — Tools | [[wiki/aba/04-tools/00_index]] | Operational tools for assessment, planning, coordination, M&E. |
| 05 — Field Instruments | [[wiki/aba/05-field-instruments/00_index]] | Data collection forms: surveys, KIIs, observation sheets, templates. |
| 06 — Lifecycle | [[wiki/aba/06-lifecycle/00_index]] | Programme phases: area selection → strategy → implementation → handover. |
| 07 — Sector Applications | [[wiki/aba/07-sector-applications/00_index]] | ABA in specific sectors: shelter, WASH, health, livelihoods, protection. |
| 08 — Coordination | [[wiki/aba/08-coordination/00_index]] | Multi-actor coordination models, platforms, information management. |
| 09 — Monitoring & Learning | [[wiki/aba/09-monitoring-learning/00_index]] | MEL frameworks, resilience indicators, adaptive management, outcome tracking. |
| 10 — Transition & Scale | [[wiki/aba/10-transition-scale/00_index]] | Handover readiness, municipal integration, replication and scale-up. |
| 11 — Patterns | [[wiki/aba/11-patterns/00_index]] | Recurring design patterns and proven approaches across contexts. |
| 12 — Risks & Contradictions | [[wiki/aba/12-risks-contradictions/00_index]] | Known contradictions, misuse patterns, evidence gaps, protection risks. |
| 13 — Agent Prompts | [[wiki/aba/13-agent-prompts/00_index]] | Reusable AI agent prompts: ingest, query, lint, build tools, quality review. |

## Claim Types

| Symbol | Meaning |
|--------|---------|
| ✅ Fact | Verified externally |
| 🔹 Inference | Agent-derived from facts |
| 🎯 Decision | Deliberate choice |
| 💡 Hypothesis | Unverified assumption |
| ❓ Unresolved | Open question |

## Review Status

| Status | Meaning |
|--------|---------|
| draft | In progress |
| reviewed | Agent verified |
| validated | User confirmed |
| stale | Needs re-verification |

## Navigation (For Agents)

1. Read [[SCHEMA]] — understand the vault structure and operations
2. Read [[memory/context]] — compressed current state, load first
3. Read [[wiki/index]] — find relevant wiki pages for the task
4. Open [[indexes/workflows]] → find the right workflow
5. Follow steps → use linked prompts
6. Log to `memory/runtime/logs/log.md`
7. Mark claims with correct type
8. Cite sources for all facts

## Quick Routing

| Task | Workflow |
|------|----------|
| Session start — load context | [[memory/context]] |
| Add a source document | [[workflows/ingest]] |
| Answer a question from the wiki | [[wiki/index]] |
| Health-check the wiki | [[workflows/lint]] |
| Model selection | [[workflows/model-routing]] |
| Coding/debugging | [[workflows/coding-tasks]] |
| Document/PDF extraction | [[workflows/document-extraction]] |
| Odoo accounting | [[workflows/odoo-accounting]] |
| Memory recall | [[memory/MEMORY]] |
| Session end — update vault | [[workflows/vault-maintenance]] |

## Memory (Only Permanent Things)

| Category | Stores |
|----------|--------|
| [[memory/context]] | Compressed current state — load every session |
| [[memory/vault-compliance-rules]] | The 10 rules (read first) |
| [[memory/governance]] | Quick reference |
| [[memory/memory-rules]] | Memory system rules |
| [[memory/runtime/logs/log]] | Append-only log |
| [[memory/categories/infrastructure]] | Servers, IPs, Docker |
| [[memory/categories/decisions]] | Architectural choices |
| [[memory/categories/procedures]] | Verified guides |
| [[memory/categories/unresolved]] | Gaps & contradictions |
| [[memory/categories/outcomes]] | Lessons learned |

## Rules

- Don't duplicate what Hermes already handles
- Vault = permanent, cross-session knowledge
- Session = temporary, use Hermes directly
- Always cite sources
- Always use claim types
- Always use review status

---

## ABA Section Index (00_index Links Only)

- **00 Overview**: Wiki orientation, usage guidance, and operating model.  
  [[wiki/aba/00-overview/00_index]]
- **01 Sources — Extracted**: Standardized source extraction notes used as evidence-ready references.  
  [[wiki/aba/01-sources/extracted/00_index]]
- **01 Sources — Raw**: Raw source library index for original documents and ingest tracking.  
  [[wiki/aba/01-sources/raw/00_index]]
- **02 Concepts**: Core ABA/urban DRR concepts and shared definitions.  
  [[wiki/aba/02-concepts/00_index]]
- **03 Frameworks**: Decision and analysis frameworks for planning and strategy.  
  [[wiki/aba/03-frameworks/00_index]]
- **04 Tools**: Operational tools for assessment, prioritization, design, and implementation support.  
  [[wiki/aba/04-tools/00_index]]
- **05 Field Instruments**: Data collection instruments and field-ready templates.  
  [[wiki/aba/05-field-instruments/00_index]]
- **06 Lifecycle**: End-to-end ABA project stages from scoping through transition.  
  [[wiki/aba/06-lifecycle/00_index]]
- **07 Sector Applications**: Sector-specific application of ABA and urban DRR approaches.  
  [[wiki/aba/07-sector-applications/00_index]]
- **08 Coordination**: Multi-actor coordination models, structures, and protocols.  
  [[wiki/aba/08-coordination/00_index]]
- **09 Monitoring Learning**: MEL frameworks, indicators, and adaptive management references.  
  [[wiki/aba/09-monitoring-learning/00_index]]
- **10 Transition Scale**: Handover, institutionalization, and scale/replication guidance.  
  [[wiki/aba/10-transition-scale/00_index]]
- **11 Patterns**: Reusable patterns and recurring implementation logic across contexts.  
  [[wiki/aba/11-patterns/00_index]]
- **12 Risks Contradictions**: Evidence caveats, trade-offs, and unresolved tensions to check before decisions.  
  [[wiki/aba/12-risks-contradictions/00_index]]
- **13 Agent Prompts**: Prompts and agent-operating assets for wiki workflows.  
  [[wiki/aba/13-agent-prompts/00_index]]
