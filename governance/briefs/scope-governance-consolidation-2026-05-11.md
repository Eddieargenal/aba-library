# Scope: Governance Consolidation

## Objective

Centralize every document containing directions on how to access, maintain, scale, or de-scale the vault into `governance/`. Eliminate duplicates. Break compound documents into single-topic sub-documents. Add a `00_index.md` to each section so agents navigate via indexes rather than loading full files. Replace four redundant root nav files with a single lightweight root `AGENTS.md`.

Done looks like: one canonical location for all operational rules, zero duplicate rules, every section discoverable via its own index, and a root entry point that routes agents into the right section index.

---

## Deliverables

1. Root `AGENTS.md` — replaces `00_Start_Here.md`, `QUICK.md`, `README.md`, `SCHEMA.md`, `architecture.md`
2. `governance/00_index.md` — top-level governance index
3. `governance/compliance-rules.md` — the 10 vault rules (authoritative, single copy)
4. `governance/governance-model.md` — principle, federated model, roles & authority, metrics dashboard (split from `library-governance_guide.md`)
5. `governance/content-lifecycle.md` — lifecycle states, schema change control, pattern governance (split from `library-governance_guide.md`)
6. `governance/evidence-promotion.md` — field finding → pattern → concept promotion path (split from `library-governance_guide.md`)
7. `governance/output-provenance.md` — external vs internal output standards, reverse dependency tracking (split from `library-governance_guide.md`)
8. `governance/review-cadence.md` — weekly/quarterly/annual schedule + governance metrics (split from `library-governance_guide.md`)
9. `governance/memory-rules.md` — memory category rules, stale thresholds (moved from `memory/memory-rules.md`)
10. `governance/schema/` — all 8 schema docs moved from root `schema/`, plus new `00_index.md` and `changelog.md`
11. `governance/workflows/` — all vault-level workflow docs moved from root `workflows/`, plus new `00_index.md`
12. `governance/aba/` — ABA-specific operational docs moved from `wiki/aba/`, plus new `00_index.md`
13. All broken references updated in files that linked to moved locations

---

## In Scope

- Moving `schema/` folder contents → `governance/schema/`
- Moving vault-level `workflows/` folder contents → `governance/workflows/`
- Moving `memory/vault-compliance-rules.md` → `governance/compliance-rules.md`
- Moving `memory/memory-rules.md` → `governance/memory-rules.md`
- Moving `wiki/aba/AGENTS.md` → `governance/aba/AGENTS.md`
- Moving `wiki/aba/CLAUDE.md` → `governance/aba/CLAUDE.md`
- Moving `wiki/aba/00-overview/agent-contract.md` → `governance/aba/agent-contract.md`
- Moving `wiki/aba/00-overview/agent-operating-model.md` → `governance/aba/agent-operating-model.md`
- Moving `wiki/aba/00-overview/how-to-use-this-wiki.md` → `governance/aba/how-to-use-this-wiki.md`
- Moving `wiki/aba/13-agent-prompts/` → `governance/aba/prompts/`
- Moving `wiki/workflows/lint-plan.md` → `governance/workflows/lint-plan.md`
- Splitting `governance/library-governance_guide.md` into 5 single-topic sub-documents
- Creating `governance/schema/changelog.md` (was missing — critical gap)
- Creating `00_index.md` in `governance/`, `governance/schema/`, `governance/workflows/`, `governance/aba/`
- Creating root `AGENTS.md` (new single entry point)
- Deleting: `memory/governance.md`, `wiki/vault-compliance-rules.md`, `SCHEMA.md`, `library-architecture.md`, `00_Start_Here.md`, `QUICK.md`, `README.md`, `architecture.md`, `governance/library-governance_guide.md` (replaced by splits)
- Updating all internal references/links in remaining files that pointed to moved locations
- Deconflicting the 4 copies of the 10 compliance rules into 1

## Out of Scope

- ABA domain content (concepts, frameworks, tools, sources, field instruments, lifecycle, sector-apps, coordination, monitoring, transition, risks) — no changes to `wiki/aba/02-*` through `wiki/aba/12-*`
- `wiki/aba/00-overview/00_index.md` and `wiki/aba/00-overview/urban-drr-aba-knowledge-map.md` — stay in wiki/aba/00-overview/ (domain overview, not ops docs)
- `agents/`, `tools/`, `prompts/`, `templates/`, `indexes/`, `sources/`, `memory/categories/`, `memory/runtime/` — not operational governance docs
- `archive/` — append-only, no changes
- Odoo, Lebanon NLP, or other project workflows not related to vault governance

---

## Constraints

- Vault is a local git repo — git commit required before any file moves
- No files may be deleted without their content either merged into a surviving file or confirmed as pure duplicate
- `governance/library-governance_guide.md` must be fully decomposed — no content loss during split
- `odoo-accounting.md` and `coding-tasks.md` in `workflows/` are domain workflows — move them to `governance/workflows/` per user direction but flag them as candidates for future domain-specific folders
- CLAUDE.md move is a behavioral risk (see Risks)

---

## Dependencies and Access

- Full read/write access to `/Users/eddieargenal/Documents/obsidian-vault/`
- Git available at vault root
- Complete inventory of 38 operational docs (already done)
- Full content of `library-governance_guide.md` required for split (353 lines, read in full)

---

## Acceptance Criteria

- [ ] All 38 operational docs are under `governance/` or are deleted as confirmed duplicates
- [ ] Zero files with operational rules exist outside `governance/` (except root `AGENTS.md` and wiki/aba/ domain content indexes)
- [ ] The 10 compliance rules exist in exactly one file: `governance/compliance-rules.md`
- [ ] `governance/library-governance_guide.md` is deleted; its 5 successor docs exist and contain all original content
- [ ] Every section under `governance/` has a `00_index.md`
- [ ] `governance/schema/changelog.md` exists and contains at least the initial schema creation event
- [ ] Root `AGENTS.md` exists; `00_Start_Here.md`, `QUICK.md`, `README.md`, `SCHEMA.md`, `architecture.md`, `library-architecture.md` are deleted
- [ ] No broken wikilinks remain in files that previously linked to moved locations
- [ ] Git snapshot commit exists before any changes

---

## Risks and Rollback

| Risk | Mitigation |
|---|---|
| `wiki/aba/CLAUDE.md` auto-loaded by Claude Code from `wiki/aba/` — moving it breaks automatic loading | Leave a thin stub `wiki/aba/CLAUDE.md` pointing to `governance/aba/CLAUDE.md` after move |
| Same risk for `wiki/aba/AGENTS.md` | Same stub pattern |
| Content loss during `library-governance_guide.md` split | Split docs must collectively contain 100% of original content; verify line count |
| Broken links in wiki pages that reference moved schema/workflow paths | Grep all `.md` files for old paths before deletion; update or stub |
| Rollback | Git commit before first file move; `git checkout HEAD~1` restores full prior state |

---

## Assumptions

- `odoo-accounting.md` and `coding-tasks.md` move to `governance/workflows/` now; may be relocated to a future domain-specific folder later
- `memory/context.md`, `memory/current-handoff.md`, `memory/next-session.md`, `memory/categories/` stay in `memory/` — they are runtime state, not policy
- `wiki/aba/00-overview/00_index.md` stays in wiki/aba/ — it is a domain content index, not an ops doc
- Mermaid diagrams from `architecture.md` are folded into `governance/governance-model.md`
- `governance/vault-quality-remediation/` and `governance/briefs/` stay where they are (already correctly placed)

---

## Open Questions

None — all decisions captured from user intake.

---

## User Approval

Status: pending
