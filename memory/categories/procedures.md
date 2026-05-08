---
type: memory-category
category: procedures
status: active
updated: 2026-05-08
title: Procedures Memory
---

# Procedure Memory

Step-by-step procedures with prerequisites and verification steps.

## Template

```
### [PROCEDURE-KEY]
- purpose: [what this procedure accomplishes]
- status: validated | proposed | superseded
- source: user-stated | user-confirmed | agent-inferred
- updated: YYYY-MM-DD
- prerequisites:
  - [prerequisite 1]
  - [prerequisite 2]
- steps:
  1. [step 1]
  2. [step 2]
  3. [step 3]
- verification: [how to confirm the procedure succeeded]
- last_executed: YYYY-MM-DD
- failure_notes: [known failure modes or gotchas]
```

## Records

<!-- Procedure entries below using the template above. Format: 🔹 [key] for agent-derived, 🎯 for user decisions -->

### vault-aba-integration-2026-05-08
- purpose: Merged _system/urban-drr-aba-wiki into wiki/aba/ as a unified vault structure
- status: validated
- source: user-directed integration work, 2026-05-08
- updated: 2026-05-08
- prerequisites:
  - Vault git snapshot taken
  - All ABA wiki files intact
  - Core vault functioning
- steps:
  1. Moved _system/urban-drr-aba-wiki → wiki/aba/
  2. Moved _system/briefs → governance/briefs/
  3. Rewrote all external wikilinks (_system references → wiki/aba/)
  4. Removed dead JSONL indexes (key-index, keyword-index, relations)
  5. Fixed stale wikilinks (behavioral, projects, tools, pending categories)
  6. Updated SCHEMA.md, 00_Start_Here.md, QUICK.md, wiki/index.md
  7. Populated memory/context.md
- verification: All wikilinks resolve, zero broken links outside archive/logs
- failure_notes: wiki/index.md was accidentally wiped during write — restored from git