---
type: skill
title: ABA/DRR Wiki Librarian
skill_id: librarian
version: 1.0.0
status: active
created: 2026-05-11
updated: 2026-05-11
installed_at: ~/.claude/skills/librarian/SKILL.md
invocation: /librarian [operation] [optional-context]
tags: [skill, librarian, wiki, aba, drr, operations]
operations: [open, close, query, ingest, extract, lint, build-index, build-concept, build-framework, build-tool, build-instrument, crosslink, review-tool, promote]
---

# ABA/DRR Wiki Librarian — Skill

Executes any wiki operation against the ABA/DRR Field Knowledge Wiki.
Invoke via `/librarian [operation] [optional-context]` in a Claude Code session.

The canonical skill file lives at `~/.claude/skills/librarian/SKILL.md`.
This vault copy is the authoritative reference for editing and version control.
After editing this file, sync to the installed path.

---

## Operations Reference

| Operation | Argument | What it does |
|---|---|---|
| `open` | — | Load handoff → check lint queue → clear compliance → ready |
| `close` | — | Fill handoff → update changelog → lint → rebuild index → append log |
| `query` | question | Frontmatter-first domain question answering with source citations |
| `ingest` | source-path or metadata | Full ingest pipeline: extract → wire → contradict-check → index |
| `extract` | pdf-path | Create structured extraction page with full frontmatter from raw PDF |
| `lint` | — | CRITICAL + HIGH + MEDIUM quality checks; file report |
| `build-index` | — | Run `scripts/build-index.py` to regenerate `indexes/agent-index.md` |
| `build-concept` | concept name (optional) | Two-phase concept ID + synthesis from extracted sources |
| `build-framework` | lifecycle-stage slug | Build Tier 1 framework with decision logic and failure modes |
| `build-tool` | decision question | Build tool with all 10 criteria per decision domain |
| `build-instrument` | tool_id | Generate field instrument with data quality checks |
| `crosslink` | — | Wire new pages into existing pages' frontmatter + wikilinks |
| `review-tool` | tool_id | Score all 10 criteria per domain; produce audit report |
| `promote` | page-slug | Check promotion gate eligibility with independence verification |

---

## Vault Root
`/Users/eddieargenal/Documents/obsidian-vault`

## Key File Paths
```
indexes/agent-index.md         ← query entry point
memory/current-handoff.md      ← session continuity
memory/runtime/logs/log.md     ← append-only operation log
governance/aba/CLAUDE.md       ← ABA domain operating rules
governance/schema/changelog.md ← schema change log
wiki/aba/01-sources/extracted/ ← extracted source pages
wiki/aba/02-concepts/          ← concept pages
wiki/aba/03-frameworks/        ← framework pages (Tier 1 + Tier 2)
wiki/aba/04-tools/             ← tool pages
wiki/aba/05-field-instruments/ ← field instrument pages
wiki/aba/outputs/internal/     ← lint reports, synthesis outputs
scripts/build-index.py         ← regenerates indexes/agent-index.md
```

---

## Read this first — always

Before executing any operation, confirm you have read `AGENTS.md` in the vault root.
It contains the operating model, session protocol, and promotion gates.

---

## OPEN — Session open protocol

**When**: At the start of every session before any other work.

**Steps:**

1. Read `memory/current-handoff.md`. Note:
   - In-progress tasks from the previous session
   - Open contradictions
   - Deferred compliance items
   - Recommended first action

2. Find the most recent lint report in `wiki/aba/outputs/internal/`. List files matching `lint-report-*.md`, open the most recent. Note all CRITICAL and HIGH findings.

3. Clear compliance queue before new work:
   - Resolve all CRITICAL findings now
   - Resolve HIGH findings unless the user explicitly defers them
   - Do not begin assigned work until the queue is clear

4. Confirm to the user: handoff loaded, lint queue reviewed, compliance items cleared (list what was cleared or deferred). Ready to begin.

---

## CLOSE — Session close protocol

**When**: At the end of every session before exiting.

**Steps:**

