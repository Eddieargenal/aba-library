---
title: Vault Alignment Audit — Remediation Brief
type: brief
brief_id: brief-alignment-audit-2026-05-12
version: "1.0"
status: active
created: 2026-05-12
updated: 2026-05-12
authors: ["Claude Code / plan-agent-team"]
reference_doc: "aba-wiki-detailed description.md (v2.4, 2026-05-12)"
related_docs: [governance/00_governance-index.md, governance/schema/changelog.md]
---

# Brief: ABA/DRR Vault Alignment Audit — Remediation Plan

## Planner Metadata
- Planning tier: 3 (full discovery)
- Planner team size: 6 scouts + 1 lead synthesizer
- Date: 2026-05-12
- Reference spec: `aba-wiki-detailed description.md` v2.4
- Recommended execution team size: 3–4 agents

---

## Objective

Bring the vault into full alignment with spec v2.4 so that frontmatter queries return correct results, governance documents are authoritative, and the agent operating model is self-consistent. Done looks like: all required frontmatter fields present and in controlled vocabulary, governance docs in sync, build scripts correct, and a human decision recorded on the 9-stage vs 11-stage lifecycle model.

---

## Deliverables

1. One governance decision recorded: 9-stage vs 11-stage lifecycle model
2. `governance/schema/frontmatter-schema.md` rewritten to match spec v2.4 exactly
3. `governance/schema/changelog.md` updated with v2.4 entry (2026-05-12)
4. `governance/aba/CLAUDE.md` directory paths corrected
5. `scripts/build-index.py` exclude filter updated for v2.4 index naming
6. All tool and framework `lifecycle_stage` values converted to correct slugs
7. All 22 source page `status:` values corrected to valid vocabulary
8. All tool `source_foundation` IDs corrected to match actual `source_id` slugs
9. Concept `maturity` vocabulary normalized to spec (`emerging|established|contested`)
10. Field instrument `format` vocabulary normalized to spec
11. `wiki/aba/outputs/internal/00_internal-index.md` created
12. `memory/current-handoff.md` updated to reflect this audit session
13. `indexes/agent-index.md` regenerated via `scripts/build-index.py`

---

## Context

- Vault root: `/Users/eddieargenal/Documents/obsidian-vault/`
- Spec: `aba-wiki-detailed description.md` v2.4 (updated 2026-05-12)
- 321 total .md files; 226 in wiki subtree; 22 extracted sources; 17 tools; 18 field instruments; 25 concepts; 9 Tier 1 + 30 Tier 2 frameworks
- Latest lint report: `wiki/aba/outputs/internal/lint-report-2026-05-11.md`
- Prior lint cycle resolved: 41 orphan framework pages, 75 missing frontmatter fields
- One open lint item (deferred): H-3 — 14 tools missing field_instruments (human decision gate)
- `scripts/build-index.py` exists and is functional except for exclude filter bug
- No `lint_wiki.py` exists — lint runs are manual bash checks only

---

## Hard Constraints

- **Do not close H-3** (14 tools missing field_instruments) — this requires domain expert input, not agent action
- **Do not fix lifecycle_stage slug values in tools/frameworks until the 9-stage vs 11-stage governance decision is recorded** — wrong slug mapping would create worse drift
- **Do not modify raw source PDFs** — immutable layer
- **All schema changes must be logged in `governance/schema/changelog.md`** before execution
- **`frontmatter-schema.md` is the authoritative schema reference** — it must be corrected before agents write any new pages
- **Every schema change to frontmatter-schema.md requires a changelog entry**

---

## Soft Constraints

- Prefer in-place frontmatter edits over page rewrites
- Batch edits to the same page type together to reduce context switching
- Regenerate `indexes/agent-index.md` as the final step (not between page edits)
- Keep `memory/current-handoff.md` updated at session close

---

## Known Unknowns Resolved

