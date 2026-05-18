# Brief: Vault Audit Remediation — 2026-05-11

## Planner Metadata
- Planning tier: 1 (all unknowns resolved via local verification)
- Planner team size: 1 (lead synthesizer only)
- Date: 2026-05-11
- Recommended execution team size: 3

---

## Objective

Close 10 open findings from the Vault Audit Report dated 2026-05-11. Done = zero critical failures, all active files have required frontmatter fields, IASC duplicate resolved with content merged, lint report filed to correct path with cadence documented, and all structural gaps patched.

---

## Deliverables

1. Minimum frontmatter on all 32 Tier 2 frameworks (C-2)
2. IASC 2010 duplicate resolved — unique content merged into hyphen file, underscore extracted file + PDF deleted (C-3)
3. `outputs/` folder created; existing lint report moved there (H-1)
4. `status:` field on all 70 currently non-compliant files (H-2)
5. Fresh lint report at `outputs/lint-report-2026-05-11.md` (H-4)
6. Lint cadence expectation added to `governance/review-cadence.md` (H-4)
7. `wiki/aba/01-sources/raw/2021_unhcr_aba-humanitarian-early-recovery.pdf` deleted; raw index updated (M-2)
8. `memory/next-session.md` and `memory/current-handoff.md` filled with current vault state (M-3)
9. `used_by_outputs: []` field on all 9 Tier 1 frameworks (M-4)
10. `maturity:` field on `wiki/aba/02-concepts/concept-cluster-map.md` (M-5)
11. `## Data Quality Checks` section on `wiki/aba/05-field-instruments/duplication-gap-analysis-matrix.md` (L-3)

---

## Context

**Vault root:** `/Users/eddieargenal/Documents/obsidian-vault/`
**Git repo:** yes

**Verified facts (resolved during planning):**

- **IASC files differ** — `2010_iasc_` (underscore) and `2010-iasc-` (hyphen) extractions of the same document are complementary, not identical. Underscore emphasizes area-based shift rationale; hyphen has action matrix detail. Merge strategy: hyphen file is canonical (per its own frontmatter `canonical_file`); add any unique paragraphs from underscore's extracted text and key insights sections into hyphen file, then delete underscore extracted file and underscore PDF (`2010_iasc_meeting-humanitarian-challenges-urban-areas-strategy.pdf`).
- **Lint script:** exists at `wiki/aba/scripts/lint_wiki.py` — run with `python3 wiki/aba/scripts/lint_wiki.py` from vault root
- **03-frameworks/00_index.md Tier 2 section:** already lists all 32 frameworks — index is complete. Only frontmatter addition needed for C-2.
- **Tier 2 framework frontmatter target:**
  ```yaml
  ---
  type: framework
  tier: 2
  status: reference
  created: YYYY    ← derive from year prefix in filename
  updated: 2026-05-11
  ---
  ```
- **Tier 1 framework frontmatter pattern:** `type: framework`, `status: active`, `lifecycle_stage`, `related_tools`, `related_concepts`, `source_foundation` — add `used_by_outputs: []` at end
- **Field instruments:** already have `type`, `instrument_id`, `format`, `related_tools`, `required_for_decision_domains`, `created`, `updated` — missing only `status:`. Use `status: draft` (no field validation on record).
- **70 files missing `status:`** — breakdown:
  - `governance/aba/AGENTS.md`, `governance/aba/CLAUDE.md` → `status: active`
  - `governance/schema/` (7 files: citation-rules, ingest-rules, lint-rules, naming-conventions, page-types, query-rules, tool-quality-standard) → `status: active`
  - `indexes/` (4: memory, templates, tools, workflows) → `status: active`
  - `sources/README.md` → `status: active`
  - `templates/memory-record-template.md`, `templates/task-log-template.md` → `status: reference`
  - `wiki/aba/03-frameworks/` Tier 2 (32 files) → `status: reference` ← handled by WU-2 (C-2) simultaneously
  - `wiki/aba/05-field-instruments/` (18 files) → `status: draft`
  - `outputs/toolkits/aba-technical-guide.md` → `status: draft`
