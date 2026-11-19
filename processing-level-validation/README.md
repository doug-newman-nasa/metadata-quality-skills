# Processing Level Validation Skill Family

Skills that check whether a collection's declared `ProcessingLevel` in CMR matches the processing level described in its ATBD and User Guide documentation.

## Skills

| Skill | Role | Depends on |
|---|---|---|
| `Collection_Processing_Level_Validation_Skill` | Retrieves the collection's CMR record, reads its ATBD and User Guide documents, and returns a verdict (CONFIRMED, MISMATCH, AMBIGUOUS or UNVERIFIABLE) with quoted evidence and a recommended level. | Earthdata MCP `get_collections`; documents linked from CMR `related_urls` |

The skill's complementary skills are `Collection_ATBD_Analysis_Skill` and `Collection_Lineage_via_ATBD_Skill` in [lineage/](../lineage/), and `Generic_Collection_Keyword_Extraction_Skill` in [keyword-extraction/](../keyword-extraction/). It does not call them.

## Folders

- `skills/`: the skill definition.
- `notebooks/`: no notebooks yet.
- `reports/`: validation reports for individual collections.
- `metrics/`: no metrics files yet.
