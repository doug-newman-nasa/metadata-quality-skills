# Processing Level Validation: VJ209CMG_NRT v2

**Skill:** Collection_Processing_Level_Validation_Skill v1.2
**Run date:** 2026-11-03

**Concept ID:** C4231443668-LANCEMODIS  |  **Provider:** LANCEMODIS  |  **Data type:** NEAR_REAL_TIME
**Verdict:** ❌ MISMATCH  |  **Confidence:** HIGH

| | Value |
|---|---|
| Declared `ProcessingLevel.Id` (raw) | `2` |
| Declared (normalized) | `2` |
| Level in Entry Title | `3` ("VIIRS/JPSS2 Surface Reflectance Daily **L3** Global 0.05 Deg CMG NRT"). **Disagrees with the declared level** |
| Evidence-based level | `3` (16 of 16 evidence weight = 100%) |
| **Recommended `ProcessingLevel.Id`** | **`3`** |

## How the Collection Was Selected
Candidate search: `get_collections(keyword="L3", processing_level_id=["2"], has_granules=true)` returned 27 hits. This collection was the only result in the first page whose title names a level (L3) different from its declared level (2).

## Documents Assessed
| Class | URL | Status | Used |
|---|---|---|---|
| User Guide (linked in CMR) | https://viirsland.gsfc.nasa.gov/PDF/VIIRS_Surf_Refl_UserGuide_v2.0.pdf | 200 OK (PDF, 45 pp.). WebFetch could not decode it; text extracted locally with pypdf | ✓ |
| ATBD | None in CMR `related_urls` | Missing | — |
| Sibling ATBD (from VJ209CMG, C2817366674-LPCLOUD) | https://lpdaac.usgs.gov/documents/122/VNP09_ATBD.pdf | Identified, not fetched (not needed) | — |

## Evidence
| # | Source | Location | Quote | Type | Implies | Weight |
|---|---|---|---|---|---|---|
| 1 | User Guide | p. 7, Table 2 | "VNP09CMG … VIIRS/NPP Daily Surface Reflectance L3 Global DDR 0.05°x0.05° grid CMG." | EXPLICIT† | L3 | 4 |
| 2 | User Guide | p. 9, §2.4 "NPP/ VIIRS Level 3 Surface Reflectance Product Description" | "The Level 3 daily CMG product, VNP09CMG, is produced at 0.05 degree resolution on a global grid." | EXPLICIT† | L3 | 4 |
| 3 | User Guide | p. 29, §3.2.4 | "VIIRS/NPP Surface Reflectance Daily L3 Global 0.05 Deg CMG (hdf 5 format)" | EXPLICIT† | L3 | 4 |
| 4 | User Guide | p. 29, §3.2.4 | "We use a weighted average of the best quality observation form [sic] the Level 2 product." | INPUT_BASED | L3 | 2 |
| 5 | CMR | `entry_title` | "…Surface Reflectance Daily L3 Global 0.05 Deg CMG NRT" | CMR | L3 | 1 |
| 6 | CMR | `abstract` | "This product uses a weighted average of the best quality observation and is formatted as a CMG for use in climate simulation models." | CMR | L3 | 1 |
| 7 | CMR (sibling) | VJ209CMG v002, C2817366674-LPCLOUD | `processing_level_id: "3"`; title "…Daily L3 Global 0.05Deg CMG V002" | CMR | L3 | 1 |

† **Platform-sibling attribution.** The User Guide is written for Suomi-NPP (`VNP09CMG`) and never mentions VJ209CMG, JPSS2/NOAA-21, or NRT. The CMR record for this collection links this guide as its User's Guide, and VJ209CMG differs from VNP09CMG only by platform prefix (and the `_NRT` suffix). Under skill v1.2, these statements are therefore scored as EXPLICIT. Under the stricter v1.1 rules, items 1–3 would be INDIRECT and the verdict would be AMBIGUOUS, although the evidence would still be 100% L3.

**Level scores:** `{"3": 16}`. No document evidence supports Level 2.

**Possible source of the error:** The abstract contains boilerplate copied from the L2/L2G products: "Pixels when not produced are replaced by fill values in the Level-2 and Level-2G products." The user guide's own description of the product family distinguishes the CMG product from the L2 and L2G products (p. 6): "The following surface reflectance products are generated at the Land SIPS: One Level 2 VIIRS surface reflectance product (VNP09), three Level 2G surface reflectance products (VNP09GA, VNP09G1KI, and VNP09GHKI), a global CMG-grid daily L3 surface reflectance (VNP09CMG), and two multi-day surface reflectance products (VNP09A1 and VNP09H1)." This passage was not scored separately because it repeats the Table 2 listing (item 1).

**Method notes:** Text was extracted from the PDF with pypdf. The statement that the guide "never mentions VJ209CMG, JPSS2/NOAA-21, or NRT" comes from a case-insensitive search of the extracted text for `VJ2`, `JPSS`, `NOAA-21`, `NRT`, and `near real`, which returned no matches. The guide's page headers identify it as "VIIRS-NPP NASA LAND SIPS V2 Reprocessing Surface Reflectance products – April 2023".

## Findings
1. **Processing level mismatch.** The record declares `2`, but the User Guide, entry title, abstract, and the science-quality sibling (VJ209CMG, declared `3`) all identify a Level 3 gridded daily composite.
2. **Title and declared level disagree** within the same record ("L3" in the title vs. `2` in ProcessingLevel).
3. **No ATBD linked.** The science-quality sibling VJ209CMG links `VNP09_ATBD.pdf`, but the NRT record does not.
4. **User Guide not specific to the product.** The linked guide (v2.0, April 2023) covers only the Suomi-NPP products and does not mention NOAA-21 or the NRT stream.
5. **Abstract boilerplate** mentions Level-2 and Level-2G products, which may have caused the misclassification.
6. **The same mismatch appears across the NRT CMG family.** VNP09CMG_NRT and VJ109CMG_NRT also declare `2` with "L3" in their titles (see the table below). This is based on CMR evidence only and has not been validated against their documents.

## Recommended Actions
- Update UMM-C `ProcessingLevel.Id` from `"2"` to `"3"`.
- Add a RelatedUrl with Type `VIEW RELATED INFORMATION` and Subtype `ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)` pointing to `https://lpdaac.usgs.gov/documents/122/VNP09_ATBD.pdf`, matching the VJ209CMG record.
- **Apply the same fix across the family.** A CMR check found that all three LANCE NRT CMG records declare `2` while their titles say "L3":

  | Short Name | Concept ID | Declared | Title Level |
  |---|---|---|---|
  | VNP09CMG_NRT | C2780134650-LANCEMODIS | 2 | L3 |
  | VJ109CMG_NRT | C2780814625-LANCEMODIS | 2 | L3 |
  | VJ209CMG_NRT | C4231443668-LANCEMODIS | 2 | L3 |

  Only VJ209CMG_NRT received a full document-based validation. The other two are flagged from CMR evidence only, so their verdict is AMBIGUOUS until their linked documents are checked. Their `related_urls` have not yet been inspected.
- Provider: NASA/GSFC/EOS/ESDIS/LANCE MODIS.
