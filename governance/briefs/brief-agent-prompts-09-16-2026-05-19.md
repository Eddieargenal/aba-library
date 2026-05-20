---
type: brief
status: active
created: 2026-05-19
---

# Brief: Agent Prompt Rewrites — Agents 09–16

## Planner Metadata
- Planning tier: 2
- Planner team size: 2 (vault scout + lead synthesizer)
- Date: 2026-05-19
- Recommended execution team size: 4

## Objective

Rewrite 8 agent prompt files (09–16) from task-list stubs to full output contracts at the same quality standard as agent-08. When done, any agent following these prompts can execute its role without ambiguity about inputs, output schema, field rules, gate criteria, or acceptance conditions.

## Deliverables

1. `governance/aba/prompts/agent-09-finding-routing-agent.md`
2. `governance/aba/prompts/agent-10-advisory-orchestrator-agent.md`
3. `governance/aba/prompts/agent-11-section-retrieval-and-evidence-packet-agent.md`
4. `governance/aba/prompts/agent-12-packet-consolidator-and-claim-ledger-agent.md`
5. `governance/aba/prompts/agent-13-claim-ledger-writing-agent.md`
6. `governance/aba/prompts/agent-14-citation-reviewer-agent.md`
7. `governance/aba/prompts/agent-15-risk-reviewer-agent.md`
8. `governance/aba/prompts/agent-16-output-storage-and-promotion-agent.md`

## Context

### Vault root
`/Users/eddieargenal/Documents/obsidian-vault`

### Quality standard reference
`governance/aba/prompts/agent-08-extracted-source-agent.md` — the rewritten agent-08 is the template for what "done" looks like: Role, Inputs contract, Output contract with field-level rules, Gate criteria, Constraints, Acceptance checklist.

### Human review gates
- Gate B: routing/proposal review — triggered by agent-09 before any `create-*` or contradiction write
- Gate C: field-critical advisory review — triggered by agent-15 before final output delivery
- Gate D: field update promotion review — triggered by agent-16 when promotion proposals are written

### Advisory chain sequence (fixed, do not reorder)
```
agent-10 (orchestrate)
  → agent-11 (retrieve, one call per section, parallel)
  → agent-12 (consolidate packets into claim ledger)
  → agent-13 (write draft from claim ledger)
  → agent-14 + agent-15 (citation + risk review, parallel)
  → agent-13 (revise if edits required)
  → agent-16 (store final output)
```

### O- ID format (defined here — not previously defined in vault)
`O-YYYY-MM-DD-{slug}` where slug is a short kebab-case description of the advisory topic.
Example: `O-2026-05-19-area-selection-urban-flooding`
File location: `outputs/field-advice/O-YYYY-MM-DD-{slug}.md`

### Evidence packet ID format
`EP-YYYY-MM-DD-{slug}-{section_id}`
File location: `outputs/evidence-packets/EP-YYYY-MM-DD-{slug}-{section_id}.md`

### Proposed update (PU-) format
`PU-{slug}` — stored under `outputs/proposed-library-updates/PU-{slug}.md`

### Runtime modes and ceilings (from AGENTS.md)
- `full`: max_sections = 6
- `edge_laptop`: max_sections = 3
- `minimal_offline`: max_sections = 1
- `no_llm`: emergency files only (`emergency/` directory)

### index_build_id pinning rule
Agent-10 reads `indexes/current/manifest.json` and locks the `build_id` for the entire advisory run. All downstream agents (11–16) reference this same `index_build_id`. No agent may read from a different build.

---

## Hard Constraints

- `integration_action` enum in agent-09 must exactly match agent-08's 10 values: `create-concept`, `enrich-concept`, `create-framework`, `enrich-framework`, `create-tool`, `enrich-tool`, `create-risk`, `enrich-risk`, `source_only`, `flag-for-review`
- Agent-09 `create-*` actions: produce a full draft using the template in `governance/templates/v26/` that matches the page type; mark `retrieval_status: draft`; do NOT write to canonical wiki folder — write to `outputs/proposed-library-updates/` as a PU- record; Gate B before any `create-*` write
- Agent-09 must update the integration-map table in the extracted source page: status field changes from `pending` to `routed` for each processed finding
- Agent-09 must also update `status: routed` in the corresponding `findings:` frontmatter entry on the extracted source page
- Agent-11 every claim must have at least one `source_id` + `source_pages` reference from `source-evidence-index.jsonl`
- Agent-12 must never silently resolve contradictions — all merges logged in consolidation_audit_log
- Agent-13 must use only approved claims from the claim ledger — no fabrication, no inference from outside the ledger
- Agent-14 and agent-15 run in parallel after agent-13 produces draft; agent-13 revises only if both reviews are complete
- Agent-16 must never overwrite a previously stored output — always assign a new O- ID
- No prompt may reference another prompt file as a dependency

