#!/usr/bin/env python3
"""
export_fieldwise.py — the FieldWise vault export (FieldWise PRD #30; ADR-0006 in FieldWise: the vault is written only
here).

A clean build becomes one zip that FieldWise imports. Each anchored section of a usable or limited synthesis page
becomes one note: Markdown with simple `key: value` front matter, titled "Page title — Section".

  plan_export(pages, result, build_id)  pure: pages and their compiled build in, a Plan (notes + report) out
  write_package(plan, out_path)         the zip: one .md file per note and manifest.json
  export_from_disk(vault, out_dir)      the command: pins indexes/current, refuses a stale or unclean build

Run:  python3 scripts/export-fieldwise.py   (writes exports/fieldwise-<build_id>.zip)
"""

import hashlib
import json
import re
import zipfile
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List

FORMAT = "fieldwise-vault/1"
SYNTHESIS_AUTHORITY = "FieldWise ABA library"
VALID_DAYS = 365
# synthesis page types that carry guidance; sources (A2), output templates and slice specs never become notes here
SYNTHESIS_TYPES = {"concept", "framework", "tool", "field-instrument", "risk", "known-tension", "advisory-playbook",
                   "decision-protocol", "synthesis"}
EXPORTED_STATUS = {"usable", "limited"}
ANCHOR = re.compile(r'<a id="([^"]+)"></a>')


class NotClean(Exception):
    """The build has critical lint errors: nothing is exported."""


class StaleBuild(Exception):
    """The pages changed after the current build, or the build has no content digest: rebuild first."""


@dataclass
class Note:
    file: str
    front: Dict[str, str]
    body: str

    def text(self) -> str:
        head = "\n".join(f"{k}: {v}" for k, v in self.front.items())
        return f"---\n{head}\n---\n{self.body.strip()}\n"


@dataclass
class Plan:
    build_id: str
    notes: List[Note] = field(default_factory=list)
    report: Dict[str, Any] = field(default_factory=dict)


def _sections(body: str) -> List[tuple]:
    """(anchor id, heading, text) for each anchored section, in order."""
    marks = list(ANCHOR.finditer(body))
    out = []
    for i, m in enumerate(marks):
        chunk = body[m.end(): marks[i + 1].start() if i + 1 < len(marks) else len(body)].strip()
        heading = re.match(r"#+\s*(.+)", chunk)
        out.append((m.group(1), heading.group(1).strip() if heading else m.group(1), chunk))
    return out


def _in_scope(p) -> bool:
    """Usable or limited guidance pages only; overview maps describe the library, not guidance."""
    fm = p.frontmatter
    return (fm.get("type") in SYNTHESIS_TYPES and fm.get("retrieval_status") in EXPORTED_STATUS
            and not p.rel_path.startswith("00-overview/"))


def plan_export(pages, result, build_id: str) -> Plan:
    if result.critical:
        raise NotClean(f"build {build_id} has {len(result.critical)} critical error(s): fix them and rebuild")
    plan = Plan(build_id=build_id, report={"held_back": []})
    for p in pages:
        fm = p.frontmatter
        if not _in_scope(p):
            continue
        missing = next((f for f in ("last_reviewed", "accepted_by") if not fm.get(f)), None)
        if missing:   # a page nobody reviewed, or nobody accepted, never becomes approved guidance
            plan.report["held_back"].append({"aba_id": fm["id"], "path": p.rel_path, "reason": f"no {missing}"})
            continue
        valid = date.fromisoformat(str(fm["last_reviewed"])) + timedelta(days=VALID_DAYS)
        for sid, heading, text in _sections(p.body):
            title = f"{fm['title']} — {heading}"
            plan.notes.append(Note(
                file=f"{fm['id']}--{sid}.md",
                front={"title": title, "kind": "synthesis", "aba_id": fm["id"], "aba_section": sid,
                       "authority": SYNTHESIS_AUTHORITY, "author": str(fm["accepted_by"]),
                       "valid_until": valid.isoformat(), "retrieval_status": fm["retrieval_status"],
                       "build_id": build_id},
                body=text))
    return plan


def write_package(plan: Plan, out_path, exported_at: str = "") -> Path:
    """The zip FieldWise imports: the notes and manifest.json, which pins the build and holds a SHA-256 digest of
    each note's bytes, so FieldWise can refuse a package that was changed after export."""
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    files = {n.file: n.text().encode("utf-8") for n in plan.notes}
    # plan_export refuses a build with critical errors, so every package records 0
    manifest = {"format": FORMAT, "build_id": plan.build_id, "critical_error_count": 0,
                "exported_at": exported_at or datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "notes": [{"file": f, "sha256": hashlib.sha256(b).hexdigest()} for f, b in files.items()],
                "report": plan.report}
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in files.items():
            z.writestr(name, data)
        z.writestr("manifest.json", json.dumps(manifest, indent=1, ensure_ascii=False))
    return out


def export_from_disk(vault, out_dir) -> Path:
    """Export the build in indexes/current. The pages on disk must still be the pages that build compiled (same
    content digest); otherwise the export would carry text the build never checked."""
    from compile_index import compile_index
    from pages import pages_digest, read_pages
    vault = Path(vault)
    wiki = vault / "wiki" / "aba"
    manifest = json.loads((vault / "indexes" / "current" / "manifest.json").read_text(encoding="utf-8"))
    pages = read_pages(wiki)
    if manifest.get("content_digest") != pages_digest(pages):
        raise StaleBuild(f"the pages changed after build {manifest['build_id']} (or it has no content digest): "
                         "rebuild with scripts/build-index.py first")
    result = compile_index(pages, target_exists=lambda p: (vault / p).exists(),
                           today=datetime.now(timezone.utc).date())
    plan = plan_export(pages, result, build_id=manifest["build_id"])
    return write_package(plan, Path(out_dir) / f"fieldwise-{manifest['build_id']}.zip")