- **9 Tier 1 frameworks:** `2017-aba-appropriateness-decision-framework.md`, `2017-area-selection-framework.md`, `2017-neighborhood-diagnosis-framework.md`, `2026-area-based-coordination-framework.md`, `2017-joint-prioritization-framework.md`, `2017-integrated-area-strategy-framework.md`, `2019-implementation-adaptation-framework.md`, `2017-transition-handover-framework.md`, `2015-urban-drr-response-design-framework.md`

---

## Hard Constraints

- IASC underscore file must NOT be deleted until its unique content is merged into the hyphen file
- `status:` values must match context: `active` for operational docs, `reference` for Tier 2 frameworks and templates, `draft` for unvalidated field instruments and toolkit
- Append-only files (`archive/CHANGELOG.md`, `memory/runtime/logs/log.md`) must NOT be modified
- The lint script output must be filed to `outputs/` — not to the old `outputs/wiki-lint-report.md` path
- `2026-05-07.md` (daily note at root) — do NOT add status: to this file

## Soft Constraints

- Keep frontmatter additions minimal — do not add fields beyond what the scope specifies
- `used_by_outputs: []` should be added as the last field in each Tier 1 framework's frontmatter block
- Lint cadence addition to `governance/review-cadence.md` should be a short section, not a full rewrite

---

## Known Unknowns Resolved

| Question | Finding | Confidence |
|---|---|---|
| Are IASC underscore and hyphen files identical? | No — different content, complementary extractions. Must merge before deleting. | High |
| Does a lint script exist? | Yes — `wiki/aba/scripts/lint_wiki.py` | High |
| Does 03-frameworks/00_index.md already list all 32 Tier 2 frameworks? | Yes — all 32 listed. No index updates needed for C-2. | High |
| What frontmatter do Tier 2 frameworks need? | type, tier, status, created, updated — 5 fields | High |
| What status: value for field instruments? | draft — no field validation on record | High |

## Unresolved Questions

None.

---

## Work Units

### WU-1: Git Snapshot
- Objective: Commit current vault state before any changes
- Inputs: current vault state
- Output: commit `chore: pre-audit-remediation snapshot`
- Dependencies: none — first
- Complexity: Tier 1
- Validation: `git log --oneline -1`

### WU-2: C-2 — Add Frontmatter to 32 Tier 2 Frameworks
- Objective: Add minimum frontmatter to all 32 Tier 2 framework files
- Inputs: all `*.md` files in `wiki/aba/03-frameworks/` that currently lack a `---` frontmatter block (32 files — all dated 2007–2026 except the 9 Tier 1 files)
- Tier 1 files to SKIP (already have frontmatter): `2017-aba-appropriateness-decision-framework.md`, `2017-area-selection-framework.md`, `2017-neighborhood-diagnosis-framework.md`, `2026-area-based-coordination-framework.md`, `2017-joint-prioritization-framework.md`, `2017-integrated-area-strategy-framework.md`, `2019-implementation-adaptation-framework.md`, `2017-transition-handover-framework.md`, `2015-urban-drr-response-design-framework.md`
- Frontmatter to prepend to each file:
  ```yaml
  ---
  type: framework
  tier: 2
  status: reference
  created: YYYY
  updated: 2026-05-11
  ---
  ```
  Where `YYYY` is the 4-digit year prefix from the filename.
- Output: 32 files each beginning with the above frontmatter block
- Dependencies: WU-1
- Complexity: Tier 1
- Validation: `grep -rL "^status:" wiki/aba/03-frameworks/ | grep -v "00_index"` returns empty (or only Tier 1 files already compliant)

### WU-3: C-3 — Merge IASC Duplicate and Delete Underscore Files
- Objective: Resolve the two-file IASC 2010 duplicate by merging unique content, then deleting the underscore variant
- Inputs:
  - `wiki/aba/01-sources/extracted/2010_iasc_meeting-humanitarian-challenges-urban-areas-strategy.md` (underscore — to be merged then deleted)
  - `wiki/aba/01-sources/extracted/2010-iasc-meeting-humanitarian-challenges-urban-areas-strategy.md` (hyphen — canonical, to be enriched)
