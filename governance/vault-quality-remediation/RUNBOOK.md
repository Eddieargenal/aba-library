---
type: runbook
title: Vault Quality Remediation — Team Runbook
version: 1.1.0
status: validated
updated: 2026-05-08
tags: ['governance', 'remediation', 'runbook', 'team']
sources: ['governance/vault-quality-remediation/SKILL.md', 'wiki/workflows/lint-plan.md']
---

# Vault Quality Remediation — Team Runbook

Quick reference for running a governance remediation pass on the Karpathy llm-wiki vault. Follow SKILL.md for full step details; use this page for fast orientation and go/no-go checks.

---

## Prerequisites

| Requirement | Check |
|---|---|
| Git access to vault repo | `git status` returns no error |
| Vault root confirmed | `ls SCHEMA.md wiki/index.md` both exist |
| `memory/vault-compliance-rules.md` present | `ls memory/vault-compliance-rules.md` |
| `memory/runtime/logs/log.md` present | `ls memory/runtime/logs/log.md` |
| Active diagnosis page exists | `ls wiki/diagnosis/` |
| No in-progress merge or rebase | `git status` shows clean working tree or only tracked changes |

If any prerequisite fails, stop and resolve before continuing.

---

## Quick Start (6 commands)

```bash
# 1. Snapshot
git add -A && git commit -m "chore: pre-remediation snapshot $(date +%Y-%m-%d)"

# 2. Verify wiki/index.md frontmatter
head -12 wiki/index.md

# 3. Check vault-compliance-rules page
ls wiki/vault-compliance-rules.md && grep -c "^[0-9]*)" wiki/vault-compliance-rules.md

# 4. Check lint plan page
ls wiki/workflows/lint-plan.md

# 5. Check SCHEMA.md link-audit section
grep -n "Link Audit" SCHEMA.md

# 6. Tail log for last audit entry
tail -20 memory/runtime/logs/log.md
```

If all checks pass, the vault is already compliant — run Step 6 (audit scan) and update the diagnosis page, then you're done.

---

## Step-by-Step Execution

### Step 1 — Git snapshot
```bash
git add -A
git commit -m "chore: pre-remediation snapshot $(date +%Y-%m-%d)"
```
**Go criteria**: commit succeeds, `git log --oneline -1` shows the snapshot.

---

### Step 2 — Consolidate wiki/index.md frontmatter
Read the file. If lines before `# Wiki Index` contain more than one `---` pair, collapse to one canonical block:

```yaml
---
type: audit-catalog
scope: wiki-master
status: validated
updated: <today>
title: Wiki Index
sources: ['wiki/index.md']
tags: ['wiki', 'index', 'governance']
---
```

Also fix any `||` table-row corruption → `|`.

**Go criteria**: `head -12 wiki/index.md` shows one `---` open, one `---` close, then `# Wiki Index`.

**Failure mode**: File is locked or binary. Check for Obsidian sync conflicts (`.md.sync-conflict-*` files).

---

### Step 3 — Publish vault-compliance-rules on-wiki
If `wiki/vault-compliance-rules.md` is absent, create it mirroring `memory/vault-compliance-rules.md` (read-only source). If it exists, verify 10 rules and cross-links.

**Go criteria**: `grep -c "^[0-9]*)" wiki/vault-compliance-rules.md` returns `10`. File has `[[index]]` and `[[../SCHEMA]]` cross-links.

**Failure mode**: memory/vault-compliance-rules.md is missing. Stop — escalate to vault owner. Do not create rules from memory.

---

### Step 4 — Publish lint plan on-wiki
If `wiki/workflows/lint-plan.md` is absent, create `wiki/workflows/` directory and the file. If it exists, verify frontmatter and cross-links.

Required frontmatter fields: `type`, `status`, `updated`, `title`, `sources`, `tags`.
Required cross-links: `[[../index]]`, `[[../../SCHEMA]]`, `[[../../workflows/lint]]`, `[[../vault-compliance-rules]]`.

**Go criteria**: file exists, `status: validated`, numbered checks present, log destination stated.

---

