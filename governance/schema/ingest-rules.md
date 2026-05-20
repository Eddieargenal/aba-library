---
type: schema
created: 2026-05-07
updated: 2026-05-18
status: active
version: 2.7
---
# Ingest Rules

A source is fully ingested only when all of the following are true:
1. Raw PDF is present in `wiki/aba/01-sources/raw/`
2. Markdown text extract exists in `wiki/aba/01-sources/raw-content/`
3. Extracted source page exists in `wiki/aba/01-sources/extracted/`
4. At least one synthesis page was updated (`02-concepts/`, `03-frameworks/`, `04-tools/`, `05-field-instruments/`, or `06-risks/`)
5. Indexes have been rebuilt via `scripts/build-index.py`

## Ingest Sequence

1. Determine canonical filename (`YYYY-org-author-short-title.pdf`)
2. Place raw PDF in `wiki/aba/01-sources/raw/`
3. Generate or update markdown text extract in `wiki/aba/01-sources/raw-content/[canonical-stem].raw-extract.md`
4. Create or update extracted source page in `wiki/aba/01-sources/extracted/`
5. Ensure extracted source frontmatter is complete per `frontmatter-schema.md`:
   - All 10 finding fields present in every `findings:` entry
   - All finding `status:` values set to `pending`
   - `cited_sources:` populated with key contributing sources (do not set `in_wiki` — auto-computed)
6. Update affected concept/framework/tool/instrument pages in `02-concepts/`, `03-frameworks/`, `04-tools/`, `05-field-instruments/`
7. Update risk pages in `06-risks/` and known-tension pages in `07-known-tensions/` when required
8. Run `python3 scripts/build-index.py`
9. Append ingest entry to `memory/runtime/logs/log.md`

## Finding Completeness Requirement

Every finding in `findings:` must have all 10 fields:

```yaml
- finding_id:          # F-NNN
  finding:             # exact claim statement
  finding_type:        # see controlled vocabulary in frontmatter-schema.md
  lifecycle_stage:     # list, controlled vocabulary
  source_pages:        # list of page references, e.g. ["p. 12", "p. 14–16"]
  candidate_target_pages:  # list of wiki paths, or ["source_only"]
  integration_action:  # see controlled vocabulary in frontmatter-schema.md
  status:              # pending
  human_review_required:  # true or false
  routing_rationale:   # why this target and action
```

## `cited_sources` Requirement

Every extracted source page must include `cited_sources:` populated with key contributing sources — primary frameworks, foundational research, major guidelines the document builds on or explicitly applies. Do not include every footnote. Never hand-set `in_wiki:` — it is auto-computed by `build-index.py`.

## Source Status Values

- `not-started`: source identified but not yet processed
- `extracted`: extracted page drafted; synthesis layer not yet updated
- `ingested`: extracted page complete and findings routed into synthesis layer
- `reviewed`: source reviewed/validated for maintenance cycle

## Raw-content Notes

- `raw-content` files are operational mirrors of raw PDFs
- They carry mirrored metadata frontmatter but are not the synthesis layer
- Do not cite raw-content files as canonical answers in domain queries