| Question | Finding | Confidence |
|---|---|---|
| Are lifecycle_stage values in correct slug format? | NO — all tools (~17) and frameworks (~20+) use human-readable strings, not slugs. ALL lifecycle_stage queries fail silently. | High |
| Does the vault use the 9-stage or 11-stage lifecycle model? | DIVERGED — 06-lifecycle/ dir has 11 stages (00–10); spec defines 9 (0–8). Stages diverge starting at stage 3. | High |
| Is frontmatter-schema.md in sync with spec? | NO — significantly drifted: missing `contradicts:` from all types, framework/synthesis schemas entirely absent, legacy fields present, wrong concept status/maturity vocab | High |
| Are source_foundation references in tools/frameworks resolvable? | NO — all tools and frameworks use underscored filenames as source IDs; actual source pages use hyphenated slugs. All cross-references are broken. | High |
| Does build-index.py correctly exclude 00_*-index.md pages? | NO — exclude filter is `{"00_index.md"}`; spec v2.4 requires `fname.startswith("00_")`. All descriptive index files are ingested as content. | High |
| What maturity vocabulary do concept pages use? | Non-spec: "sapling" and "seed" (20/25 pages). Spec requires `emerging\|established\|contested`. Every maturity query fails. | High |
| What status vocabulary do source pages use? | All 22 use `status: active` — not in spec vocabulary (`not-started\|extracted\|ingested\|reviewed`). | High |
| Do pages have `contradicts:` present? | YES — actual pages have `contradicts: []` on all sampled sources, tools, concepts, frameworks. The *schema document* omits it, but pages comply. | High |
| Is changelog.md current for v2.4? | NO — last entry 2026-05-11. The 2026-05-12 index renaming changes are not logged. | High |
| Does governance/aba/CLAUDE.md have correct paths? | NO — references `./01sources/`, `./04tools/`, `./06lifecycle/` without hyphens. | High |
| Do field instruments have correct lifecycle_stage slugs? | YES — field instruments are the most compliant page type; lifecycle_stage uses correct slugs. | High |
| Do validated tools have field_instruments linked? | NOT APPLICABLE — all 17 tools are `status: draft`. No promotion gate violation yet. | High |
| Does lint_wiki.py exist? | NO — lint is manual bash only. No automated lint script. | High |

---

## Unresolved Questions

| Question | Why Unresolved | Recommended Approach |
|---|---|---|
| 9-stage vs 11-stage lifecycle model: which is authoritative? | Governance decision — the spec says 9, the vault content uses 11. Stages 3–8 have different semantic mapping. | **Human decides before WU-4 executes.** Record decision in `governance/schema/changelog.md`. If 11-stage wins, spec v2.5 must be written. If 9-stage wins, lifecycle pages 03/04/06/07 must be renamed and tools/frameworks remap their stages. |
| What status value should the 22 ingested source pages carry? | `ingested` or `reviewed`? Both are valid spec values. `active` is not. | Human confirms which applies; agent batch-updates. Likely `ingested` for documents extracted but not formally reviewed. |
| What is the intended status of concept-cluster-map.md (maturity: established, source_count: 0)? | Logically contradictory per spec — established requires source backing. | Human resolves: correct source_count or downgrade maturity to `emerging`. |
| Should a lint_wiki.py script be created? | Not in scope of alignment audit but creates fragility. | Flag for follow-up session. Manual lint is adequate short-term. |
| Are ALL tools and frameworks affected by lifecycle_stage slug issue (not just sampled pages)? | Only 3 of 17 tools and 2 of ~39 frameworks were directly read. | WU-4 execution agent should grep all files before fixing. |

---

## Work Units

### WU-1: Governance Decisions (Human Gate)
**Do first — blocks WU-4 and WU-5**
- **Objective:** Record two governance decisions that block downstream agent work
- **Inputs:** This brief; `wiki/aba/06-lifecycle/` directory; spec v2.4 lifecycle stage table
- **Decisions needed:**
  1. **9-stage vs 11-stage**: Is the authoritative lifecycle model the 9-stage spec vocabulary or the 11-stage 06-lifecycle/ directory model?
  2. **Source status**: What value should fully extracted/ingested source pages carry — `ingested` or `reviewed`?
  3. **concept-cluster-map**: Correct source_count or downgrade maturity?
- **Output:** Decisions recorded as comments in `governance/schema/changelog.md` under a `## [2026-05-12] governance decision | lifecycle model` entry
- **Dependencies:** None
- **Complexity tier:** 1 (human judgment only)
- **Validation:** changelog.md has the decisions recorded before WU-4 begins

---