- Merge strategy:
  1. Read both files in full
  2. The hyphen file has better action matrix detail; the underscore file has better area-based-shift rationale
  3. In the hyphen file, in the extracted text section, add a note about the complementary extraction and incorporate any key unique sentences from the underscore file's extracted text and key insights that are NOT already covered
  4. Update `notes:` field in hyphen frontmatter to remove "Duplicate extraction exists" notice and replace with "Merged with underscore variant 2026-05-11"
  5. Write updated hyphen file
  6. Delete underscore extracted file: `rm wiki/aba/01-sources/extracted/2010_iasc_meeting-humanitarian-challenges-urban-areas-strategy.md`
  7. Delete underscore PDF: `rm "wiki/aba/01-sources/raw/2010_iasc_meeting-humanitarian-challenges-urban-areas-strategy.pdf"`
  8. Check for any references to the underscore filename in other extracted files and concept pages: `grep -r "2010_iasc_" wiki/aba/ --include="*.md"` — update any found to the hyphen filename
- Output: single IASC 2010 extracted file (hyphen), merged content, underscore files gone
- Dependencies: WU-1
- Complexity: Tier 2
- Validation: `ls wiki/aba/01-sources/extracted/ | grep iasc` shows only 2 files (hyphen + 2026); `ls wiki/aba/01-sources/raw/ | grep 2010_iasc` shows empty

### WU-4: H-1 — Create outputs/internal/ and Move Existing Lint Report
- Objective: Create the correct output filing path and move the misplaced lint report
- Inputs: `outputs/wiki-lint-report.md` (existing lint report at wrong path)
- Output:
  - `outputs/` folder created
  - `outputs/lint-report-2026-05-09.md` (moved from `wiki-lint-report.md`)
  - `outputs/wiki-lint-report.md` no longer exists
- Dependencies: WU-1
- Complexity: Tier 1
- Validation: `ls outputs/` shows `lint-report-2026-05-09.md`; `ls outputs/wiki-lint-report.md` errors

### WU-5: H-2 — Add status: to Non-Framework Non-Instrument Files (38 files)
- Objective: Add `status:` field to all non-framework, non-field-instrument files missing it
- The 32 Tier 2 frameworks are handled by WU-2; the 18 field instruments by WU-6b below
- Files and values:
  - `governance/aba/AGENTS.md` → `status: active`
  - `governance/aba/CLAUDE.md` → `status: active`
  - `governance/schema/citation-rules.md` → `status: active`
  - `governance/schema/ingest-rules.md` → `status: active`
  - `governance/schema/lint-rules.md` → `status: active`
  - `governance/schema/naming-conventions.md` → `status: active`
  - `governance/schema/page-types.md` → `status: active`
  - `governance/schema/query-rules.md` → `status: active`
  - `governance/schema/tool-quality-standard.md` → `status: active`
  - `indexes/memory.md` → `status: active`
  - `indexes/templates.md` → `status: active`
  - `indexes/tools.md` → `status: active`
  - `indexes/workflows.md` → `status: active`
  - `sources/README.md` → `status: active`
  - `templates/memory-record-template.md` → `status: reference`
  - `templates/task-log-template.md` → `status: reference`
  - `outputs/toolkits/aba-technical-guide.md` → `status: draft`
- Method: For each file, read frontmatter, add `status: [value]` as a new line after the last existing frontmatter field but before the closing `---`
- Dependencies: WU-1
- Complexity: Tier 1
- Validation: `grep -rL "^status:" governance/aba/AGENTS.md governance/aba/CLAUDE.md governance/schema/ indexes/ sources/README.md templates/ outputs/toolkits/` returns empty

### WU-6: H-2b — Add status: draft to 18 Field Instruments + H-4 Lint + M-4 + M-5 + L-3
- Objective: Add `status: draft` to 18 field instruments; run lint script; fill handoff files; patch concept and instrument pages

**Part A — Field instrument status (18 files):**
- All files in `wiki/aba/05-field-instruments/` except `00_index.md`
- Add `status: draft` to each file's frontmatter (after `updated:` field)
- Files: decision-memo-template, duplication-gap-analysis-matrix, hazard-exposure-vulnerability-capacity-matrix, household-mini-survey, kii-guide-community-leaders, kii-guide-market-actors, kii-guide-municipality, kii-guide-ngos-cbos, kii-guide-protection-actors, kii-guide-service-provider, local-resource-inventory, operational-feasibility-checklist, participation-feasibility-checklist, participatory-mapping-guide, rapid-area-observation-form, service-functionality-mapping-sheet, stakeholder-5w-mapping-form, transect-walk-observation-form

