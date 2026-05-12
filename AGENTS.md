---
type: agent-guide
status: active
updated: 2026-05-11
---

# ABA/DRR Field Knowledge Wiki — Agent Operating Guide

## Mission

This wiki is a persistent, compounding operational memory for urban disaster risk reduction and area-based emergency response. Instead of searching a document library at decision time, the LLM incrementally builds and maintains structured synthesis pages that sit between the raw source literature and the operational team. The agent's job is to draft, maintain, and query this wiki — the human validates what matters.

## Architecture

Four layers. Never bypass the synthesis layer to answer a question.

- **Raw sources** — immutable PDFs in `sources/`; LLM reads during ingest only, never modifies
- **Extracted sources** — one LLM-generated structured page per document in `wiki/aba/01-sources/extracted/`; read instead of the PDF on all subsequent queries
- **The wiki** — synthesis layer: concepts (`02-concepts/`), frameworks (`03-frameworks/`), tools (`04-tools/`), field instruments (`05-field-instruments/`), outputs (`outputs/internal/`)
- **Schema** — `AGENTS.md` (this file) + `governance/aba/CLAUDE.md` + `governance/schema/` + `governance/aba/prompts/`

Full operating rules for ABA domain work: `governance/aba/CLAUDE.md` — read it before any domain task.

**File format rule:** ALL vault files must use `.md` extension. No `.txt`, `.csv`, or other formats.

## Query Model

Primary navigation is **frontmatter queries, not wikilink traversal**.

1. Read `indexes/agent-index.md` — identify relevant pages by type, lifecycle_stage, status, and relationships
2. Read only the 3–5 relevant pages
3. Synthesize answer with `source_id` citations
4. If new reusable synthesis emerges, file to `wiki/aba/outputs/internal/` as `type: synthesis`

A page with a missing `lifecycle_stage:` or `contradicts:` field is a **retrieval blackhole** — it will not surface in frontmatter queries, silently.

## Session Protocol

**Open:**
1. Read `memory/current-handoff.md`
2. Read the latest lint report from `wiki/aba/outputs/internal/lint-report-YYYY-MM-DD.md`
3. Clear any CRITICAL/HIGH compliance items before taking on new work
4. Begin assigned task

**Close:**
1. Fill `memory/current-handoff.md` with session summary
2. If schema changed: append to `governance/schema/changelog.md`
3. Run lint checks; file report to `wiki/aba/outputs/internal/lint-report-YYYY-MM-DD.md`
4. Run `scripts/build-index.py` to regenerate `indexes/agent-index.md`
5. Append to `memory/runtime/logs/log.md` using format: `## [YYYY-MM-DD] type | description`

## Promotion Gates

| Promotion | Requirement | Who decides |
|---|---|---|
| Finding → concept page | Appears in ≥2 independent extracted sources | LLM proposes, human approves |
| Concept → Tier 1 framework | Defined decision logic + explicit use conditions | Human approves |
| Tier 1 → linked tool/instrument | Field-applicable scoring criteria + known failure modes | Human approves |
| Tool → validated status | All `field_instruments` linked + `data_quality_checks: true` | Human approves |

**Source independence rule:** Two documents citing the same underlying evaluation are not independent. Verify distinct evidence bases before flagging a promotion.

## Lint Checks

**CRITICAL** — fix before any new work:
- Missing required frontmatter fields per page type (retrieval blackhole)
- `contradicts:` field absent on any source, tool, framework, or concept page
- `field_instruments: []` on any tool with `status: validated`
- `governance/schema/changelog.md` not updated since last schema change

**HIGH** — clear within the session:
- `data_quality_checks: false` on any validated field instrument
- `source_count < 2` on any Tier 1 concept page
- Unresolved contradictions older than 30 days
- Orphan pages with no inbound wikilinks

## Quick Routing

| Task | File |
|---|---|
| Session start | `memory/current-handoff.md` |
| Governance / rule question | `governance/00_governance-index.md` |
| ABA operating rules | `governance/aba/CLAUDE.md` |
| Ingest a source | `governance/aba/prompts/ingest-new-source.md` |
| Query the wiki | `indexes/agent-index.md` → read relevant pages |
| Lint / health check | `governance/aba/prompts/lint-wiki.md` |
| Build page index | `scripts/build-index.py` |
| Session end | `memory/current-handoff.md` (fill) + `memory/runtime/logs/log.md` (append) |

## Vault Structure

```
obsidian-vault/
├── AGENTS.md                    ← vault entry point (this file) — read every session
├── governance/                  ← ALL operational rules, schemas, workflows
│   ├── 00_index.md              ← governance entry point
│   ├── aba/CLAUDE.md            ← ABA operating rules (read for domain work)
│   ├── aba/prompts/             ← operational agent prompts
│   └── schema/                  ← frontmatter schema, lint rules, changelog
├── wiki/aba/                    ← Urban DRR + ABA domain knowledge (13 sections)
│   ├── 01-sources/extracted/    ← extracted source pages (22)
│   ├── 02-concepts/             ← concept pages (25)
│   ├── 03-frameworks/           ← framework pages (41: 9 Tier 1, 32 Tier 2)
│   ├── 04-tools/                ← tool pages (17)
│   ├── 05-field-instruments/    ← field instrument pages (18)
│   └── outputs/internal/        ← lint reports, synthesis outputs
├── scripts/                     ← automation scripts
│   └── build-index.py           ← regenerates indexes/agent-index.md from frontmatter
├── indexes/                     ← generated indexes (do not hand-edit)
│   └── agent-index.md           ← LLM-readable page index — read this first on any query
├── memory/                      ← runtime: handoffs, logs, context
│   ├── current-handoff.md       ← session-to-session continuity
│   └── runtime/logs/log.md      ← append-only operation log
└── sources/                     ← raw source documents (read-only, never modify)
```