1. **Fill handoff.** Write a structured summary to `memory/current-handoff.md`:
   ```
   ## Session: YYYY-MM-DD
   ### Completed
   - [task]: [files changed]
   ### Open contradictions
   - [slug]: [description]
   ### Deferred items
   - [item]: [reason for deferral]
   ### Recommended first action next session
   [specific action]
   ```

2. **Update schema changelog if schema changed.** Append a row to `governance/schema/changelog.md`:
   `| YYYY-MM-DD | agent | description | files affected | migration notes |`

3. **Run lint.** Execute the LINT operation. File the report to `wiki/aba/outputs/internal/lint-report-YYYY-MM-DD.md`.

4. **Rebuild index.** Run: `python3 scripts/build-index.py`

5. **Append to log.** Append to `memory/runtime/logs/log.md`:
   ```
   ## [YYYY-MM-DD] maintenance | Session close
   - [key action 1]
   - files changed: [list]
   ```

---

## QUERY — Answer a domain question

**Context**: question to answer.

**Rule**: Never answer a tool question with only conceptual advice. Always include evidence collection, analysis method, and source citations.

**Steps:**

1. Read `indexes/agent-index.md`. Identify relevant pages by lifecycle_stage, type, status, title keywords.
2. Read only the 3–5 most relevant pages. Do not read all pages.
3. Check `wiki/aba/12-risks-contradictions/` for known tensions.
4. Produce structured answer:
   - Decision question · Evidence required · Field data points · Collection method
   - Relevant field instruments · Analysis method · Decision threshold
   - Source citations (source_id references) · Known tensions
5. If new reusable synthesis emerges: file to `wiki/aba/outputs/internal/` as type: synthesis.
6. Append to log: `## [YYYY-MM-DD] query | [brief description]`

---

## INGEST — Ingest a new source

**Context**: path to source file or metadata (title, author, year, URL).

**Steps:**
1. Determine canonical filename: `YYYY-org-author-short-title.md`
2. Run EXTRACT if source page doesn't exist yet
3. Set `contradicts:` field — read relevant concept/framework pages, check for conflicts; `[]` = checked and clear
4. Update affected concept pages (`source_count`, links)
5. Update affected tool pages (`source_foundation`)
6. Update affected framework pages (wikilinks)
7. Update affected field instruments if source describes data collection
8. Update `wiki/aba/12-risks-contradictions/` if contradiction found
9. Run BUILD-INDEX
10. Append to log: `## [YYYY-MM-DD] ingest | [Source title]`
11. Commit if git available

**Output checklist:**
- [ ] Extracted source page exists
- [ ] `contradicts:` field set (not missing)
- [ ] Affected pages updated
- [ ] `indexes/agent-index.md` regenerated
- [ ] Log entry appended

---

## EXTRACT — Extract a source page from a raw PDF

**Context**: path to PDF in `wiki/aba/01-sources/raw/`.

**Output**: `wiki/aba/01-sources/extracted/YYYY-org-author-short-title.md`

**Steps:**
1. Determine canonical filename (match PDF filename, swap `.pdf` → `.md`)
2. Read document: title, author, institution, year, URL, methodology, key findings, lifecycle stages, tools described, contradictions
3. Write extraction page with complete frontmatter (all required source fields)
4. Write body: `## Key Findings` · `## Key Concepts` · `## Methodology` · `## Lifecycle Stages` · `## Field Tools and Instruments` · `## Contradictions and Tensions` · `## Citation`
5. Run INGEST to wire into wiki

**Confidence:**
- `high` — direct field evidence (evaluation, assessment report)
- `medium` — practitioner judgment, expert synthesis, pilot evidence
- `low` — theoretical/untested (conceptual frameworks, policy guidance)

---

## LINT — Run wiki quality check

**Output**: `wiki/aba/outputs/internal/lint-report-YYYY-MM-DD.md`

