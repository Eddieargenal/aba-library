#!/usr/bin/env python3
"""
export_fieldwise.py — the FieldWise vault export (FieldWise PRD #30; ADR-0006 in FieldWise: the vault is written only
here).

A clean build becomes one zip that FieldWise imports. Each anchored section of a usable or limited synthesis page
becomes one Synthesis note: Markdown with simple `key: value` front matter, titled "Page title — Section". An
extracted source page becomes Standard notes under its publisher (issue #51): its fixed guidance sections (split at
subheadings when long), one note per finding and one tension note per Known Tensions row.

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
# synthesis page types that carry guidance; output templates and slice specs never become notes
SYNTHESIS_TYPES = {"concept", "framework", "tool", "field-instrument", "risk", "known-tension", "advisory-playbook",
                   "decision-protocol", "synthesis"}
EXPORTED_STATUS = {"usable", "limited"}
SOURCE_FOLDER = "01-sources/extracted/"   # raw-content mirrors are copies, never notes
# the only source sections that carry guidance; task seeds, integration maps, steps 13-16 and the Gate A queue are
# extraction workflow and never leave the library
GUIDANCE_SECTIONS = ("summary", "key-concepts", "methods-and-tools", "known-tensions", "decision-logic")
ANCHOR = re.compile(r'<a id="([^"]+)"></a>')
SUBHEADING = re.compile(r"(?m)^###+\s*(.+)$")
SPLIT_WORDS = 600
# a finding is a "**F-001** — claim" paragraph or a "| F-001 | claim |" table row; "→ see <object>" pointers are dropped
FINDING = re.compile(r"(?m)^(?:\*\*(F-\d+)\*\*\s*—\s*|\|\s*(F-\d+)\s*\|\s*)([^|\n]+?)(?:\s*→ see [^|\n]*)?\s*(?:\||$)")


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


def _is_source(p) -> bool:
    return p.frontmatter.get("type") == "source" and p.rel_path.startswith(SOURCE_FOLDER)


def _in_scope(p) -> bool:
    """Usable or limited guidance pages and extracted sources only; overview maps describe the library, not
    guidance."""
    fm = p.frontmatter
    if fm.get("retrieval_status") not in EXPORTED_STATUS:
        return False
    return _is_source(p) or (fm.get("type") in SYNTHESIS_TYPES and not p.rel_path.startswith("00-overview/"))


def _findings(fm, text) -> List[tuple]:
    """(section id, heading, body, extra front matter) for each finding in the Findings section. The front matter
    list gives each finding its pages and lifecycle stages; task seeds are workflow, and routing rationales and
    object pointers are notes for the extraction agents, so neither leaves."""
    meta = {f.get("finding_id"): f for f in fm.get("findings") or []}
    out = []
    for in_text, in_table, claim in FINDING.findall(text):
        fid = in_text or in_table
        f = meta.get(fid, {})
        if f.get("finding_type") == "task-seed":
            continue
        body = claim.strip()
        if f.get("source_pages"):
            body += "\n\nPages: " + ", ".join(f["source_pages"])
        out.append((f"finding-{fid.lower()}", f"Finding {fid}", body,
                    {"lifecycle_stage": ", ".join(f.get("lifecycle_stage") or [])}))
    return out


def _tensions(heading, text) -> List[tuple]:
    """One tension note per row of the Known Tensions table, in FieldWise's tension format. The text outside the
    table stays as the section note, so each tension is in one note only; no text left means no section note."""
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith("|") and "Tension ID" in l), None)
    if start is None:
        return [("known-tensions", heading, text, {})]
    end = next((i for i in range(start, len(lines)) if not lines[i].startswith("|")), len(lines))
    out = []
    for row in lines[start + 2:end]:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        tid, first, first_at, second, second_at, _type, why = (cells + [""] * 7)[:7]
        short = "TNS-" + tid.rsplit("TNS-", 1)[-1]
        body = f"Position A: {first} ({first_at})\nPosition B: {second} ({second_at})"
        if why:
            body += f"\nWhy it matters: {why}"
        out.append((short.lower(), f"Tension {short}", body, {"role": "tension"}))
    rest = re.sub(r"\n{3,}", "\n\n", "\n".join(lines[:start] + lines[end:])).strip()
    if rest != lines[0].strip():   # more than the heading is left
        out.insert(0, ("known-tensions", heading, rest, {}))
    return out


def _split(sid, heading, text) -> List[tuple]:
    """A section over about SPLIT_WORDS words becomes one note per subheading, plus one for the text before the
    first subheading. A subheading with no text of its own (it only groups the ones below it) gives no note."""
    marks = list(SUBHEADING.finditer(text))
    if len(text.split()) <= SPLIT_WORDS or not marks:
        return [(sid, heading, text, {})]
    out, seen = [(sid, heading, text[:marks[0].start()].strip(), {})], set()
    for i, m in enumerate(marks):
        chunk = text[m.start(): marks[i + 1].start() if i + 1 < len(marks) else len(text)].strip()
        if not chunk.partition("\n")[2].strip():
            continue
        sub = m.group(1).strip()
        slug = base = f"{sid}--" + re.sub(r"[^a-z0-9]+", "-", sub.lower()).strip("-")
        n = 2
        while slug in seen:   # two subheadings with one name still give two notes
            slug, n = f"{base}-{n}", n + 1
        seen.add(slug)
        out.append((slug, f"{heading}: {sub}", chunk, {}))
    return out


def _publisher(fm) -> str:
    return str(fm.get("institution") or fm.get("author") or "")


def _old_format(p) -> bool:
    """The old source template anchors only its summary, so that one anchor runs over every later section (Key
    concepts, Quality Checklist, ...): a guidance section that holds another heading of its own level."""
    for sid, _, text in _sections(p.body):
        top = re.match(r"(#+)\s", text)
        if sid in GUIDANCE_SECTIONS and top and re.search(rf"(?m)^#{{1,{len(top.group(1))}}}\s", text[top.end():]):
            return True
    return False


def _parts(p) -> List[tuple]:
    """(section id, heading, body, extra front matter) for each note a page gives."""
    if not _is_source(p):
        return [(sid, heading, text, {}) for sid, heading, text in _sections(p.body)]
    out = []
    for sid, heading, text in _sections(p.body):
        if sid == "findings":
            out += _findings(p.frontmatter, text)
        elif sid == "known-tensions":
            out += _tensions(heading, text)
        elif sid in GUIDANCE_SECTIONS:
            out += _split(sid, heading, text)
    return out


def _held_back(p) -> str:
    """Why a page in scope stays in the library, or "" when it is exported."""
    fm = p.frontmatter
    missing = next((f for f in ("last_reviewed", "accepted_by") if not fm.get(f)), None)
    if missing:   # a page nobody reviewed, or nobody accepted, never becomes approved guidance
        return f"no {missing}"
    if _is_source(p) and not _publisher(fm):
        return "no publisher"
    if _is_source(p) and _old_format(p):   # no section bounds: its workflow text would leave with its summary
        return "old source format"
    return ""


def plan_export(pages, result, build_id: str) -> Plan:
    if result.critical:
        raise NotClean(f"build {build_id} has {len(result.critical)} critical error(s): fix them and rebuild")
    plan = Plan(build_id=build_id, report={"held_back": []})
    for p in pages:
        fm = p.frontmatter
        if not _in_scope(p):
            continue
        reason = _held_back(p)
        if reason:
            plan.report["held_back"].append({"aba_id": fm["id"], "path": p.rel_path, "reason": reason})
            continue
        valid = date.fromisoformat(str(fm["last_reviewed"])) + timedelta(days=VALID_DAYS)
        # a source's guidance is a Standard note under its publisher; the library's own pages are Synthesis notes
        kind, authority = ("standard", _publisher(fm)) if _is_source(p) else ("synthesis", SYNTHESIS_AUTHORITY)
        for sid, heading, text, extra in _parts(p):
            plan.notes.append(Note(
                file=f"{fm['id']}--{sid}.md",
                front={"title": f"{fm['title']} — {heading}", "kind": kind, "aba_id": fm["id"], "aba_section": sid,
                       "authority": authority, "author": str(fm["accepted_by"]),
                       "valid_until": valid.isoformat(), "retrieval_status": fm["retrieval_status"],
                       "build_id": build_id, **extra},
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
