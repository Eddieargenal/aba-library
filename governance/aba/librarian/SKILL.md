---
type: skill
title: ABA/DRR Wiki Librarian
skill_id: librarian
version: 2.0.0
status: active
created: 2026-05-11
updated: 2026-05-18
installed_at: ~/.claude/skills/librarian/SKILL.md
invocation: /librarian [operation] [optional-context]
tags: [skill, librarian, wiki, aba, drr, operations]
operations: [open, close, query, ingest, extract, lint, build-index, build-concept, build-framework, build-tool, build-instrument, build-known-tension, build-advisory-playbook, build-slice, crosslink, review-tool, promote]
---

# ABA/DRR Wiki Librarian — Skill (v2.0.0)

Executes any wiki operation against the ABA/DRR Field Knowledge Wiki.
Invoke via `/librarian [operation] [optional-context]` in a Claude Code session.

The canonical skill file lives at `~/.claude/skills/librarian/SKILL.md`.
This vault copy is the authoritative reference for editing and version control.
After editing this file, sync to the installed path.

---

## Operations Reference

| Operation | Argument | What it does |
|---|---|---|
| `open` | — | Load handoff → check lint queue → clear compliance → ready |
| `close` | — | Fill handoff → update changelog → lint → rebuild index → append log |
| `query` | question | JSONL-index-first domain question answering with evidence packets |
| `ingest` | source-path or metadata | Full ingest pipeline: mirror → extract → route findings → index |
| `extract` | pdf-path | Create structured extraction page with v2.6 frontmatter from raw PDF |
| `lint` | — | Run build-index.py; report critical errors and warnings from lint-report.json |
| `build-index` | — | Run `scripts/build-index.py` to compile JSONL indexes to `indexes/current/` |
| `build-concept` | concept name (optional) | Two-phase concept ID + synthesis from extracted sources |
| `build-framework` | lifecycle-stage slug | Build framework with decision logic and failure modes |
| `build-tool` | decision question | Build tool with decision domains, evidence, instruments |
| `build-instrument` | tool id (T- prefix) | Generate field instrument with data quality checks |
| `build-known-tension` | tension description | Build KTN- page documenting conflicting operational principles |
| `build-advisory-playbook` | recurring question type | Build P- page guiding a recurring field advisory pattern |
| `build-slice` | slice scope description | Build SS- slice spec and package `field-repo/` |
| `crosslink` | — | Wire new pages into existing pages' frontmatter relationship arrays |
| `review-tool` | tool id (T- prefix) | Score all 10 criteria per domain; produce audit report |
| `promote` | page id (any prefix) | Check promotion gate eligibility with independence verification |

---

## Vault Root
`/Users/eddieargenal/Documents/obsidian-vault`

## Key File Paths
```
indexes/current/agent-index.jsonl        ← query entry point (one row per page)
indexes/current/graph-edges.jsonl        ← valid relationship graph
indexes/current/section-index.jsonl      ← page section line ranges
indexes/current/source-evidence-index.jsonl ← source → finding → claim map
indexes/current/unresolved-edges.jsonl   ← ghost nodes and broken references
indexes/current/manifest.json            ← active build metadata
indexes/current/lint-report.json         ← build diagnostics

memory/current-handoff.md               ← session continuity
memory/runtime/logs/log.md              ← append-only operation log
governance/aba/CLAUDE.md                ← ABA domain operating rules
governance/schema/frontmatter-schema.md ← canonical schema
governance/schema/lint-rules.md         ← lint policy
governance/aba/prompts/                 ← agent prompt pack (agent-01 through agent-20)

wiki/aba/01-sources/raw/                ← immutable raw PDFs
wiki/aba/01-sources/raw-content/        ← markdown mirrors of raw PDFs
wiki/aba/01-sources/extracted/          ← structured extracted source pages
wiki/aba/02-concepts/                   ← concept pages (C-)
wiki/aba/03-frameworks/                 ← framework pages (F-)
wiki/aba/04-tools/                      ← tool pages (T-)
wiki/aba/05-field-instruments/          ← field instrument pages (I-)
wiki/aba/06-risks/                      ← risk pages (R-)
wiki/aba/07-known-tensions/             ← known tension pages (KTN-)
wiki/aba/08-advisory-playbooks/         ← advisory playbook pages (P-)
wiki/aba/09-decision-protocols/         ← decision protocol pages (D-)
wiki/aba/10-output-templates/           ← output template pages (O-)
wiki/aba/11-slice-specs/                ← slice specification pages (SS-)
wiki/aba/12-synthesis/                  ← synthesis outputs

scripts/build-index.py                  ← JSONL index compiler
```