**CRITICAL checks** (fix before any other work):
```bash
# C-1: Missing required frontmatter fields per type
python3 - <<'EOF'
import os, re, yaml
VAULT = "/Users/eddieargenal/Documents/obsidian-vault"
REQUIRED = {
    "source": ["type","source_id","confidence","lifecycle_stage","contradicts","created","updated"],
    "tool": ["type","title","tier","contradicts"],
    "field-instrument": ["type","instrument_id","title","related_tools","lifecycle_stage","data_quality_checks","contradicts"],
    "concept": ["type","title","contradicts","source_count"],
    "framework": ["type","framework_id","title","tier","contradicts"],
}
DIRS = {
    "source": "wiki/aba/01-sources/extracted",
    "concept": "wiki/aba/02-concepts",
    "framework": "wiki/aba/03-frameworks",
    "tool": "wiki/aba/04-tools",
    "field-instrument": "wiki/aba/05-field-instruments",
}
for ptype, rel_dir in DIRS.items():
    dirpath = os.path.join(VAULT, rel_dir)
    for fname in os.listdir(dirpath):
        if not fname.endswith(".md") or fname.startswith("00_"): continue
        content = open(os.path.join(dirpath, fname)).read()
        m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not m: print(f"CRITICAL C-1 no-frontmatter: {rel_dir}/{fname}"); continue
        try: fm = yaml.safe_load(m.group(1)) or {}
        except: print(f"CRITICAL C-1 yaml-error: {rel_dir}/{fname}"); continue
        for field in REQUIRED[ptype]:
            if field not in fm: print(f"CRITICAL C-1 missing-{field}: {rel_dir}/{fname}")
EOF

# C-2: contradicts field absent
grep -rL "^contradicts:" wiki/aba/01-sources/extracted/ wiki/aba/02-concepts/ wiki/aba/03-frameworks/ wiki/aba/04-tools/ 2>/dev/null

# C-3: validated tools with empty field_instruments
python3 - <<'EOF'
import os, re, yaml
VAULT = "/Users/eddieargenal/Documents/obsidian-vault"
tooldir = os.path.join(VAULT, "wiki/aba/04-tools")
for fname in os.listdir(tooldir):
    if not fname.endswith(".md") or fname.startswith("00_"): continue
    content = open(os.path.join(tooldir, fname)).read()
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m: continue
    try: fm = yaml.safe_load(m.group(1)) or {}
    except: continue
    if fm.get("status") == "validated" and not fm.get("field_instruments"):
        print(f"CRITICAL C-3: wiki/aba/04-tools/{fname}")
EOF
```

**HIGH checks:**
```bash
# H-1: validated instruments without data_quality_checks
python3 - <<'EOF'
import os, re, yaml
VAULT = "/Users/eddieargenal/Documents/obsidian-vault"
instdir = os.path.join(VAULT, "wiki/aba/05-field-instruments")
for fname in os.listdir(instdir):
    if not fname.endswith(".md") or fname.startswith("00_"): continue
    content = open(os.path.join(instdir, fname)).read()
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m: continue
    try: fm = yaml.safe_load(m.group(1)) or {}
    except: continue
    if fm.get("status") == "validated" and fm.get("data_quality_checks") is False:
        print(f"HIGH H-1: wiki/aba/05-field-instruments/{fname}")
EOF

# H-2: established/contested concepts with source_count < 2
python3 - <<'EOF'
import os, re, yaml
VAULT = "/Users/eddieargenal/Documents/obsidian-vault"
conceptdir = os.path.join(VAULT, "wiki/aba/02-concepts")
for fname in os.listdir(conceptdir):
    if not fname.endswith(".md") or fname.startswith("00_"): continue
    content = open(os.path.join(conceptdir, fname)).read()
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m: continue
    try: fm = yaml.safe_load(m.group(1)) or {}
    except: continue
    if fm.get("maturity") in ("established","contested") and (fm.get("source_count") or 0) < 2:
        print(f"HIGH H-2 ({fm.get('source_count','?')} sources): wiki/aba/02-concepts/{fname}")
EOF

# H-3: tools with empty field_instruments
python3 - <<'EOF'
import os, re, yaml
VAULT = "/Users/eddieargenal/Documents/obsidian-vault"
tooldir = os.path.join(VAULT, "wiki/aba/04-tools")
for fname in os.listdir(tooldir):
    if not fname.endswith(".md") or fname.startswith("00_"): continue
    content = open(os.path.join(tooldir, fname)).read()
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m: continue
    try: fm = yaml.safe_load(m.group(1)) or {}
    except: continue
    if not fm.get("field_instruments"):
        print(f"HIGH H-3: wiki/aba/04-tools/{fname}")
EOF
```