**Part B — M-5: Add maturity: to concept-cluster-map.md:**
- File: `wiki/aba/02-concepts/concept-cluster-map.md`
- Add `maturity: established` to frontmatter

**Part C — L-3: Add Data Quality Checks section to duplication-gap-analysis-matrix.md:**
- File: `wiki/aba/05-field-instruments/duplication-gap-analysis-matrix.md`
- Read the file to understand context
- Append a section: `## Data Quality Checks` with at minimum these checks:
  - Source verification: confirm 5W data from at least 2 independent actor sources before mapping a gap or overlap
  - Recency threshold: flag any actor data older than 30 days as potentially stale
  - Coverage validation: verify that mapped coverage areas correspond to actual operational areas, not planned areas
  - Respondent cross-check: if a gap is identified by only one informant, note as unconfirmed pending second source

**Part D — M-4: Add used_by_outputs: [] to 9 Tier 1 frameworks:**
- Files (all in `wiki/aba/03-frameworks/`):
  - `2017-aba-appropriateness-decision-framework.md`
  - `2017-area-selection-framework.md`
  - `2017-neighborhood-diagnosis-framework.md`
  - `2026-area-based-coordination-framework.md`
  - `2017-joint-prioritization-framework.md`
  - `2017-integrated-area-strategy-framework.md`
  - `2019-implementation-adaptation-framework.md`
  - `2017-transition-handover-framework.md`
  - `2015-urban-drr-response-design-framework.md`
- Add `used_by_outputs: []` as the last field before closing `---` in each file's frontmatter

- Dependencies: WU-1
- Complexity: Tier 1
- Validation:
  - `grep -rL "^status:" wiki/aba/05-field-instruments/` returns empty (excluding 00_index.md)
  - `grep "maturity:" wiki/aba/02-concepts/concept-cluster-map.md` returns a result
  - `grep "Data Quality Checks" wiki/aba/05-field-instruments/duplication-gap-analysis-matrix.md` returns a result
  - `grep -l "used_by_outputs" wiki/aba/03-frameworks/` shows 9 files

### WU-7: H-4 — Run Lint Script + File Report + Add Cadence
- Objective: Generate a fresh lint report, file it correctly, add cadence expectation to governance
- Dependencies: WU-4 must complete first (outputs/internal/ folder must exist)
- Steps:
  1. Run: `cd /Users/eddieargenal/Documents/obsidian-vault && python3 wiki/aba/scripts/lint_wiki.py > /tmp/lint-output-2026-05-11.txt 2>&1`
  2. Read the output at `/tmp/lint-output-2026-05-11.txt`
  3. Write a formatted lint report to `outputs/lint-report-2026-05-11.md` with frontmatter:
     ```yaml
     ---
     type: lint-report
     status: complete
     generated: 2026-05-11
     method: automated-script
     ---
     ```
     And the lint output as the body (match format of `lint-report-2026-05-09.md`)
  4. Read `governance/review-cadence.md`; append a new section:
     ```markdown
     ## Lint Cadence Expectation
     - **Target frequency:** Weekly (every 7 days)
     - **Filing path:** `outputs/lint-report-YYYY-MM-DD.md`
     - **Trigger:** After any ingest, or on the weekly review schedule
     - **Responsible:** Agent Maintainer (per governance/governance-model.md)
     - **Last run:** 2026-05-11
     ```
- Complexity: Tier 1
- Validation:
  - `outputs/lint-report-2026-05-11.md` exists and has content
  - `grep "Lint Cadence" governance/review-cadence.md` returns a result

### WU-8: M-2 — Delete 2021_unhcr PDF + Update Raw Index
- Objective: Remove the unextracted PDF and update the inventory
- Steps:
  1. `rm "wiki/aba/01-sources/raw/2021_unhcr_aba-humanitarian-early-recovery.pdf"`
  2. Read `wiki/aba/01-sources/raw/00_index.md`
  3. Find the entry for `2021_unhcr_aba-humanitarian-early-recovery` and update its status to `deleted` with a note: `deleted: 2026-05-11 — no extraction completed; removed during audit remediation`
