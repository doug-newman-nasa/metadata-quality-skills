# Keyword Extraction Skill Family

Skills that extract public documentation for a CMR collection and use the Earthdata keyword tool to suggest science keywords.

## Skills

| Skill | Role | Depends on |
|---|---|---|
| `Generic_Collection_Keyword_Extraction_Skill` | Pulls the collection's documentation and suggests GCMD science keywords. | Earthdata MCP `get_keywords` and `get_collections` |

This skill has no hard dependencies on other families. Its complementary skills are `Collection_ATBD_Analysis_Skill` in [lineage/](../lineage/) and `Collection_Processing_Level_Validation_Skill` in [processing-level-validation/](../processing-level-validation/).

## Folders

- `skills/`: the skill definition.
- `notebooks/`: no notebooks yet.
- `reports/`: keyword extraction reports for individual collections.
- `metrics/`: no metrics files yet.
