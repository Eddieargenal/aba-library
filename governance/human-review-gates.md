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

## Enforcement: a `gate_state` field, backed by the review process

Gates A–D are enforced by a combination of a mechanical publish-block and human
review:

- **Mechanical (opt-in, per page):** a page may declare a `gate_state`
  frontmatter field. While it is anything other than `cleared`
  (e.g. `awaiting-gate-b`), the build emits a **critical** (`gate_pending:…`)
  that blocks atomic publish to `indexes/current/`; an unrecognized value is a
  critical too (`invalid_gate_state:…`, fail-closed). A gate-pending page
  therefore cannot be published until its gate is cleared. Enforced by
  `rule_gate_state` in the lint registry — the controlled values live in
  `GATE_STATE_VOCAB` (`scripts/schema.py`).
- **Review process (the default):** the field is **optional**. A page that does
  not carry `gate_state` imposes no constraint, so for unannotated pages the
  gates remain a human checklist backed by PR review — nothing technically forces
  a page through a gate it never declared. Agent prompts that "halt" at a gate
  (e.g. Gate B in agent-09, Gate C in agent-15) describe expected agent
  behaviour, not a runtime block.

In short: gate state is **enforced wherever a page opts in by declaring it**, and
remains a review process everywhere else. A richer always-on mechanism (requiring
every gated page to carry the field, or a gate-queue artifact) is out of scope
here.