---

## Read this first — always

Before executing any operation, confirm you have read `AGENTS.md` in the vault root.
It contains the operating model, session protocol, and promotion gates.

---

## OPEN — Session open protocol

**When**: At the start of every session before any other work.

**Steps:**

1. Read `memory/current-handoff.md`. Note:
   - In-progress tasks from the previous session
   - Open contradictions
   - Deferred compliance items
   - Recommended first action

2. Read `indexes/current/manifest.json`. Note `build_status`, `critical_error_count`, `warning_count`.

3. Read `indexes/current/lint-report.json`. Extract all `critical_errors`. Note all `warnings`.

4. Clear compliance queue before new work:
   - Resolve all critical errors now
   - Resolve high warnings unless the user explicitly defers them
   - Do not begin assigned work until the queue is clear

5. Confirm to the user: handoff loaded, lint queue reviewed, compliance items cleared (list what was cleared or deferred). Ready to begin.

---

## CLOSE — Session close protocol

**When**: At the end of every session before exiting.

**Steps:**

1. **Fill handoff.** Write a structured summary to `memory/current-handoff.md`:
   ```
   ## Session: YYYY-MM-DD
   ### Completed
   - [task]: [files changed]
   ### Open contradictions
   - [slug]: [description]
   ### Deferred items
   - [item]: [reason for deferral]
   ### Recommended first action next session
   [specific action]
   ```

2. **Update schema changelog if schema changed.** Append a row to `governance/schema/changelog.md`:
   `| YYYY-MM-DD | agent | description | files affected | migration notes |`

3. **Run lint.** Execute the LINT operation. Note critical error count and warning count.

4. **Rebuild index.** Run: `python3 scripts/build-index.py`

5. **Append to log.** Append to `memory/runtime/logs/log.md`:
   ```
   ## [YYYY-MM-DD] maintenance | Session close
   - [key action 1]
   - files changed: [list]
   ```

---

## QUERY — Answer a domain question

**Context**: question to answer.

**Rule**: Never answer a tool question with only conceptual advice. Always include evidence collection, analysis method, and source citations. All claims must trace to source IDs.

**Steps:**

1. Read `indexes/current/manifest.json` — pin the `build_id` for this query session.
2. Read `indexes/current/agent-index.jsonl` — filter rows by `type`, `lifecycle_stage`, `primary_topics`, and title keywords to identify candidate pages.
3. Follow relationships in `indexes/current/graph-edges.jsonl` from candidate pages.
4. Retrieve section spans for target sections via `indexes/current/section-index.jsonl`.
5. Check `wiki/aba/06-risks/` for applicable risks.
6. Check `wiki/aba/07-known-tensions/` for known tensions relevant to the question.
7. Produce structured answer:
   - Decision question · Evidence required · Field data points · Collection method
   - Relevant field instruments · Analysis method · Decision threshold
   - Source citations (stable IDs from `source_basis:`) · Known tensions
8. If new reusable synthesis emerges: file to `outputs/field-advice/` as type: synthesis.
9. Append to log: `## [YYYY-MM-DD] query | [brief description]`

---

## INGEST — Ingest a new source

