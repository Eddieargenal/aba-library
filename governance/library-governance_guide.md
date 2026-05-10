# Knowledge Library Governance Framework v2.0

*Aligned to the Knowledge Library Architecture (4-Zone) and Karpathy LLM Wiki Principles*

---

## Foundational Operating Principle

> **The LLM is the primary author and maintainer of synthesized knowledge. Humans set direction, approve changes, and review quality. The moment humans write wiki content directly at scale, the compounding mechanic breaks and you have a traditional KM system.**

This principle governs every role, policy, and workflow in this framework. Zone 2–3 content is **LLM-owned markdown**. Humans are product owners, not editors.[cite:28][cite:32]

---

## Governance Model: Federated + LLM-Native

The library adopts a **federated LLM-native governance model**[cite:24]:

- Central authority (Library Steward) sets universal standards — schema, lint rules, agent navigation, promotion protocols — and these are non-negotiable
- Domain Stewards manage sector content accuracy within centrally defined structure
- LLM agents own all writing, index maintenance, linting, and synthesis
- Humans approve, direct, and review — they do not draft

A purely centralized model creates bottlenecks. A fully decentralized model causes schema drift and inconsistency. The federated model protects the two most critical assets: **index reliability** and **schema discipline** — while allowing domain experts to manage knowledge without central approval for every edit.[cite:24]

---

## Roles & Authority Map

| Role | Authority Level | Primary Accountabilities |
|---|---|---|
| **Library Steward** | Final approver | Schema integrity, promotion/demotion rules, agent contract (`AGENTS.md`), governance decisions |
| **Technical Maintainer** | Implements approved changes | Lint tooling, schema migrations, file structure, changelog entries, LLM tooling |
| **Domain Stewards** (per sector) | Approve sector content | Accuracy of shelter, WASH, DRR, protection, livelihoods, coordination, tenure content in Zones 2–3 |
| **Agent Maintainer** | Manages LLM behavior | `AGENTS.md`, agent prompts, retrieval rules, runtime contradiction logic, fallback ladder |
| **Evidence Reviewer** | Gates field findings | Validates field instrument findings before `11-patterns/` entry; enforces evidence criteria |
| **Knowledge Governance Council** | Strategic direction | Quarterly cross-cutting decisions, scope changes, promotion disputes, multi-sector contradictions |
| **LLM Agent** | Primary author | All wiki synthesis, index auto-maintenance, lint reports, output drafts, backlink management |

> **Hard rule:** No agent may silently rewrite schema or governance rules. Agents propose; humans approve.[cite:23]

---

## The Agent Contract: `AGENTS.md`

The single most important file in the library. **Every agent reads this first, every time.** It consolidates what was previously split across `schema/`, `00-overview/`, and `13-agent-prompts/` into one authoritative behavioral contract — consistent with Karpathy's `AGENTS.md` / `CLAUDE.md` single-schema principle.[cite:36][cite:28]

### 1. Library Structure Map

A concise description of all zones, folders, and their purpose — precise enough that an agent can navigate without reading the full library. Each zone entry includes: folder name, purpose, mutability class, and when an agent should or should not read it.

### 2. Mutability Rules

| Location | Mutable? | By Whom |
|---|---|---|
| `raw/` | Never | No one — input only |
| `schema/` | Controlled | Technical Maintainer after Steward approval |
| `AGENTS.md` | Controlled | Agent Maintainer after Steward approval |
| `00-overview/` | Controlled | Library Steward |
| `01-05/` Zone 2 | LLM-drafted, human-approved | LLM drafts; Domain Steward approves |
| `06-10/` Zone 3 | LLM-drafted, human-approved | LLM drafts; Domain Steward approves |
| `11-patterns/` | Open intake, gated promotion | LLM logs; Evidence Reviewer gates promotion |
| `12-risks-contradictions/` | Open addition, governed removal | Any role adds; Steward approves removals |
| `outputs/` | Traceable | LLM drafts; content owner approves for release |

### 3. Runtime Contradiction Rule

Before answering any advisory or prescriptive query, the agent checks `12-risks-contradictions/00_index.md` for relevant `risk_tags`. If a contradiction exists, the agent discloses it and qualifies the recommendation — it does not suppress or work around it.[cite:23]

```
IF query is descriptive       → contradiction check: optional
IF query is advisory          → contradiction check: required
IF query is prescriptive      → contradiction check: mandatory
IF query is donor-facing      → contradiction check: mandatory + disclose if found
```

Relevant `risk_tags` include: `targeting`, `tenure`, `municipal_authority`, `informal_settlements`, `cash_assistance`, `relocation`, `WASH`, `DRR`, `protection`.

### 4. Fallback Ladder

The agent follows this ladder in strict order — no skipping.[cite:23]

```
1. Read relevant 00_index.md
2. Read the most likely file named in the index
3. Check neighboring zone index
4. Search metadata/tags across indexes only
5. Abstain or request clarification
6. [Only with explicit human permission] Broader source search
```