### Step 5 — Add Link Audit section to SCHEMA.md
If `grep -n "Link Audit" SCHEMA.md` returns nothing, append the `## Link Audit` section per SKILL.md Step 5.

**Go criteria**: `grep -n "Link Audit" SCHEMA.md` returns a line number.

**Failure mode**: SCHEMA.md already has a partial `## Link Audit` section. Read the full section first; extend, do not duplicate.

---

### Step 6 — Run audit and append log
Run the four checks (broken wikilinks, orphans, missing frontmatter, stale pages). Append one structured entry to `memory/runtime/logs/log.md`.

Log format:
```
## [YYYY-MM-DD] lint | vault-wide audit
- Broken wikilinks: N — [list or "none"]
- Orphan pages: N — [list or "none"]
- Missing frontmatter: N — [list]
- Stale pages: N — [list]
- Issues found: N
- Logged to unresolved: yes/no
```

**Go criteria**: `tail -30 memory/runtime/logs/log.md` shows today's lint entry.

**Failure mode**: `log.md` does not exist. Create it with `mkdir -p memory/runtime/logs && touch memory/runtime/logs/log.md`, then append.

---

### Step 7 — Update diagnosis page
Append `## Remediation Summary` to the active diagnosis page. Include:
- Status table (all 6 tasks)
- Outstanding items
- Next diagnostic date (30 days from today)
- Update `status:` to `validated` and `updated:` to today

**Go criteria**: `grep "Remediation Summary" wiki/diagnosis/<active-diagnosis>.md` returns a result.

---

### Step 8 — Register new pages in wiki/index.md
Add Governance and Diagnosis sections to `wiki/index.md` if absent. Register:
- `[[vault-compliance-rules]]`
- `[[workflows/lint-plan]]`
- New diagnosis/audit pages

**Go criteria**: `grep "vault-compliance-rules" wiki/index.md` and `grep "workflows/lint-plan" wiki/index.md` both return results.

---

### Step 9 — Final commit
```bash
git add wiki/ SCHEMA.md memory/runtime/logs/log.md governance/
git commit -m "feat: vault governance remediation $(date +%Y-%m-%d)"
```

---

## Outputs to Verify

| Output | Location | Check |
|---|---|---|
| Pre-edit snapshot | git log | `git log --oneline -2` shows snapshot |
| Clean index frontmatter | `wiki/index.md` | Single `---` block, no `\|\|` rows |
| Governance reference | `wiki/vault-compliance-rules.md` | 10 rules, cross-linked |
| Lint plan | `wiki/workflows/lint-plan.md` | Steps + log destination |
| SCHEMA link-audit | `SCHEMA.md` | `## Link Audit` section present |
| Audit log entry | `memory/runtime/logs/log.md` | Today's lint entry |
| Diagnosis updated | `wiki/diagnosis/<date>.md` | `## Remediation Summary` present |
| Index updated | `wiki/index.md` | Governance + Diagnosis sections |

---

## Cadence

| Event | Trigger | Owner |
|---|---|---|
| Full remediation pass | After any vault quality diagnosis | Vault maintainer |
| Audit scan only (Step 6) | Monthly or after major ingest | Any team member |
| Diagnosis page review | 30 days after last pass | Vault maintainer |

**Next scheduled diagnostic**: 2026-06-08

---

## Failure Modes and Mitigations

| Failure | Cause | Mitigation |
|---|---|---|
| Frontmatter corruption | Edit made without reading first | `git checkout wiki/index.md` to restore |
| Duplicate log entries | Appended twice | Log is append-only — duplicates are benign; add a note |
| 10-rule mismatch | Source file updated | Re-read `memory/vault-compliance-rules.md`; update wiki mirror |
| SCHEMA edit conflict | Simultaneous edits | Read full SCHEMA.md first; resolve manually |
| Audit false positives (wikilinks) | Obsidian resolves relative paths differently | Log as-is; never auto-delete flagged pages |

---

See also: [[SKILL]] · [[../../wiki/vault-compliance-rules]] · [[../../wiki/workflows/lint-plan]] · [[../../SCHEMA]]