**Context**: path to source file or metadata (title, author, year, URL).

**Steps:**
1. Confirm raw PDF is in `wiki/aba/01-sources/raw/`
2. Run EXTRACT — create raw-content mirror and extracted source page with v2.6 frontmatter
3. Identify reusable findings in the extracted source page
4. Run finding routing (see agent-09 prompt: `governance/aba/prompts/agent-09-finding-routing-agent.md`):
   - For each finding: search existing pages first, assign integration action, update existing pages where approved
   - Create proposal stubs (`PU-`) only when no existing page can absorb the finding
   - Flag contradiction-sensitive routing for Gate B human review
5. Set `contradicts:` field on extracted source page — `[]` = checked and clear
6. Run BUILD-INDEX
7. Append to log: `## [YYYY-MM-DD] ingest | [Source title]`

**Output checklist:**
- [ ] Extracted source page exists with `id: S-{slug}`
- [ ] Raw-content mirror exists in `01-sources/raw-content/`
- [ ] `contradicts:` field set (not missing)
- [ ] `cited_sources:` populated (key contributing sources only; `in_wiki` not hand-set)
- [ ] Integration map populated with routing decisions
- [ ] Affected existing pages updated or `PU-` stubs created
- [ ] Index rebuilt, manifest published
- [ ] Log entry appended

---

## EXTRACT — Extract a source page from a raw PDF

**Context**: path to PDF in `wiki/aba/01-sources/raw/`.

**Output**: `wiki/aba/01-sources/extracted/{filename}.md`

**Steps:**
1. Determine canonical filename (match PDF filename, swap `.pdf` → `.md`)
2. Read document: title, author, institution, year, URL, methodology, key findings, lifecycle stages, tools described, contradictions
3. Write extraction page using template at `governance/templates/v26/extracted-source-template.md`
4. Required frontmatter fields: `id: S-{slug}`, `type: source`, `retrieval_status: usable`, `source_id:`, `lifecycle_stage:`, `primary_topics:`, `findings:` (list), `sections:`, `contradicts: []`
5. Required body sections with anchors:
   - `<a id="summary"></a>` before `## Summary`
   - `<a id="findings"></a>` before `## Findings`
   - `<a id="integration-map"></a>` before `## Integration Map`
6. Populate the `findings:` frontmatter list — each finding must have: `finding_id`, `finding`, `finding_type`, `lifecycle_stage`, `source_pages`, `candidate_target_pages`, `integration_action`, `status`, `human_review_required`, `routing_rationale`
7. Populate `cited_sources:` — key contributing sources only (primary frameworks, foundational research, major guidelines the document explicitly builds on or applies). Do not include every footnote. Never set `in_wiki:` — it is auto-computed by `build-index.py`.
8. Populate the Integration Map table in body
9. Run INGEST to wire into wiki

**Confidence:**
- `high` — direct field evidence (evaluation, assessment report)
- `medium` — practitioner judgment, expert synthesis, pilot evidence
- `low` — theoretical/untested (conceptual frameworks, policy guidance)

---

## LINT — Run wiki quality check

**Steps:**
1. Run: `python3 scripts/build-index.py`
2. Read `indexes/current/lint-report.json`
3. Report all `critical_errors` — these must be fixed before new work
4. Report all `warnings` — review and prioritize
5. Note `build_status` from `indexes/current/manifest.json`

**Critical errors that block publish:**
- `missing_id` — page lacks stable `id:` field
- `duplicate_id` — same id used by two pages
- `invalid_yaml_frontmatter` — YAML parse failure
- `missing_type` — page lacks `type:` field
- `missing_retrieval_status` — page lacks `retrieval_status:`
- `missing_lifecycle_stage` — required type lacks lifecycle_stage
- `unresolved_edge:{id}` — relationship points to a missing page
- `section_error:{anchor}` — declared section anchor missing in body

