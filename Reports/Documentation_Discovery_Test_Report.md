# Documentation Discovery: Test Run (5 EOSDIS Collections)

**Skill:** Collection_Documentation_Discovery_Skill v1.0  |  **Run date:** 2026-11-05
**Input audit:** `EOSDIS_Collections_Missing_ATBD_UserGuide.csv` (Coverage Audit run 2026-11-04, `consortium=EOSDIS`, Level 0 excluded)
**Search method:** fallback. `WebSearch` returned an API error on every call in this environment, so Step 4 used the NTRS API and crawled Earthdata pages.

## Summary

Five collections were chosen to test each discovery route: sibling, in-record, landing-page crawl, campaign data, and partner-agency data.

| | ATBD | User's Guide |
|---|---:|---:|
| `FOUND_SIBLING` | 1 | 1 |
| `FOUND_RETAG` | 0 | 1 |
| `CANDIDATE` | 0 | 1 |
| `NOT_APPLICABLE` | 2 | — |
| `NOT_FOUND` | 2 | 2 |

The run produced four recommendations, two of them on nasa.gov (tier 1). See [Documentation_Discovery_Test_Recommendations.json](Documentation_Discovery_Test_Recommendations.json).

## Worklist Statistics (full EOSDIS, Step 1)

| Measure | Count |
|---|---:|
| Collections missing both documents | 3,425 |
| Product families | 3,260 |
| With in-record candidates (mis-tagged or untyped links) | 99 |
| With sibling candidates in CMR | 163 |
| With a landing or project page | 2,845 |
| Needing a web search (no in-record or sibling candidate) | 3,168 |
| ATBD not expected (campaign or in-situ keywords) | 591 |

About 7% of the gap (in-record plus sibling candidates) can be resolved from CMR alone, without any web search.

## Results

| Short Name | Ver | Provider | Doc | Outcome | Tier | Conf. | URL |
|---|---|---|---|---|---|---|---|
| MCD19A2N | 6.1NRT | LANCEMODIS | User's Guide | `FOUND_SIBLING` | 2 | HIGH | https://lpdaac.usgs.gov/documents/1500/MCD19_User_Guide_V61.pdf |
| MCD19A2N | 6.1NRT | LANCEMODIS | ATBD | `FOUND_SIBLING` | 2 | HIGH | https://lpdaac.usgs.gov/documents/111/MCD19_ATBD.pdf |
| AER_DBDT_D10KM_L3_MODIS_AQUA | 001 | GES_DISC | User's Guide | `FOUND_RETAG` (READ-ME → USER'S GUIDE) | 1 | HIGH | https://docserver.gesdisc.eosdis.nasa.gov/public/project/Community/Gupta/TASNPP_AOD_Level3_README.pdf |
| AER_DBDT_D10KM_L3_MODIS_AQUA | 001 | GES_DISC | ATBD | `NOT_FOUND` | — | — | — |
| DORIS_data_cycle | 1 | CDDIS | User's Guide | `CANDIDATE` | 1 | LOW | https://www.earthdata.nasa.gov/data/space-geodesy-techniques/doris/multiday-preprocessed-doris-data |
| DORIS_data_cycle | 1 | CDDIS | ATBD | `NOT_APPLICABLE` (preprocessed tracking data) | — | — | — |
| AAOE_Aerosol_AircraftInSitu_ER2_Data | 1 | LARC_CLOUD | User's Guide | `NOT_FOUND` | — | — | — |
| AAOE_Aerosol_AircraftInSitu_ER2_Data | 1 | LARC_CLOUD | ATBD | `NOT_APPLICABLE` (airborne in-situ) | — | — | — |
| ALOS_PSR_L1.1 | 1 | ASF | User's Guide | `NOT_FOUND` | — | — | — |
| ALOS_PSR_L1.1 | 1 | ASF | ATBD | `NOT_FOUND` | — | — | — |

### Evidence

**MCD19A2N 6.1NRT** (C2407807500-LANCEMODIS): sibling route
- The worklist matched it to MCD19A2 v061 (LPCLOUD) through the LANCE trailing-`N` rule. That rule was added during this test; without it, the collection had no sibling match.
- User's Guide: the title page reads "MODIS Multi-Angle Implementation of Atmospheric Correct [sic] (MAIAC) Data User's Guide Collection 6.1 Version 3.1" (November 2022, 24 pp.). It names `MCD19A2` 11 times, e.g., "3.2.1 Atmospheric Properties File (MCD19A2)". Collection 6.1 matches `6.1NRT`.
- ATBD: "MAIAC: Multi-Angle Implementation of Atmospheric Correction for MODIS, Algorithm Theoretical Basis Document (ver. 1.0)", 77 pp. It is an algorithm-level document that predates the C6.1 short names, which is acceptable under the version rule.
- **nasa.gov equivalence check:** neither the Earthdata MODIS NRT page nor `modis-land.gsfc.nasa.gov` has a copy (the latter returned 404). The tier-2 LP DAAC URLs stand. They are also persistent document-ID URLs.

