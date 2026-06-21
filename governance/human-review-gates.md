---
type: governance
status: active
created: 2026-05-18
updated: 2026-06-21
---

# Human Review Gates

- Gate A: extracted source review before routing.
- Gate B: routing and proposal review before high-risk synthesis updates.
- Gate C: field-critical advisory review before operational use.
- Gate D: field update promotion review before canonical merge.

## Enforcement is a review process, not an automated mechanism

Gates A–D are enforced **socially and through PR review** — not by code. This is
a deliberate design point, recorded here so the gate status is not mistaken for
a machine-enforced state:

- There is **no gate-queue file and no gate check in `scripts/`**. The build
  (`build-index.py` / the lint registry) validates data integrity and surfaces
  warnings; it does **not** track or block on gate state.
- A gate annotation in frontmatter (e.g. `Awaiting Gate B`) is an **advisory
  label, not an enforced state**. Nothing technically prevents an agent or
  author from proceeding past a gate; the gate holds only because a human
  reviewer (and the PR process) declines to merge work that skipped it.
- Agent prompts that "halt" at a gate (e.g. Gate B in agent-09, Gate C in
  agent-15) describe **expected agent behaviour**, not an enforced runtime
  block.

Treat the gates as a human checklist backed by code review. Building a
mechanical enforcement layer (a gate-state field plus a lint block, or a
gate-queue artifact) is **out of scope here** and tracked separately as
gate-state enforcement (issue #30).
