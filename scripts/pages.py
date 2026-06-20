"""
pages.py — the filesystem -> Page seam

read_pages(root) walks a vault's markdown and returns the Pages the index is
built from: skips the ingest-only raw/raw-content layers and 00_-prefixed index
files, splits frontmatter through the shared parser, and flags unparseable
frontmatter with `_yaml_error` (compile_index turns that into a critical).

Kept apart from compile_index (which stays pure) and from build-index.py (which
is hyphenated and unimportable) so the scan/parse path has a real test surface
— see test_pages.py.
"""

from pathlib import Path
from typing import List

from compile_index import Page
import frontmatter

SKIP_PREFIXES = ("01-sources/raw-content/", "01-sources/raw/")


def read_pages(root: Path) -> List[Page]:
    pages: List[Page] = []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if rel.startswith(SKIP_PREFIXES):
            continue
        if path.name.startswith("00_"):
            continue
        text = path.read_text(encoding="utf-8")
        fm_text, body = frontmatter.split(text)
        if fm_text is None:
            pages.append(Page(path=path, rel_path=rel, frontmatter={}, body=body))
            continue
        try:
            fm = frontmatter.parse_yaml(fm_text)
        except Exception:
            fm = {"_yaml_error": True}
        pages.append(Page(path=path, rel_path=rel, frontmatter=fm, body=body))
    return pages
