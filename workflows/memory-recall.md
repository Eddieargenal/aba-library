---
type: workflow
scope: memory-recall
status: active
updated: 2026-05-06
---

# Workflow: Memory Recall

Use this workflow when the user asks about previous decisions, facts, or session history.

## Steps

1. **Classify the query type.**

   | Query Type | Example |
   |---|---|
   | exact key | "what did we decide about X?" |
   | keyword | "anything about Docker networking?" |
   | temporal | "what changed last session?" |
   | relational | "what decisions relate to the VPS setup?" |

2. **Search MEMORY.md first.**
   - Open [[../memory/MEMORY]].
   - Look for a pointer to the relevant category or entry.
   - If found, open that category file directly.

3. **Search the relevant category file.**
   - Open the most likely category: infrastructure, decisions, procedures, outcomes.
   - Scan that file for the relevant entry.

4. **If no matching category found, say no memory was found.**
   - Do not guess. Do not fabricate. Do not produce a plausible-sounding answer.

5. **If nothing is found, say no memory was found.**
   - Do not guess. Do not fabricate. Do not produce a plausible-sounding answer.
   - Say clearly: "No memory found for this query."

7. **Do not fabricate memory.**
   - If a fact was not explicitly stored in a category file, it is not in memory.
   - Agent-inferred guesses about what "probably" happened are not memory.

## Linked Files

- [[../memory/MEMORY]]
- [[../memory/categories/infrastructure]]
- [[../memory/categories/decisions]]
- [[../memory/categories/procedures]]
- [[../memory/categories/outcomes]]
