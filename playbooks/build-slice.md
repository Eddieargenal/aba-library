# Playbook: Build Slice

1. Define slice scope in `wiki/aba/11-slice-specs/{slice_id}.md` using `governance/templates/v26/slice-spec-template.md` — specify `decision_domains`, `lifecycle_stage`, `hazards`, `expected_runtime_mode`
2. Identify pages in scope by filtering `indexes/current/agent-index.jsonl` on `lifecycle_stage` and `primary_topics`
3. Copy scoped wiki pages (concepts, frameworks, tools, instruments, risks, playbooks) into `field-repo/wiki/`
4. Copy supporting extracted source pages (stubs or full) into `field-repo/sources/extracted/`
5. Copy `indexes/current/` into `field-repo/indexes/current/`
6. Copy `emergency/` into `field-repo/emergency/`
7. Update `field-repo/slice-manifest.json` with `slice_id`, `base_library_build_id`, `coverage`, `raw_sources_included`, `expected_runtime_mode`, `known_limitations`
8. Review `field-repo/indexes/current/unresolved-edges.jsonl` — out-of-slice nodes should have `status: external_missing`; annotate any that lack this status
