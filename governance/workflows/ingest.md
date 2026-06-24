---
type: workflow
status: validated
updated: 2026-05-12
---

# Ingest Workflow

Add a new source document to the ABA wiki and propagate updates through all required layers.

> **Authoritative.** This file is the single source of truth for the ingest sequence. The quick-reference in `playbooks/ingest-source.md`, the librarian RUNBOOK, and agent prompts 07–09 derive from it — if steps disagree, this file wins.

## When to Use

When a new source PDF (or equivalent canonical source document) must be integrated into the wiki.

## Pre-conditions

- Canonical filename is defined (`YYYY-org-author-short-title.pdf`)
- Raw file is available
- Source is not already ingested in `wiki/aba/01-sources/extracted/`

## Steps

### 1. Save raw source (immutable)

Place the raw PDF in:

`wiki/aba/01-sources/raw/[canonical-filename].pdf`

Never edit this file after placement.

### 2. Generate raw-content markdown mirror

Create or update:

`wiki/aba/01-sources/raw-content/[canonical-stem].raw-extract.md`

Rules:
- preserve source text faithfully
- keep page-level separators/structure
- no synthesis in this file

### 3. Create or update extracted source page

Create or update:

`wiki/aba/01-sources/extracted/[canonical-stem].md`

Use schema from `governance/schema/frontmatter-schema.md`:
- `type: source`
- required `contradicts: []` (or populated list)
- complete source metadata

### 4. Sync agreed frontmatter to raw-content

Run:

`python3 scripts/sync_extracted_frontmatter_to_raw_content.py --apply`

This copies the agreed metadata subset from extracted pages to matching raw-content files and sets:
- `type: source_raw_extract`
- `zone: raw-content`

### 5. Update synthesis layer pages

Update all impacted pages in:
- `wiki/aba/02-concepts/`
- `wiki/aba/03-frameworks/`
- `wiki/aba/04-tools/`
- `wiki/aba/05-field-instruments/`
- `wiki/aba/06-risks/`
- `wiki/aba/07-known-tensions/` (if conflicts/tensions appear)
- `wiki/aba/09-decision-protocols/`

### 6. Rebuild agent index

Run:

`python3 scripts/build-index.py`

### 7. Log ingest operation

Append to:

`memory/runtime/logs/log.md`

Format:

`## [YYYY-MM-DD] ingest | Source title`

### 8. Validate completion

Confirm:
- raw PDF exists in `01-sources/raw/`
- raw-content mirror exists in `01-sources/raw-content/`
- extracted source page exists in `01-sources/extracted/`
- affected synthesis pages updated
- `indexes/agent-index.md` regenerated

## Related

- [[../schema/ingest-rules]]
- [[../schema/frontmatter-schema]]
- [[../aba/prompts/ingest-new-source]]
