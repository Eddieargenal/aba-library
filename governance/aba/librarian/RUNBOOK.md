---
type: runbook
title: ABA/DRR Wiki Librarian — Playbook
skill_id: librarian
version: 1.0.0
status: active
created: 2026-05-11
updated: 2026-05-11
sources: [governance/aba/librarian/SKILL.md, AGENTS.md]
tags: [runbook, librarian, wiki, aba, drr, playbook]
---

# ABA/DRR Wiki Librarian — Playbook

Quick reference for running any wiki operation. For full procedure details, see `SKILL.md`.
Invoke with `/librarian [operation] [optional-context]` in a Claude Code session.

---

## Prerequisites

| Requirement | Check |
|---|---|
| Vault root accessible | `ls /Users/eddieargenal/Documents/obsidian-vault/AGENTS.md` |
| Agent index current | `ls indexes/agent-index.md` |
| Python 3 available | `python3 --version` |
| build-index.py present | `ls scripts/build-index.py` |
| Handoff file present | `ls memory/current-handoff.md` |
| Log file present | `ls memory/runtime/logs/log.md` |

---

## Operation Quick Reference

| Operation | When | Produces |
|---|---|---|
| `/librarian open` | Every session start | Loaded context, cleared compliance queue |
| `/librarian close` | Every session end | Filled handoff, lint report, rebuilt index, log entry |
| `/librarian query [question]` | Any domain question | Structured answer with source citations |
| `/librarian ingest [path]` | New document added | Source page wired into wiki, index rebuilt |
| `/librarian extract [pdf]` | New PDF in `wiki/aba/01-sources/raw/` | Extraction page in `wiki/aba/01-sources/extracted/` |
| `/librarian lint` | Weekly + after major changes | Lint report in outputs/ |
| `/librarian build-index` | After any page change | Updated indexes/agent-index.md |
| `/librarian build-concept [name]` | After ingest pass | Concept page in 02-concepts/ |
| `/librarian build-framework [stage]` | Gap in lifecycle coverage | Framework page in 03-frameworks/ |
| `/librarian build-tool [question]` | Framework exists, tool needed | Tool page in 04-tools/ |
| `/librarian build-instrument [tool-id]` | Tool domain lacks instrument | Instrument page in 05-field-instruments/ |
| `/librarian crosslink` | After any build pass | Updated frontmatter + wikilinks across pages |
| `/librarian review-tool [tool-id]` | Before promoting a tool | Tool audit report in outputs/internal/ |
| `/librarian promote [slug]` | Page may be ready for next gate | Promotion report, status update if eligible |

---

## Common Workflows

### New source document arrives
```
/librarian extract [path-to-pdf]
/librarian ingest [path-to-extracted-page]
/librarian build-concept              ← if new concepts emerge
/librarian crosslink                  ← wire new pages together
/librarian build-index                ← always last
```

### Weekly maintenance session
```
/librarian open                       ← loads handoff + clears lint queue
[do assigned work]
/librarian close                      ← lint + rebuild index + fill handoff + log
```

### Build a new lifecycle stage tool from scratch
```
/librarian build-framework [stage]    ← requires ≥2 ingested sources first
/librarian build-tool [decision-question]
/librarian build-instrument [tool-id] ← repeat per decision domain
/librarian crosslink
/librarian review-tool [tool-id]      ← quality gate before use
/librarian build-index
```

### Promote a concept to active status
```
/librarian promote [concept-slug]     ← checks source_count, independence, tensions
[human reviews and approves]
/librarian crosslink                  ← update related pages
/librarian build-index
```

### Answer a field team question
```
/librarian query [question]           ← frontmatter query → 3–5 pages → structured answer
```
Output is filed to `outputs/` as type: synthesis if reusable.

---

## Promotion Gates (go/no-go)

| Gate | Minimum requirement | Who approves |
|---|---|---|
| Finding → concept page | source_count ≥ 2, independent sources, known_tensions set | LLM proposes, human approves |
| Concept → Tier 1 framework | Decision logic explicit, use conditions defined, failure modes listed | Human approves |
| Framework → linked tool | Scoring criteria + failure modes in framework body | Human approves |
| Tool draft → validated | All field_instruments linked, data_quality_checks: true on all | Human approves |

**Independence rule**: Two reports from the same underlying field evaluation are not independent sources.

---

## Lint Severity Reference

| Severity | Finding | Action |
|---|---|---|
| CRITICAL | Missing required frontmatter field | Fix before any new work |
| CRITICAL | `contradicts:` field absent (not `[]` — absent) | Fix before any new work |
| CRITICAL | Tool validated with no field_instruments | Fix before any new work |
| CRITICAL | Schema changelog not updated after schema change | Fix before any new work |
| HIGH | `data_quality_checks: false` on validated instrument | Fix this session |
| HIGH | Established/contested concept with source_count < 2 | Fix this session |
| HIGH | Unresolved contradiction > 30 days old | Escalate to human |
| HIGH | Tool page with empty field_instruments (any status) | Defer only with explicit reason |
| MEDIUM | Orphan page (no inbound wikilinks) | Fix next crosslink pass |

---

## Controlled Vocabulary

**`lifecycle_stage`** slugs:
`appropriateness-decision` · `area-selection` · `neighbourhood-diagnosis` · `joint-prioritization` · `coordination-design` · `integrated-area-strategy` · `implementation-adaptation` · `monitoring-learning` · `transition-handover`

**`source_type`**: `iasc-guidance` · `ifrc-framework` · `un-policy` · `academic` · `field-evaluation` · `ngo-guidance` · `government-policy`

**`confidence`**: `high` (direct field evidence) · `medium` (practitioner judgment) · `low` (theoretical)

**`maturity`**: `emerging` · `established` · `contested`

**`status` (editorial)**: `draft` · `active` · `archived` · `superseded` · `reference`

**`format` (instruments)**: `form` · `checklist` · `guide` · `matrix` · `survey` · `dashboard`

---

## Session Log Format

All log entries in `memory/runtime/logs/log.md` use:
```
## [YYYY-MM-DD] type | brief description
- key action
- files changed: [list]
```
Where `type` is: `ingest` · `query` · `lint` · `schema` · `maintenance`

---

## Key Go/No-Go Checks Before New Work

- [ ] Handoff loaded (`memory/current-handoff.md` read)
- [ ] Latest lint report reviewed
- [ ] All CRITICAL findings resolved
- [ ] HIGH findings resolved or explicitly deferred
- [ ] `indexes/agent-index.md` is current (run `build-index` if pages changed last session)

---

## Key Go/No-Go Checks at Session Close

- [ ] `memory/current-handoff.md` filled with session summary
- [ ] Schema changelog updated if any frontmatter field changed
- [ ] Lint report filed to `outputs/lint-report-YYYY-MM-DD.md`
- [ ] `scripts/build-index.py` run — count confirmed
- [ ] Log entry appended to `memory/runtime/logs/log.md`
