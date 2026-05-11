# Brief: Governance Consolidation

## Planner Metadata
- Planning tier: 2
- Planner team size: 2 scouts + lead synthesizer
- Date: 2026-05-11
- Recommended execution team size: 4

---

## Objective

Centralize all 38 operational/governance documents into `governance/`. Eliminate 4 duplicate copies of the 10 compliance rules. Split `library-governance_guide.md` (353 lines) into 5 single-topic sub-documents. Add `00_index.md` to each governance section. Replace 5 root nav files with a single root `AGENTS.md`. Leave no broken links. Delete no file until its links are updated and its content is confirmed absorbed.

Done = one authoritative governance directory, zero duplicate rules, every section discoverable via its own index, root entry point that routes agents into section indexes.

---

## Deliverables

1. Root `AGENTS.md` — single vault entry point
2. `governance/00_index.md` — governance section index
3. `governance/compliance-rules.md` — 10 rules, single authoritative copy
4. `governance/governance-model.md` — split from `library-governance_guide.md` (+ Mermaid diagrams from `architecture.md`)
5. `governance/content-lifecycle.md` — split from `library-governance_guide.md`
6. `governance/evidence-promotion.md` — split from `library-governance_guide.md`
7. `governance/output-provenance.md` — split from `library-governance_guide.md`
8. `governance/review-cadence.md` — split from `library-governance_guide.md`
9. `governance/memory-rules.md` — moved from `memory/memory-rules.md`
10. `governance/schema/` — 8 schema docs moved + `00_index.md` + `changelog.md` (new)
11. `governance/workflows/` — 10 workflow docs moved + `lint-plan.md` + `00_index.md`
12. `governance/aba/` — ABA ops docs moved + `00_index.md`
13. `governance/aba/prompts/` — 13 agent prompts moved + `00_index.md`
14. `wiki/aba/AGENTS.md` stub — pointer to `governance/aba/AGENTS.md`
15. `wiki/aba/CLAUDE.md` stub — pointer to `governance/aba/CLAUDE.md`
16. 30 files with updated internal links (~75 changes)
17. 9 files deleted (confirmed duplicates/empty/absorbed)
18. `governance/vault-quality-remediation/SKILL.md` and `RUNBOOK.md` marked `status: superseded`

---

## Context

**Vault root:** `/Users/eddieargenal/Documents/obsidian-vault/`
**Git repo:** yes — commit snapshot before any changes
**Total vault files:** 318 markdown files
**Operational docs inventory:** 38 files already mapped (see scope doc)

