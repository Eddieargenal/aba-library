# Routing record — S-youngfoundation2010

Re-route pass under the #7 by-path, action-branched contract. Targets read from
frontmatter `findings[].candidate_target_pages` (parsed via the real YAML loader).
PU- stubs are **auto-seeded drafts** (claim text verbatim from the source's body
`#findings` prose; sections to be synthesised) — **pending Gate B**. No wiki page
or the source integration map was edited.

## Outcome — 18 findings
| Bucket | Count | Findings |
|--------|-------|----------|
| `create-*` → PU- stub | 12 | F-002, F-003, F-004, F-006, F-008, F-009, F-010, F-011, F-012, F-013, F-014, F-015 |
| `enrich-*` **blocked** (target missing) | 3 | F-001, F-005, F-007 |
| `source_only` no-op | 3 | F-016, F-017, F-018 |

Before #7 all 18 would have escalated to `flag-for-review`.

## Blocked enrichments — foundational pages not yet created
| Finding | Target (missing) |
|---------|------------------|
| F-001 | `wiki/aba/02-concepts/neighbourhood-concept.md` |
| F-005 | `wiki/aba/02-concepts/neighbourhood-boundaries.md` |
| F-007 | `wiki/aba/04-tools/neighbourhood-boundary-definition-tool.md` |

These are core pages multiple sources will want to enrich — they should be created (promoted from a `create-*` proposal) **before** the enrich findings can route. Same create-before-enrich ordering nuance seen in Twigg (F-003).

## Gate B packet
- **12 PU- stubs** (auto-seeded) — paths under `outputs/proposed-library-updates/`.
- **human_review_required:** F-002 (`create-framework` — a foundational three-lens framework that "could conflict with or supersede related concept pages"; the source itself flagged it for verification before creation).
- **flag-for-review (blocked enrich):** F-001, F-005, F-007.

## Behavioural observations (this is the "how it behaves" part)
1. **Target-folder taxonomy is inconsistent across sources.** YF routes tools to `04-tools/` and decision-rules to `09-decision-protocols/` (both exist). **Twigg routed to `03-tasks/` and `04-decision-rules/`, which do not exist in the wiki.** Routing-by-path works regardless, but promotion will need a folder-normalisation step, and any enrich pointing at a non-canonical folder will never resolve.
2. **New type appeared:** `create-framework` (F-002, F-006) — absent from Twigg. The framework template routed correctly.
3. **Auto-seeding is lower-fidelity than hand-routing.** These 12 are seeded skeletons (verbatim claim + scaffold), versus Twigg's hand-synthesised stubs. A seeder bug (matching a terse summary occurrence of the finding id instead of the prose claim) was caught and fixed by restricting extraction to the `#findings` section.

## Follow-up candidates
- **Folder-taxonomy normalisation** across extracted sources' `candidate_target_pages` (real, verified — unlike the withdrawn #14).
- Promote the 3 foundational concept/tool pages first to unblock the enrich findings.
