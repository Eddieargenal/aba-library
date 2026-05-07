"""
ingest_source.py — Urban DRR ABA Wiki source ingestion script

TODO[agent]: Implement this script to automate source ingestion.

Intended behavior:
1. Accept a PDF path as argument
2. Generate canonical filename from metadata
3. Copy PDF to raw/pdf/
4. Extract text using pdfplumber or pdfminer to raw/extracted/
5. Parse extracted text to generate source page frontmatter
6. Create or update source page in wiki/01-sources/
7. Update affected concept, tool, lifecycle, and field instrument pages
8. Update index.md
9. Append to log.md
10. Commit changes if git available

Usage: python ingest_source.py /path/to/document.pdf [--dry-run]

Dependencies: pdfplumber, openpyxl, gitpython
"""
raise NotImplementedError("Script not yet implemented. See wiki/13-agent-prompts/ingest-new-source.md for manual procedure.")
