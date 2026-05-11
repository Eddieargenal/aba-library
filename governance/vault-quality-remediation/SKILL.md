---
type: skill
title: Vault Quality Remediation
version: 1.1.0
status: superseded
updated: 2026-05-11
superseded_by: governance/00_index.md
superseded_date: 2026-05-11
superseded_note: describes 2026-05-08 remediation sprint — vault structure consolidated 2026-05-11
tags: ['governance', 'remediation', 'lint', 'karpathy', 'skill']
dependencies:
  - SCHEMA.md
  - memory/vault-compliance-rules.md
  - wiki/index.md
  - wiki/vault-compliance-rules.md
  - wiki/workflows/lint-plan.md
  - memory/runtime/logs/log.md
---
1
# Skill: Vault Quality Remediation

Reusable skill to execute a remediation pass for a Karpathy-style llm-wiki vault. Idempotent — safe to re-run; all writes are additive or replace broken content with valid content. All changes are logged to `memory/runtime/logs/log.md`.

## When to use

- After a vault quality diagnosis flags structural or governance issues
- When `wiki/index.md` shows duplicated or malformed frontmatter
- When governance rules are not mirrored on-wiki
- When a lint workflow page is missing or incomplete
- After any major vault restructure

---

## Step 1: Pre-edit Git Snapshot

**Goal**: capture vault state before any edits so every change is reversible.

```bash
cd <vault-root>
git add -A
git commit -m "chore: pre-remediation snapshot $(date +%Y-%m-%d)"
```

Rollback any single file: `git checkout wiki/index.md`

---

## Step 2: Consolidate wiki/index.md Frontmatter

**Goal**: ensure exactly one YAML frontmatter block at the top.

Required fields:
```yaml
---
type: audit-catalog
scope: wiki-master
status: validated
updated: <YYYY-MM-DD>
title: Wiki Index
sources: ['wiki/index.md']
tags: ['wiki', 'index', 'governance']
---
```

Rules:
- Read the full file first
- Remove any duplicate or orphaned frontmatter blocks
- Fix `||` table-row corruption → `|`
- Update `updated:` to today's date
- Preserve all existing content below the frontmatter block

Validation: `head -12 wiki/index.md` must show exactly one opening `---` and one closing `---` before the `# Wiki Index` heading.

---

## Step 3: Publish On-Wiki Governance Reference

**Goal**: create or verify `wiki/vault-compliance-rules.md` mirrors all 10 rules from `memory/vault-compliance-rules.md`.

Required frontmatter:
```yaml
---
type: memory
status: validated
updated: <YYYY-MM-DD>
title: Vault Compliance Rules (On-Wiki Canonical Reference)
sources: ['memory/vault-compliance-rules.md']
tags: ['governance', 'rules', 'compliance']
---
```

Rules:
- Source is read-only: `memory/vault-compliance-rules.md`
- Must list all 10 rules (numbered, with summary)
- Must include cross-links: `[[index]]`, `[[../SCHEMA]]`, `[[workflows/lint-plan]]`
- Must be registered in `wiki/index.md` under a Governance section

Validation: `grep -c "^[0-9]*)" wiki/vault-compliance-rules.md` returns 10.

---

## Step 4: Publish On-Wiki Lint Plan

**Goal**: create or verify `wiki/workflows/lint-plan.md` as a self-contained, runnable lint reference.

Required frontmatter:
```yaml
---
type: workflow
status: validated
updated: <YYYY-MM-DD>
title: Wiki Lint Plan
sources: ['workflows/lint.md', 'SCHEMA.md']
tags: ['lint', 'workflow', 'governance']
---
```

Required content:
- Inputs (wiki/index.md, log.md, memory/categories/, SCHEMA.md)
- Numbered checks (frontmatter, broken links, orphans, stale pages, cross-link health, source drift, log hygiene, governance traceability)
- Output template (lint report format)
- Run cadence (per-ingest + monthly)
- Log destination: `memory/runtime/logs/log.md`
- Cross-links: `[[../index]]`, `[[../../SCHEMA]]`, `[[../../workflows/lint]]`, `[[../vault-compliance-rules]]`

