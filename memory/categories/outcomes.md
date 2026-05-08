---
type: memory-category
category: outcomes
status: active
updated: 2026-05-08
title: Outcomes Memory
---

# Outcome Memory

Results, lessons, and applied impacts from completed tasks and resolved decisions.

Move resolved items from [[unresolved.md]] here.

## Template

```
### [OUTCOME-KEY]
- decision_key: [related decision or pending key]
- action_taken: [what was actually done]
- result: [what happened]
- observed_at: YYYY-MM-DD
- impact: [what changed as a result]
- lesson: [what should be done differently next time, if anything]
- applied_to: [which project or system was affected]
- source_session: [session ID or date of the session where this was logged]
```

## Records

<!-- Add outcome records below using the template above. -->

### hermes-tui-slash-debug-fix
- decision_key: n/a
- ✅ Action: Removed `console.log('[slash] handler called with:', cmd)` from `ui-tui/src/app/createSlashHandler.ts`; removed a debug-heavy `/quit` implementation and duplicate dead-code comma
- source: agent-debugging session, 2026-05-08
- status: validated
- impact: Cleaned TUI slash handler, resolved hanging behaviornds (history, save, snapshot) from `core.ts`; rebuilt dist with `npm run build`
- result: All slash commands functional again; user confirmed "it worked"
- observed_at: 2026-05-08
- impact: Ink TUI terminal rendering restored — raw console output inside an Ink process writes to the terminal stream directly, corrupting the UI so command output appeared invisible
- lesson: Never leave `console.log` in TUI code that runs inside Ink; any stdout/stderr write outside Ink's render loop corrupts the terminal. Symptom looks like "commands not working" but is actually a rendering corruption.
- applied_to: hermes-agent TUI (`ui-tui/`)
- source_session: 2026-05-08
