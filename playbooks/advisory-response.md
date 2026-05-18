# Playbook: Advisory Response

1. Pin `index_build_id` from `indexes/current/manifest.json` — use this build ID for the entire session
2. Classify the user's question by decision domain and lifecycle stage (see controlled vocabulary in `governance/schema/frontmatter-schema.md`)
3. Filter `indexes/current/agent-index.jsonl` for relevant pages by `type`, `lifecycle_stage`, and `primary_topics`
4. Follow `indexes/current/graph-edges.jsonl` to traverse related concepts, frameworks, tools, and risks from seed pages
5. Retrieve exact sections using `indexes/current/section-index.jsonl` line ranges — read only the relevant sections, not full pages
6. Build evidence packet (`EP-*`) per `governance/aba/prompts/agent-11-section-retrieval-and-evidence-packet-agent.md` — every claim must have source support
7. Consolidate claim ledger via `governance/aba/prompts/agent-12-packet-consolidator-and-claim-ledger-agent.md`
8. Draft output from approved claims only via `governance/aba/prompts/agent-13-claim-ledger-writing-agent.md` — no unsupported assertions
9. Run citation review (`agent-14`) — verify every factual claim has a claim ID with source support
10. Run risk review (`agent-15`) — check checklist misuse, false precision, protection-sensitive data, escalation triggers
11. Store final output in `outputs/field-advice/` with output ID `O-{date}-{slug}.md`