**Scout 1 findings (content):**
- `library-governance_guide.md` is 353 lines; all lines map cleanly to 5 split files — no orphaned content
- One substantive error in `memory/governance.md` Rule 4: path `memory/categories/unresolved/contradictions/` is wrong (subdirectory doesn't exist); correct path is `memory/categories/unresolved.md`
- `wiki/vault-compliance-rules.md` has one unique additive section ("Optional governance signals") not in authoritative source — must carry forward to `governance/compliance-rules.md`
- `architecture.md` contains 6 Mermaid diagrams unique in the vault — must fold into `governance/governance-model.md`
- `SCHEMA.md` contains Log Format and Link Audit bash commands not present elsewhere — must move to `governance/workflows/`
- Root nav unique content to preserve in root `AGENTS.md`: routing table, ABA section index, folder ASCII tree, Memory Truth States table, Design Philosophy, "What Is Not Here", Key Rules guardrails, agent nav flow, Special Files table

**Scout 2 findings (links):**
- 32 files contain references needing update (~75 individual changes)
- 2 high-complexity files (SKILL.md, RUNBOOK.md): 15+ embedded bash-path references each — recommend marking superseded rather than updating
- 7 files safe to delete with no nav link cleanup (memory/governance.md, library-architecture.md, wiki/vault-compliance-rules.md, 00_Start_Here.md, QUICK.md, SCHEMA.md, architecture.md)
- `governance/aba/prompts/` folder must be created BEFORE any prompt files are moved (5 files reference the new path)
- `indexes/workflows.md` and `wiki/index.md` each need 10+ wikilink updates — best as full table section rewrites

---

## Hard Constraints

- Git snapshot commit MUST happen before any file is moved or deleted
- No file may be deleted until its content is confirmed absorbed into a surviving file AND all links pointing to it are updated
- `governance/library-governance_guide.md` must be fully decomposed — verify all 353 lines are distributed before deleting
- `wiki/aba/CLAUDE.md` and `wiki/aba/AGENTS.md` must remain as stubs after their content moves to `governance/aba/` — do NOT delete them (Claude Code auto-loads from directory)
- The 10 compliance rules must end up in exactly one file: `governance/compliance-rules.md`
- Append-only files (`archive/CHANGELOG.md`, `memory/runtime/logs/log.md`) must NOT be modified — historical path references in these files are acceptable log entries
- All content from root nav files must be accounted for before deletion — content cannot be silently dropped

## Soft Constraints

- Prefer wikilinks (`[[...]]`) over relative markdown paths where the destination is within the vault
- Keep `governance/00_index.md` scannable (table format, one row per section, purpose + when-to-read)
- Root `AGENTS.md` should be under 80 lines — it is a routing file, not a content file
- New `00_index.md` files should follow the same format as existing ones in `wiki/aba/`

---

## Known Unknowns Resolved

| Question | Finding | Confidence |
|---|---|---|
| What are the section boundaries in library-governance_guide.md for 5 split files? | All 353 lines mapped: governance-model (L1-117 + L334-352), content-lifecycle (L120-160 + L215-257), evidence-promotion (L164-211), output-provenance (L260-302), review-cadence (L306-330) | High |
| Are there content differences across 4 copies of the 10 rules? | One substantive error (Rule 4 wrong path in memory/governance.md); one additive section in wiki/vault-compliance-rules.md to carry forward; all other differences are wording compressions | High |
| Which files contain references to paths being moved/deleted? | 32 files, ~75 link changes; complete map in Scout 2 findings | High |
| Are any deletions unsafe (unique content, surviving links)? | 7 files confirmed safe; SKILL.md/RUNBOOK.md should be superseded not updated | High |
| Does architecture.md have unique content? | Yes — 6 Mermaid diagrams unique in vault; must fold into governance/governance-model.md | High |

## Unresolved Questions

- `governance/aba/CLAUDE.md` and `governance/aba/AGENTS.md` will be the full content files, but stubs remain in `wiki/aba/`. Stub format not specified — use "See `governance/aba/[CLAUDE|AGENTS].md`" redirect pattern. Execution agents should use a thin redirect stub (~5 lines) so Claude Code auto-load still works.
- `odoo-accounting.md` and `coding-tasks.md` are domain workflows moved to `governance/workflows/` per user direction — flag them in `governance/workflows/00_index.md` as candidates for future domain-specific relocation.

---

## Work Units

### WU-1: Git Snapshot
- Objective: Commit current vault state as rollback point
- Inputs: Current vault state
- Output: Git commit with message "chore: pre-consolidation snapshot"
- Dependencies: None — must run first
- Complexity: Tier 1
- Validation: `git log --oneline -1` confirms commit exists

### WU-2: Create Folder Structure
- Objective: Create all new subdirectories before any files move
- Inputs: None
- Output: `governance/schema/`, `governance/workflows/`, `governance/aba/`, `governance/aba/prompts/` directories exist
- Dependencies: WU-1
- Complexity: Tier 1
- Validation: `ls governance/` shows all 4 subdirs

### WU-3: Split library-governance_guide.md → 5 Sub-Documents
- Objective: Write 5 new governance sub-documents from the source file
- Inputs: `/Users/eddieargenal/Documents/obsidian-vault/governance/library-governance_guide.md` (read in full)
- Output:
  - `governance/governance-model.md` — sections: Foundational Operating Principle (L7-11), Governance Model (L15-24), Roles & Authority Map (L28-40), The Agent Contract: AGENTS.md (L44-117), What v2 Closes (L334-352) PLUS the 6 Mermaid diagrams from `architecture.md` PLUS the Three-Layer Architecture table and Special Files table from `SCHEMA.md`
  - `governance/content-lifecycle.md` — sections: Content Lifecycle & States (L120-140), Schema Change Control (L144-160), Pattern Governance (L215-231), Linting (L234-257)
  - `governance/evidence-promotion.md` — section: Field Evidence Promotion Path (L164-211)
  - `governance/output-provenance.md` — section: Output Provenance Standard (L260-302)
  - `governance/review-cadence.md` — sections: Review Cadence (L306-314), Governance Metrics Dashboard (L318-330)
- Dependencies: WU-2
- Complexity: Tier 2
- Validation: Line count of all 5 output files combined ≥ 353 lines. Each file has YAML frontmatter with `type`, `status`, `created`, `updated`.

### WU-4: Write governance/compliance-rules.md
- Objective: Single authoritative copy of the 10 rules, deconflicted
- Inputs:
  - `/Users/eddieargenal/Documents/obsidian-vault/memory/vault-compliance-rules.md` (authoritative source)
  - Carry forward: "Optional governance signals" section from `wiki/vault-compliance-rules.md`
  - Fix: Rule 4 path — correct path is `memory/categories/unresolved.md` (not `unresolved/contradictions/`)
- Output: `governance/compliance-rules.md` — 10 rules with full examples, stale thresholds table, summary card, enforcement section, + "Optional governance signals" addendum
- Dependencies: WU-2
- Complexity: Tier 1
- Validation: File contains all 10 rules, correct Rule 4 path, Optional governance signals section present

### WU-5: Move schema/ → governance/schema/ + Create Index + Create Changelog
- Objective: Move 8 schema files, create section index, create missing changelog
- Inputs: All files in `/Users/eddieargenal/Documents/obsidian-vault/schema/`
- Output:
  - `governance/schema/frontmatter-schema.md`
  - `governance/schema/lint-rules.md`
  - `governance/schema/ingest-rules.md`
  - `governance/schema/query-rules.md`
  - `governance/schema/citation-rules.md`
  - `governance/schema/naming-conventions.md`
  - `governance/schema/page-types.md`
  - `governance/schema/tool-quality-standard.md`
  - `governance/schema/00_index.md` — table: file | purpose | when to read | when NOT to read
  - `governance/schema/changelog.md` — initial entry: `2026-05-07 | system | Initial schema creation — 8 files: frontmatter-schema, lint-rules, ingest-rules, query-rules, citation-rules, naming-conventions, page-types, tool-quality-standard | all schema files | n/a (initial creation)`
- Dependencies: WU-2
- Complexity: Tier 1
- Validation: `ls governance/schema/` shows 10 files; `schema/` root folder is empty (ready for deletion)

### WU-6: Move workflows/ → governance/workflows/ + lint-plan.md + Create Index
- Objective: Move 10 vault workflow files + lint-plan from wiki/workflows/
- Inputs: All files in `/Users/eddieargenal/Documents/obsidian-vault/workflows/` + `wiki/workflows/lint-plan.md`
- Also: append SCHEMA.md's Log Format block and Link Audit bash commands to `governance/workflows/vault-maintenance.md` and `governance/workflows/lint.md` respectively (content only present in SCHEMA.md)
- Output:
  - `governance/workflows/ingest.md`, `query.md`, `lint.md`, `vault-maintenance.md`, `vault-initialization.md`, `model-routing.md`, `document-extraction.md`, `memory-recall.md`, `coding-tasks.md`, `odoo-accounting.md`, `lint-plan.md`
  - `governance/workflows/00_index.md` — table: workflow | trigger | output | note (flag odoo-accounting and coding-tasks as domain workflows, candidates for future relocation)
- Dependencies: WU-2
- Complexity: Tier 1
- Validation: `ls governance/workflows/` shows 12 files; `workflows/` root folder empty; `wiki/workflows/` empty

### WU-7: Move ABA Ops Docs → governance/aba/ + Create Index
- Objective: Move ABA-specific operational docs from wiki/aba/
- Inputs:
  - `wiki/aba/AGENTS.md`
  - `wiki/aba/CLAUDE.md`
  - `wiki/aba/00-overview/agent-contract.md`
  - `wiki/aba/00-overview/agent-operating-model.md`
  - `wiki/aba/00-overview/how-to-use-this-wiki.md`
  - `wiki/aba/13-agent-prompts/` (all 13 prompt files + 00_index.md)
- Output:
  - `governance/aba/AGENTS.md`
  - `governance/aba/CLAUDE.md`
  - `governance/aba/agent-contract.md`
  - `governance/aba/agent-operating-model.md`
  - `governance/aba/how-to-use-this-wiki.md`
  - `governance/aba/prompts/` (14 files including 00_index.md)
  - `governance/aba/00_index.md` — table: file | purpose | when to read
- Dependencies: WU-2
- Complexity: Tier 1
- Validation: `ls governance/aba/` shows 6 files + prompts/; `ls governance/aba/prompts/` shows 14 files

### WU-8: Move memory/memory-rules.md → governance/memory-rules.md
- Objective: Move memory behavior policy to governance
- Inputs: `memory/memory-rules.md`
- Output: `governance/memory-rules.md`
- Dependencies: WU-2
- Complexity: Tier 1
- Validation: File exists at new path

### WU-9: Write governance/00_index.md
- Objective: Top-level governance section index — agents read this to find the right sub-document
- Format: Table with columns: Document | Type | Purpose | When to Read | When NOT to Read
- Must include entries for: compliance-rules, governance-model, content-lifecycle, evidence-promotion, output-provenance, review-cadence, memory-rules, schema/ (pointer to schema/00_index.md), workflows/ (pointer to workflows/00_index.md), aba/ (pointer to aba/00_index.md)
- Dependencies: WU-3, WU-4, WU-5, WU-6, WU-7, WU-8
- Complexity: Tier 1
- Validation: All 10 sections have entries; format is scannable

### WU-10: Write Root AGENTS.md
- Objective: Replace 5 root nav files with single lightweight routing file (<80 lines)
- Inputs (unique content to preserve — read these files):
  - `00_Start_Here.md` → routing table, ABA section index, agent nav sequence, memory category table, Key Rules block
  - `QUICK.md` → folder ASCII tree, Memory Truth States table, ABA quick nav
  - `README.md` → Design Philosophy, "What Is Not Here", Intended Users
  - `SCHEMA.md` → Special Files table (AGENTS.md, CLAUDE.md, indexes, log)
  - `architecture.md` → Navigation Quick Reference table
- Output: `AGENTS.md` at vault root
- Content structure:
  1. One-sentence vault purpose
  2. Design Philosophy (4 bullets)
  3. Intended Users
  4. Folder Structure (ASCII tree — updated to show governance/ as consolidated home)
  5. Agent Navigation Flow (5-step: start → governance/00_index.md → section index → file → answer)
  6. Quick Routing table (task → section index → file)
  7. ABA Section Index (00-13 with descriptions)
  8. Memory Category table
  9. Memory Truth States table
  10. Special Files table
  11. Key Rules / "What Is Not Here" guardrails
- Dependencies: WU-3, WU-4, WU-5, WU-6, WU-7, WU-8 (must know final paths)
- Complexity: Tier 2
- Validation: File is under 80 lines; contains all 11 sections; no references to deleted file paths

### WU-11: Write wiki/aba/ Stubs
- Objective: Create thin redirect stubs so Claude Code auto-loading still works
- Output 1: `wiki/aba/AGENTS.md` — stub content:
  ```
  # ABA Wiki — Agent Entry Point
  This file has moved. Full content: [[../../governance/aba/AGENTS]]
  ```
  (plus 2-3 line summary of what the full AGENTS.md contains)
- Output 2: `wiki/aba/CLAUDE.md` — stub content:
  ```
  # ABA Wiki — Operating Rules
  This file has moved. Full content: [[../../governance/aba/CLAUDE]]
  ```
  (plus 2-3 line summary)
- Dependencies: WU-7
- Complexity: Tier 1
- Validation: Both stub files exist; both contain valid wikilinks to governance/aba/

### WU-12: Update All Links (30 files, ~75 changes)
- Objective: Update every internal reference to moved/deleted paths
- Dependencies: WU-3–WU-11 must be complete (all destinations must exist before updating links)
- Complexity: Tier 2
- Validation: `grep -r "schema/\|workflows/\|13-agent-prompts\|vault-compliance-rules\|memory/governance\|00_Start_Here\|QUICK\.md\|SCHEMA\.md\|library-architecture\|library-governance_guide" /Users/eddieargenal/Documents/obsidian-vault --include="*.md" | grep -v "governance/\|archive/\|memory/runtime/\|governance/briefs/"` returns zero results

**Files to update (from Scout 2 link map):**

1 update each:
- `agents/Hermes.md` — `../workflows/model-routing` → `../governance/workflows/model-routing`
- `agents/OpenClaw.md` — same
- `tools/hermes.md` — same
- `tools/openrouter.md` — same
- `tools/obsidian.md` — `../00_Start_Here` → `../AGENTS`
- `templates/tool-template.md` — `../workflows/` → `../governance/workflows/`
- `memory/context.md` — `[[../SCHEMA]]` → `[[../AGENTS]]`
- `wiki/aba/13-agent-prompts/lint-wiki.md` — `schema/lint-rules.md` → `../../../../governance/schema/lint-rules.md` [NOTE: this file is moving to governance/aba/prompts/ — update at destination]
- `wiki/aba/13-agent-prompts/review-tool-quality.md` — same pattern
- `wiki/aba/13-agent-prompts/build-new-tool-from-sources.md` — same pattern

2–5 updates each:
- `indexes/workflows.md` — 10 wikilinks: `../00_Start_Here` → `../AGENTS`; `../workflows/[name]` → `../governance/workflows/[name]` (rewrite full table section)
- `indexes/memory.md` — `[[vault-compliance-rules]]` → `[[../governance/compliance-rules]]`; `[[memory-rules]]` → `[[../governance/memory-rules]]`
- `indexes/templates.md` — `../workflows/model-routing` → `../governance/workflows/model-routing`
- `sources/README.md` — `../workflows/ingest` → `../governance/workflows/ingest`; `../SCHEMA.md` → `../AGENTS.md`
- `wiki/index.md` — 11 wikilinks (rewrite workflow and compliance refs)
- `wiki/aba/00-overview/00_index.md` — 3 wikilinks: agent-contract, agent-operating-model, how-to-use-this-wiki → `../../governance/aba/[name]`
- `wiki/aba/00-overview/agent-contract.md` [at new path governance/aba/] — 3 plain text schema/ refs → governance/schema/
- `wiki/aba/00-overview/agent-operating-model.md` [at new path] — 5 wikilinks → governance/aba/prompts/
- `wiki/aba/01-sources/extracted/00_index.md` — 1 plain text path
- `wiki/aba/01-sources/raw/00_index.md` — 3 plain text paths
- `workflows/vault-initialization.md` [at new path governance/workflows/] — `../00_Start_Here` → `../../AGENTS`; `../memory/memory-rules` → `../../governance/memory-rules`
- `workflows/lint.md` [at new path] — 2 plain text refs
- `workflows/query.md` [at new path] — 2 refs
- `schema/query-rules.md` [at new path governance/schema/] — 2 plain text refs

Do NOT update:
- `archive/CHANGELOG.md` — append-only log, historical references are acceptable
- `memory/runtime/logs/log.md` — append-only log
- `memory/categories/procedures.md` — only contains log entries, not nav links
- `governance/vault-quality-remediation/SKILL.md` — mark superseded instead (WU-14)
- `governance/vault-quality-remediation/RUNBOOK.md` — mark superseded instead (WU-14)

### WU-13: Delete Deprecated Files
- Objective: Remove 9 confirmed-absorbed or duplicate files
- Dependencies: WU-12 must be fully complete first
- Files to delete (in this order — confirm content absorbed before each):
  1. `memory/governance.md` — duplicate of compliance-rules; unique content: none (error in Rule 4, not worth preserving)
  2. `wiki/vault-compliance-rules.md` — "Optional governance signals" section absorbed into WU-4
  3. `library-architecture.md` — empty
  4. `governance/library-governance_guide.md` — fully split in WU-3 (verify line coverage before deleting)
  5. `SCHEMA.md` — Log Format and Link Audit commands absorbed in WU-6; Special Files table in WU-10
  6. `00_Start_Here.md` — all unique content absorbed in WU-10
  7. `QUICK.md` — all unique content absorbed in WU-10
  8. `README.md` — all unique content absorbed in WU-10
  9. `architecture.md` — 6 Mermaid diagrams absorbed in WU-3; Navigation Quick Ref absorbed in WU-10
- Complexity: Tier 1
- Validation: `ls` confirms files gone; no broken links in post-deletion grep check

### WU-14: Mark SKILL.md and RUNBOOK.md as Superseded
- Objective: Flag remediation docs as historical artifacts describing a now-completed sprint
- Files: `governance/vault-quality-remediation/SKILL.md`, `governance/vault-quality-remediation/RUNBOOK.md`
- Action: Add/update YAML frontmatter `status: superseded`, `superseded_by: governance/00_index.md`, `superseded_date: 2026-05-11`, `note: describes 2026-05-08 remediation sprint — vault structure has since been consolidated`
- Dependencies: WU-12
- Complexity: Tier 1
- Validation: Both files have updated frontmatter

### WU-15: Write governance/schema/changelog.md
- Objective: Create the missing schema changelog — critical gap flagged in audit
- Output: `governance/schema/changelog.md` with backfill entry for initial schema creation
- Format:
  ```
  | date | author | change | files affected | migration |
  | 2026-05-07 | system | Initial schema creation — 8 schema files established | all schema files | n/a (initial creation) |
  | 2026-05-11 | consolidation | schema/ moved to governance/schema/ | all 8 schema files | update references from schema/ to governance/schema/ |
  ```
- Dependencies: WU-5
- Complexity: Tier 1
- Validation: File exists with both entries

---

## Sequencing

```
WU-1 (git snapshot)
  └─ WU-2 (create folders)
       └─ [parallel] WU-3, WU-4, WU-5, WU-6, WU-7, WU-8, WU-10, WU-15
                          └─ [parallel] WU-9, WU-11
                                             └─ WU-12 (link updates — all destinations must exist)
                                                   └─ [parallel] WU-13, WU-14
```

---

## Risks and Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Content loss during library-governance_guide.md split | Medium | Verify combined line count of 5 output files ≥ 353 before deleting source |
| wiki/aba/CLAUDE.md auto-load broken | High if not handled | Stub file MUST remain at wiki/aba/CLAUDE.md — covered in WU-11 |
| Broken links after file moves | High | WU-12 runs before WU-13; post-deletion grep confirms zero remaining stale refs |
| Relative path depth errors in moved ABA files | Medium | All internal refs in moved files updated at destination (not at source) |
| SKILL.md/RUNBOOK.md bash commands break post-consolidation | Low (they're superseded) | WU-14 marks them superseded — no attempt to update bash paths |

---

## Acceptance Criteria

- [ ] Git snapshot commit exists before any file moves
- [ ] `governance/` contains all 38 operational docs (or their successors)
- [ ] The 10 compliance rules exist in exactly one file: `governance/compliance-rules.md`
- [ ] `governance/library-governance_guide.md` is deleted; 5 successor docs exist and collectively cover all 353 source lines
- [ ] Every section under `governance/` has a `00_index.md` (governance/, schema/, workflows/, aba/)
- [ ] `governance/schema/changelog.md` exists with backfill entries
- [ ] Root `AGENTS.md` exists and is under 80 lines
- [ ] `00_Start_Here.md`, `QUICK.md`, `README.md`, `SCHEMA.md`, `architecture.md`, `library-architecture.md`, `memory/governance.md` are deleted
- [ ] `wiki/aba/AGENTS.md` and `wiki/aba/CLAUDE.md` are thin stubs (not deleted)
- [ ] Post-deletion grep for stale paths returns zero results (excluding archive/ and memory/runtime/logs/)
- [ ] `governance/vault-quality-remediation/SKILL.md` and `RUNBOOK.md` have `status: superseded`

---

## Execution Command

```
/execute-with-agent-team /Users/eddieargenal/Documents/obsidian-vault/governance/briefs/brief-governance-consolidation-2026-05-11.md 4
```
