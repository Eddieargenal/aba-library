---
type: agent-prompt
prompt_id: build-concept-pages-from-sources
status: operational
created: 2026-05-11
updated: 2026-05-11
---

# Build Concept Pages from Extracted Sources

## Purpose

Build or rewrite concept pages in `./02-concepts/` using material drawn exclusively from files in `./01-sources/extracted/`. Concepts are identified bottom-up from what the literature actually defines, not top-down from a predetermined taxonomy.

This prompt runs in two phases:
- **Phase 1 — Concept identification:** scan all extracted files and cluster concepts into families
- **Phase 2 — Concept definition:** for each concept family, do a full-file pass across all extracted files and synthesize a complete concept page

Do not write concept pages from general knowledge. Every claim in a concept page must trace to at least one extracted source file.

---

## Phase 1 — Concept identification and clustering

### Step 1.1 — Collect raw concept candidates

Read every file in `./01-sources/extracted/`. For each file, extract all bullets from the `# Key concepts` section. Record:
- The concept name (the term before the colon)
- The definition as stated
- The source filename and page reference

Do this for all files before moving to clustering.

### Step 1.2 — Cluster into concept families

Group the raw candidates into concept families. A concept family is a set of candidates that refer to the same underlying idea, even if named slightly differently across sources.

Rules:
- Merge candidates with the same referent even if the label differs (e.g., "area-based approach," "ABA," "neighbourhood approach," "settlement approach" may cluster depending on how sources use them — check definitions, not just labels)
- Do NOT merge concepts that share a label but have genuinely different referents (e.g., "resilience" as community capacity vs. "resilience" as engineering property — keep separate and flag as contested)
- A concept that appears in only one file is still a valid candidate; note it as low-corroboration

### Step 1.3 — Score each concept family

For each concept family, count:
- **Source count:** how many extracted files define or use this concept
- **Definition convergence:** do the definitions agree (consistent), partially agree (partial), or conflict (contested)?
- **Operationalizability:** does at least one source attach a tool, method, or decision framework to this concept?

Output a prioritized concept list in this format:

| Concept family | Source count | Convergence | Operationalizable | Notes |
|---|---|---|---|---|
| Area-based approach | 8 | Consistent | Yes | Core — build first |
| Urban resilience | 4 | Contested | Yes | 4 competing definitions |
| Neighbourhood (place/community/policy unit) | 3 | Partial | No | Definitional debate is the content |
| ... | | | | |

Build concept pages in descending order of source count. Do not skip low-corroboration concepts — flag them as emerging and note which single source grounds them.

---

## Phase 2 — Concept definition (full-file pass)

For each concept family, do a second complete pass through all extracted files — not just the `# Key concepts` section. Collect material from every section that mentions or implies the concept.

### Step 2.1 — Full-file collection per concept

For each concept family, scan every extracted file for relevant material in these sections, in this order:

| Section | What to collect |
|---|---|
| `# Key concepts` | Primary definition(s) and page references |
| `# Summary` | How the document frames or uses this concept — often contains the most concise statement of why the concept matters |
| `# Claims worth citing` | Citable formulations — these become the concept page's quotable claims |
| `# Limitations / cautions` | Scope limits, contested applications, when the concept breaks down — these become counterexamples and known risks |
| `# Coordination implications` | How the concept behaves in multi-actor settings |
| `# DRR implications` | How the concept applies to risk reduction contexts |
| `# Operational implications` | Practical constraints and enabling conditions |
| `# Tools or methods extracted` | Operationalizable instruments linked to this concept |
| `# Field data collection implications` | What evidence is needed to assess or apply this concept in the field |
| `# Project lifecycle relevance` | At which project phases this concept is most active |

Record source filename and page reference for every item collected.

### Step 2.2 — Identify the authoritative definition

When multiple sources define the same concept:
1. Prefer the definition that is most precise and most broadly supported across sources
2. If definitions genuinely conflict, present all variants and name each by source
3. If one source is the origin (first to define it, or cited by others), mark it as the primary authority
4. Do not invent a synthetic definition that no source states — synthesize the framing, not the definition itself

### Step 2.3 — Write the concept page

Write the concept page using the structure below. Every section must draw from the collected material. Do not add sections; do not remove sections; do not merge sections.

---

## Concept page structure

Save to: `./02-concepts/CONCEPT-SLUG.md`

Use kebab-case for the filename. Match or improve on existing filenames in `./02-concepts/` where pages already exist.

```markdown
---
type: concept
status: active
maturity: [seed | sapling | evergreen]
source_count: [number of extracted files that define or use this concept]
related_tools:
  - [tool filenames without path, from 04-tools/]
related_lifecycle_stages:
  - "[stage name]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

**Maturity rules:**
- `seed` — defined in 1 source; no operationalizable instrument attached
- `sapling` — defined in 2+ sources; evidence base present; missing counterexamples or open questions
- `evergreen` — defined in 3+ sources; evidence base present; counterexamples documented; open questions stated; at least one tool attached

---

### `# Definition`

One paragraph maximum. State the concept as precisely as the sources allow.

If sources agree: write a single authoritative definition and cite the primary source.

If sources partially agree: write the core shared definition, then note variations in a sub-list:
```markdown
Variants across sources:
- [Source A (year)]: "..." (p. X)
- [Source B (year)]: "..." (p. X)
```

If sources contest the concept: state the contested territory directly — do not paper over disagreement with vague synthesis. Example: "'Urban resilience' has no single agreed definition across sources in this wiki. Four formulations are in use: ..."

