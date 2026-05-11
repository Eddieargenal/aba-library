# Scope: Vault Audit Remediation — 2026-05-11

## Objective

Resolve all open findings from the Vault Audit Report dated 2026-05-11. Three findings were already closed by the governance consolidation sprint (C-1, L-1, L-2). This sprint closes the remaining 10 open findings across critical, high, medium, and low severity. Done looks like: zero critical failures, all active files with required frontmatter, IASC duplicate resolved, lint report filed to correct path with cadence documented.

---

## Deliverables

1. **C-2 closed** — Minimum frontmatter added to all 32 Tier 2 frameworks; all 32 appear in `03-frameworks/00_index.md`
2. **C-3 closed** — IASC duplicate resolved: underscore extracted file deleted, underscore PDF deleted, all references updated to hyphen canonical
3. **H-1 closed** — `wiki/aba/outputs/internal/` folder created; existing lint report moved there with correct filename
4. **H-2 closed** — `status:` field added to all 70 non-compliant files (governance/schema, indexes, templates, field instruments, framework stubs, outputs, governance/aba stubs)
5. **H-4 closed** — Fresh lint report filed to `wiki/aba/outputs/internal/lint-report-2026-05-11.md`; cadence expectation added to `governance/review-cadence.md`
6. **M-2 closed** — `2021_unhcr_aba-humanitarian-early-recovery.pdf` deleted from raw; `wiki/aba/01-sources/raw/00_index.md` updated to reflect deletion
7. **M-3 closed** — `memory/next-session.md` and `memory/current-handoff.md` filled with current vault state
8. **M-4 closed** — `used_by_outputs: []` field added to all 9 Tier 1 frameworks
9. **M-5 closed** — `maturity:` field added to `wiki/aba/02-concepts/concept-cluster-map.md`
10. **L-3 closed** — `## Data Quality Checks` section added to `wiki/aba/05-field-instruments/duplication-gap-analysis-matrix.md`

---

## In Scope

- Adding `type: framework`, `tier: 2`, `status: reference`, `created: [YYYY]`, `updated: 2026-05-11` frontmatter to 32 Tier 2 framework files in `wiki/aba/03-frameworks/`
- Verifying 32 Tier 2 frameworks appear in `wiki/aba/03-frameworks/00_index.md` (Tier 2 section); adding any missing entries
- Deleting `wiki/aba/01-sources/extracted/2010_iasc_meeting-humanitarian-challenges-urban-areas-strategy.md` (underscore duplicate)
- Deleting `wiki/aba/01-sources/raw/2010_iasc_meeting-humanitarian-challenges-urban-areas-strategy.pdf` (underscore duplicate)
- Checking all extracted source files and concept pages for references to the underscore IASC filename; updating to hyphen canonical
- Creating `wiki/aba/outputs/internal/` folder
- Moving `wiki/aba/outputs/wiki-lint-report.md` → `wiki/aba/outputs/internal/lint-report-2026-05-09.md`
- Adding `status:` field to 70 files across: `governance/aba/`, `governance/schema/`, `indexes/`, `templates/`, `sources/`, `wiki/aba/05-field-instruments/` (18 files), `wiki/aba/outputs/`
- Running the wiki lint procedure (from `governance/aba/prompts/lint-wiki.md`) and filing result to `wiki/aba/outputs/internal/lint-report-2026-05-11.md`
- Adding cadence expectation to `governance/review-cadence.md`: weekly lint target, filing path
- Deleting `wiki/aba/01-sources/raw/2021_unhcr_aba-humanitarian-early-recovery.pdf`
- Updating `wiki/aba/01-sources/raw/00_index.md` to mark 2021_unhcr as deleted, note deletion date
- Writing current context into `memory/next-session.md` and `memory/current-handoff.md`
- Adding `used_by_outputs: []` to frontmatter of all 9 Tier 1 frameworks in `wiki/aba/03-frameworks/`
- Adding `maturity: established` to frontmatter of `wiki/aba/02-concepts/concept-cluster-map.md`
- Adding `## Data Quality Checks` section to `wiki/aba/05-field-instruments/duplication-gap-analysis-matrix.md`

## Out of Scope