- Dependencies: WU-1
- Complexity: Tier 1
- Validation: `ls wiki/aba/01-sources/raw/ | grep 2021` returns empty; `grep "2021_unhcr" wiki/aba/01-sources/raw/00_index.md` shows updated entry

### WU-9: M-3 — Fill next-session.md and current-handoff.md
- Objective: Replace blank template stubs with actual current vault state
- Files: `memory/next-session.md`, `memory/current-handoff.md`
- Content for `current-handoff.md`:
  - What's Happening Now: Audit remediation sprint in progress — closing 10 open findings from Vault Audit Report 2026-05-11
  - What's Left: After this sprint — H-3 (14 tool instruments, requires domain expert), M-1 (pattern candidates, requires domain expert), and the quarterly governance council review
  - Notes: Governance consolidation completed same day — all operational docs now in governance/; all links updated; git history clean
- Content for `next-session.md`:
  - Next Session Should: Run a fresh lint report to confirm remediation closed the audit findings; check if H-3 (tool instruments) is ready for domain input
  - Quick Context: Two-sprint day — governance consolidation + audit remediation. Vault at governance/00_index.md for all rules; wiki/aba/ for domain content.
  - If Blocked: Check git log for last two commits; read governance/briefs/ for scope and brief docs
- Dependencies: WU-1
- Complexity: Tier 1
- Validation: Both files non-empty; neither contains the placeholder `<!-- ... -->` comment blocks

---

## Sequencing

```
WU-1 (git snapshot)
  └─ [parallel] WU-2, WU-3, WU-4, WU-5, WU-6, WU-8, WU-9
                    └─ WU-4 completes first
                           └─ WU-7 (lint report — needs outputs/internal/ to exist)
```

Note: WU-7 depends on WU-4. Executor should start WU-7 only after WU-4 confirms completion.

---

## Risks and Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Lint script fails or produces no output | Low | If script errors, run manual lint from governance/aba/prompts/lint-wiki.md instead; document method in lint report frontmatter |
| IASC merge loses unique content | Medium | Agent must read both files in full before writing merged version; diff confirms deletable sections |
| Wrong status: value assigned | Low | Per explicit value map in WU-5 and WU-6; no guessing |
| frontmatter prepend breaks file if it already has partial frontmatter | Low | Check each file for existing `---` before prepending; 32 Tier 2 frameworks confirmed as having zero frontmatter |

---

## Acceptance Criteria

- [ ] `grep -rL "^status:" wiki/aba/03-frameworks/ | grep -v "00_index"` returns empty
- [ ] `grep -rL "^status:" wiki/aba/05-field-instruments/ | grep -v "00_index"` returns empty
- [ ] `grep -rL "^status:" governance/schema/ governance/aba/AGENTS.md governance/aba/CLAUDE.md indexes/ sources/README.md templates/` returns empty
- [ ] `ls wiki/aba/01-sources/extracted/ | grep iasc` shows exactly 2 files (hyphen + 2026)
- [ ] `ls wiki/aba/01-sources/raw/ | grep 2010_iasc` returns empty
- [ ] `ls wiki/aba/01-sources/raw/ | grep 2021` returns empty
- [ ] `ls outputs/` shows `lint-report-2026-05-09.md` and `lint-report-2026-05-11.md`
- [ ] `ls outputs/wiki-lint-report.md` errors (file does not exist at old path)
- [ ] `grep "Lint Cadence" governance/review-cadence.md` returns a result
- [ ] `grep -l "used_by_outputs" wiki/aba/03-frameworks/` shows 9 files
- [ ] `grep "maturity:" wiki/aba/02-concepts/concept-cluster-map.md` returns a result
- [ ] `grep "Data Quality Checks" wiki/aba/05-field-instruments/duplication-gap-analysis-matrix.md` returns a result
- [ ] `memory/next-session.md` and `memory/current-handoff.md` contain no `<!--` placeholder blocks

---

## Execution Command

```
/execute-with-agent-team /Users/eddieargenal/Documents/obsidian-vault/governance/briefs/brief-audit-remediation-2026-05-11.md 3
```
