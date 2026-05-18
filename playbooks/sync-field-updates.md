# Playbook: Sync Field Updates

1. Field agent writes proposed update to `outputs/proposed-library-updates/PU-{date}-{slug}.md`
   - Required fields: `proposal_id`, `created_on_device`, `base_library_build_id`, `target_page_id`, `proposal_type`, `reason`, `suggested_change`, `evidence` (field_note_id references), `review_required: true`, `status: pending_sync`
2. HQ reviewer reads proposal and checks evidence references — confirm field_note_id files exist or are described
3. If accepted: apply change to canonical page, update frontmatter `updated:` date, rebuild indexes via `python3 scripts/build-index.py`; set proposal `status: accepted`
4. If rejected: note rejection reason in proposal file, set `status: rejected` — do not modify canonical page
5. Append operation to `memory/runtime/logs/log.md`: `## [YYYY-MM-DD] sync | PU-{id} — [accepted/rejected]: [brief reason]`
