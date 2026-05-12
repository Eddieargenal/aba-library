# Librarian — Session Protocol

Full open/close protocol for every ABA wiki agent session.

---

## Open Protocol

Run these steps at the start of every session, in order:

**Step 1 — Load handoff**
Read `memory/current-handoff.md`. Note any in-progress tasks, open contradictions, and pending compliance items from the previous session.

**Step 2 — Check lint queue**
Read the most recent lint report from `wiki/aba/outputs/internal/`. Look for any files named `lint-report-YYYY-MM-DD.md` and open the latest. Note all CRITICAL and HIGH findings.

**Step 3 — Clear compliance before new work**
Before starting any new task: resolve all CRITICAL findings. Resolve HIGH findings unless explicitly deferred by the user. Do not begin assigned work until compliance queue is clear.

**Step 4 — Begin task**
Proceed with the session's assigned work.

---

## Close Protocol

Run these steps at the end of every session, in order:

**Step 1 — Fill handoff**
Write a structured summary to `memory/current-handoff.md`:
- Tasks completed this session
- Files changed (list each file)
- Open contradictions discovered (if any)
- Deferred items (with reason)
- Recommended first action for next session

**Step 2 — Update schema changelog (if schema changed)**
If any frontmatter field was added, removed, or renamed during this session:
Append a row to `governance/schema/changelog.md`:
`| YYYY-MM-DD | agent | description of change | files affected | migration notes |`

**Step 3 — Run lint**
Check for:
- Missing required frontmatter fields per page type (CRITICAL)
- Missing `contradicts:` field on any source, tool, framework, or concept page (CRITICAL)
- `field_instruments: []` on any tool with `status: validated` (CRITICAL)
- `data_quality_checks: false` on any validated field instrument (HIGH)
- Orphan pages with no inbound wikilinks (MEDIUM)

File report to: `wiki/aba/outputs/internal/lint-report-YYYY-MM-DD.md`

**Step 4 — Rebuild index**
Run: `python3 scripts/build-index.py`
This regenerates `indexes/agent-index.md` from current frontmatter. Always run after any page is added, removed, or has frontmatter changed.

**Step 5 — Append to log**
Append to `memory/runtime/logs/log.md`:
```
## [YYYY-MM-DD] type | brief description
- key action 1
- key action 2
- files changed: [list]
```
Where `type` is one of: `ingest` · `query` · `lint` · `schema` · `maintenance`

---

## Reference

| File | Purpose |
|---|---|
| `memory/current-handoff.md` | Session continuity — read at open, write at close |
| `indexes/agent-index.md` | Query entry point — run frontmatter query here first |
| `wiki/aba/outputs/internal/` | Lint reports and synthesis outputs |
| `governance/schema/changelog.md` | Schema change log — append on any schema change |
| `memory/runtime/logs/log.md` | Append-only operation log |
| `scripts/build-index.py` | Regenerates agent-index.md — run at close |