For high-risk outputs, the fallback is **abstain or escalate** — never broad-search. Broad-searching the whole library breaks the architecture's core discipline: agents answer from canonical knowledge, not raw accumulation.

### 5. Index Auto-Maintenance Rule

After every ingest or content update, the agent updates the relevant `00_index.md` automatically. Index entries are generated from file frontmatter. Humans lint-check indexes periodically; they do not write them manually.[cite:28]

Every compliant index entry answers six questions:
1. What is this file?
2. When should an agent read it?
3. When should an agent *not* read it?
4. What source or framework does it depend on?
5. What risks or contradictions are linked to it?
6. What outputs use it?

### 6. Standard Agent Workflows

The agent contract defines five named, callable workflows:

| Workflow | Trigger | Output |
|---|---|---|
| `INGEST` | New source added to `raw/` | Compiled wiki entry, updated `00_index.md`, backlinks added |
| `QUERY` | Human or agent question | Answer with contradiction checks and fallback ladder applied |
| `LINT` | Scheduled or on-demand | `lint-report-YYYY-MM-DD.md` filed to `outputs/internal/` |
| `PROMOTE` | Pattern reaches promotion threshold | Drafted concept/framework/tool update with evidence block |
| `OUTPUT` | Request for external artifact | Drafted output with full provenance block |

---

## Content Lifecycle & States

Every file carries a `status` field. Transitions are governed and logged.

```
draft → under_review → approved → active → superseded → archived
```

### Source Metadata (`01-sources/`)

```yaml
status: active | superseded | archived | under_review
review_cycle: quarterly | annual | event_triggered
last_reviewed: YYYY-MM-DD
next_review: YYYY-MM-DD
supersedes:
superseded_by:
foundational: true | false
```

The 2007–2026 date range is not a problem if each source is clearly marked as `foundational`, `still_valid`, `partially_superseded`, or `historical`. Age alone does not determine relevance.

---

## Schema Change Control

Every change to `schema/` follows this mandatory sequence:[cite:23]

```
1. Change proposed (any role) + rationale documented
2. Impact assessed via lint check against existing files
3. Sample migration tested on 3–5 representative files
4. Library Steward approves
5. Technical Maintainer applies change
6. All affected 00_index.md files updated by LLM agent
7. Lint rules updated
8. Change logged in schema/changelog.md
   [date | author | change description | files affected | migration applied]
```

**No agent silently rewrites schema rules. Ever.**

---

## Field Evidence Promotion Path

The highest-risk pathway in the architecture. Field findings **never feed directly** into `02-concepts/`, `03-frameworks/`, or `04-tools/`. They enter a gated review queue.[cite:24]

```
Field Instrument Finding
        ↓
LLM logs as Finding Note in 11-patterns/
[evidence_status: raw_finding]
        ↓
Evidence Reviewer validates source, context, method, protection risks
[evidence_status: reviewed_finding]
        ↓
Pattern candidate — repeated across ≥2 contexts or critically validated
[pattern_status: candidate]
        ↓
Domain Steward reviews + contradiction check against 12-risks-contradictions/
[pattern_status: under_review]
        ↓
Concept / Framework / Tool update drafted by LLM agent
        ↓
Library Steward approves
        ↓
Knowledge Layer updated + all affected 00_index.md files refreshed
[pattern_status: promoted]
```

### Evidence Eligibility Criteria (all must be met)

- Source is known and context is described
- Method is documented
- Finding is not a one-off anecdote
- Protection/do-no-harm risks checked
- Contradictory evidence considered
- Applicability limits stated
- Human Evidence Reviewer has approved

### Evidence Frontmatter

```yaml
evidence_status: raw_finding | reviewed_finding | candidate_pattern | validated_pattern | promoted
confidence: low | medium | high
reviewed_by:
review_date:
applicability:
limits:
protection_check: passed | flagged | pending
```

---

## Pattern Governance (`11-patterns/`)

Without discipline, `11-patterns/` becomes a graveyard of interesting observations. Every pattern requires the following frontmatter:[cite:23]

```yaml
pattern_status: candidate | under_review | validated | promoted | rejected | archived
promotion_target: concept | framework | tool | risk_register | none
evidence_count:
contexts_observed: []
review_by:
review_date:
contradictions_checked: true | false
applicability:
```

Promotion requires: observation in ≥2 contexts (or strong validation in one critical context), contradiction check passed, applicability boundaries defined, existing concepts/frameworks checked for duplication, and Domain Steward approval.[cite:24]

---

## Linting: Proactive LLM Health Checks

Linting is **not a static audit** — it is a regular LLM-run diagnostic that produces a `lint-report-YYYY-MM-DD.md` filed into `outputs/internal/` and fed back into the wiki as an internal output. This converts the contradiction register from a static log into a **living diagnostic layer**.[cite:32]

### Lint Checks Include

