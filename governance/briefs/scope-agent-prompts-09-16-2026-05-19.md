---
type: scope
status: pending-approval
created: 2026-05-19
---

# Scope: Agent Prompt Rewrites — Agents 09–16

## Objective

Rewrite 8 agent prompt files from task-list stubs to full, executable output contracts — the same standard as the recently rewritten agent-08. When done, any agent following these prompts can execute its role without ambiguity about inputs, output schema, field rules, gate criteria, or acceptance conditions.

## Deliverables

1. `governance/aba/prompts/agent-09-finding-routing-agent.md` — full output contract
2. `governance/aba/prompts/agent-10-advisory-orchestrator-agent.md` — full output contract
3. `governance/aba/prompts/agent-11-section-retrieval-and-evidence-packet-agent.md` — full output contract
4. `governance/aba/prompts/agent-12-packet-consolidator-and-claim-ledger-agent.md` — full output contract
5. `governance/aba/prompts/agent-13-claim-ledger-writing-agent.md` — full output contract
6. `governance/aba/prompts/agent-14-citation-reviewer-agent.md` — full output contract
7. `governance/aba/prompts/agent-15-risk-reviewer-agent.md` — full output contract
8. `governance/aba/prompts/agent-16-output-storage-and-promotion-agent.md` — full output contract

## In Scope

- Full rewrite of all 8 prompt files to the agent-08 quality standard
- Agent-09: fix integration_action enum to match agent-08 (10-value enum); add create-* full draft rule; add integration-map writeback contract
- Agents 10–16: add field-level rules for every output field; explicit gate trigger criteria; acceptance checklists
- Preserving and clarifying the existing gate structure (Gate B → agent-09, Gate C → agent-15)

## Out of Scope

- Agents 01–08 (01–07 infra/setup; 08 already done)
- Agents 17–20 (field operations — separate session)
- Changes to the index builder, schema files, or templates
- Content migration or synthesis page creation
- Redesigning the advisory workflow — only documenting what the current architecture requires

## Constraints

- `integration_action` enum in agent-09 must exactly match agent-08:
  `create-concept`, `enrich-concept`, `create-framework`, `enrich-framework`, `create-tool`, `enrich-tool`, `create-risk`, `enrich-risk`, `source_only`, `flag-for-review`
- `create-*` actions in agent-09: agent must draft a full page using the relevant template in `governance/templates/v26/`; new pages are staged as proposed (not promoted); Gate B triggers before any synthesis page is written
- Agent-09 must update the integration-map table in the extracted source page (status: `pending` → `routed`) after completing each finding
- Agent-11 output packet schema: fields defined in current stub (`packet_id`, `section_id`, `section_title`, `index_build_id`, `pages_read`, `claims`, `recommendations`, `risks`, `open_questions`, `human_review_flags`, `packet_status`) — add field-level rules, not new fields
- Agent-16 output storage: must use `O-` stable ID prefix; store under `outputs/field-advice/`; promotion proposals use `PU-` prefix under `outputs/proposed-library-updates/`
- All prompts must be standalone — no cross-references to other prompt files as required reading
- Vault root: `/Users/eddieargenal/Documents/obsidian-vault`

## Dependencies and Access

- `governance/aba/prompts/agent-08-extracted-source-agent.md` — quality standard reference
- `governance/schema/frontmatter-schema.md` — field schemas and controlled vocabularies
- `governance/human-review-gates.md` — gate definitions (A/B/C/D)
- `AGENTS.md` — advisory flow, runtime modes, runtime ceilings
- `governance/templates/v26/` — templates for `create-*` page drafts (agent-09)
- All 8 current stub files (inputs to rewrite)

## Acceptance Criteria

- [ ] Each prompt has: Role, Inputs contract, Output contract, field-level rules, Gate criteria, Constraints, Acceptance checklist
- [ ] Agent-09 integration_action enum exactly matches agent-08's 10-value enum
- [ ] Agent-09 specifies what to produce for each action type (enrich-* vs create-* vs source_only)
- [ ] Agent-09 specifies integration-map writeback (status field update on extracted source page)
- [ ] Agent-10 specifies explicit lifecycle classification vocabulary and decision domain taxonomy
- [ ] Agent-11 output packet has field-level rules for every field in the schema
- [ ] Agent-12 specifies merge conflict resolution rules and claim approval criteria
- [ ] Agent-13 specifies fallback output structure and citation format
- [ ] Agent-14 specifies what constitutes unsupported vs weak claim, and exact review report schema
- [ ] Agent-15 specifies Gate C trigger conditions explicitly
- [ ] Agent-16 specifies O- ID format, file naming convention, and PU- promotion criteria
- [ ] No prompt references another prompt file as a dependency
- [ ] `python3 scripts/build-index.py` still produces 0 critical errors after edits (prompts are not indexed but confirm no side effects)

## Risks and Rollback

| Risk | Mitigation |
|---|---|
| Agent-09 integration_action mismatch with agent-08 | Enum is locked in scope; any deviation is a defect |
| Advisory chain (10–16) has inter-agent contracts — wrong output schema in one breaks downstream | Review each agent's output against the next agent's input contract before finalizing |
| create-* rule in agent-09 implies agent must know template paths — if template doesn't exist, agent is blocked | Templates for all page types exist in `governance/templates/v26/`; agent-09 should cite the directory, not individual files |
| Gate C trigger criteria are vague in current stub | Agent-15 must explicitly state: checklist misuse, false precision, protection-sensitive data, escalation triggers — all named in current stub; add thresholds |

## Assumptions

- The advisory workflow sequence is fixed: agent-10 orchestrates → agent-11 retrieves → agent-12 consolidates → agent-13 writes → agent-14 citation review → agent-15 risk review → agent-16 stores. No reordering in scope.
- `index_build_id` pinning rule (all agents in one advisory run use the same build ID) applies to agents 10–14 and is documented in agent-10; agents 11–14 reference it but do not re-explain it.
- Gate B is agent-09's gate; Gate C is agent-15's gate. Agent-10 orchestrates Gate C trigger via agent-15 but does not itself trigger it.
- Promotion proposals (PU-) from agent-16 are out of scope for this rewrite — agent-16 identifies candidates and writes stubs, not full proposals.

## Open Questions

- What is the exact O- ID format for advisory outputs? (e.g. `O-YYYY-MM-DD-slug` or sequential `O-NNN`) — to be resolved during planning by reading existing outputs/ directory

## User Approval

Status: pending
