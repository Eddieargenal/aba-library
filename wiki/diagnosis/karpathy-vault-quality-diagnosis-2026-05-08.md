---
type: diagnosis
status: validated
updated: 2026-05-08
title: Karpathy llm-wiki vault quality diagnosis
sources: ['wiki/index.md', 'SCHEMA.md', 'memory/vault-compliance-rules.md']
tags: ['wiki', 'quality', 'audit', 'karpathy', 'governance']
---

# Executive summary
This diagnostic assesses the quality and governance of the Obsidian wiki vault used by the Karpathy-style llm-wiki skill. Key issues observed:
- Frontmatter consistency: several pages (notably wiki/index.md) exhibit multiple overlapping or duplicated frontmatter blocks, risking parsing errors and governance drift.
- Compliance mapping: the vault defines a set of governance rules (vault-compliance-rules.md) in memory; the wiki itself should explicitly expose and reference these rules or embed a formal mirror in the wiki as a canonical reference.
- Page health signals: lint/audit workflows exist in the vault, but consistent enforcement and auto-remediation are not described in the wiki's own workflow pages.

# Findings by category
- Frontmatter hygiene
  - wiki/index.md currently contains duplicated frontmatter and inconsistent keys. This undermines tooling that relies on frontmatter (e.g., taxonomy checks, search filtering).
  - Recommended fix: unify to a single frontmatter block with required keys: type, scope, status, updated, title, sources, tags.
- Governance visibility
  - Vault rules exist in memory (memory/vault-compliance-rules.md) but are not mirrored in wiki/index.md as a canonical governance reference. This makes it hard for editors to ensure new content complies.
  - Recommended fix: add a wiki page vault-compliance-rules.md (or reference) and ensure all new pages cite the wiki's governance rules.
- Audit & lint coverage in the wiki
  - The wiki contains a lint workflow description but lacks a ready-to-run, self-contained, page-level lint script or a clear on-wiki execution plan.
  - Recommended fix: include a self-contained lint plan page (prompts/workflows) that can be invoked by the agent to produce a structured issue report.
- Cross-link integrity
  - The wiki currently references many pages via wikilinks; a programmatic check for broken links and orphan pages is recommended and should be codified in SCHEMA.md.
  - Recommended fix: run periodic in-repo link audits and log results in memory/runtime/logs or wiki log.

# Immediate action plan (0-24h)
1) Normalize wiki/index.md frontmatter to a single, correct block and ensure required fields exist.
2) Create or mirror a canonical wiki vault-compliance-rules page referencing memory/vault-compliance-rules.md and embedding the 10 rules as a reference block.
3) Add a new on-wiki lint plan page that describes how the lint passes operate and how results are logged (to memory/runtime/logs/log.md).
4) Run a first-pass audit (list orphan pages, broken links, missing citations) and summarize results in a new on-wiki diagnosis page.

# Proposed governance alignment
- Adopt the 10 vault compliance rules as the canonical standard for the wiki, wired to wiki content through [sources] and [claims] tag conventions.
- Use a single, machine-parseable frontmatter schema for all pages: type, status, updated, title, sources, tags, scope, and optionally citations and risk signals.
- Ensure all new pages are cross-linked to at least two other pages and appended to wiki/index.md.

# Acceptance criteria for completion
- wiki/index.md contains a single, valid frontmatter block with required fields.
- A new vault-compliance-rules page exists in wiki space and links to the canonical memory rules.
- A wiki lint page exists detailing steps and a sample lint report format.
- A diagnosis page exists with a concrete remediation plan and next steps.
---

## Remediation Summary

Remediation completed: 2026-05-08

| # | Task | Status |
|---|------|--------|
| 1 | `wiki/index.md` frontmatter consolidated to single canonical block; `||` table corruption fixed; new pages added to index | ✅ Done |
| 2 | `wiki/vault-compliance-rules.md` created — 10 rules, cross-linked from index and SCHEMA.md | ✅ Done |
| 3 | `wiki/workflows/lint-plan.md` created — 10-step lint routine, output template, log destination | ✅ Done |
| 4 | Vault-wide audit run — broken wikilinks (65 for manual review), orphans (0), missing frontmatter (2 pages), stale pages (0); results appended to `memory/runtime/logs/log.md` | ✅ Done |
| 5 | `SCHEMA.md` `## Link Audit` section added with check descriptions, bash examples, and log format | ✅ Done |
| 6 | This diagnosis page updated with remediation summary | ✅ Done |

### Outstanding items from audit
- 2 pages missing frontmatter (`memory/categories/outcomes.md`, `memory/categories/procedures.md`) — add `type:`, `status:`, `updated:` fields
- 65 wikilinks flagged for manual verification (many resolve in Obsidian; priority: `../archive/CHANGELOG`, `../memory/governance`, `../memory/categories/behavioral/pending/projects/tools`)

Next scheduled diagnostic: **2026-06-08** (30-day follow-up)

References: [[../vault-compliance-rules]] · [[../workflows/lint-plan]] · [[../../SCHEMA]]