**MEDIUM checks:**
```bash
# M-1: orphan pages (no inbound wikilinks)
python3 - <<'EOF'
import os, re
VAULT = "/Users/eddieargenal/Documents/obsidian-vault"
DIRS = ["wiki/aba/01-sources/extracted","wiki/aba/02-concepts","wiki/aba/03-frameworks","wiki/aba/04-tools","wiki/aba/05-field-instruments"]
all_pages = {}
for d in DIRS:
    for f in os.listdir(os.path.join(VAULT, d)):
        if f.endswith(".md") and not f.startswith("00_"):
            all_pages[f.replace(".md","")] = 0
link_re = re.compile(r'\[\[([^\]|]+)')
for root, dirs, files in os.walk(os.path.join(VAULT, "wiki/aba")):
    for f in files:
        if not f.endswith(".md"): continue
        for m in link_re.findall(open(os.path.join(root, f), errors="ignore").read()):
            slug = m.strip().split("/")[-1]
            if slug in all_pages: all_pages[slug] += 1
orphans = [k for k,v in all_pages.items() if v == 0]
print("\n".join(f"MEDIUM M-1 orphan: {k}" for k in sorted(orphans)) or "NONE")
EOF
```

**Report format:**
```yaml
---
type: lint-report
status: complete
generated: YYYY-MM-DD
method: librarian-skill
---
```
Include: summary table, then CRITICAL / HIGH / MEDIUM findings with exact file paths.

**Log entry:**
```
## [YYYY-MM-DD] lint | Weekly wiki quality check
- pages scanned: N | critical: N | high: N | medium: N
- report: wiki/aba/outputs/internal/lint-report-YYYY-MM-DD.md
```

---

## BUILD-INDEX — Regenerate the agent index

```bash
python3 /Users/eddieargenal/Documents/obsidian-vault/scripts/build-index.py
```
Confirm count. Append to log: `## [YYYY-MM-DD] maintenance | Rebuilt agent index — N pages`

---

## BUILD-CONCEPT — Build concept pages from extracted sources

**Context**: concept family name (optional — omit for full pass).

**Rule**: Every claim must trace to at least one extracted source. Never write from general knowledge.

**Phase 1 — Identify candidates** (skip for single concept rebuild):
1. Read all `wiki/aba/01-sources/extracted/` — extract `## Key Concepts` sections
2. Cluster by shared referent; score by source_count, convergence, operationalizability
3. Prioritize: ≥2 independent sources + ABA/DRR relevance

**Phase 2 — Build page**:
1. Full-file pass across ALL sections of all extracted files for the target concept
2. Write concept page with complete frontmatter (type, title, status: draft, maturity, source_count, related_tools, related_frameworks, related_concepts, related_lifecycle_stages, known_tensions, contradicts, used_by_outputs, created, updated)
3. Body: `## Definition` · `## Operationalization` · `## Evidence Base` · `## Known Tensions` (if any) · `## Promotion Status`
4. Set source_count = number of independent sources (verify distinct evidence bases)
5. Flag for promotion if source_count ≥ 2
6. Run BUILD-INDEX

---

## BUILD-FRAMEWORK — Build a framework page

**Context**: lifecycle stage slug.

**Do NOT create if**: framework already exists, source material not ingested, or logic belongs in a tool page.

