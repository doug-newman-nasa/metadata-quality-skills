# ATBD & User's Guide Coverage Audit: EOSDIS Collections

**Skill:** Collection_Documentation_Coverage_Audit_Skill v1.0
**Run date:** 2026-11-04 (CMR snapshot 13:19 UTC)  |  **CMR filter:** `consortium=EOSDIS`  |  **Excluded levels:** `0`

## Summary

11,388 EOSDIS collections → 103 Level 0 excluded → 11,285 assessed → **3,425 (30.3%) have neither an ATBD nor a User's Guide RelatedUrl.**

- 98 of the 3,425 probably have the document already, but under the wrong Subtype. These are the cheapest to fix.
- 1,154 have a closely related document, such as a READ-ME, HOW-TO, or PI documentation, that a curator could review.
- 636 have no documentation links at all.
- Five providers account for 79% of the gap: LARC_CLOUD, GES_DISC, OB_DAAC, ESDIS, and CDDIS (2,720 of the 3,425).
- Much of the gap is airborne and in-situ field-campaign data. An ATBD is not usually expected for these collections, although a user guide or campaign document is.

## Coverage Classes

| Class | Collections | % of assessed |
|---|---:|---:|
| `USER_GUIDE_ONLY` | 4,798 | 42.5% |
| `BOTH` | 1,813 | 16.1% |
| `ATBD_ONLY` | 1,249 | 11.1% |
| **Covered subtotal** | **7,860** | **69.7%** |
| `MISSING_GENERAL_DOCS_ONLY` (only general documentation, publications, or links with no Subtype) | 1,537 | 13.6% |
| `MISSING_ALT_DOCS` (READ-ME, HOW-TO, PI documentation, etc.) | 1,154 | 10.2% |
| `MISSING_NO_DOCS` (no `VIEW RELATED INFORMATION` links) | 636 | 5.6% |
| `MISSING_POSSIBLE_MISTAG` (URL or description names an ATBD or user guide) | 98 | 0.9% |
| **Missing subtotal** | **3,425** | **30.3%** |

## By Provider

| Provider | Assessed | Missing | % missing | Breakdown of missing |
|---|---:|---:|---:|---|
| LARC_CLOUD | 1,733 | 1,096 | 63.2% | GENERAL_DOCS_ONLY 715, ALT_DOCS 344, POSSIBLE_MISTAG 32, NO_DOCS 5 |
| GES_DISC | 2,069 | 768 | 37.1% | ALT_DOCS 684, GENERAL_DOCS_ONLY 39, POSSIBLE_MISTAG 31, NO_DOCS 14 |
| OB_DAAC | 455 | 394 | 86.6% | NO_DOCS 375, GENERAL_DOCS_ONLY 19 |
| ESDIS | 327 | 258 | 78.9% | GENERAL_DOCS_ONLY 128, NO_DOCS 65, ALT_DOCS 65 |
| CDDIS | 204 | 204 | 100.0% | GENERAL_DOCS_ONLY 202, ALT_DOCS 1, NO_DOCS 1 |
| POCLOUD | 1,004 | 169 | 16.8% | GENERAL_DOCS_ONLY 114, ALT_DOCS 37, POSSIBLE_MISTAG 18 |
| NSIDCV0 | 312 | 116 | 37.2% | GENERAL_DOCS_ONLY 103, POSSIBLE_MISTAG 12, ALT_DOCS 1 |
| LANCEMODIS | 170 | 93 | 54.7% | GENERAL_DOCS_ONLY 72, NO_DOCS 21 |
| OB_CLOUD | 477 | 90 | 18.9% | GENERAL_DOCS_ONLY 84, ALT_DOCS 6 |
| ASF | 155 | 68 | 43.9% | NO_DOCS 56, ALT_DOCS 11, GENERAL_DOCS_ONLY 1 |
| MLHUB | 58 | 58 | 100.0% | NO_DOCS 58 |
| NSIDC_CPRD | 610 | 37 | 6.1% | GENERAL_DOCS_ONLY 34, ALT_DOCS 3 |
| OMINRT | 22 | 22 | 100.0% | NO_DOCS 21, ALT_DOCS 1 |
| LAADS | 195 | 16 | 8.2% | NO_DOCS 14, ALT_DOCS 1, GENERAL_DOCS_ONLY 1 |
| ASIPS | 15 | 15 | 100.0% | GENERAL_DOCS_ONLY 15 |
| NCCS | 7 | 7 | 100.0% | GENERAL_DOCS_ONLY 4, NO_DOCS 3 |
| LPCLOUD | 792 | 5 | 0.6% | POSSIBLE_MISTAG 5 |
| ORNL_CLOUD | 1,986 | 4 | 0.2% | NO_DOCS 3, GENERAL_DOCS_ONLY 1 |
| LANCEAMSR2 | 7 | 3 | 42.9% | GENERAL_DOCS_ONLY 3 |
| GHRC_DAAC | 685 | 2 | 0.3% | GENERAL_DOCS_ONLY 2 |
| LPDAAC_ECS | 2 | 0 | 0.0% | — |

## By Processing Level

| Normalized level | Assessed | Missing | % missing |
|---|---:|---:|---:|
| 1 (sub-level not specified) | 406 | 197 | 48.5% |
| 1A | 249 | 68 | 27.3% |
| 1B | 755 | 92 | 12.2% |
| 1C | 17 | 3 | 17.6% |
| 2 | 3,726 | 1,724 | 46.3% |
| 3 | 4,194 | 529 | 12.6% |
| 4 | 1,529 | 668 | 43.7% |
| MISSING (no ProcessingLevel) | 359 | 133 | 37.0% |
| NON_STANDARD | 50 | 11 | 22.0% |

