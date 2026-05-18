# Playbook: Rebuild Indexes

1. Run from vault root: `python3 scripts/build-index.py`
2. Review JSON output: check `critical_error_count` (must be 0 to publish), `warning_count`, `published`
3. If `published: false`: open `indexes/builds/{build_id}/lint-report.json`, resolve all critical errors listed, re-run
4. If `published: true`: confirm `indexes/current/manifest.json` reflects the new `build_id` and `active: true`
5. Review `indexes/current/unresolved-edges.jsonl` — ghost nodes are warnings, not publish blockers; log each for the repair queue
6. Optionally review `indexes/current/section-index.jsonl` to confirm section anchors resolved for new pages
