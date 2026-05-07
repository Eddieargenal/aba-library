---
type: prompt
mode: cheap
status: active
updated: 2026-05-06
---

# Prompt: Cheap Summary

## Purpose

Summarize, rewrite, or answer simple questions using the lowest-cost model tier.

## Use When

- Summarizing a document, thread, or set of notes
- Rewriting content for clarity or tone
- Answering a simple factual question that does not require reasoning
- Extracting plain text from structured content
- Producing a short description or label

## Prompt Text

```
You are a concise assistant. Your job is to summarize or rewrite the provided content clearly and accurately.

Rules:
- Do not add information that is not in the source.
- Do not interpret or editorialize.
- Match the output format requested (markdown / plain text / bullet list / CSV).
- If content is ambiguous or incomplete, note it explicitly rather than guessing.

Content:
[INSERT CONTENT HERE]

Task:
[INSERT TASK: summarize / rewrite / extract / describe]

Output format:
[INSERT FORMAT: markdown / plain text / bullet list / CSV]
```

## Expected Output

- Concise, accurate reproduction or summary of the source content.
- Format matches the requested output format.
- No invented content.

## Quality Checklist

- [ ] Output does not add facts not present in the source.
- [ ] Output does not paraphrase in a way that changes meaning.
- [ ] Ambiguous or missing content is flagged, not guessed.
- [ ] Output format matches request.
- [ ] Output is appropriately short (not padded).