## By Collection Data Type

| CollectionDataType | Assessed | Missing | % missing |
|---|---:|---:|---:|
| Not set | 7,256 | 2,175 | 30.0% |
| SCIENCE_QUALITY | 3,497 | 1,079 | 30.9% |
| NEAR_REAL_TIME | 275 | 134 | 48.7% |
| EXPEDITED | 186 | 20 | 10.8% |
| OTHER | 63 | 15 | 23.8% |
| LOW_LATENCY | 8 | 2 | 25.0% |

## Findings

1. **The gap is concentrated in a few providers.** LARC_CLOUD (1,096) and GES_DISC (768) together hold 54% of the missing collections. Several smaller providers are missing coverage for every collection they hold: CDDIS (204), MLHUB (58), OMINRT (22), ASIPS (15), and NCCS (7). ORNL_CLOUD, GHRC_DAAC, and LPCLOUD are each below 1% missing.
2. **Much of the gap is field-campaign and in-situ data.**
   - OB_DAAC: 375 records have no documentation links. They are SeaBASS cruise and field-campaign collections (e.g., `PVST`, `Chesapeake`, `JGOFS`, `AAOT`, `ACE-ASIA`).
   - LARC_CLOUD: the missing records are dominated by airborne campaigns, including DISCOVER-AQ (77), FIRE (117), NARSTO (59), PEM-Tropics (33), and ERBE (38).
   - An ATBD does not really apply to these collections, but a user guide or campaign document usually does exist. The requirement for them should probably be "User's Guide (or equivalent)" rather than "ATBD".
3. **GES_DISC usually has the document, but under a different Subtype.** Of its 684 `MISSING_ALT_DOCS` collections, the linked Subtypes include READ-ME (675), HOW-TO (202), and PI DOCUMENTATION (122). A collection can have more than one. Many GES_DISC READMEs are in practice data user guides. For example, OMI products link `README.OMI_DUG.pdf`, where "DUG" stands for Data User's Guide, under `READ-ME`.
4. **98 links are probably mis-tagged** (`MISSING_POSSIBLE_MISTAG`). These collections are mainly in LARC_CLOUD (32), GES_DISC (31), POCLOUD (18), NSIDCV0 (12), and LPCLOUD (5). One example is `GPM_2ADPRENV` v07, which links `ATBD_GPM_DPR_n3_dec15.pdf`, but not with the ATBD Subtype. The matching URLs are listed in the CSV `detail` column.
5. **Level 2 and Level 4 have the most gaps.** About 46% of L2 and 44% of L4 collections are missing both documents, compared with 12–13% for L1B and L3. Collections declared as plain `1`, with no sub-level, are missing at 48.5%. That pattern lines up with the processing-level quality issues found by `Collection_Processing_Level_Validation_Skill`.
6. **NRT collections are missing more often than science-quality ones** (48.7% vs. 30.9%). This is consistent with the VJ209CMG_NRT validation, where the NRT record lacked the ATBD that its science-quality counterpart links.
7. **The `ESDIS` provider is a small subset.** It holds 327 CIESIN/SEDAC records, 258 of them missing. Results filtered by the ESDIS provider should not be mistaken for EOSDIS-wide results.

## Recommended Actions

| Priority | Class | Count | Action |
|---|---|---:|---|
| 1 | `MISSING_POSSIBLE_MISTAG` | 98 | Re-tag the existing RelatedUrl with Subtype `ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)` or `USER'S GUIDE`. This is a metadata-only change, and the candidate URLs are in the CSV. |
| 2 | `MISSING_ALT_DOCS` | 1,154 | Have DAAC curators review the READ-ME, HOW-TO, and PI documents and re-tag any that act as user guides. Start with GES_DISC (684) and LARC_CLOUD (344). |
| 3 | `MISSING_GENERAL_DOCS_ONLY` | 1,537 | Check whether a `GENERAL DOCUMENTATION` link is really a user guide or an ATBD. Where none exists, add one. Start with LARC_CLOUD (715), CDDIS (202), and ESDIS (128). |
| 4 | `MISSING_NO_DOCS` | 636 | Add at least a user guide or campaign document link. Start with OB_DAAC SeaBASS (375), MLHUB (58), ASF (56), and OMINRT (21). For NRT collections, link the ATBD of the matching science-quality collection. |
| — | Policy | — | Decide whether field-campaign and in-situ collections must have an ATBD or only a User's Guide, so that compliance numbers measure the right thing. |

## Method & Caveats

- **Population:** CMR Search API `collections.umm_json?consortium=EOSDIS`, fully paged with `CMR-Search-After`. 11,388 records were retrieved, matching `CMR-Hits`.
- **Level 0 exclusion:** `ProcessingLevel.Id` was normalized using the rules in the Processing Level Validation skill. 103 records normalized to `0` and were excluded. The 359 records with no ProcessingLevel were kept.
- **Covered** means at least one RelatedUrl has Subtype `ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)` or `USER'S GUIDE`, compared case-insensitively. The documents themselves were not fetched, so a broken link still counts as covered.
- **Mis-tag detection** is a regex over the URL and Description text. It can produce some false positives and false negatives.
- CMR changes daily. Re-run the skill to refresh these numbers.

## Output Files

- [EOSDIS_Collections_Missing_ATBD_UserGuide.csv](EOSDIS_Collections_Missing_ATBD_UserGuide.csv): all 3,425 collections missing both documents, with columns `short_name, version, provider, concept_id, processing_level, data_type, status, detail`
- [EOSDIS_ATBD_UserGuide_Coverage_Summary.json](EOSDIS_ATBD_UserGuide_Coverage_Summary.json): the summary counts used in this report