### WU-2: Fix governance/schema/frontmatter-schema.md
**Can run in parallel with WU-3**
- **Objective:** Rewrite frontmatter-schema.md to exactly match spec v2.4 schemas for all 6 page types
- **Inputs:** `governance/schema/frontmatter-schema.md` (current, drifted), spec v2.4 schema definitions
- **Specific changes:**
  - SOURCE: Replace `authors_or_orgs` with separate `author:` and `institution:` fields; add `foundational:`, `source_type:`, `file_type:`, `review_cycle:`, `last_reviewed:`, `next_review:`, `ingest_date:`, `ingest_status:`, `lifecycle_stage:`, `tags:`, `wiki_pages:`, `notes:`, `contradicts:`; remove legacy fields (`original_filename`, `source_matrix_row`, `used_for`, `relevance`); correct status vocab to `not-started|extracted|ingested|reviewed`
  - TOOL: Add `tier:`, `related_frameworks:`, `used_by_outputs:`, `contradicts:`
  - FIELD INSTRUMENT: Rename `related_tool:` → `related_tools:`; add `lifecycle_stage:`, `primary_users:`, `data_quality_checks:`, `status:`
  - CONCEPT: Correct status vocab to `draft|active|archived`; add `related_frameworks:`, `related_concepts:`, `known_tensions:`, `contradicts:`, `used_by_outputs:`
  - FRAMEWORK: Add complete framework schema (currently absent)
  - SYNTHESIS: Add complete synthesis schema (currently absent)
- **Output:** Updated `governance/schema/frontmatter-schema.md`
- **Dependencies:** None (schema fix is independent of governance decisions)
- **Complexity tier:** 2
- **Validation:** Every field in spec v2.4 schema blocks is present in the updated schema file; no legacy fields remain

---

### WU-3: Fix governance/aba/CLAUDE.md paths + changelog
**Can run in parallel with WU-2**
- **Objective:** Correct broken directory paths in CLAUDE.md; log v2.4 changes in changelog.md
- **Inputs:** `governance/aba/CLAUDE.md`, `governance/schema/changelog.md`
- **Specific changes:**
  - CLAUDE.md: Replace `./01sources/` → `./01-sources/`, `./04tools/` → `./04-tools/`, `./06lifecycle/` → `./06-lifecycle/` (and any other path references missing hyphens)
  - changelog.md: Add entry for v2.4 (2026-05-12): index file renaming to `00_*-index.md` pattern, librarian skill exclusion filter update, governance reference updates
- **Output:** Updated CLAUDE.md and changelog.md
- **Dependencies:** None
- **Complexity tier:** 1
- **Validation:** All directory paths in CLAUDE.md use hyphen separators; changelog has a 2026-05-12 entry

---

### WU-4: Fix lifecycle_stage values in tools and frameworks
**BLOCKED BY WU-1 (governance decision on stage model)**
- **Objective:** Convert all lifecycle_stage values in tool and framework pages from human-readable strings to spec slugs
- **Inputs:** WU-1 decision; all files in `wiki/aba/04-tools/` and `wiki/aba/03-frameworks/`; spec 9-stage vocabulary (or updated vocabulary if 11-stage wins)
- **Scope:** 17 tool pages + ~39 framework pages
- **If 9-stage wins:** Map values to slugs using this table:
  - "0. Appropriateness decision" → `appropriateness-decision`
  - "1. Area selection and boundary definition" → `area-selection`
  - "2. Area profile and systems diagnosis" → `neighbourhood-diagnosis`
  - "3. Community and stakeholder engagement" → ⚠ NO SLUG — escalate to human
  - "4. Joint risk and needs prioritization" → `joint-prioritization`
  - "5. Integrated area strategy" → `integrated-area-strategy`
  - "6. Program design and modality selection" → ⚠ NO SLUG — escalate to human
  - "7. Detailed technical design" → ⚠ NO SLUG — escalate to human
  - "8. Area-based implementation" → `implementation-adaptation`
  - "9. Monitoring, learning, and adaptation" → `monitoring-learning`
  - "10. Transition, handover, and scaling" → `transition-handover`
- **Output:** All tool and framework pages with slug-format lifecycle_stage values
- **Dependencies:** WU-1
- **Complexity tier:** 2
- **Validation:** `grep -r "lifecycle_stage:" wiki/aba/04-tools/ wiki/aba/03-frameworks/` shows only valid slugs, no human-readable strings

---

### WU-5: Fix source status + source_foundation cross-references
**Can start after WU-1 decision on source status**
- **Objective:** (a) Correct `status: active` → correct vocab on all 22 source pages; (b) correct all `source_foundation:` lists in tools and frameworks to use actual source_id slugs
- **Inputs:** WU-1 decision on source status value; all 22 extracted source pages; all 17 tool pages; all ~39 framework pages; the source_id mapping (build from actual frontmatter in extracted/ pages)
- **Approach:**
  1. Build source_id lookup map: grep all `source_id:` values from `wiki/aba/01-sources/extracted/`
  2. Update all 22 source pages: `status: active` → `status: [decision from WU-1]`
  3. Update source_foundation lists in all tools and frameworks: match underscored filename references to actual source_id slugs