- H-3: Creating field instruments for 14 tool pages — requires domain expert input
- M-1: Drafting pattern candidates for `11-patterns/` — requires domain expert input
- Any changes to Tier 1 framework content
- Any changes to concept, tool, lifecycle, coordination, or source content beyond the specific frontmatter and field fixes listed
- Extracting content from any PDF
- Automated scheduling of lint runs
- `2026-05-07.md` daily note — leave as-is (not a wiki page)

---

## Constraints

- Vault is a git repo — commit current state before any changes
- The IASC underscore file must be read and compared to the hyphen file before deletion — confirm they are the same source
- `status:` values must be contextually appropriate: `active` for governance/operational docs, `reference` for Tier 2 frameworks, `draft` for field instruments with no validation record, `validated` for instruments with known field use
- `used_by_outputs: []` added as empty list — no outputs currently use these frameworks
- Lint report must follow the format of the existing `lint-report-2026-05-09.md`
- Append-only files (`archive/CHANGELOG.md`, `memory/runtime/logs/log.md`) must NOT be modified

## Dependencies and Access

- Full read/write access to `/Users/eddieargenal/Documents/obsidian-vault/`
- Git available at vault root
- `governance/aba/prompts/lint-wiki.md` — lint procedure reference
- `wiki/aba/outputs/wiki-lint-report.md` — existing lint report (move, don't delete content)
- `wiki/aba/03-frameworks/00_index.md` — must be read before adding Tier 2 index entries

---

## Acceptance Criteria

- [ ] `status:` field present in all 70 currently-non-compliant files (verify via grep)
- [ ] 32 Tier 2 frameworks have frontmatter with at least: `type`, `tier`, `status`, `created`, `updated`
- [ ] `wiki/aba/03-frameworks/00_index.md` Tier 2 section lists all 32 frameworks
- [ ] Only one IASC 2010 extracted file exists (hyphen version); underscore deleted
- [ ] Only one IASC 2010 PDF exists (hyphen version); underscore deleted
- [ ] `wiki/aba/outputs/internal/lint-report-2026-05-09.md` exists (moved from wiki-lint-report.md)
- [ ] `wiki/aba/outputs/wiki-lint-report.md` no longer exists at old path
- [ ] `wiki/aba/outputs/internal/lint-report-2026-05-11.md` exists and is non-empty
- [ ] `governance/review-cadence.md` includes a lint cadence section (weekly target, filing path)
- [ ] `wiki/aba/01-sources/raw/2021_unhcr_aba-humanitarian-early-recovery.pdf` deleted
- [ ] `wiki/aba/01-sources/raw/00_index.md` updated to reflect PDF deletion
- [ ] `memory/next-session.md` and `memory/current-handoff.md` are filled (not blank templates)
- [ ] All 9 Tier 1 frameworks in `wiki/aba/03-frameworks/` have `used_by_outputs: []` in frontmatter
- [ ] `wiki/aba/02-concepts/concept-cluster-map.md` has `maturity:` field
- [ ] `wiki/aba/05-field-instruments/duplication-gap-analysis-matrix.md` has `## Data Quality Checks` section

---

## Risks and Rollback

| Risk | Mitigation |
|---|---|
| IASC underscore and hyphen files have different content | Read both before deleting; if different, merge unique content into hyphen file first |
| Adding wrong status: value to field instruments | Use `draft` as default for any instrument without explicit validation record |
| Lint report format mismatch | Read existing `lint-report-2026-05-09.md` as format template |
| Rollback | Git commit before sprint begins; `git checkout HEAD~1` restores prior state |

---

## Assumptions

- `governance/aba/AGENTS.md` and `governance/aba/CLAUDE.md` get `status: active` (they are operational stubs)
- All `governance/schema/` files get `status: active`
- All `indexes/` files get `status: active`
- All `wiki/aba/05-field-instruments/` files get `status: draft` (no field validation on record)
- `wiki/aba/outputs/toolkits/aba-technical-guide.md` gets `status: draft`
- Tier 2 frameworks get `status: reference` and `tier: 2`
- `created:` year in Tier 2 framework frontmatter derived from the year prefix in the filename (e.g. `2017-` → `created: 2017`)
- The 9 Tier 1 frameworks are: aba-appropriateness-decision, area-selection, neighborhood-diagnosis, area-based-coordination, joint-prioritization, integrated-area-strategy, implementation-adaptation, transition-handover, urban-drr-response-design

---

## Open Questions

None — all decisions captured.

---

## User Approval

Status: pending
