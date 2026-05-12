# Raw Content Provenance Map

This map links files from `.codex-extracts/` to raw source PDFs in `wiki/aba/01-sources/raw/`.

## Matched to Raw PDFs

| `.codex-extracts` file | Renamed file in `raw-content/` | Matched raw PDF | Match basis |
|---|---|---|---|
| `2017_undrr_resilient_handbook.txt` | `2017-undrr-how-to-make-cities-more-resilient-handbook-2017-edition.raw-extract.md` | `2017-undrr-how-to-make-cities-more-resilient-handbook-2017-edition.pdf` | Year + title token alignment (`undrr`, `resilient`, `handbook`) |
| `2018_allen_neighbourhood_lit_review.txt` | `2018_allen-building-better_concepts-of-neighbourhood-literature-review.raw-extract.md` | `2018_allen-building-better_concepts-of-neighbourhood-literature-review.pdf` | Year + author (`allen`) + neighbourhood literature tokens |
| `2019_alnap_campbell_barrio_mio_case_study.txt` | `2019-alnap-campbell-barrio-mio-katye-neighbourhood-approach-cities-case-study.raw-extract.md` | `2019-alnap-campbell-barrio-mio-katye-neighbourhood-approach-cities-case-study.pdf` | Year + author (`campbell`) + title phrase overlap |
| `2019_alnap_sanderson_urban_contexts.txt` | `2019_alnap-sanderson-humanitarian-response-urban-contexts.raw-extract.md` | `2019_alnap-sanderson-humanitarian-response-urban-contexts.pdf` | Year + author (`sanderson`) + exact title phrase overlap |
| `2019_journal_urbanism_neighbourhood_evolution.txt` | `2019_journal-urbanism_understanding-neighbourhood-concept-evolution.raw-extract.md` | `2019_journal-urbanism_understanding-neighbourhood-concept-evolution.pdf` | Year + journal + exact title phrase overlap |
| `2019_reach_unhcr_area_based_assessment_guide.txt` | `2019-reach-unhcr-area-based-assessment-key-informants-practical-guide.raw-extract.md` | `2019-reach-unhcr-area-based-assessment-key-informants-practical-guide.pdf` | Year + org tokens (`reach`, `unhcr`) + area-based assessment title overlap |
| `2019_replication_scale_up_learning_note.txt` | `2019-replication-scale-up-learning-note-framework.raw-extract.md` | `2019-replication-scale-up-learning-note-framework.pdf` | Exact year + title-token match |
| `2026_iasc_aba_coord_tor.txt` | `2026-iasc-standard-terms-reference-area-based-coordination-tor.raw-extract.md` | `2026-iasc-standard-terms-reference-area-based-coordination-tor.pdf` | Year + `iasc` + `area-based coordination` + `tor` |

## Unmatched in Current Raw Folder

| `.codex-extracts` file | Renamed file in `raw-content/` | Notes |
|---|---|---|
| `2024_unhcr_aba_her_apr2024.txt` | `2024-unhcr-syria-factsheet-aba-her-apr2024.unmatched-raw-extract.md` | No 2024 UNHCR raw PDF found in `wiki/aba/01-sources/raw/`. Content begins with `FACTSHEET - UNHCR SYRIA`, suggesting a source not yet added to the raw corpus. |
