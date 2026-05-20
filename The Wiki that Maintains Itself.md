
# The Wiki That Maintains Itself

After thirty years of urban crisis response, the field has produced hundreds of frameworks, tools, and field guides. Most teams still rediscover the same lessons independently. The knowledge exists. It just doesn't accumulate.

The reason isn't apathy. Every humanitarian knowledge base starts the same way: a shared drive, a folder structure, a burst of enthusiasm. Within eighteen months it's a graveyard — not because the content was wrong, but because maintenance is labor-intensive and nobody planned for the labor. Updating cross-references, keeping concept summaries current when new evidence arrives, noting when a 2013 framework has been partly superseded by 2026 guidance — the bookkeeping grows faster than the value, and teams abandon it.

The ABA/DRR Field Knowledge Wiki is a different bet: assign the maintenance to an LLM, and design the architecture around the specific ways LLMs fail at that job.

Instead of retrieving from raw documents at query time and re-deriving the same synthesis on every question, the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files that sits between the raw source literature and the operational team. When a new guidance document arrives, the LLM reads it, extracts the key findings, and integrates them into the existing wiki: updating concept pages, revising framework summaries, noting where the new evidence reinforces or challenges existing synthesis, flagging contradictions that field teams need to resolve. The knowledge is compiled once and kept current — not re-derived on every query.

## The Shape of the System

The wiki has seven layers, each with a distinct role:

| Layer | What it is | What it does |
|---|---|---|
| **Raw sources** | Curated PDFs | The evidence floor — immutable, never modified |
| **Raw-content mirror** | Markdown text extracts | Fast local reading for agent tooling; derived, not authoritative |
| **Extracted sources** | One structured page per document | Key claims, methodology notes, integration map, and a required `contradicts:` field |
| **Wiki synthesis** | Concepts, frameworks, tools, risks, playbooks | The knowledge layer — where findings compound into operational guidance |
| **Compiled JSONL indexes** | Generated artifacts (`agent-index.jsonl`, `graph-edges.jsonl`, `section-index.jsonl`) | Machine-readable graph built from frontmatter; agents retrieve from here, never write to it |
| **Advisory agent pipeline** | Orchestrator, section agents, writing agent, reviewers | Converts a field question into validated guidance through evidence packets and a claim ledger |
| **Runtime layer** | Full, edge laptop, minimal offline, no-LLM | System degrades gracefully under low bandwidth, weak models, or no connectivity |

The trust hierarchy runs upward: raw sources are authoritative, extracted pages summarize them, wiki pages synthesize across multiple extracted pages, and compiled indexes are derived artifacts — never the source of truth. Markdown and frontmatter are canonical; everything else is generated from them.

## Who Does What

The human's job is to curate sources, approve promotions, resolve contradictions that require judgment, and ask operational questions. The LLM's job is everything else: reading new documents, updating cross-references, maintaining consistency across dozens of pages, flagging contradictions, running lint checks. In practice: LLM agent open on one side, Obsidian open on the other. The LLM edits wiki pages based on the conversation; you browse the results in real time — following links, checking the graph view, reading the updated pages.

A useful way to hold the model: *Obsidian is the IDE. The LLM is the programmer. The wiki is the codebase.*

The distinction matters because it clarifies what "quality-affecting decision" means. Promoting a finding to a concept page, approving a new Tier 1 framework, resolving a contradiction between two field evaluations — these require human judgment. Updating a cross-reference after an ingest, regenerating the index, running the weekly lint check — these don't.

## Designed for Failure

The architecture was built around specific LLM weaknesses. Understanding them is part of operating the system correctly.

| Failure mode | What happens without a fix | Architectural response |
|---|---|---|
| **False consensus** | LLMs synthesize toward agreement — genuine contradictions get quietly smoothed over | Required `contradicts:` field on every page type; missing field = CRITICAL lint failure |
| **Silent frontmatter omissions** | A missing `lifecycle_stage:` causes a page to vanish from agent queries — silently, with no error | Lint CRITICAL checks run before any new work begins |
| **Governance drift** | LLMs follow behavioral contracts at session start and drift under task pressure | Session open/close protocol enforced by the librarian skill; Stop hook catches close failures |
| **Source conflation** | Two documents citing the same underlying evaluation get treated as independent evidence | Source independence rule blocks promotion until distinct evidence bases are confirmed |
| **Runtime collapse** | If the model or connectivity fails, the system has no fallback | Four runtime modes (full → edge laptop → minimal offline → no-LLM); emergency playbooks and printable checklists work without any model |

Each countermeasure adds friction deliberately. The schema is not lean — it's load-bearing. And the system was designed to remain useful even when the model isn't there at all.

## A Session in Practice