Create `wiki/workflows/` directory if absent: `mkdir -p wiki/workflows`

---

## Step 5: Add Link-Audit Section to SCHEMA.md

**Goal**: codify the check-and-log pattern for broken links, orphans, and missing frontmatter in SCHEMA.md.

Append after `## Governance Reference`:

Section heading: `## Link Audit`

Required subsections:
- `### What to check` — broken wikilinks, orphans, missing frontmatter, stale pages
- `### How to run` — bash commands for each check
- `### Log target` — log format referencing `memory/runtime/logs/log.md`
- Reference: `[[wiki/workflows/lint-plan]]`

Validation: `grep -n "Link Audit" SCHEMA.md` returns a line number.

---

## Step 6: Run Audit and Append Log

**Goal**: programmatic scan of vault; append structured results to `memory/runtime/logs/log.md`.

Checks to run (exclude `sources/`, `.obsidian/`, `_system/`, `archive/`):

```bash
# Missing required frontmatter (type/status/updated)
grep -rL "^type:" --include="*.md" wiki/ memory/categories/ workflows/ tools/ agents/ prompts/

# Stale pages (updated before threshold — 90 days)
# Threshold = today minus 90 days

# Broken wikilinks (extract [[targets]], check file existence)
grep -roh "\[\[[^\]]*\]\]" --include="*.md" wiki/ | sed 's/.*\[\[//;s/\]\].*//' | sort -u

# Orphan pages (not linked from any other .md)
# For each .md in wiki/ and memory/categories/, check if any other file links to it
```

Log format to append:
```
## [YYYY-MM-DD] lint | vault-wide audit
- Broken wikilinks: N — [list or "none"]
- Orphan pages: N — [list or "none"]
- Missing frontmatter: N — [list]
- Stale pages: N — [list]
- Issues found: N
- Logged to unresolved: yes/no
```

Note: never overwrite `log.md` — append only.

---

## Step 7: Update Diagnosis Page

**Goal**: append `## Remediation Summary` to the active diagnosis page.

Required content:
- Table of all 6 tasks with ✅/❌ status
- Outstanding items from audit
- Next scheduled diagnostic date (30 days from today)
- Cross-links: `[[../vault-compliance-rules]]`, `[[../workflows/lint-plan]]`, `[[../../SCHEMA]]`

Update frontmatter `status:` to `validated` and `updated:` to today.

---

## Step 8: Update wiki/index.md Index Tables

**Goal**: register new pages in wiki/index.md so they are not orphans.

Add a `## Governance` section (if absent) with rows for:
- `[[vault-compliance-rules]]`
- `[[workflows/lint-plan]]`

Add a `## Diagnosis & Audit` section with rows for any new diagnosis/audit pages.

Update `updated:` in frontmatter to today.

---

## Acceptance Criteria

- [ ] `git log --oneline -1` shows pre-remediation snapshot
- [ ] `head -12 wiki/index.md` shows exactly one frontmatter block
- [ ] `grep -c "^[0-9]*)" wiki/vault-compliance-rules.md` returns 10
- [ ] `wiki/workflows/lint-plan.md` exists with numbered steps and log destination
- [ ] `grep -n "Link Audit" SCHEMA.md` returns a result
- [ ] `tail -30 memory/runtime/logs/log.md` shows a lint entry dated today
- [ ] Active diagnosis page has `## Remediation Summary` section
- [ ] `grep "vault-compliance-rules" wiki/index.md` returns a result

---

## Idempotency Notes

- Frontmatter consolidation: read first — if already a single block, skip
- vault-compliance-rules.md: if exists and has 10 rules, skip creation; add missing cross-links only
- lint-plan.md: if exists, verify frontmatter completeness and cross-links; extend if needed
- SCHEMA.md link-audit: if `## Link Audit` section already exists, skip
- Log: always append — never check for existing entries before appending

---

See also: [[../../wiki/vault-compliance-rules]] · [[../../wiki/workflows/lint-plan]] · [[../../SCHEMA]] · [[../../wiki/index]]