**AER_DBDT_D10KM_L3_MODIS_AQUA 001** (C3618504061-GES_DISC): in-record route
- The record links `TASNPP_AOD_Level3_README.pdf` as `READ-ME`. This 16-page GES DISC document (rev. Aug 13, 2025) has these sections: *2.1 File Naming Convention, 2.2 File Format and Structure, 3.3 Data Fields, 3.4 Fill Values, 4 Using the Data*. It names `AER_DBDT_D10KM_L3_MODIS_AQUA` explicitly. It is a user guide in function, so re-tag it.
- ATBD: no ATBD was found in the record or on the landing page. The landing page loads its content with JavaScript, so a plain fetch shows no links. The record's `PUBLICATIONS` link (Gupta et al. 2020, MDPI *Remote Sensing*) describes the method but is tier 5, so it cannot be used as an ATBD. A search with `WebSearch` working would be the next step.

**DORIS_data_cycle 1** (C1000000000-CDDIS): crawl route
- The record's `GENERAL DOCUMENTATION` link points to the Earthdata DORIS holdings page. One level down is the *Multi-Day Preprocessed DORIS Data* page (tier 1). It has a description, DOI, format ("DORIS 2.2"), file naming convention (`sss/sssdataMMM.LLL.Z` with satellite codes), and the archive path.
- It is a product web page rather than a guide document, so it is `CANDIDATE`, LOW. The page also links the official format specification `ftp://ftp.ids-doris.org/pub/ids/data/doris22.fmt` (tier 3, International DORIS Service), which should be added as `DATA PRODUCT SPECIFICATION`.
- ATBD marked `NOT_APPLICABLE`: these are preprocessed tracking measurements, not retrieved geophysical products. The worklist's keyword rule did **not** flag this, so the call was a judgment made during verification.

**AAOE_Aerosol_AircraftInSitu_ER2_Data 1** (C3966856115-LARC_CLOUD): campaign route
- The ATBD was correctly marked `NOT_APPLICABLE` by the worklist (title contains "Aircraft In-Situ").
- The ESPO archive page loads its content with JavaScript. The NTRS search "Airborne Antarctic Ozone Experiment ER-2 aerosol" returned 6 hits, all 1989–1990 journal reprints and conference papers, with no data documentation. The record already links the AAOE mission plan and science overview as `GENERAL DOCUMENTATION`.
- For 1987-era airborne data, the ASDC data files' own headers (ICARTT or legacy NASA-Ames format) may be the only documentation that exists. The DAAC should confirm this.

**ALOS_PSR_L1.1 1** (C1206485527-ASF): partner-agency route
- The record links the JAXA *PALSAR Level 1.1 format* PDF as `DATA PRODUCT SPECIFICATION` (tier 3). That is a format description, not a user guide.
- The ASF data-set page now returns `301` to `https://www.earthdata.nasa.gov/data/instruments/palsar` (tier 1), but that page has no product documents. The ASF ALOS PALSAR user guides need a search engine to find, so this result should be re-run with `WebSearch` working.

## Findings

1. **The sibling and in-record routes give the best results.** Both HIGH-confidence results came from data already in CMR. Doing Steps 1–2 for all 262 collections with such candidates (99 in-record, 163 sibling) needs no web search.
2. **README-as-guide is a recurring pattern** at GES DISC. The audit counted 675 `READ-ME` links among GES DISC's 768 missing collections. If others are like the one tested, many GES DISC gaps need only a re-tag.
3. **Pages that load content with JavaScript block crawling** at GES DISC and ESPO. For those providers, Step 3 adds little, and Step 4 (web search) is what matters.
4. **ASF documentation has moved to earthdata.nasa.gov.** The redirect turns ASF candidates into tier 1, but the product guides were not on the instrument page.
5. **The `atbd_expected` rule misses non-campaign ancillary data** such as DORIS tracking data, orbit and ephemeris files, and archive information records. The rule should be extended (see below).

## Recommended Follow-ups

- Re-run Step 4 with `WebSearch` working, for the three `NOT_FOUND` items and the AER_DBDT ATBD.
- Extend `atbd_expected` to treat these as not needing an ATBD: space-geodesy tracking data (DORIS, SLR, VLBI, GNSS observation files), ephemeris and attitude files (e.g., `AM1EPHNE`), and CDDIS archive information collections.
- Run Steps 1–2 for all 262 CMR-resolvable collections as the next batch, starting with GES DISC READMEs.

## Method & Caveats

- Documents were downloaded with `curl` into an isolated directory, and text was extracted with `pypdf` in a venv (`python -I`). The `Ignoring wrong pointing object` warnings for the GES DISC README did not affect the extracted text.
- `NOT_FOUND` results come from fallback search only, so they are weaker evidence than a full `WebSearch` run.
- No CMR metadata was modified.
