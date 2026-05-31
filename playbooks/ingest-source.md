# Playbook: Ingest Source

> **Source of truth:** `governance/workflows/ingest.md`. This is a derived quick-reference; if it disagrees with the workflow, the workflow wins.

1. Add raw PDF to `wiki/aba/01-sources/raw/` — filename: `YYYY-org-author-short-title.pdf`
2. Create raw-content mirror at `wiki/aba/01-sources/raw-content/{source_id}.raw-extract.md` — markdown text extraction of the PDF content
3. Create extracted source page at `wiki/aba/01-sources/extracted/{source_id}.md` using `governance/templates/v26/extracted-source-template.md`
   - Populate all frontmatter fields including `id: S-{slug}`, `retrieval_status:`, `lifecycle_stage:`, `findings:` list
   - Each finding must have: `finding_id`, `finding`, `finding_type`, `lifecycle_stage`, `source_pages`, `candidate_target_pages`, `integration_action`, `status`
   - Include `## Integration Map` table in body
4. Sync frontmatter to raw-content mirror: `python3 scripts/sync_extracted_frontmatter_to_raw_content.py --apply`
5. Run `python3 scripts/build-index.py` and review lint output — zero critical errors required before proceeding
6. Pause at Gate A: human reviews extracted source page and approves findings before routing begins