- **Output:** All source pages with valid status; all tool/framework source_foundation lists with resolvable source_ids
- **Dependencies:** WU-1 (for status value)
- **Complexity tier:** 2
- **Validation:** No source page has `status: active`; grep source_foundation values in tools against source_id list — all must match

---

### WU-6: Fix vocabulary — concept maturity + field instrument format
**Independent — can run any time**
- **Objective:** Normalize non-spec vocabulary values in concept maturity and field instrument format fields
- **Inputs:** All 25 concept pages; all 18 field instrument pages
- **Specific changes:**
  - Concepts: `sapling` → `emerging`; `seed` → `emerging`; verify `established` and `contested` remain where semantically correct; fix `concept-cluster-map` (maturity: established, source_count: 0) per WU-1 decision
  - Field instruments: Normalize format values to spec vocabulary:
    - `kii guide` → `guide`
    - `observation form` → `form`
    - `mapping form` → `form`
    - `mapping sheet` → `form`
    - `inventory form` → `form`
    - `analysis matrix` → `matrix`
    - `document template` → ⚠ no spec equivalent; flag for human decision (closest: `form`)
- **Output:** All concept pages with spec-valid maturity; all field instrument pages with spec-valid format
- **Dependencies:** WU-1 for concept-cluster-map decision only
- **Complexity tier:** 1
- **Validation:** `grep -r "maturity:" wiki/aba/02-concepts/` shows only `emerging|established|contested`; `grep -r "^format:" wiki/aba/05-field-instruments/` shows only spec values

---

### WU-7: Fix build-index.py + structural gaps
**Independent — can run any time**
- **Objective:** Fix the build-index.py exclude filter; create missing internal index; rename ambiguous lifecycle page
- **Inputs:** `scripts/build-index.py`; `wiki/aba/outputs/internal/`; `wiki/aba/06-lifecycle/00-appropriateness-decision.md`
- **Specific changes:**
  1. `build-index.py`: Change exclude set `{"00_index.md"}` → update logic to `fname.startswith("00_")`
  2. Create `wiki/aba/outputs/internal/00_internal-index.md` (stub index listing lint reports)
  3. Rename `wiki/aba/06-lifecycle/00-appropriateness-decision.md` → `appropriateness-decision.md` (remove `00-` prefix that collides with index naming convention)
  4. Fix 3 tool pages with null `field_instruments:` → `field_instruments: []` (`01-aba-feasibility-and-necessity-assessment-tool.md`, `05-hevc-risk-mapping-tool.md`, `06-stakeholder-coordination-mapping-tool.md`)
- **Output:** Fixed script; new index file; renamed lifecycle page; corrected tool frontmatter
- **Dependencies:** None
- **Complexity tier:** 1
- **Validation:** Run `python3 scripts/build-index.py` — output should not include any `00_*-index.md` pages; confirm `indexes/agent-index.md` is regenerated correctly

---

### WU-8: Regenerate agent-index.md + close session
**Runs last — depends on all prior WUs**
- **Objective:** Regenerate the agent index to reflect all remediated frontmatter; update handoff; append log entry
- **Inputs:** All prior WUs complete; `scripts/build-index.py`
- **Steps:**
  1. Run `python3 scripts/build-index.py` from vault root
  2. Verify `indexes/agent-index.md` contains no `00_*-index.md` entries and no invalid vocabulary values
  3. Update `memory/current-handoff.md` with this session's summary and next open items
  4. Append to `memory/runtime/logs/log.md`: `## [2026-05-12] remediation | Alignment audit remediation complete — lifecycle model decision pending`
- **Output:** Fresh `indexes/agent-index.md`; updated handoff; log entry
- **Dependencies:** WU-2 through WU-7 (all)
- **Complexity tier:** 1
- **Validation:** `indexes/agent-index.md` is newer than pre-remediation timestamp; log.md has 2026-05-12 entry

---

## Alignment Summary by Dimension

