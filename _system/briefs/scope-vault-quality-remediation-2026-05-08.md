# Scope: Vault Quality Remediation — Karpathy Governance Alignment

## Objective
Bring the Obsidian vault at `/Users/eddieargenal/Documents/obsidian-vault` into full compliance with Karpathy-style agentic knowledge management standards by completing all 6 remediation tasks identified in the 2026-05-08 diagnosis. All work must be complete today (2026-05-08).

## Deliverables
1. **wiki/index.md frontmatter cleaned** — single canonical YAML frontmatter block with fields: `type`, `scope`, `status`, `updated`, `title`, `sources`, `tags`. All duplicate/overlapping blocks removed.
2. **wiki/vault-compliance-rules.md created** — mirrors the 10 vault compliance rules from memory, maps them to frontmatter/tagging conventions, cross-linked from diagnosis page.
3. **wiki/workflows/lint.md created** — self-contained on-wiki lint plan: steps, what to check, expected outputs, log destination.
4. **Audit run + log appended** — programmatic scan for broken wikilinks, orphan pages, missing frontmatter fields, stale pages (90+ days); results appended to `memory/runtime/logs/log.md`.
5. **SCHEMA.md link-audit section added** — codifies check-and-log pattern for broken links and orphans; run instructions and log target documented.
6. **Diagnosis page updated** — remediation summary appended, next scheduled diagnostic date set.

## In Scope
- `/Users/eddieargenal/Documents/obsidian-vault/wiki/index.md` — frontmatter consolidation
- `/Users/eddieargenal/Documents/obsidian-vault/wiki/vault-compliance-rules.md` — new file
- `/Users/eddieargenal/Documents/obsidian-vault/wiki/workflows/lint.md` — new file
- `/Users/eddieargenal/Documents/obsidian-vault/SCHEMA.md` — link-audit section addition
- `/Users/eddieargenal/Documents/obsidian-vault/wiki/diagnosis/karpathy-vault-quality-diagnosis-2026-05-08.md` — remediation summary append
- `/Users/eddieargenal/.claude/projects/-Users-eddieargenal/memory/vault-compliance-rules.md` — read-only source for governance rules
- `memory/runtime/logs/log.md` — append-only audit log target
- Vault-wide programmatic scan (wikilinks, frontmatter, staleness)

## Out of Scope
- Obsidian plugin configuration or `.obsidian/` settings changes
- Content rewrites or knowledge restructuring beyond frontmatter fixes
- Any files outside the vault directory
- Memory system changes (memory files are read-only sources, not targets)
- Creating new knowledge pages unrelated to governance/lint

## Constraints
- **Git commit first**: stage a git commit of current state before any file edits
- **Read before edit**: every file must be read before modification
- **Preserve valid content**: fix/extend only; never remove valid existing content
- **Single frontmatter block**: all new and edited pages must have exactly one YAML frontmatter block at the top
- **Log all changes**: append a summary of every file changed to `memory/runtime/logs/log.md`
- **Deadline**: all 6 deliverables complete by end of today (2026-05-08)
- **Follow existing schema**: match existing frontmatter field names and tag conventions exactly

## Dependencies and Access
- Vault path: `/Users/eddieargenal/Documents/obsidian-vault` (git repo, branch: main)
- Governance rules source: `/Users/eddieargenal/.claude/projects/-Users-eddieargenal/memory/vault-compliance-rules.md`
- Audit log target: `memory/runtime/logs/log.md` (relative to vault root, create if missing)
- Diagnosis page: `wiki/diagnosis/karpathy-vault-quality-diagnosis-2026-05-08.md`
- SCHEMA.md: vault root `SCHEMA.md`

## Acceptance Criteria
- [ ] `wiki/index.md` has exactly one YAML frontmatter block with all 6 required fields
- [ ] `wiki/vault-compliance-rules.md` exists, lists all 10 rules, references source, and is cross-linked from the diagnosis page
- [ ] `wiki/workflows/lint.md` exists with step-by-step lint instructions and log destination
- [ ] Audit scan completed; results (counts + lists) appended to `memory/runtime/logs/log.md`
- [ ] `SCHEMA.md` contains a `## Link Audit` (or equivalent) section with run + log instructions
- [ ] Diagnosis page has a `## Remediation Summary` section with date and status of each fix
- [ ] Git commit exists capturing pre-edit state

## Risks and Rollback
- **Frontmatter corruption**: mitigated by git commit before edits; rollback via `git checkout wiki/index.md`
- **Audit false positives**: log results as-is without auto-deleting any flagged pages
- **Missing memory/runtime/logs/ path**: create directory if absent before writing
- **SCHEMA.md conflicts**: read full file first; add section at end if no `Link Audit` section exists

## Assumptions
- The vault's existing frontmatter schema uses the fields: `type`, `scope`, `status`, `updated`, `title`, `sources`, `tags` (will verify by reading SCHEMA.md)
- `memory/vault-compliance-rules.md` contains exactly 10 rules (will verify on read)
- `wiki/workflows/` directory may not exist yet; create it if needed
- Stale threshold is 90 days from today (2026-05-08), meaning pages last updated before 2026-02-07

## Open Questions
- None — all required fields confirmed.

## User Approval
Status: pending
