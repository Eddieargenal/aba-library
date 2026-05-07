---
type: schema
version: 1.0.0
updated: 2026-05-07
---

# Vault Schema

**Read this file before performing any wiki operation.** It is the authoritative LLM instruction document for this vault — it defines the three layers, three operations, special files, and all content conventions.

---

## Three-Layer Architecture

| Layer | Location | Rule |
|-------|----------|------|
| **Sources** | `sources/` | Raw documents. Read only. Never edit. |
| **Wiki** | `memory/`, `workflows/`, `tools/`, `agents/`, `prompts/` | LLM-maintained knowledge pages. |
| **Schema** | `SCHEMA.md`, `vault-compliance-rules.md` | Conventions and structure definitions. |

---

## Special Files

| File | Purpose | Rule |
|------|---------|------|
| `wiki/index.md` | Master catalog of all wiki pages | Read first on every query. Update after every ingest. |
| `memory/runtime/logs/log.md` | Append-only operation timeline | Append after every ingest, query that produces new knowledge, and lint. |
| `00_Start_Here.md` | Agent entry point and routing table | Start here when navigating the vault. |
| `SCHEMA.md` | This file — LLM instruction document | Read before any wiki operation. |

---

## Three Operations

### 1. Ingest — Add new knowledge from a source document
Full procedure: [[workflows/ingest]]

Summary:
1. Save raw document to `sources/YYYY-MM-DD_slug.md`
2. Read it — extract facts, decisions, entities, open questions
3. Update or create wiki pages; cite source on every claim
4. Update `wiki/index.md` with any new or changed pages
5. Append to log: `## [YYYY-MM-DD] ingest | [source title]`

### 2. Query — Answer a question from the wiki
Full procedure: [[workflows/query]]

Summary:
1. Read `wiki/index.md` to find relevant pages
2. Open and read those pages
3. Synthesize answer with citations
4. If answer warrants retention, file as new wiki page and update index
5. Append to log if new knowledge was filed

### 3. Lint — Health check the wiki
Full procedure: [[workflows/lint]]

Summary:
1. Scan all wiki pages for: missing sources, stale status, orphan pages, contradictions
2. Log issues to `memory/categories/unresolved.md`
3. Produce a repair list
4. Append to log: `## [YYYY-MM-DD] lint | [findings summary]`

---

## Wiki Folder Map

| Folder | Contains | Wiki/Index section |
|--------|----------|--------------------|
| `memory/categories/` | Long-term knowledge: facts, decisions, procedures, outcomes | Knowledge Base |
| `workflows/` | Step-by-step task procedures | Operations |
| `tools/` | Tool capability cards | Tools |
| `agents/` | Agent profiles | Agents |
| `prompts/` | Reusable prompt templates | Prompts |
| `templates/` | File scaffolds for creating new pages | — |
| `sources/` | Raw source documents (read-only) | Not cataloged in wiki/index.md |
| `archive/` | Historical records: sessions, changelogs, postmortems | — |

---

## Page Conventions

### Required frontmatter
```yaml
---
type: [memory|workflow|tool|agent|prompt|template|schema]
status: [draft|reviewed|validated|stale]
updated: YYYY-MM-DD
---
```

### Claim types (required on all factual statements)
| Symbol | Type | When to use |
|--------|------|-------------|
| ✅ | Fact | Verified externally, has a source citation |
| 🔹 | Inference | Agent-derived from facts |
| 🎯 | Decision | Deliberate choice with rationale |
| 💡 | Hypothesis | Unverified assumption |
| ❓ | Unresolved | Open question — log to `memory/categories/unresolved.md` |

### Source citation format
Every factual claim must end with: `[source: description, verified YYYY-MM-DD]`

### Supersession (never silently delete)
```markdown
### Superseded
- date: YYYY-MM-DD
- superseded_by: [[link-to-new-claim]]
- reason: [why it changed]
```

---

## Review Status Thresholds

Pages past their threshold revert to `stale` and must be re-verified before use.

| Category | Stale after |
|----------|-------------|
| infrastructure | 14 days |
| decisions | 90 days |
| procedures | 30 days |
| outcomes | 180 days |
| unresolved | 30 days |

---

## Log Format

```
## [YYYY-MM-DD] ingest | [source title]
- Source: sources/YYYY-MM-DD_slug.md
- Updated pages: [list]
- New pages: [list if any]
- Open questions logged: [yes/no]

## [YYYY-MM-DD] query | [question summary]
- Pages consulted: [list]
- New page filed: [yes/no, link if yes]

## [YYYY-MM-DD] lint | [scope]
- Issues found: [count]
- Logged to unresolved: [yes/no]
```

---

## Governance Reference

- Full 10 rules: [[vault-compliance-rules]]
- Quick rules card: [[memory/governance]]
- Memory categories: [[memory/MEMORY]]
