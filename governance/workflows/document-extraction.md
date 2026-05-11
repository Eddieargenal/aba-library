---
type: workflow
scope: document-extraction
status: active
updated: 2026-05-11
---

# Workflow: Document Extraction

Use this workflow for extracting content from PDFs, images, spreadsheets, or other documents.

## Steps

1. **Identify the source file type.**
   - PDF, image (PNG/JPG), spreadsheet (XLSX/CSV), Word document, or other.
   - Confirm the extraction target: full text, specific table, specific section, structured data.

2. **Extract exactly.**
   - Reproduce content as it appears in the source.
   - Do not paraphrase, summarize, or interpret unless explicitly asked.

3. **Preserve tables where possible.**
   - Render tables as markdown tables or CSV as appropriate.
   - If table structure cannot be preserved, note that clearly.

4. **Do not invent missing content.**
   - If a field is blank, empty, or missing in the source — leave it blank.
   - Never fill in missing values with guesses or placeholders.

5. **Flag illegible content.**
   - If text is unclear, corrupted, or cut off, mark it with `[ILLEGIBLE]` or `[TRUNCATED]`.
   - Do not guess what illegible content says.

6. **Produce structured output as requested.**
   - Default output: markdown.
   - If user requests CSV, produce CSV.
   - If user requests JSON, produce JSON.
   - Match the requested format exactly.

7. **Log extraction issues.**
   - If extraction was partial, incomplete, or had quality problems, log it in [[../../memory/runtime/logs/task-log]].

## Model Tier

- Standard text extraction → cheap mode → [[../../prompts/cheap-summary]]
- Complex structured extraction with layout reconstruction → code mode

## Linked Files

- [[../../prompts/cheap-summary]]
- [[../../memory/runtime/logs/task-log]]
