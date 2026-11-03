# Processing Level Validation: MOD11A2 v061

**Skill:** Collection_Processing_Level_Validation_Skill v1.0
**Run date:** 2026-11-03

**Concept ID:** C2269056084-LPCLOUD  |  **Provider:** LPCLOUD
**Verdict:** ✅ CONFIRMED  |  **Confidence:** HIGH

| | Value |
|---|---|
| Declared `ProcessingLevel.Id` (raw) | `3` |
| Declared (normalized) | `3` |
| Level in Entry Title | `3` ("MODIS/Terra Land Surface Temperature/Emissivity 8-Day **L3** Global 1km SIN Grid V061") |
| Evidence-based level | `3` (16 of 16 evidence weight = 100%) |
| **Recommended `ProcessingLevel.Id`** | No change |

## Documents Assessed
| Class | URL | Status | Used |
|---|---|---|---|
| ATBD | https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf | 200 OK (PDF, 77 pp.). WebFetch could not decode it; text extracted locally with pypdf | ✓ |
| User Guide | https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf | 200 OK (PDF, 37 pp.). WebFetch could not decode it; text extracted locally with pypdf | ✓ |
| General Documentation (File Spec) | https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD11A2 | Not fetched (documents above were sufficient) | — |

## Evidence
| # | Source | Location | Quote | Type | Implies | Weight |
|---|---|---|---|---|---|---|
| 1 | User Guide | p. 7, Table 1 | "MOD11A2 … L3 1200 rows by 1200 columns 1km (actual 0.928km) eight days Sinusoidal" | EXPLICIT | L3 | 4 |
| 2 | User Guide | p. 25, Table 16 (ArchiveMetadata.0) | "LongName "MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid"" | EXPLICIT | L3 | 4 |
| 3 | User Guide | p. 7 | "The sixth product, MOD11A2, is an eight-day LST product by averaging from two to eight days of the MOD11A1 product." | INDIRECT | L3 | 2 |
| 4 | User Guide | p. 6, with p. 7 Table 1 (MOD11A1 = L3) | "A level 3 (L3) product is a geophysical product that has been temporally and or spatially manipulated, and is usually in a gridded map projection format referred to as tiles." Input MOD11A1 is listed as L3, and MOD11A2 is a temporal average of it. | INPUT_BASED | L3 | 2 |
| 5 | ATBD | p. 53, product flow diagram | "MOD_PR11C MOD.AM1.V2.lst_8dy.L3" | INDIRECT* | L3 | 2 |
| 6 | CMR | `entry_title` | "…8-Day L3 Global 1km SIN Grid V061" | CMR | L3 | 1 |
| 7 | CMR | `abstract` | "Each pixel value in the MOD11A2 is a simple average of all the corresponding MOD11A1 LST pixels collected within that 8-day period." | CMR | L3 | 1 |

\* The ATBD (v3.3) predates the current product names and never uses the string "MOD11A2" (0 occurrences). Its 8-day LST product is labeled with the legacy file name `MOD.AM1.V2.lst_8dy.L3`. Because the name does not exactly match the target product, this is scored as INDIRECT rather than EXPLICIT.

**Level scores:** `{"3": 16}`. No evidence points to any other level.

## Findings
1. The declared processing level (`3`) matches the User Guide, ATBD, entry title, and abstract.
2. The ATBD is an at-launch document (version 3.3) covering both the L2 (MOD11_L2) and L3 LST products. It uses legacy product names and does not mention MOD11A2 by name. The User Guide is the authoritative version-specific source for this collection.
3. **Link-quality issue in the User Guide PDF:** The User Guide PDF has 310 embedded hyperlinks to the third-party domain `ipassist.biz`. By comparison, it has 55 links to the guide's own host (`www.icess.ucsb.edu`). WebFetch noted that these include the table-of-contents entries where links to the MODIS LST user guide pages are expected. The CMR `related_urls` entry itself points correctly to lpdaac.usgs.gov. The problem is inside the hosted document.

## Recommended Actions
- No change to `ProcessingLevel.Id`.
- Report Finding 3 to LP DAAC User Services so they can review the embedded `ipassist.biz` links in `MOD11_User_Guide_V61.pdf`.