**Warnings (review and address):**
- `missing_sections` — page has no `sections:` declaration
- `orphan_page:{id}` — page has no inbound graph edges
- `derived_source_id:{id}` — source page id was derived from source_id (fix: add explicit `id:`)
- `derived_retrieval_status:{value}` — retrieval_status was derived from status (fix: add explicit `retrieval_status:`)

**Log entry:**
```
## [YYYY-MM-DD] lint | Wiki quality check
- build_status: {status} | critical: N | warnings: N
```

---

## BUILD-INDEX — Compile JSONL indexes

```bash
python3 /Users/eddieargenal/Documents/obsidian-vault/scripts/build-index.py
```

Outputs to `indexes/current/`: `agent-index.jsonl`, `graph-edges.jsonl`, `unresolved-edges.jsonl`, `section-index.jsonl`, `source-evidence-index.jsonl`, `manifest.json`, `lint-report.json`.

Publishes atomically only when `critical_error_count == 0`.

Confirm: `build_status`, `page_count`, `edge_count` from manifest output.
Append to log: `## [YYYY-MM-DD] maintenance | Rebuilt indexes — N pages, N edges`

---

## BUILD-CONCEPT — Build concept pages from extracted sources

**Context**: concept family name (optional — omit for full pass).

**Rule**: Every claim must trace to at least one extracted source via `source_basis:`. Never write from general knowledge.

**Phase 1 — Identify candidates** (skip for single concept rebuild):
1. Read `indexes/current/agent-index.jsonl` — filter `type: source` rows
2. Read relevant extracted source pages — extract findings by concept referent
3. Cluster by shared referent; score by number of independent sources, convergence, operationalizability
4. Prioritize: ≥2 independent sources + ABA/DRR relevance

**Phase 2 — Build page**:
1. Full-file pass across ALL sections of relevant extracted files for the target concept
2. Use template: `governance/templates/v26/concept-template.md`
3. Required frontmatter:
   ```yaml
   id: C-{slug}
   type: concept
   title:
   slug:
   retrieval_status: draft
   lifecycle_stage: []
   primary_topics: []
   related_concepts: []
   related_frameworks: []
   related_tools: []
   related_risks: []
   source_basis: []        # list source_id references with finding_ids
   known_tensions: []
   contradicts: []
   used_by_playbooks: []
   output_templates: []
   sections:
     - id: definition
       anchor: "#definition"
       purpose: Operational definition
     - id: field-use
       anchor: "#field-use"
       purpose: Field application guidance
     - id: risks
       anchor: "#risks"
       purpose: Risks and safeguards
   created:
   updated:
   ```
4. Body sections with anchors: `## Definition` · `## Field Use` · `## Risks`
5. Populate `source_basis:` with at least one independent source
6. Set `retrieval_status: usable` only after human promotion approval
7. Run BUILD-INDEX

---

## BUILD-FRAMEWORK — Build a framework page

**Context**: lifecycle stage slug or decision domain.

**Do NOT create if**: framework already exists, source material not ingested, or logic belongs in a tool page.

**Steps:**
1. Read `indexes/current/agent-index.jsonl` — filter `type: framework`, confirm gap
2. Read relevant extracted sources filtered by `lifecycle_stage`
3. Use template: `governance/templates/v26/framework-template.md`
4. Required frontmatter:
   ```yaml
   id: F-{slug}
   type: framework
   title:
   slug:
   retrieval_status: draft
   lifecycle_stage: []
   primary_topics: []
   related_concepts: []
   related_frameworks: []
   related_tools: []
   related_risks: []
   source_basis: []        # minimum 2 independent sources for usable status
   known_tensions: []
   contradicts: []
   used_by_playbooks: []
   output_templates: []
   sections:
     - id: decision-scope
       anchor: "#decision-scope"
       purpose: Decision domain and scope
     - id: application-logic
       anchor: "#application-logic"
       purpose: Core framework logic
     - id: limitations
       anchor: "#limitations"
       purpose: Limitations and caveats
   created:
   updated:
   ```