- Files missing required frontmatter fields (status, review date, tags, source links)
- `00_index.md` entries that are stale, vague, or missing
- Patterns in `candidate` status older than 90 days with no review activity
- Outputs past their `valid_until` date with no supersession record
- Concepts or frameworks referenced in outputs but not linked in indexes
- Contradictions discovered during query activity not yet logged in `12-risks-contradictions/`
- New article candidates based on emerging gaps or cross-document connections
- Schema drift (naming inconsistencies, non-standard tags, duplicate concepts)

### Lint Failure Levels

| Level | Condition | Action |
|---|---|---|
| **Critical** | Unlogged schema change; agent navigation broken | Block publication; escalate to Steward immediately |
| **High** | Missing frontmatter on active files; stale outputs in circulation | Flag in lint report; 7-day resolution target |
| **Medium** | Patterns past review date; vague index entries | Flag in lint report; quarterly resolution |
| **Low** | New article candidates; connection suggestions | Log for Governance Council review |

---

## Output Provenance Standard

### Two Output Classes

**External outputs** — toolkits, decision memos, donor proposals, slide decks, training materials that leave the vault:

```yaml
output_id:
title:
output_type: decision_memo | toolkit | proposal_section | slide_deck | training_material
created_date:
created_by:
drafted_by: [LLM agent]
source_files_used: []
concepts_used: []
frameworks_used: []
tools_used: []
risk_checks_used: []
contradictions_checked: true | false
library_version:
schema_version:
review_status: draft | reviewed | approved | superseded
valid_until:
superseded_by:
```

**Internal outputs** — Q&A responses, analyses, explorations that file back into the wiki:[cite:32]

```yaml
output_id:
query:
response_date:
confidence: low | medium | high
source_files_used: []
contradictions_checked: true | false
filed_to: [target folder — e.g. 11-patterns/, 09-monitoring-learning/]
```

Internal outputs use a **lightweight filing path** — no full provenance block required — because their purpose is to compound the library's knowledge, not to produce certified artifacts. Every query should make the library smarter.

### Reverse Dependency Tracking

Every framework carries a `used_by_outputs: []` field. When a framework is updated, the Technical Maintainer identifies all affected outputs via this field and flags them for review. This prevents stale artifacts from circulating undetected.[cite:23]

---

## Review Cadence

| Frequency | Activities |
|---|---|
| **After every ingest** | LLM updates relevant `00_index.md`; adds backlinks; checks contradiction relevance |
| **Weekly** | Agent Maintainer reviews lint queue; clears critical and high flags |
| **Quarterly** | Governance Council: reviews `01-sources/` for new authoritative docs; clears stale guidance flags; reviews `11-patterns/` promotion queue; checks output validity dates; reviews lint report |
| **Annually** | Full relevance review of all primary sources; revalidate major concepts, frameworks, tools; Steward reviews `AGENTS.md` for behavioral drift; full schema review |
| **Event-triggered** | New donor guidance; new cluster/agency standard; major emergency evaluation; contradiction discovered during use; repeated field finding challenging existing framework; new urban/ABA/DRR guidance |

---

## Governance Metrics (Quarterly Dashboard)

| Metric | Target | Alert Threshold |
|---|---|---|
| `00_index.md` coverage (% files with compliant entries) | 100% | < 95% |
| Frontmatter compliance (% active files with all required fields) | 100% | < 98% |
| Stale content (% files past `next_review` date) | 0% | > 5% |
| Pattern queue age (avg days in `candidate` status) | < 90 days | > 180 days |
| External output provenance completeness | 100% | < 100% |
| Contradiction register response time (discovery → logged) | < 7 days | > 14 days |
| Lint report frequency | Weekly | > 14 days between reports |
| Schema changelog entries | All changes logged | Any unlogged change = critical failure |
| Internal outputs filed back into wiki | Tracked | Not tracked = compounding failure |

---

## What v2 Closes

v1 showed **information flow** clearly. v2 adds the missing layers:

| Layer | v1 Status | v2 Status |
|---|---|---|
| Authority flow | Implicit | Explicit — roles, authority levels, change protocols |
| LLM-native authorship | Assumed | Stated as foundational operating principle |
| Agent contract | Fragmented across 3 folders | Consolidated in single `AGENTS.md` |
| Compounding mechanic | Shown in diagram | Governed — internal outputs always file back in |
| Proactive linting | Static contradiction register | LLM-run health checks with failure levels |
| Trigger layer | Absent | Automated lint runs, review date alerts, pattern queue aging |
| Output classes | Single class | External (full provenance) vs. internal (lightweight filing) |

The structure was already strong. v2 makes the **discipline behind the structure** as explicit as the structure itself. Without this layer, the architecture is a well-designed system maintained by hope. With it, it becomes a durable, agent-native knowledge system capable of scaling to 10x content volume without structural failure.[cite:28][cite:24]

---

*Document version: 2.0 | Prepared: May 2026 | Review cycle: Annual or upon major schema change*
