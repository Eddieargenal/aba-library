"""
schema.py — single source of truth for the ABA/DRR data model (v2.7)

All controlled vocabularies, required-field tables, id-prefix rules, relationship
(edge) fields, and the raw-content sync field lists live here. Both
`build-index.py` and `sync_extracted_frontmatter_to_raw_content.py` import from
this module, so a vocabulary change is a one-file edit.

Rule *logic* stays in the consuming scripts; this module holds only the data the
rules read. The prose schema docs (governance/schema/*.md, governance/id-registry.md)
carry the same lists inside ```schema:<key>``` fenced blocks; `check-schema.py`
verifies those blocks against the tables below (non-blocking).
"""

# --- Controlled vocabularies -------------------------------------------------

# schema:retrieval_status
RETRIEVAL_STATUS_VOCAB = {"usable", "limited", "deprecated", "draft"}

# schema:lifecycle_stage
LIFECYCLE_VOCAB = {
    "appropriateness-decision",
    "area-selection",
    "neighbourhood-diagnosis",
    "joint-prioritization",
    "coordination-design",
    "integrated-area-strategy",
    "implementation-adaptation",
    "monitoring-learning",
    "transition-handover",
}

# Finding statuses that count as fully routed/closed (everything else is "open")
TERMINAL_FINDING_STATUS = {"integrated", "done", "complete", "resolved", "source_only"}

# schema:promotion_stage — epistemic-validation axis (ADR-0001). How far a claim
# has climbed the promotion ladder; the retrieval ranker's primary trust signal.
# ORDER is the ladder sequence (low -> high); the ranker uses it as the ordinal
# for promotion_stage ordering (ADR-0004). VOCAB derives from it.
PROMOTION_STAGE_ORDER = ("finding", "concept", "framework", "tool", "validated")
PROMOTION_STAGE_VOCAB = set(PROMOTION_STAGE_ORDER)

# schema:implementation_tier — which actor tier a page serves (ADR-0001). Split
# out of lifecycle_stage; "all" covers pages serving every tier.
IMPLEMENTATION_TIER_VOCAB = {"design", "execution", "synthesis", "all"}

# schema:cross_cutting_topics — OPTIONAL controlled tags for cross-cutting themes
# that span lifecycle stages and tiers (ADR-0003). Validated only when present;
# never required. Distinct from `primary_topics`, which stays free-text keywords
# (the split avoids overloading an existing field). Seed set; grows as
# cross-cutting query patterns emerge.
CROSS_CUTTING_TOPICS_VOCAB = {
    "relational-trust",
    "compound-risk",
    "co-design",
    "exception-flagging",
    "design-capture",
    "cognitive-load",
}

# Contradiction-aging thresholds, in days (ADR-0001 / atomic-task framework).
# Computed from last_reviewed against today; never a trusted frontmatter string.
CONTRADICTION_AGING_WARN_DAYS = 30
CONTRADICTION_AGING_BLOCK_DAYS = 90

# --- Required-field tables ---------------------------------------------------

STRICT_REQUIRED = ["id", "type", "title", "retrieval_status"]

LIFECYCLE_REQUIRED_TYPES = {
    "source",
    "concept",
    "framework",
    "tool",
    "field-instrument",
    "risk",
    "advisory-playbook",
    "decision-protocol",
    "output-template",
}

# Technical pages must rest on evidence: usable ones require source_basis.
TECHNICAL_TYPES = {"concept", "framework", "tool", "field-instrument", "risk", "decision-protocol"}

# Pages on the promotion ladder require promotion_stage + implementation_tier
# (ADR-0001). Same membership as TECHNICAL_TYPES today; named separately because
# "on the ladder" and "rests on evidence" are distinct ideas that may diverge.
LADDER_TYPES = set(TECHNICAL_TYPES)

MAX_PRIMARY_TOPICS = 6

# --- Stable id prefixes ------------------------------------------------------

# schema:id_prefix
ID_PREFIX_BY_TYPE = {
    "source": "S-",
    "concept": "C-",
    "framework": "F-",
    "tool": "T-",
    "field-instrument": "I-",
    "risk": "R-",
    "known-tension": "KTN-",
    "advisory-playbook": "P-",
    "decision-protocol": "D-",
    "output-template": "O-",
    "slice-spec": "SS-",
    "overview": "OVR-",
}

# --- Relationship (edge) vocabulary ------------------------------------------

# Maps a frontmatter array field to the graph-edge relation name it compiles to.
REL_FIELDS = {
    "related_concepts": "related_concept",
    "related_frameworks": "related_framework",
    "related_tools": "related_tool",
    "related_risks": "related_risk",
    "source_basis": "source_basis",
    "known_tensions": "known_tension",
    "contradicts": "contradicts",
    "used_by_playbooks": "used_by_playbook",
    "output_templates": "output_template",
    "requires_concepts": "requires_concept",
    "parent_frameworks": "parent_framework",
    "required_inputs": "requires_input",
    "compatible_instruments": "compatible_instrument",
    "mitigated_by": "mitigated_by",
    "risk_applies_to": "risk_applies_to",
    "escalation_triggers": "escalation_trigger",
}

# --- Raw-content sync field lists --------------------------------------------

# Fields copied from extracted source pages into their raw-content mirror.
COPIED_FIELDS = [
    "status",
    "title",
    "author",
    "institution",
    "year",
    "source_id",
    "source_type",
    "source_url",
    "file_type",
    "canonical_file",
    "created",
    "updated",
    "ingest_date",
    "ingest_status",
    "confidence",
]

# Ordered output schema for raw-content frontmatter.
OUTPUT_ORDER = [
    "type",
    "zone",
    "status",
    "title",
    "author",
    "institution",
    "year",
    "source_id",
    "source_type",
    "source_url",
    "file_type",
    "canonical_file",
    "created",
    "updated",
    "ingest_date",
    "ingest_status",
    "confidence",
]
