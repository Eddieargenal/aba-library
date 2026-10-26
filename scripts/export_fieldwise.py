#!/usr/bin/env python3
"""
export_fieldwise.py — the FieldWise vault export (FieldWise PRD #30; ADR-0006 in FieldWise: the vault is written only
here).

A clean build becomes one zip that FieldWise imports. Each anchored section of a usable or limited synthesis page
becomes one Synthesis note: Markdown with simple `key: value` front matter, titled "Page title — Section". An
extracted source page becomes Standard notes under its publisher (issue #51): its fixed guidance sections (split at
subheadings when long), one note per finding and one tension note per Known Tensions row.
Each note ends with labelled link lines (Same page, Tensions, Sources, Related) built only from the build's valid
graph edges (issue #52); links that cannot be written are listed in the report.

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

from schema import LICENCE_FIELDS

ALL_RIGHTS_RESERVED = "all-rights-reserved"

FORMAT = "fieldwise-vault/1"
SYNTHESIS_AUTHORITY = "FieldWise ABA library"
SYNTHESIS_LICENCE = "aba-library"   # written in this library; its short quotes stay under their sources' terms
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
TENSION_RELATIONS = {"known_tension", "contradicts"}
# a body link to a page: [[slug]], [[slug#part|alias]], or a Markdown link to a .md path; web links stay as they are
BODY_LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]*))?\]\]|\[([^\]]*)\]\(([^)\s]+\.md)(?:#[^)]*)?\)")
PAGE_FIELDS = ("promotion_stage", "lifecycle_stage", "limited_to", "sectors")
# a short quote from an all-rights-reserved source: about two sentences (CONTEXT.md, Licence)
QUOTE = re.compile(r'"([^"\n]+)"|“([^”\n]+)”')
QUOTE_WORDS, QUOTE_SENTENCES = 50, 2
LINK_LABELS = ("Same page", "Tensions", "Sources", "Related")   # the line labels FieldWise reads, in this order
# a finding is a "**F-001** — claim" paragraph or a "| F-001 | claim |" table row; "→ see <object>" pointers are dropped
FINDING = re.compile(r"(?m)^(?:\*\*(F-\d+)\*\*\s*—\s*|\|\s*(F-\d+)\s*\|\s*)([^|\n]+?)(?:\s*→ see ([^|\n]*))?\s*(?:\||$)")


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
    for in_text, in_table, claim, _ in FINDING.findall(text):
        fid = in_text or in_table
        f = meta.get(fid, {})
        if f.get("finding_type") == "task-seed":
            continue
        body = claim.strip()
        if f.get("source_pages"):
            body += "\n\nPages: " + ", ".join(f["source_pages"])
        stages = ", ".join(f.get("lifecycle_stage") or [])   # none of its own: the source's stages stay
        out.append((f"finding-{fid.lower()}", f"Finding {fid}", body, {"lifecycle_stage": stages} if stages else {}))
    return out


def _tension_rows(text):
    """(first line, end line, rows) of the Known Tensions table in a section's lines; rows hold each tension's short
    ID, both positions with their pages, why it matters and its related object IDs. None when there is no table."""
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith("|") and "Tension ID" in l), None)
    if start is None:
        return None
    end = next((i for i in range(start, len(lines)) if not lines[i].startswith("|")), len(lines))
    rows = []
    for row in lines[start + 2:end]:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        tid, first, first_at, second, second_at, _type, why, objects = (cells + [""] * 8)[:8]
        rows.append({"short": "TNS-" + tid.rsplit("TNS-", 1)[-1], "first": first, "first_at": first_at,
                     "second": second, "second_at": second_at, "why": why,
                     "objects": {o.strip() for o in objects.split(",") if o.strip()}})
    return start, end, rows


def _tensions(heading, text) -> List[tuple]:
    """One tension note per row of the Known Tensions table, in FieldWise's tension format. The text outside the
    table stays as the section note, so each tension is in one note only; no text left means no section note."""
    table = _tension_rows(text)
    if table is None:
        return [("known-tensions", heading, text, {})]
    start, end, rows = table
    out = []
    for r in rows:
        body = f"Position A: {r['first']} ({r['first_at']})\nPosition B: {r['second']} ({r['second_at']})"
        if r["why"]:
            body += f"\nWhy it matters: {r['why']}"
        out.append((r["short"].lower(), f"Tension {r['short']}", body, {"role": "tension"}))
    lines = text.splitlines()
    rest = re.sub(r"\n{3,}", "\n\n", "\n".join(lines[:start] + lines[end:])).strip()
    if rest != lines[0].strip():   # more than the heading is left
        out.insert(0, ("known-tensions", heading, rest, {}))
    return out


def _tension_objects(p) -> Dict[str, set]:
    """{tension note section ID: the object IDs its row relates to} for a source page."""
    for sid, _, text in _sections(p.body):
        table = _tension_rows(text) if sid == "known-tensions" else None
        if table:
            return {r["short"].lower(): r["objects"] for r in table[2]}
    return {}


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


def _page_fields(fm, is_source=False) -> Dict[str, str]:
    """The page fields FieldWise reads from each note (issue #53), as one-line text; lists are comma-joined and an
    empty field is left out. A source's notes are at the finding stage: one source's extracted claims, which never
    count alone at FieldWise's highest tier."""
    # a Standard note is under its source's licence; a Synthesis note is the library's own text
    out = {"promotion_stage": "finding", "licence": str(fm["licence"])} if is_source else {"licence": SYNTHESIS_LICENCE}
    for key in PAGE_FIELDS:
        v = fm.get(key)
        text = ", ".join(str(x) for x in v) if isinstance(v, list) else str(v or "")
        if text.strip():
            out.setdefault(key, " ".join(text.split()))
    if fm.get("bundle") is True:   # marked for FieldWise's static bundle; entry still needs approval there
        out["bundle"] = "true"
    v = fm.get("search_terms")
    terms = [" ".join(t.split()) for t in v if isinstance(t, str) and t.strip()] if isinstance(v, list) else []
    if terms:   # an officer's words for the page's issue: FieldWise searches them and never shows them
        out["search_terms"] = ", ".join(terms)
    return out


def _held_back(p) -> str:
    """Why a page in scope stays in the library, or "" when it is exported."""
    fm = p.frontmatter
    missing = next((f for f in ("last_reviewed", "accepted_by") if not fm.get(f)), None)
    if missing:   # a page nobody reviewed, or nobody accepted, never becomes approved guidance
        return f"no {missing}"
    if _is_source(p) and not _publisher(fm):
        return "no publisher"
    if _is_source(p) and not all(str(fm.get(f) or "").strip() for f in LICENCE_FIELDS):
        return "no checked licence"   # a person has not checked the publication's terms: nothing of it leaves
    if _is_source(p) and fm.get("licence") == ALL_RIGHTS_RESERVED:   # only short quotes in synthesis pages leave
        return "all rights reserved"
    if _is_source(p) and _old_format(p):   # no section bounds: its workflow text would leave with its summary
        return "old source format"
    return ""


def plan_export(pages, result, build_id: str) -> Plan:
    if result.critical:
        raise NotClean(f"build {build_id} has {len(result.critical)} critical error(s): fix them and rebuild")
    plan = Plan(build_id=build_id, report={"held_back": [], "no_derivatives": []})
    named = {}   # all-rights-reserved sources: named by title in synthesis notes, never linked
    for p in pages:
        fm = p.frontmatter
        if not _in_scope(p):
            continue
        reason = _held_back(p)
        if reason:
            plan.report["held_back"].append({"aba_id": fm["id"], "path": p.rel_path, "reason": reason})
            if reason == "all rights reserved":
                named[fm["id"]] = fm["title"]
            continue
        if _is_source(p) and str(fm["licence"]).endswith("-nd"):   # notes are summaries: a person decides if they fit
            plan.report["no_derivatives"].append({"aba_id": fm["id"], "licence": str(fm["licence"])})
        valid = date.fromisoformat(str(fm["last_reviewed"])) + timedelta(days=VALID_DAYS)
        # a source's guidance is a Standard note under its publisher; the library's own pages are Synthesis notes
        kind, authority = ("standard", _publisher(fm)) if _is_source(p) else ("synthesis", SYNTHESIS_AUTHORITY)
        for sid, heading, text, extra in _parts(p):
            plan.notes.append(Note(
                file=f"{fm['id']}--{sid}.md",
                front={"title": f"{fm['title']} — {heading}", "kind": kind, "aba_id": fm["id"], "aba_section": sid,
                       "authority": authority, "author": str(fm["accepted_by"]),
                       "valid_until": valid.isoformat(), "retrieval_status": fm["retrieval_status"],
                       "build_id": build_id, **_page_fields(fm, _is_source(p)), **extra},
                body=text))
    plan.report["long_quotes"] = _long_quotes(plan.notes, pages, named)
    plan.report["dropped_links"] = _add_links(plan.notes, pages, result.valid_edges, result.unresolved_edges, named)
    return plan


def _finding_objects(p) -> Dict[str, str]:
    """{object ID: finding ID} from the "→ see <object>" pointers of a source's findings."""
    out = {}
    for sid, _, text in _sections(p.body):
        if sid == "findings":
            for in_text, in_table, _, see in FINDING.findall(text):
                for oid in re.findall(r"[A-Za-z0-9-]+-[A-Z]+-\d+", see):
                    out.setdefault(oid, in_text or in_table)
    return out


def _unique(items) -> List[str]:
    return list(dict.fromkeys(items))


class _Links:
    """The link lines of every exported note, from the build's valid graph edges. A link to a page points to its
    first exported note (a source's first note is its Summary)."""

    def __init__(self, notes, pages, edges, unresolved, named=None):
        self.named = named or {}   # {source ID: title} of sources named without a link
        self.first, self.by_page, self.titles = {}, {}, {}
        for n in notes:
            self.first.setdefault(n.front["aba_id"], n.front["title"])
            self.by_page.setdefault(n.front["aba_id"], []).append(n.front["title"])
            self.titles[(n.front["aba_id"], n.front["aba_section"])] = n.front["title"]
        self.pages = {p.frontmatter.get("id"): p for p in pages}
        self.stems = {}   # how a body link names a page: its file name or its ID
        for p in pages:
            self.stems.setdefault(Path(p.rel_path).stem, p.frontmatter.get("id"))
            self.stems.setdefault(str(p.frontmatter.get("id")), p.frontmatter.get("id"))
        self.dropped, self.out = [], {}   # out: {page: {relation: [target page IDs]}} for valid exported edges
        for e in edges:
            if e["from"] not in self.first:
                continue
            if e["to"] in self.first:
                self.out.setdefault(e["from"], {}).setdefault(e["relation"], []).append(e["to"])
            else:
                self.dropped.append({"from": e["from"], "relation": e["relation"], "to": e["to"],
                                     "reason": "not exported"})
        self.unresolved = [{"from": e["from"], "relation": e["relation"], "to": e["to"], "reason": "unresolved"}
                           for e in unresolved if e["from"] in self.first]
        self.findings = {s: _finding_objects(self.pages[s]) for s in self.first if _is_source(self.pages[s])}
        self.rows = {s: _tension_objects(self.pages[s]) for s in self.findings}

    def _targets(self, page, relations=None, but=()) -> List[str]:
        """The exported pages a page links to through these relations (all when None), less the ones in but."""
        return [t for r, ts in self.out.get(page, {}).items()
                if (relations is None or r in relations) and r not in but for t in ts]

    def _evidence(self, page):
        """(source, finding IDs, object IDs) for each source_basis item of a page that is a valid exported edge:
        the item's finding_ids and object_id, each completed through the source's "→ see" pointers."""
        for item in self.pages[page].frontmatter.get("source_basis") or []:
            src = item.get("source_id") if isinstance(item, dict) else None
            if src not in self._targets(page, {"source_basis"}):
                continue
            objects = self.findings.get(src, {})
            fids = list(item.get("finding_ids") or [])
            oids = {o for o, f in objects.items() if f in fids}
            if item.get("object_id"):
                oids.add(item["object_id"])
                fids += [objects[item["object_id"]]] if item["object_id"] in objects else []
            yield src, fids, oids

    def _resting_on(self, src, oids) -> List[str]:
        """The tension notes of a source whose row relates to one of these objects."""
        return [self.titles[(src, sec)] for sec, objs in self.rows.get(src, {}).items()
                if objs & oids and (src, sec) in self.titles]

    def sources(self, page) -> List[str]:
        """The finding notes behind a page's evidence objects, or the source's Summary when no exported finding
        matches."""
        out = []
        for src, fids, _ in self._evidence(page):
            found = [self.titles[(src, f"finding-{f.lower()}")] for f in fids
                     if (src, f"finding-{f.lower()}") in self.titles]
            out += found or [self.first[src]]
        return out

    def tensions(self, page, section) -> List[str]:
        """Known tension and contradicts edges, and the tension rows whose related objects this note rests on: a
        finding rests on the objects its pointer names, a page on its evidence objects."""
        out = [self.first[t] for t in self._targets(page, TENSION_RELATIONS)]
        if page in self.findings:
            out += self._resting_on(page, {o for o, f in self.findings[page].items()
                                           if section == f"finding-{f.lower()}"})
        for src, _, oids in self._evidence(page):
            out += self._resting_on(src, oids)
        return out

    def rewrite_body(self, page, body) -> str:
        """A body link becomes a wikilink to the target's first note when it matches a valid edge from the page;
        otherwise it becomes plain text and is reported."""
        def one(m):
            slug, alias, text, path = m.groups()
            label = alias or text
            target = self.stems.get(Path(path).stem if path else slug.strip())
            if target in self._targets(page):
                return f"[[{self.first[target]}|{label}]]" if label else f"[[{self.first[target]}]]"
            self.dropped.append({"from": page, "relation": "body", "to": path or slug.strip(),
                                 "reason": "no valid edge"})
            return label or slug.strip().replace("-", " ")
        return BODY_LINK.sub(one, body)

    def lines(self, note) -> List[str]:
        page, title = note.front["aba_id"], note.front["title"]
        links = {"Same page": [t for t in self.by_page[page] if t != title],
                 "Tensions": self.tensions(page, note.front["aba_section"]),
                 "Sources": self.sources(page),
                 "Related": [self.first[t] for t in self._targets(page, but=TENSION_RELATIONS | {"source_basis"})]}
        plain = {"Sources": self.named_sources(page)}
        return [f"{label}: " + " ".join([f"[[{t}]]" for t in _unique(links[label])] + plain.get(label, []))
                for label in LINK_LABELS if links[label] or plain.get(label)]

    def named_sources(self, page) -> List[str]:
        """The all-rights-reserved sources a page's evidence rests on, as plain text: they give no notes to link."""
        items = self.pages[page].frontmatter.get("source_basis") or []
        return _unique(f"{self.named[i['source_id']]} (all rights reserved)" for i in items
                       if isinstance(i, dict) and i.get("source_id") in self.named)


def _long_quotes(notes, pages, named) -> List[Dict[str, Any]]:
    """Quotes over the short-quote limit in synthesis notes whose page cites an all-rights-reserved source. Such a
    source may leave only as short quotes with the page, so each long one is for a person to cut; it does not block."""
    by_id = {p.frontmatter.get("id"): p for p in pages}
    out = []
    for n in notes:
        if n.front["kind"] != "synthesis":
            continue
        cited = [i.get("source_id") for i in by_id[n.front["aba_id"]].frontmatter.get("source_basis") or []
                 if isinstance(i, dict) and i.get("source_id") in named]
        for src in _unique(cited):
            for m in QUOTE.finditer(n.body):
                q = m.group(1) or m.group(2)
                words, sentences = len(q.split()), len(re.findall(r"[.!?](?:\s|$)", q))
                if words > QUOTE_WORDS or sentences > QUOTE_SENTENCES:
                    out.append({"aba_id": n.front["aba_id"], "aba_section": n.front["aba_section"], "source": src,
                                "words": words, "sentences": sentences, "start": q[:60]})
    return out


def _add_links(notes, pages, edges, unresolved, named=None) -> List[Dict[str, str]]:
    """End each note with labelled link lines of wikilinks to exported note titles, which FieldWise follows by kind.
    Returns the links dropped from exported pages: edges to pages that are not exported, body links that match no
    valid edge, and unresolved edges."""
    links = _Links(notes, pages, edges, unresolved, named)
    for n in notes:
        n.body = links.rewrite_body(n.front["aba_id"], n.body)
        block = links.lines(n)
        if block:
            n.body = n.body.rstrip() + "\n\n" + "\n".join(block)
    return links.dropped + links.unresolved


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