5. Body sections with anchors: `## Decision Scope` · `## Application Logic` · `## Limitations`
6. Include: decision question, use conditions, decision logic, evidence requirements, known failure modes, known tensions
7. `source_basis` < 2 independent sources → keep `retrieval_status: draft`
8. Run BUILD-INDEX

---

## BUILD-TOOL — Build a tool page

**Context**: decision question.

**Quality standard**: Tool FAILS if it only lists questions without defining evidence collection.

**Steps:**
1. Confirm a framework covers this decision domain — if not, run BUILD-FRAMEWORK first
2. Read `indexes/current/agent-index.jsonl` + relevant framework and concept pages
3. Use template: `governance/templates/v26/tool-template.md`
4. Required frontmatter:
   ```yaml
   id: T-{slug}
   type: tool
   title:
   slug:
   retrieval_status: draft
   lifecycle_stage: []
   primary_topics: []
   related_concepts: []
   related_frameworks: []
   related_tools: []
   related_risks: []
   source_basis: []
   known_tensions: []
   contradicts: []
   used_by_playbooks: []
   output_templates: []
   requires_concepts: []
   parent_frameworks: []
   required_inputs: []
   compatible_instruments: []   # I- prefixed ids
   mitigated_by: []
   sections:
     - id: purpose
       anchor: "#purpose"
       purpose: Tool purpose
     - id: decision-questions
       anchor: "#decision-questions"
       purpose: Questions the tool answers
     - id: method
       anchor: "#method"
       purpose: Data and analysis method
     - id: risks
       anchor: "#risks"
       purpose: Risks and safeguards
   created:
   updated:
   ```
5. Body sections with anchors: `## Purpose` · `## Decision Questions` · `## Method` · `## Risks`
6. For each decision domain define: evidence required · field data points · collection method · respondent/source · compatible instrument · analysis method · scoring rule · data quality checks · risks/safeguards · source IDs
7. Run BUILD-INSTRUMENT for any domain without a linked instrument
8. Set `retrieval_status: usable` only after all instruments linked and human approves
9. Run BUILD-INDEX

---

## BUILD-INSTRUMENT — Generate a field instrument

**Context**: tool id (T- prefix).

**Steps:**
1. Read parent tool page — identify domains needing instruments
2. For each domain: choose format (survey, checklist, FGD guide, observation log, etc.), design questions with enumerator guidance, define skip patterns and cross-checks
3. Required frontmatter:
   ```yaml
   id: I-{slug}
   type: field-instrument
   title:
   slug:
   retrieval_status: draft
   lifecycle_stage: []
   primary_topics: []
   related_concepts: []
   related_frameworks: []
   related_tools: []
   related_risks: []
   source_basis: []
   known_tensions: []
   contradicts: []
   used_by_playbooks: []
   output_templates: []
   instrument_format:       # survey | checklist | fgd-guide | interview-guide | observation-log
   parent_tools: []         # T- ids of tools this instrument supports
   data_quality_checks: false
   respondent_type: []
   sections:
     - id: purpose
       anchor: "#purpose"
       purpose: Instrument purpose
     - id: instructions
       anchor: "#instructions"
       purpose: Enumerator instructions
     - id: questions
       anchor: "#questions"
       purpose: Question fields
     - id: data-quality-checks
       anchor: "#data-quality-checks"
       purpose: Data quality verification steps
     - id: ethical-safeguards
       anchor: "#ethical-safeguards"
       purpose: Protection and consent requirements
   created:
   updated:
   ```
4. Body sections with anchors: `## Purpose` · `## Instructions` · `## Questions / Fields` · `## Data Quality Checks` · `## Analysis Use` · `## Ethical Safeguards`
5. Add `I-{slug}` to parent tool's `compatible_instruments:` list
6. Set `data_quality_checks: true` only when `## Data Quality Checks` section is fully defined
7. Run BUILD-INDEX