**Steps:**
1. Read `wiki/aba/03-frameworks/00_frameworks-index.md` — confirm gap
2. Read gold standard: `wiki/aba/03-frameworks/2017-aba-appropriateness-decision-framework.md`
3. Read relevant extracted sources (query by lifecycle_stage)
4. Write framework page with complete frontmatter (tier: 1, source_foundation: [≥2 independent])
5. Body: `## Decision Question` · `## Use Conditions` · `## Decision Logic` · `## Evidence Requirements` · `## Known Failure Modes` · `## Source Foundation` · `## Known Tensions`
6. source_foundation < 2 → status: draft, flag gap
7. Run BUILD-INDEX

---

## BUILD-TOOL — Build a tool page

**Context**: decision question.

**Quality standard**: Tool FAILS if it only lists questions without defining evidence collection.

**Steps:**
1. Confirm Tier 1 framework covers this decision — if not, run BUILD-FRAMEWORK first
2. Read index + relevant framework and concept pages
3. Define 3–7 decision domains. For each, define ALL 10: decision question · evidence required · field data points · collection method · respondent/source · field instrument · analysis method · scoring rule · data quality checks · risks/safeguards · source_ids
4. Write tool page with complete frontmatter (tool_id, tier: 1, field_instruments: [], ...)
5. Run BUILD-INSTRUMENT for any domain without a linked instrument
6. status: validated requires all field_instruments linked + data_quality_checks: true — human approves
7. Run BUILD-INDEX

---

## BUILD-INSTRUMENT — Generate a field instrument

**Context**: tool_id.

**Steps:**
1. Read parent tool page — identify domains needing instruments
2. For each domain: choose format, design questions with enumerator guidance, define skip patterns and cross-checks
3. Write instrument page with complete frontmatter (instrument_id, format, related_tools, data_quality_checks: true)
4. Body: `## Purpose` · `## Instructions` · `## Questions / Fields` · `## Data Quality Checks` · `## Analysis Use` · `## Ethical Safeguards`
5. Add instrument_id to parent tool's `field_instruments:` list
6. Set data_quality_checks: true only when `## Data Quality Checks` is fully defined
7. Run BUILD-INDEX

---

## CROSSLINK — Update cross-links

**Steps:**
1. For each new page: identify which existing pages should link to it
   - concept → tool/framework/source pages
   - tool → concept/framework pages
   - framework → tool/concept pages
   - instrument → parent tool page
2. Edit target page frontmatter lists + add `[[wikilink]]` in body
3. Run LINT orphan check
4. Run BUILD-INDEX
5. Append to log: `## [YYYY-MM-DD] maintenance | Updated cross-links`

---

## REVIEW-TOOL — Audit a tool page

**Context**: tool_id or filename.

**10-criterion scoring per domain:**
1. Evidence required · 2. Field data points · 3. Collection method · 4. Respondent/source
5. Field instrument (linked) · 6. Analysis method · 7. Scoring rule · 8. Data quality checks
9. Risks and safeguards · 10. Source foundation

**Steps:**
1. Read tool page
2. Score all 10 criteria per decision domain (✓ pass / ✗ fail / — missing)
3. Check frontmatter: field_instruments non-empty, source_foundation ≥2, contradicts set
4. Write findings to `wiki/aba/outputs/internal/tool-review-[tool-id]-YYYY-MM-DD.md`
5. Add `TODO[agent]: [description]` for each failed criterion

---

## PROMOTE — Check promotion eligibility

**Context**: page slug.

**Gates:**
| From | To | Requirement | Who approves |
|---|---|---|---|
| Finding | Concept page | ≥2 independent extracted sources | LLM proposes, human approves |
| Concept | Tier 1 framework | Decision logic + use conditions defined | Human approves |
| Framework | Linked tool/instrument | Scoring criteria + failure modes | Human approves |
| Tool draft | Tool validated | All instruments linked + DQ checks true | Human approves |

**Independence rule**: Two documents citing the same underlying evaluation are NOT independent.

**Steps:**
1. Read the page — identify type and status
2. Verify gate criteria; verify source independence for concepts
3. Output: current status · criteria met/not met · recommendation
4. If eligible: update status field, add `## Promotion Status` note for human review
5. Append to log: `## [YYYY-MM-DD] maintenance | Promotion check: [slug]`
