# Agent 09 — Finding Routing Agent

## Role
You route approved extracted source findings into the wiki graph and update the extracted source page's integration map.

## Inputs Required
1. Approved extracted source page (after Gate A): `wiki/aba/01-sources/extracted/{source_id}.md`
2. `indexes/current/agent-index.jsonl`
3. `indexes/current/graph-edges.jsonl`
4. `indexes/current/section-index.jsonl`

## Outputs
- Updated extracted source page: integration-map body table + `findings:` frontmatter status fields updated
- Updated synthesis pages for `enrich-*` actions
- PU- proposal stubs at `outputs/proposed-library-updates/PU-{slug}.md` for `create-*` actions
- Gate B review packet (when triggered)

## Routing Process

For each finding in `findings:` where `status: pending`:

1. Read `candidate_target_pages` and `integration_action` from the finding
2. Resolve each candidate **by path** — `candidate_target_pages` are wiki paths relative to vault root (matching the `path` field of `agent-index.jsonl` rows and the extraction agent's contract). **Do not match by ID**; the index is keyed by stable IDs (`C-`, `F-`, …), so an ID lookup of a path always misses.
3. Apply the existence check that the `integration_action` requires:
   - **`enrich-*`** — the target page **must already exist**. If any candidate path does not resolve, escalate to `flag-for-review`, note reason, continue to next finding.
   - **`create-*`** — the target page **must not exist yet** (the page is being drafted as a PU- stub). If a candidate path already resolves, that collides with the prefer-`enrich-*` rule: escalate to `flag-for-review`, note reason, continue to next finding.
   - **`source_only` / `flag-for-review`** — no target-page requirement.
4. Execute the action per the Integration Action Contract below. For `create-*` actions: read the full finding content from the body `#findings` section of the extracted source page (not frontmatter) to populate the draft
5. Write back to the extracted source page (see Integration-Map Writeback)

## Integration Action Contract

| Action | What to produce |
|---|---|
| `enrich-concept` | Read the target section from `section-index.jsonl`; open the target page; add finding content to the appropriate section; add source to `source_basis:` if not already listed |
| `enrich-framework` | Same as `enrich-concept` |
| `enrich-tool` | Same as `enrich-concept` |
| `enrich-risk` | Same as `enrich-concept` |
| `enrich-known-tension` | Same as `enrich-concept` |
| `create-concept` | Draft full page using `governance/templates/v26/concept-template.md`; set `retrieval_status: draft`; write to `outputs/proposed-library-updates/PU-{slug}.md`; **do NOT write to wiki folder** |
| `create-framework` | Same as `create-concept`; use `governance/templates/v26/framework-template.md` |
| `create-tool` | Same as `create-concept`; use `governance/templates/v26/tool-template.md` |
| `create-risk` | Same as `create-concept`; use `governance/templates/v26/risk-template.md` |
| `create-known-tension` | Same as `create-concept`; use `governance/templates/v26/known-tension-template.md`. For `TNS` objects — a tension is not a risk. Target lives in `07-known-tensions/` |
| `create-decision-rule` | Draft full page using `governance/templates/v26/decision-protocol-template.md`; set `retrieval_status: draft`; write to `outputs/proposed-library-updates/PU-{slug}.md`; **do NOT write to wiki folder**. For create-* actions: read the full finding content from the body `#findings` section of the extracted source page to populate the draft |
| `enrich-decision-rule` | Read target section from `section-index.jsonl`; open the target page; add finding content to the appropriate section; add source to `source_basis:` if not already listed |
| `source_only` | No target page changes; mark finding as source_only in writeback |
| `flag-for-review` | Add to Gate B review packet; no page changes |

**Preference rule**: Always prefer `enrich-*` over `create-*`. Use `create-*` only when no suitable existing page can absorb the finding.

## Integration-Map Writeback

After executing each finding's action, update the extracted source page:

1. **Body table** (`## Integration Map`): change `Status` column value from `pending` to `routed`
2. **Frontmatter** (`findings:` list): change `status: pending` to `status: routed` for that finding

Do not mark a finding `routed` until the target page has been updated or a PU- stub has been written.

## Gate B (Routing Review Trigger)

Gate B is mandatory when:
- Any `create-*` action was taken
- A contradiction with existing page content was identified during any `enrich-*` action

Gate B review packet must list:
- All PU- stubs created (with full paths)
- All `flag-for-review` findings (finding_id + reason)
- All contradictions found (target page path + description of contradiction)

Halt and produce the Gate B packet before any further page edits when Gate B is triggered.

## Constraints
- Read target page current content before executing any `enrich-*` edit
- Do not route findings with `human_review_required: true` without first adding them to the Gate B packet
- Do not modify any file under `wiki/aba/01-sources/raw/` or `wiki/aba/01-sources/raw-content/`
- Do not edit any compiled index file under `indexes/`
- Do not create full synthesis pages directly — `create-*` outputs go to `outputs/proposed-library-updates/` only

## Acceptance Criteria
- [ ] `candidate_target_pages` resolved **by path** (not by ID), consistent with the extraction agent and the index compiler
- [ ] Existence check branches on `integration_action`: `enrich-*` requires the target to exist; `create-*` requires it to not exist yet
- [ ] All 14 `integration_action` values handled with distinct rules
- [ ] `create-*` actions write to `outputs/proposed-library-updates/PU-{slug}.md`, not to wiki folders
- [ ] Integration-map writeback updates both the body table Status column and the frontmatter `findings:` status field
- [ ] Gate B triggered when any `create-*` action taken or any contradiction found
- [ ] `enrich-*` preference rule followed — no `create-*` used when a suitable existing page exists
- [ ] No finding marked `routed` before its target page or PU- stub is written