---

## BUILD-KNOWN-TENSION — Document a known operational tension

**Context**: description of the tension (two conflicting operational principles or evidence bases).

**Steps:**
1. Confirm this tension is not already documented — check `indexes/current/agent-index.jsonl` filtering `type: known-tension`
2. Required frontmatter:
   ```yaml
   id: KTN-{slug}
   type: known-tension
   title:
   slug:
   retrieval_status: draft
   lifecycle_stage: []
   primary_topics: []
   related_concepts: []
   related_frameworks: []
   related_tools: []
   related_risks: []
   source_basis: []
   known_tensions: []
   contradicts: []
   used_by_playbooks: []
   output_templates: []
   tension_between: []     # list of ids (C-, F-, T-, R-) in tension
   tension_type:           # evidence-conflict | design-tradeoff | resource-constraint | context-dependent
   resolution_status:      # unresolved | partially-resolved | context-dependent
   sections:
     - id: tension-description
       anchor: "#tension-description"
       purpose: What the tension is and why it arises
     - id: evidence-basis
       anchor: "#evidence-basis"
       purpose: Source evidence on each side
     - id: field-guidance
       anchor: "#field-guidance"
       purpose: How practitioners should navigate this tension
   created:
   updated:
   ```
3. Write page in `wiki/aba/07-known-tensions/`; use `governance/templates/v26/known-tension-template.md` if available
4. Run CROSSLINK — add `known_tensions: [KTN-{slug}]` to all pages involved in the tension
5. Run BUILD-INDEX

---

## BUILD-ADVISORY-PLAYBOOK — Document a recurring advisory pattern

**Context**: recurring field question type.

**Steps:**
1. Confirm this playbook does not already exist — check `indexes/current/agent-index.jsonl` filtering `type: advisory-playbook`
2. Required frontmatter:
   ```yaml
   id: P-{slug}
   type: advisory-playbook
   title:
   slug:
   retrieval_status: draft
   lifecycle_stage: []
   primary_topics: []
   related_concepts: []
   related_frameworks: []
   related_tools: []
   related_risks: []
   source_basis: []
   known_tensions: []
   contradicts: []
   used_by_playbooks: []
   output_templates: []
   decision_domain:        # e.g. area-selection | drr-framework-adaptation | community-assessment
   lifecycle_stages: []
   entry_conditions: []    # when to use this playbook
   exit_conditions: []     # when the advisory is complete
   sections:
     - id: decision-context
       anchor: "#decision-context"
       purpose: What decision this playbook supports
     - id: retrieval-focus
       anchor: "#retrieval-focus"
       purpose: Which page types and topics to retrieve
     - id: advisory-logic
       anchor: "#advisory-logic"
       purpose: How to structure the advisory output
     - id: output-format
       anchor: "#output-format"
       purpose: Required output structure
   created:
   updated:
   ```
3. Write page in `wiki/aba/08-advisory-playbooks/`; use `governance/templates/v26/advisory-playbook-template.md` if available
4. Run CROSSLINK — add `used_by_playbooks: [P-{slug}]` to all concept/tool/framework pages the playbook depends on
5. Run BUILD-INDEX

---

## BUILD-SLICE — Package a field deployment slice

**Context**: slice scope (decision domains, lifecycle stages, hazards).

**Steps:**
1. Define slice scope: decision_domains, lifecycle_stages, hazards
2. Create slice spec page in `wiki/aba/11-slice-specs/`:
   ```yaml
   id: SS-{slug}
   type: slice-spec
   title:
   slug:
   retrieval_status: draft
   lifecycle_stage: []
   primary_topics: []
   related_concepts: []
   related_frameworks: []
   related_tools: []
   related_risks: []
   source_basis: []
   known_tensions: []
   contradicts: []
   used_by_playbooks: []
   output_templates: []
   slice_id: {slug}
   decision_domains: []
   hazards: []
   expected_runtime_mode: edge_laptop   # full | edge_laptop | minimal_offline | no_llm
   raw_sources_included: false
   sections:
     - id: scope
       anchor: "#scope"
       purpose: Slice coverage and constraints
     - id: included-pages
       anchor: "#included-pages"
       purpose: List of pages included in this slice
     - id: known-limitations
       anchor: "#known-limitations"
       purpose: What is missing from this slice
   created:
   updated:
   ```
