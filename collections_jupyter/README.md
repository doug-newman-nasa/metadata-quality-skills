# collections_jupyter

Two notebooks that repair the `MetadataAssociations` flagged by `metadataUpdates/find_schema_issues.py`,
following [`Skills/Collection_Lineage_via_ATBD_Skill.md`](../Skills/Collection_Lineage_via_ATBD_Skill.md).
They target the new rules: the related collection is identified by **ShortName**, and **Version is mandatory**.

| Notebook | Input | What it fixes |
|---|---|---|
| `Collection_Lineage_Missing_Version_ATBD.ipynb` | `metadataUpdates/collections_missing_versionOct22.json` | associations that have no Version |
| `Collection_Lineage_ShortName_Mismatch_ATBD.ipynb` | `metadataUpdates/collections_shortname_mismatchOct22.json` | identifiers that are not CMR ShortNames (case, embedded version, retired version, typo, free text, unregistered) |

## Run order

1. Run the missing-version notebook.
2. Run the ShortName-mismatch notebook. Its last cell merges both sets of fixes into
   `output/combined_repaired_ummc.json`.

Both notebooks need network access to CMR GraphQL and the ATBD / user-guide URLs. Downloaded document text is
cached in `output/doc_cache/`, so later runs are faster. For page numbers and cleaner quotes, run `pip install pypdf`
first; without it, a standard-library PDF text extractor is used.

## Outputs (`output/`)

| File | Content |
|---|---|
| `<prefix>_fixes.json` | one entry per association: before/after, identifier and version basis, confidence + reason, evidence, ATBD quote, CMR checks |
| `<prefix>_repaired_ummc.json` | per collection: the repaired `MetadataAssociations` array (`umm_c_patch`) |
| `<prefix>_review_report.csv` | the same as a flat table for review |
| `<prefix>_identifier_summary.csv` | grouped by original identifier, so each one is fixed once and applied everywhere |
| `<prefix>_documents.csv` | every document fetched and its skill Step 2 validation |
| `<prefix>_lineage_report.md` | skill Step 8 report |
| `combined_repaired_ummc.json` | both notebooks' fixes applied together (written by the second notebook) |

`umm_c_patch` holds only `ShortName`, `Version` and `MetadataAssociations`. Merge the array into the full native
UMM-C record before ingesting. Set `ASSOCIATION_ID_FIELD = "EntryId"` in the configuration cell to produce
associations for UMM-C ≤ 1.18.x.

## Confidence

| Level | Meaning |
|---|---|
| HIGH | exact or case-only ShortName match, a version that is verified or the only one in CMR, and the CMR checks pass |
| MEDIUM | the identifier was inferred (typo, title match, versioned family, NRT counterpart), or the version was chosen from several |
| LOW | unresolved, self-reference, not in CMR, or an invalid processing-level progression |

Treat everything below HIGH as needing review. The `confidence_reason` column explains each case.