Include a blockquote for the single most citable definition in the entire source set:
```markdown
> "Direct quote or close paraphrase" — Author (year, p. X)
```

---

### `# Why it matters for urban DRR and response`

2–4 bullets. State what error, misallocation, or coordination failure this concept prevents when correctly applied.

Derive from: `# Summary`, `# DRR implications`, `# Operational implications` sections across source files.

Do not restate the definition — focus on the consequence of applying vs. misapplying this concept.

---

### `# Evidence base`

Organized by source. For each source that defines or significantly uses this concept:

```markdown
## [Short source label, year]
[2–4 bullets drawn from that source's Key concepts, Claims worth citing, and Summary sections. Each bullet cites a page.]
```

If the same point is made identically across multiple sources, cite the primary one and note: "Confirmed in [Source B], [Source C]."

---

### `# How this concept is contested or misused`

3–5 bullets. Draw from:
- `# Limitations / cautions` sections across all files
- Cases where multiple sources define the concept differently
- Cases where a source explicitly states what this concept is NOT

Format:
```markdown
- **Common conflation:** [what people wrongly equate this with] — [why that's wrong per sources]
- **Scope limit:** [condition under which the concept does not apply] — [source + page]
- **Contested definition:** [the specific point of disagreement between sources]
```

This section is required even for well-established concepts. If no conflation or misuse is documented in the sources, state: "No conflation or misuse documented in current source set — revisit as additional sources are ingested."

---

### `# Practical implications for field teams`

4–6 bullets. Derive from `# Operational implications`, `# Field data collection implications`, and `# Coordination implications` sections across files.

Each bullet should answer: "what does a field practitioner need to do differently because of this concept?"

Where a source attaches a tool or method, name it and link it.

---

### `# Open questions`

2–4 bullets. State what this concept cannot yet answer — derived from:
- `# Limitations / cautions` that flag unresolved evidence
- Open questions explicitly stated in source summaries
- Points where sources disagree without resolution

Format: plain statement of the unresolved question. Do not guess at answers.

---

### `# Links to tools`
```markdown
- [[../04-tools/TOOL-SLUG]]
```
Only link tools that the source material explicitly connects to this concept (via `# Tools or methods extracted` or `# Links to tool pages` in the extracted files). Do not add tools speculatively.

---

### `# Links to source pages`
```markdown
- [[../01-sources/extracted/FILENAME]] — [one-line note on how this source contributes]
```
List every extracted file that defined or substantially used this concept. Note the contribution, not just the link.

---

### `# Links to related concepts`
```markdown
- [[CONCEPT-SLUG]] — [one-line note on the relationship]
```
Only link concepts that the sources explicitly connect. Do not infer connections from general domain knowledge.

---

## Phase 2 output checklist

Before finalizing each concept page:

- [ ] Definition traces to at least one extracted source with page reference
- [ ] All contested definitions are named by source, not papered over
- [ ] "How this concept is contested or misused" section is substantive
- [ ] No claims added from general knowledge without a source file backing them
- [ ] `source_count` in frontmatter matches actual count of files referencing the concept
- [ ] `maturity` level correctly reflects source count, evidence base, and counterexample depth
- [ ] Tool links only point to tools explicitly mentioned in source material
- [ ] Source page links cover all files that contributed material

---

## Handling existing concept pages

If a concept page already exists in `./02-concepts/`:

1. Read the existing page first
2. Check whether its claims are already supported by the extracted source material
3. If yes: add source citations to existing claims, enrich with material from the full-file pass, update `source_count` and `maturity`
4. If no: flag the unsourced claim in a comment `<!-- unsourced: verify or remove -->` — do not delete without review
5. If the existing page is richer than what the sources support: keep the richer content but add source citations where possible and flag gaps

Do not delete existing concept pages. Rewrite and enrich in place.

---

## Sequence for this wiki

Based on the concept inventory from the extracted directory, build in this order:

**Tier 1 — Core, high source count, build or rewrite first:**
1. `area-based-approach` — 8+ sources
2. `urban-resilience` — 4 sources, contested definitions
3. `multi-stakeholder-engagement` — 5 sources
4. `geographic-targeting` — 3 sources
5. `participation-in-urban-response` — 3 sources
6. `urban-systems-thinking` — 3 sources

**Tier 2 — Important, moderate source count:**
7. `neighborhood-boundaries` — 3 sources, contested
8. `multi-sector-response-analysis` — 2 sources
9. `urban-displacement-vulnerability` — 2 sources
10. `area-based-coordination` — 2 sources
11. `adaptive-management` — 2 sources
12. `implementation-sequencing` — 2 sources

**Tier 3 — Emerging, single source, build last:**
13. `pilot-to-scale` — 1–2 sources
14. `contribution-vs-attribution-evaluation` — 1–2 sources
15. `drr-scope-and-sendai-targets` — 1 authoritative source
16. `convenor-role` — 1 source
17. `ki-reliability-boundaries` — 1 source (method-level concept)

---

## What not to do

- Do not write concept definitions from general knowledge — every definition needs a source file
- Do not merge contested definitions into a false consensus — disagreement between sources is content
- Do not add tools or related concepts not mentioned in the source material
- Do not build Tier 3 concepts before Tier 1 and Tier 2 are complete
- Do not treat the existing `02-concepts/` pages as authoritative — treat them as drafts to be validated against extracted sources
- Do not use the `concepts.md` flat glossary as source material — it is a framework-derived reference index, not a literature-grounded concept base