Every session follows the same open/close discipline. At the start: read the handoff note from the last session, clear any CRITICAL lint items from the queue, then begin. At the close: fill the handoff note, run lint, rebuild the index, commit. The ritual is enforced structurally — the librarian skill is injected at every session start, and a Stop hook catches sessions that close without completing the protocol.

Ingest is the heaviest operation. You drop a new source PDF into the raw folder and ask the LLM to process it. It generates a markdown extract, creates a structured extracted source page with all required frontmatter, updates every concept, framework, and tool page the new source touches, and rebuilds the index. A single source typically touches 10–20 wiki pages. The LLM proposes any promotions the new evidence supports; you review and approve. Ingesting one source at a time and staying involved is recommended — read the extracted page, check the concept updates, guide the LLM on what to emphasize.

Querying runs through a pipeline. The Orchestrator receives a field question, classifies the decision domain and lifecycle stage, and decomposes the task into sections — each handled by a temporary retrieval agent that reads only the relevant pages and produces a compact evidence packet: a set of claims, each traced back to a specific source finding and page number. A packet consolidator assembles those packets into a claim ledger. The Writing Agent then drafts the final answer — but only from claims in the ledger. It cannot add unsupported advice, drop caveats, or cite sources not present in the bundle. Before output is delivered, a citation reviewer verifies every factual claim has a source, and a risk reviewer checks for checklist misuse, false precision, and protection-sensitive data risks. Answers that reveal new connections can be filed as synthesis pages — explorations compound in the knowledge base just like sources do.

## From Evidence to Advice

The advisory pipeline enforces a separation that most LLM systems quietly skip: the agent that retrieves evidence is not the agent that writes the final answer. When a field team asks an operational question, the Orchestrator decomposes it into sections — framework adaptation, risk identification, tool selection, and so on. Each section goes to a temporary retrieval agent that reads only the pages relevant to that section and produces an evidence packet: a structured set of claims, each linked to a specific source finding and page number.

A packet consolidator assembles those packets into a claim ledger — a list of approved facts. The Writing Agent receives only the ledger. It cannot invent claims, add unsupported advice, or cite sources not present in the bundle. It can simplify, organize, and improve readability. That's the boundary.

The practical effect is that every sentence in a final advisory output traces back to a specific page in a specific source document. This matters in humanitarian contexts where guidance gets operationalized by field teams under pressure, sometimes far from anyone who can check the original source.

## How Knowledge Earns Its Place

Not everything that enters the wiki is equally trustworthy, and the system doesn't pretend otherwise. Every piece of knowledge climbs a promotion ladder — from extracted finding to concept page to Tier 1 framework to linked tool to validated tool — and each rung has explicit requirements and a human gate.

| Promotion | Requirement | Who decides |
|---|---|---|
| Finding → concept page | Appears in ≥2 independent extracted sources | LLM proposes, human approves |
| Concept → Tier 1 framework | Defined decision logic + explicit, field-testable use conditions | Human approves |
| Tier 1 → linked tool | Field-applicable scoring criteria + documented failure modes | Human approves |
| Tool → validated status | All field instruments linked + data quality checks confirmed | Human approves |

The independence requirement is strict: two documents that cite the same underlying evaluation are not independent. If independence can't be confirmed, the promotion is blocked until a third source is found. This is the structural answer to a real LLM failure mode — the tendency to treat corroborating citations as stronger evidence than they are.

## Contradictions Are Features

Every page type in the wiki carries a required `contradicts:` field. Concept pages additionally require a `known_tensions:` section. An empty `contradicts: []` is a meaningful assertion — the source was checked and found consistent. A missing field means nobody checked. The lint check treats the absence as a CRITICAL failure, not a style issue.

The aging policy sharpens this further. Unresolved contradictions older than 30 days flag HIGH. Older than 90 days, they escalate to CRITICAL and block new ingest in the affected topic area until resolved. The wiki actively resists the accumulation of unexamined disagreements.

The logic is worth naming directly: a knowledge base that tracks its own contradictions is more useful than one that projects false consensus. Thirty years of humanitarian field practice contains genuine disagreements — about when area-based approaches are appropriate, about how to draw boundaries without entrenching divisions, about what handover actually requires. Smoothing those over doesn't make them disappear. It just makes them invisible until a field team rediscovers them at the worst possible moment.

The system currently covers 22 sources and 123 pages. It will hit a scale threshold at around 80 sources — at that point the index file alone becomes too expensive to read in full, and a local search engine replaces direct index queries. That threshold is schema-defined and logged when crossed, which is a small but telling detail: the system was designed to outgrow its own current architecture without breaking. That's the actual bet — not that LLMs are reliable enough to maintain a wiki unsupervised, but that a well-governed human-LLM collaboration can build something that compounds faster than it decays.