| Dimension | Status | Severity |
|---|---|---|
| Frontmatter schema document (frontmatter-schema.md) | MISALIGNED — significant drift | CRITICAL |
| lifecycle_stage vocabulary (tools/frameworks) | MISALIGNED — full strings not slugs | CRITICAL |
| Lifecycle stage model (9 vs 11 stages) | MISALIGNED — governance divergence | CRITICAL |
| source_foundation cross-references | MISALIGNED — all references broken | CRITICAL |
| Source page status vocabulary | MISALIGNED — `active` not in spec | CRITICAL |
| build-index.py exclude filter | MISALIGNED — v2.4 pattern not applied | CRITICAL |
| Concept maturity vocabulary | MISALIGNED — sapling/seed not in spec | CRITICAL |
| changelog.md currency | MISALIGNED — v2.4 not logged | CRITICAL |
| governance/aba/CLAUDE.md paths | MISALIGNED — hyphens missing | HIGH |
| Field instrument format vocabulary | MISALIGNED — 11/18 non-conforming | HIGH |
| Tool field_instruments (3 null values) | MISALIGNED — must be [] not null | HIGH |
| Index file naming (00_*-index.md) | ALIGNED — all 20 indexes conform | OK |
| Framework file naming (YYYY-*-framework.md) | ALIGNED | OK |
| Source extraction path structure | ALIGNED | OK |
| Field instrument lifecycle_stage | ALIGNED — correct slugs | OK |
| contradicts: field presence (pages) | ALIGNED — present on all sampled pages | OK |
| known_tensions: field presence | ALIGNED — present on sampled concepts | OK |
| AGENTS.md presence | ALIGNED | OK |
| Governance file presence | ALIGNED — all required files exist | OK |
| scripts/build-index.py presence | ALIGNED | OK |
| memory/current-handoff.md | STALE — 2026-05-11, needs update | MEDIUM |
| wiki/aba/outputs/internal/ index | MISSING | MEDIUM |
| Additional wiki sections (07–12) | UNDOCUMENTED in spec — not violations | LOW |
| wiki_pages: field on sources | PRESENT but empty on all 22 | MEDIUM |
| Synthesis/output pages | NONE CREATED YET | LOW |

---

## Risks and Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Lifecycle slug mapping creates new errors if 9-stage model doesn't cover all 11 stages | HIGH | Require WU-1 governance decision first; flag unmappable stages for human review rather than guessing |
| source_foundation ID correction introduces typos in source_id slugs | MEDIUM | Build lookup map from actual source pages first; validate every corrected ID against the map |
| frontmatter-schema.md rewrite misses a field from spec | MEDIUM | Use spec v2.4 schema blocks as the literal template; do field-by-field comparison before closing |
| build-index.py fix breaks other exclusion logic | LOW | Test run after fix; confirm output doesn't include governance files or index pages |
| Concept maturity remapping loses semantic intent (sapling was "established-but-not-stable") | MEDIUM | Map conservatively: sapling → emerging, seed → emerging; leave established/contested as-is |

---

## Acceptance Criteria

- [ ] governance/schema/changelog.md has a 2026-05-12 entry logging v2.4 changes and the governance decisions from WU-1
- [ ] governance/schema/frontmatter-schema.md includes all 6 page types with all required fields matching spec v2.4 exactly
- [ ] `grep -r "lifecycle_stage:" wiki/aba/04-tools/ wiki/aba/03-frameworks/ --include="*.md"` returns only valid slugs (no strings like "1. Area selection")
- [ ] `grep -r "^status: active" wiki/aba/01-sources/ --include="*.md"` returns zero results
- [ ] `grep -r "maturity:" wiki/aba/02-concepts/ --include="*.md"` returns only `emerging|established|contested` values (no sapling/seed)
- [ ] `grep -r "^format:" wiki/aba/05-field-instruments/ --include="*.md"` returns only spec vocab values
- [ ] `python3 scripts/build-index.py` completes without error; `indexes/agent-index.md` contains no `00_*-index.md` entries
- [ ] governance/aba/CLAUDE.md contains no `./01sources/` or `./04tools/` style paths (unhyphenated)
- [ ] `wiki/aba/outputs/internal/00_internal-index.md` exists
- [ ] `memory/current-handoff.md` updated with this session
- [ ] `memory/runtime/logs/log.md` has a 2026-05-12 entry

---

## Execution Order

```
WU-1 (human)
├── WU-2 (parallel, no dependency)
├── WU-3 (parallel, no dependency)
├── WU-6 (parallel, no dependency)
├── WU-7 (parallel, no dependency)
└── [after WU-1 completes] → WU-4, WU-5
                              └── [all complete] → WU-8
```

---

## Execution Command

```
/execute-with-agent-team /Users/eddieargenal/Documents/obsidian-vault/governance/briefs/brief-alignment-audit-2026-05-12.md 4
```

**Note:** WU-1 is a human gate. Execute WU-2, WU-3, WU-6, and WU-7 first (agents can parallelize these). Pause at WU-4 and WU-5 until the human records the lifecycle model decision and source status decision in `governance/schema/changelog.md`.