## Soft Constraints

- Keep prompts tight and LLM-actionable — same register as agent-08
- Prefer tables for field-level rules (same pattern as agent-08's Finding Contract table)
- Decision domain classification in agent-10 should map to the 9-stage lifecycle vocabulary rather than introducing new categories

---

## Known Unknowns Resolved

| Question | Finding | Confidence |
|---|---|---|
| What is the exact O- ID format? | Undefined in vault — brief defines it: `O-YYYY-MM-DD-{slug}` | High (absence confirmed by vault scout) |
| Is there a controlled decision domain taxonomy for agent-10? | Not defined — use 9-stage lifecycle vocabulary as classification scheme | High (absence confirmed by vault scout) |
| What are the inter-agent handoff schemas for the advisory chain? | Derived from stub analysis — specified in Work Units below | High |

## Unresolved Questions

None. All planning unknowns resolved.

---

## Inter-Agent Contract Schemas

These schemas are the source of truth for all execution agents. Each prompt must implement them exactly.

### Section Task (agent-10 → agent-11)
```yaml
section_task:
  task_id: ST-NNN
  user_question: "original question text"
  section_focus: "specific aspect this section addresses"
  lifecycle_stage: [controlled vocabulary]
  decision_domain: "lifecycle stage label used as domain"
  index_build_id: "pinned build ID from manifest.json"
  runtime_mode: full | edge_laptop | minimal_offline | no_llm
  priority: 1-N  # ordering across parallel section tasks
```

### Evidence Packet (agent-11 → agent-12)
```yaml
evidence_packet:
  packet_id: EP-NNN
  section_id: ST-NNN
  section_title: "short label"
  index_build_id: "pinned build ID"
  packet_status: complete | partial | insufficient
  pages_read: ["path/to/page.md"]
  claims:
    - claim_id: CL-NNN
      claim: "exact claim text"
      source_id: S-slug
      source_pages: ["p. N"]
      confidence: high | medium | low
      caveat: "qualifying condition if any"
  recommendations:
    - rec_id: REC-NNN
      recommendation: "action text"
      claim_ids: [CL-NNN]
  risks:
    - risk_id: RSK-NNN
      risk: "risk text"
      mitigation: "mitigation text"
      claim_ids: [CL-NNN]
  open_questions:
    - "unanswered question text"
  human_review_flags:
    - flag_id: HRF-NNN
      reason: "why human review is needed"
      claim_id: CL-NNN  # or null if packet-level
```

### Claim Ledger + Writer Context Bundle (agent-12 → agent-13)
```yaml
claim_ledger:
  ledger_id: CL-LEDGER-NNN
  index_build_id: "pinned build ID"
  claims:
    - claim_id: CL-NNN
      claim: "exact claim text"
      sources: [{source_id: S-slug, source_pages: ["p. N"]}]
      confidence: high | medium | low
      caveat: "qualifying condition"
      approved: true | false
      approval_note: "reason if not approved"
      citation_label: "[Author (Year), p. N]"
  recommendations:
    - rec_id: REC-NNN
      recommendation: "action text"
      claim_ids: [CL-NNN]
      approved: true | false
  risks:
    - risk_id: RSK-NNN
      risk: "risk text"
      mitigation: "mitigation text"
      approved: true | false
  human_review_flags: [HRF-NNN list]
  consolidation_audit_log:
    - action: merged | dropped | flagged-contradiction
      claim_ids: [CL-NNN]
      reason: "why"

writer_context_bundle:
  user_question: "original question"
  lifecycle_stage: [controlled vocabulary]
  decision_domain: "lifecycle stage label"
  runtime_mode: full | edge_laptop | minimal_offline | no_llm
  output_template_id: "O- template ID or null"
  index_build_id: "pinned build ID"
```

### Review Reports (agent-14 and agent-15 → agent-13 / agent-10)
```yaml
citation_review_report:
  report_id: CR-NNN
  advisory_draft_id: "draft reference"
  pass_fail: pass | fail
  unsupported_claims: ["claim text or ID"]
  weak_claims: ["claim text or ID — single source or low confidence"]
  citation_laundering_flags: ["claim supported by source that doesn't actually make the claim"]
  required_edits: ["specific edit instruction"]

risk_review_report:
  report_id: RR-NNN
  advisory_draft_id: "draft reference"
  pass_fail: pass | fail
  required_safeguards: ["safeguard text"]
  escalation_triggers: ["trigger condition"]
  gate_c_triggered: true | false
  gate_c_reason: "reason if triggered"
  required_edits: ["specific edit instruction"]
```

---

## Work Units

### WU-1: Agent-09 — Finding Routing Agent
- **Objective**: Full output contract for agent-09; fix integration_action enum; specify create-*/enrich-* rules; integration-map writeback; Gate B criteria
- **Inputs**:
  - Current stub: `governance/aba/prompts/agent-09-finding-routing-agent.md`
  - Quality standard: `governance/aba/prompts/agent-08-extracted-source-agent.md`
  - Template directory: `governance/templates/v26/` (for create-* draft guidance)
  - Schema: `governance/schema/frontmatter-schema.md`
  - Gates: `governance/human-review-gates.md`
- **Output**: Rewritten `governance/aba/prompts/agent-09-finding-routing-agent.md`
- **Dependencies**: None — standalone
- **Complexity tier**: Tier 2
- **Validation method**: Prompt explicitly states all 10 integration_action values; create-* rule produces PU- not direct wiki edit; integration-map writeback rule present; Gate B criteria explicit

**Agent-09 contract specification** (execution agent must implement):

Inputs:
1. Approved extracted source page (after Gate A): `wiki/aba/01-sources/extracted/{source_id}.md`
2. `indexes/current/agent-index.jsonl`
3. `indexes/current/graph-edges.jsonl`
4. `indexes/current/section-index.jsonl`

For each finding in `findings:` where `status: pending`:

1. **Search**: Search agent-index for candidate pages matching `candidate_target_pages` or similar by topic/lifecycle match
2. **Confirm or reassign**: Accept the candidate_target_pages from agent-08 OR reassign if a better match exists in the current index
3. **Execute by action type**:

| Action | What to produce |
|---|---|
| `enrich-concept` / `enrich-framework` / `enrich-tool` / `enrich-risk` | Read the target page section from section-index; add/update content inline; add source to `source_basis:` if not present |
| `create-concept` / `create-framework` / `create-tool` / `create-risk` | Draft full page using matching template from `governance/templates/v26/`; set `retrieval_status: draft`; write to `outputs/proposed-library-updates/PU-{slug}.md`; do NOT write to wiki |
| `source_only` | No target page changes; mark finding as source_only |
| `flag-for-review` | Add to Gate B review packet; no page changes |

4. **Integration-map writeback**: After processing each finding, update the extracted source page:
   - In the `## Integration Map` body table: change `Status` column from `pending` to `routed`
   - In the `findings:` frontmatter list: change `status: pending` to `status: routed`

5. **Gate B packet**: Compile for all `create-*` and `flag-for-review` actions:
   - List of proposed new pages (PU- paths)
   - List of flagged findings with reasons
   - List of any contradictions found with existing content

Gate B trigger: mandatory when any `create-*` finding exists OR any contradiction with existing page content is identified.

Constraints:
- Prefer `enrich-*` over `create-*` — existing pages absorb findings unless no suitable page exists
- Never directly modify a canonical wiki page without reading its current content first
- Never mark a finding `routed` until the target page has been updated or a PU- has been written

Acceptance criteria:
- [ ] All 10 integration_action values in prompt
- [ ] `create-*` rule produces PU- in `outputs/proposed-library-updates/`, not wiki edit
- [ ] Integration-map writeback contract (both body table and frontmatter findings: list)
- [ ] Gate B trigger conditions explicit
- [ ] `enrich-*` preference rule stated

---

### WU-2: Agents 10–11 — Orchestrator + Section Retrieval
- **Objective**: Full output contract for agent-10 (orchestrates advisory run) and agent-11 (produces evidence packets per section)
- **Inputs**:
  - Current stubs: `agent-10-advisory-orchestrator-agent.md`, `agent-11-section-retrieval-and-evidence-packet-agent.md`
  - Quality standard: `agent-08-extracted-source-agent.md`
  - Advisory flow: `AGENTS.md` (runtime modes, advisory flow steps)
  - Inter-agent schemas from this brief
- **Output**: Two rewritten prompt files
- **Dependencies**: None — inter-agent schemas defined in this brief
- **Complexity tier**: Tier 2
- **Validation method**: Agent-10 section_task output matches agent-11 input contract exactly; agent-11 evidence packet output matches claim schema exactly; runtime ceilings enforced; index_build_id pinning rule present in both

**Agent-10 contract specification**:

Inputs:
1. User operational question (inline)
2. Runtime mode (declared by user or default: `full`)
3. `indexes/current/manifest.json` — pin build_id here
4. `indexes/current/agent-index.jsonl`

Steps:
1. Read `manifest.json`, lock `index_build_id` for entire run
2. Classify lifecycle stage (one or more of the 9-stage vocabulary) from question content
3. Use lifecycle stage as decision domain
4. Confirm runtime mode; apply ceiling (full=6, edge_laptop=3, minimal_offline=1, no_llm=emergency)
5. Select output template: search `agent-index.jsonl` for type=output-template matching lifecycle_stage; use first match or null
6. Decompose into section tasks (one per distinct aspect, up to runtime ceiling); assign task_id ST-001, ST-002, etc.
7. Dispatch section tasks to agent-11 (parallel when runtime allows)
8. Receive evidence packets; pass all to agent-12
9. Receive claim ledger + writer context bundle from agent-12; pass to agent-13
10. Receive citation review report from agent-14 and risk review report from agent-15 (parallel)
11. If either report has `pass_fail: fail`: pass required_edits back to agent-13 for revision
12. When both reports pass: pass final draft to agent-16
13. If `gate_c_triggered: true` from agent-15: halt and produce Gate C review packet before agent-16

Output: advisory workflow log (build_id, lifecycle classification, runtime mode, section tasks, status of each stage)

**Agent-11 contract specification**:

Inputs:
1. Section task (ST-NNN schema from this brief)
2. Pinned `index_build_id`
3. `indexes/current/agent-index.jsonl`
4. `indexes/current/section-index.jsonl`
5. `indexes/current/graph-edges.jsonl`
6. `indexes/current/source-evidence-index.jsonl`

Steps:
1. Identify relevant pages for the section_task by matching lifecycle_stage + decision_domain against agent-index
2. Retrieve section line ranges from section-index for identified pages
3. Read only the relevant sections (do not read full pages)
4. Extract claims with source support from source-evidence-index
5. Build evidence packet using schema from this brief (all fields required)
6. Attach human_review_flag for: thin evidence (single source), contradicting claims from different sources, claims with confidence: low, claims requiring field judgment

Evidence quality threshold: every claim must have at least one `source_id` + `source_pages` reference. Claims without source support must go to `open_questions`, not `claims`.

Output: evidence packet (EP-NNN schema from this brief); `packet_status: complete` when all section aspects have ≥1 supported claim; `partial` when some gaps exist; `insufficient` when <2 supported claims found.

---

### WU-3: Agents 12–13 — Consolidator + Writing Agent
- **Objective**: Full output contract for agent-12 (merges packets → claim ledger) and agent-13 (writes draft from ledger)
- **Inputs**:
  - Current stubs: `agent-12-packet-consolidator-and-claim-ledger-agent.md`, `agent-13-claim-ledger-writing-agent.md`
  - Quality standard: `agent-08-extracted-source-agent.md`
  - Inter-agent schemas from this brief
- **Output**: Two rewritten prompt files
- **Dependencies**: None — schemas defined in this brief
- **Complexity tier**: Tier 2
- **Validation method**: Claim ledger schema matches brief exactly; writer context bundle present; merge conflict rule explicit; citation format specified in agent-13; human review flags preserved visibly

**Agent-12 contract specification**:

Inputs:
1. One or more evidence packets (EP-NNN schema)
2. Pinned `index_build_id`

Steps:
1. Validate packet structure: all required fields present; `packet_status` checked
2. Merge overlapping claims:
   - If two claims make the same assertion with different sources: merge into one claim, union the sources list
   - If two claims make the same assertion with different wordings: use more specific wording; log the merge
   - If two claims contradict each other: do NOT merge; flag both in `consolidation_audit_log` as `flagged-contradiction`; mark both `approved: false` until human resolves
3. Assign `approved: true` to claims with ≥1 source support and no unresolved contradiction
4. Assign `approved: false` to: unsupported claims, contradicted claims
5. Generate `citation_label` for each approved claim: `[Last Author (Year), p. N]`
6. Produce writer_context_bundle from section task metadata
7. Output: claim_ledger + writer_context_bundle + consolidation_audit_log (schemas from this brief)

Constraints: Do not create new factual claims. Do not drop caveats. Do not remove human_review_flags. Contradictions must appear in audit log.

**Agent-13 contract specification**:

Inputs:
1. User question (from writer_context_bundle)
2. Claim ledger (approved claims only)
3. Writer context bundle
4. Output template: if `output_template_id` is set, read from `wiki/aba/10-output-templates/`; if null, use fallback structure

Output structure (fallback when no template):
```
## Decision Context
[restate the question and lifecycle stage]

## Key Findings
[approved claims as clear field guidance; citation labels inline]

## Recommended Actions
[approved recommendations with claim support]

## Risks and Safeguards
[approved risks with mitigations]

## Open Questions
[unresolved questions from evidence packets]

## Human Review Requirements
[all human_review_flags as explicit callout blocks — not buried in prose]

## Citations
[full citation list for all cited claims]
```

Rules:
- Every factual statement must map to an approved claim_id from the ledger
- Citation labels must match the ledger exactly (`[Last Author (Year), p. N]` format)
- Human review flags must appear as visible callout blocks (e.g. `> **Human Review Required**: reason`)
- Do not use unapproved claims for any purpose
- Do not overstate confidence beyond what the claim ledger supports
- If fewer than 3 approved claims exist for a section: note the evidence gap explicitly

Output: draft advisory text + list of claim_ids used per section.

---

### WU-4: Agents 14–16 — Citation Review + Risk Review + Storage
- **Objective**: Full output contract for agent-14 (citation audit), agent-15 (risk review + Gate C), agent-16 (storage + promotion proposals)
- **Inputs**:
  - Current stubs: `agent-14-citation-reviewer-agent.md`, `agent-15-risk-reviewer-agent.md`, `agent-16-output-storage-and-promotion-agent.md`
  - Quality standard: `agent-08-extracted-source-agent.md`
  - Gates: `governance/human-review-gates.md`
  - Inter-agent schemas from this brief
- **Output**: Three rewritten prompt files
- **Dependencies**: None — schemas defined in this brief
- **Complexity tier**: Tier 2
- **Validation method**: Agent-14 review report schema matches brief; agent-14 defines unsupported vs weak vs laundering explicitly; agent-15 lists Gate C trigger conditions; agent-15 report schema matches brief; agent-16 uses O- ID format from this brief; agent-16 never overwrites previous outputs

**Agent-14 contract specification**:

Inputs:
1. Draft advisory output (from agent-13)
2. Claim ledger (from agent-12)
3. Source evidence index: `indexes/current/source-evidence-index.jsonl`

Steps:
1. Enumerate every factual statement in the draft
2. For each statement, find the corresponding claim_id in the ledger
3. Verify: the source cited in the ledger actually makes that claim (check source-evidence-index)
4. Classify:
   - **Unsupported**: statement has no matching approved claim_id in ledger
   - **Weak**: statement's claim has only one source OR source confidence is low
   - **Citation laundering**: a source is cited but does not support the claim as stated (source is misrepresented)
5. Produce citation_review_report (schema from this brief)

Constraints: Do not add content. Do not accept "probably supported" — a claim is either traceable to the source text or it is not. Flag all three categories even if minor.

Gate: `pass_fail: pass` only when unsupported_claims and citation_laundering_flags are both empty. Weak claims may pass with a note.

**Agent-15 contract specification**:

Inputs:
1. Draft advisory output (from agent-13)
2. Claim ledger
3. Risk pages from `wiki/aba/06-risks/` (if relevant)
4. Human review flags from claim ledger

Risk categories to check (all required):
1. **Checklist misuse**: draft presents findings as universal requirements applicable without local assessment
2. **False precision**: quantified thresholds or scores stated without sufficient evidence basis
3. **Community homogeneity**: draft assumes uniform community conditions or capacities
4. **Protection-sensitive data**: draft references data collection that could expose vulnerable populations without safeguard guidance
5. **Enabling environment constraints**: draft recommends actions that require institutional capacity or political will without noting those preconditions
6. **Escalation triggers**: any condition in the draft that should trigger escalation to a senior advisor, protection officer, or cluster coordinator

Gate C trigger conditions (any one is sufficient):
- Any finding in the draft has `human_review_required: true` from the claim ledger
- Checklist misuse risk identified with no mitigation in the draft
- False precision risk identified (quantified claim not supported by evidence)
- Protection-sensitive data referenced without explicit safeguard
- Any escalation trigger identified

Output: risk_review_report (schema from this brief). If `gate_c_triggered: true`, include Gate C review packet: list of specific passages requiring human judgment before operational use.

**Agent-16 contract specification**:

Inputs:
1. Final approved advisory output (after both review agents pass or after agent-13 revision)
2. Claim ledger
3. Output template ID used
4. Index build ID
5. Human review flags

Steps:
1. Assign O- ID: `O-YYYY-MM-DD-{slug}` where slug is derived from the user question topic
2. Store advisory at `outputs/field-advice/O-YYYY-MM-DD-{slug}.md` — never overwrite an existing file; if slug collides, append `-2`, `-3`, etc.
3. Store evidence packets at `outputs/evidence-packets/EP-YYYY-MM-DD-{slug}-{section_id}.md`
4. Write frontmatter on the stored advisory:
   ```yaml
   id: O-YYYY-MM-DD-{slug}
   type: output
   index_build_id: {pinned build ID}
   output_template_id: {template used or null}
   source_basis: [list of S- IDs from claim ledger]
   human_review_flags: [list of flag IDs if any]
   created: YYYY-MM-DD
   ```
5. Identify promotion candidates: claims that would add permanent value to the wiki graph — specifically: new risk patterns, new tension patterns, reusable advisory patterns applicable beyond this specific question
6. For each promotion candidate: write PU- record at `outputs/proposed-library-updates/PU-{slug}.md` — stub only; do not modify canonical pages

Constraints: Do not overwrite. Do not promote directly to canonical pages. Do not remove review flags from the stored output.

---

## Risks and Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Agent-09 integration_action enum doesn't match agent-08 | Low — enum locked in constraints | Execution agent must verify against brief before writing |
| Inter-agent schemas in 10–16 are inconsistent across WU-2, 3, 4 | Medium — different execution agents write adjacent prompts | Brief defines all schemas; each execution agent must reference this brief's Contract Schemas section |
| Agent-15 Gate C trigger criteria too vague | Low — 6 conditions explicitly listed | Execution agent for WU-4 must implement all 6 as explicit checklist |
| Agent-16 overwrites previous output | Low — constraint explicit | O- ID includes date + slug; collision rule specified |
| create-* in agent-09 ends up in wiki folder instead of outputs/ | Medium — common mistake | PU- path explicitly specified; constraint explicit |

## Acceptance Criteria

- [ ] Agent-09: all 10 integration_action values listed; create-* → PU- not wiki; integration-map writeback rule present; Gate B criteria explicit
- [ ] Agent-10: index_build_id pinning rule; lifecycle stage as decision domain; runtime ceilings (6/3/1/emergency); section_task output matches schema in this brief
- [ ] Agent-11: evidence packet schema matches this brief; claim quality threshold stated; human_review_flag conditions explicit; packet_status tri-value (complete/partial/insufficient)
- [ ] Agent-12: merge conflict rule explicit; contradiction logging rule; claim approval criteria (approved = supported + no unresolved contradiction); consolidation_audit_log produced
- [ ] Agent-13: approved-claims-only rule; citation format `[Last Author (Year), p. N]`; human review flags as visible callout blocks; fallback output structure present
- [ ] Agent-14: unsupported / weak / citation-laundering defined and distinct; pass_fail criteria explicit
- [ ] Agent-15: all 6 risk categories checked; all 6 Gate C trigger conditions listed; gate_c_triggered field in report
- [ ] Agent-16: O- ID format `O-YYYY-MM-DD-{slug}`; no-overwrite rule; PU- for promotion candidates; source_basis in stored output frontmatter
- [ ] No prompt references another prompt file as a required dependency
- [ ] `python3 scripts/build-index.py` produces 0 critical errors after all edits

## Execution Command

```
/execute-with-agent-team governance/briefs/brief-agent-prompts-09-16-2026-05-19.md 4
```