3. Follow `playbooks/build-slice.md` to identify and package relevant pages
4. Update `field-repo/slice-manifest.json` with coverage metadata
5. Package slice into `field-repo/`
6. Run BUILD-INDEX

---

## CROSSLINK — Update relationship arrays

**Steps:**
1. For each new page: identify which existing pages should reference it by stable ID
   - concept → add to `related_concepts:` on frameworks, tools, risks
   - framework → add to `related_frameworks:` on concepts, tools
   - tool → add to `related_tools:` on concepts, frameworks
   - instrument → add to `compatible_instruments:` on parent tools
   - risk → add to `related_risks:` on concepts, frameworks, tools
   - known tension → add to `known_tensions:` on involved pages
   - playbook → add to `used_by_playbooks:` on concept/tool pages it uses
2. All relationships must use stable IDs (C-, F-, T-, I-, R-, KTN-, P- prefixes), not file paths
3. Inline `[[wikilinks]]` in body text are optional for human readability but not the graph source of truth
4. Run BUILD-INDEX
5. Check `indexes/current/unresolved-edges.jsonl` — if new edges appear there, the target page is missing; resolve before promoting
6. Append to log: `## [YYYY-MM-DD] maintenance | Updated cross-links`

---

## REVIEW-TOOL — Audit a tool page

**Context**: tool id (T- prefix) or filename.

**10-criterion scoring per domain:**
1. Evidence required · 2. Field data points · 3. Collection method · 4. Respondent/source
5. Compatible instrument (linked I- id) · 6. Analysis method · 7. Scoring rule · 8. Data quality checks
9. Risks and safeguards · 10. Source foundation (`source_basis:` populated)

**Steps:**
1. Read tool page
2. Score all 10 criteria per decision domain (✓ pass / ✗ fail / — missing)
3. Check frontmatter: `compatible_instruments:` non-empty, `source_basis:` populated, `contradicts:` set
4. Write findings to `outputs/field-advice/tool-review-{id}-YYYY-MM-DD.md`
5. Add `TODO[agent]: [description]` for each failed criterion

---

## PROMOTE — Check promotion eligibility

**Context**: page id (any prefix).

**Gates:**
| From | To | Requirement | Who approves |
|---|---|---|---|
| Extracted finding | Concept draft | ≥1 extracted source with `source_basis:` | LLM proposes, human approves |
| `retrieval_status: draft` | `retrieval_status: usable` | `source_basis:` populated, sections complete, no critical lint errors | Human approves |
| `retrieval_status: limited` | `retrieval_status: usable` | Known gaps remediated, `source_basis:` updated | Human approves |
| Tool `draft` → `usable` | All `compatible_instruments:` linked + Gate C advisory review passed | Human approves |

**Independence rule**: Two documents citing the same underlying evaluation are NOT independent sources.

**Steps:**
1. Read the page — note `id`, `type`, `retrieval_status`, `source_basis:`
2. Verify gate criteria; verify source independence (distinct evidence bases)
3. Check `indexes/current/lint-report.json` for any critical errors on this page
4. Check `indexes/current/unresolved-edges.jsonl` for any broken relationships from this page
5. Output: current status · criteria met/not met · recommendation
6. If eligible: propose `retrieval_status` change and add `## Promotion Status` section for human review
7. Append to log: `## [YYYY-MM-DD] maintenance | Promotion check: {id}`
