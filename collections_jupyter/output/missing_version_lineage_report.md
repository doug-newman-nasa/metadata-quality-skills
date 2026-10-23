# Missing Version — lineage repair report

Generated 2026-10-22 20:00 UTC from `collections_missing_versionOct22.json` following *Collection_Lineage_via_ATBD_Skill*.

* Collections: 54  · associations: 139
* Resolved: 139  · unresolved: 0
* Confidence: HIGH 133 · MEDIUM 6 · LOW 0
* Documents fetched: 19 (valid for lineage: 16)

## SENTINEL-1D_SLC v1 (`C4175278193-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_SLC v— | SENTINEL-1A_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_SLC v— | SENTINEL-1B_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_SLC v— | SENTINEL-1C_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | Sentinel-1D_META_SLC v— | SENTINEL-1D_META_SLC v1 | case_normalized / unique_in_cmr | HIGH | identifier case_normalized; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1C_SLC v1 (`C3470873558-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_SLC v— | SENTINEL-1A_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_SLC v— | SENTINEL-1B_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | SENTINEL-1C_META_SLC v— | SENTINEL-1C_META_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## AST_L1T v004 (`C3306888411-LPCLOUD`)

* Document (priority 1, valid): https://lpdaac.usgs.gov/documents/1400/AST_L1T_ATBD_V1.pdf
* Document (priority 4, valid): https://lpdaac.usgs.gov/documents/2265/ASTER_User_Guide_V4_pcP80n5.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | AST_L1A v— | AST_L1A v004 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok; document evidence |

> **AST_L1A** — AST_L1T_ATBD_V1.pdf, p. 20: "Bad pixel values, for example, pixels included in missing packets during down link, damaged detectors, and all AST_L1B pixels generated from bad pixels in an input AST_L1A scene, are evaluated and corrected, using linear interpolation to generate replacement values when feasible (Earth Remote Sensing Data Analysis Center, 2007), before radiance is converted to Digital Number (DN) values taking int"

## VNP14IMGTDL_NRT v2 (`C1942970257-LANCEMODIS`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | VNP14 v— | VNP14 v002 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## AST_L1B v004 (`C3306888201-LPCLOUD`)

* Document (priority 1, valid): https://lpdaac.usgs.gov/documents/70/AST_L1_ATBD.pdf
* Document (priority 4, valid): https://lpdaac.usgs.gov/documents/2265/ASTER_User_Guide_V4_pcP80n5.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | AST_L1A v— | AST_L1A v004 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok; document evidence |

> **AST_L1A** — ASTER_User_Guide_V4_pcP80n5.pdf, p. 12: "8.3 Cloud-Optimized GeoTIFF (COG) File Format Along with auxiliary dataset improvements, ASTER Version 4 products (except AST_L1A and AST_L1B) have transitioned from the legacy HDF-EOS2 format to Cloud Optimized GeoTIFF (COG)."

## AST_L1A v004 (`C3306888985-LPCLOUD`)

* Document (priority 1, valid): https://lpdaac.usgs.gov/documents/70/AST_L1_ATBD.pdf
* Document (priority 4, valid): https://lpdaac.usgs.gov/documents/2265/ASTER_User_Guide_V4_pcP80n5.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| DEPENDENT | AST_L1B v— | AST_L1B v004 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable; document evidence |

> **AST_L1B** — ASTER_User_Guide_V4_pcP80n5.pdf, p. 12: "8.3 Cloud-Optimized GeoTIFF (COG) File Format Along with auxiliary dataset improvements, ASTER Version 4 products (except AST_L1A and AST_L1B) have transitioned from the legacy HDF-EOS2 format to Cloud Optimized GeoTIFF (COG)."

## SENTINEL-1C_RAW v1 (`C3486496642-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_RAW v— | SENTINEL-1A_RAW v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_RAW v— | SENTINEL-1B_RAW v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | SENTINEL-1C_META_RAW v— | SENTINEL-1C_META_RAW v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_RAW v1 (`C4175250274-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_RAW v— | SENTINEL-1A_RAW v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_RAW v— | SENTINEL-1B_RAW v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_RAW v— | SENTINEL-1C_RAW v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | Sentinel-1D_META_RAW v— | SENTINEL-1D_META_RAW v1 | case_normalized / unique_in_cmr | HIGH | identifier case_normalized; version unique_in_cmr; CMR not_applicable |

## AST_L1AE v003 (`C179460405-LPDAAC_ECS`)

* Document (priority 1, valid): https://lpdaac.usgs.gov/documents/70/AST_L1_ATBD.pdf
* Document (priority 4, valid): https://asterweb.jpl.nasa.gov/content/03_data/04_Documents/ASTERHigherLevelUserGuideVer2May01.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| DEPENDENT | AST_L1B v— | AST_L1B v004 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## AST_L1BE v003 (`C179460406-LPDAAC_ECS`)

* Document (priority 1, valid): https://lpdaac.usgs.gov/documents/70/AST_L1_ATBD.pdf
* Document (priority 4, valid): https://lpdaac.usgs.gov/documents/69/AST_L1_User_Guide_V3.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | AST_L1A v— | AST_L1A v004 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |

## MOD09 v6.1NRT (`C2007657580-LANCEMODIS`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | MOD09 v— | MOD09 v6.1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## MOD09A1N v6.1NRT (`C2007661826-LANCEMODIS`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | MOD09A1N v— | MOD09A1 v061 | standard_counterpart / unique_in_cmr | MEDIUM | identifier: standard_counterpart |

## MOD09CMA v6.1NRT (`C4169087730-LANCEMODIS`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | MOD09CMA v— | MOD09CMG v061 | documented_companion / unique_in_cmr | MEDIUM | identifier: documented_companion; document evidence |

> **MOD09CMA** — MOD09_User_Guide_V61.pdf, p. 5: "MODIS surface reflectance data products MODIS surface reflectance data are found in the MOD09 series of data products, including a level 2 product (MOD09, ge nerated by PGE11's MOD_PR09.exe program), level 2G daily products (MOD09GHK, MOD09GQK, and MOD09GST, generated by PGE12's MOD_PRMGR.exe program), level 2G-Lite daily products (MOD09GA and MOD09 GQ, generated by PGE13's MOD_PR09G.exe program),"

## MOD09CMG v6.1NRT (`C2007659960-LANCEMODIS`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | MOD09CMG v— | MOD09CMG v061 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## MOD09GA v6.1NRT (`C2007661943-LANCEMODIS`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | MOD09GA v— | MOD09GA v061 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## MOD09GQ v6.1NRT (`C2007662107-LANCEMODIS`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | MOD09GQ v— | MOD09GQ v061 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## OPERA_L2_CSLC-S1-STATIC_V1 v1 (`C2795135668-ASF`)

* Document (priority 4, valid): https://d2pn8kiwq2w21t.cloudfront.net/documents/ProductSpec_CSLC-S1-STATIC.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | SENTINEL-1A_SLC v— | SENTINEL-1A_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1B_SLC v— | SENTINEL-1B_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1C_SLC v— | SENTINEL-1C_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1D_SLC v— | SENTINEL-1D_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |

## OPERA_L2_CSLC-S1_V1 v1 (`C2777443834-ASF`)

* Document (priority 1, valid): https://cumulus.asf.earthdatacloud.nasa.gov/PUBLIC/DATA/OPERA/OPERA_CSLC-S1_ATBD_D-108752_Initial_2024-06-24_signed.pdf
* Document (priority 4, valid): https://d2pn8kiwq2w21t.cloudfront.net/documents/OPERA_CSLC-S1_ProductSpec_v1.0.0_D-108278_Initial_2023-09-11_URS321269.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | SENTINEL-1A_SLC v— | SENTINEL-1A_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1B_SLC v— | SENTINEL-1B_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1C_SLC v— | SENTINEL-1C_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1D_SLC v— | SENTINEL-1D_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |

## OPERA_L2_RTC-S1-STATIC_V1 v1 (`C2795135174-ASF`)

* Document (priority 4, valid): https://d2pn8kiwq2w21t.cloudfront.net/documents/ProductSpec_RTC-S1-STATIC.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | SENTINEL-1A_SLC v— | SENTINEL-1A_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1B_SLC v— | SENTINEL-1B_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1C_SLC v— | SENTINEL-1C_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1D_SLC v— | SENTINEL-1D_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |

## OPERA_L2_RTC-S1_V1 v1 (`C2777436413-ASF`)

* Document (priority 1, valid): https://cumulus.asf.earthdatacloud.nasa.gov/PUBLIC/DATA/OPERA/D-107393_OPERA_RTC-S1_ATBD_Initial_2024-06-25_wsigs.pdf
* Document (priority 4, valid): https://cumulus.asf.earthdatacloud.nasa.gov/PUBLIC/DATA/OPERA/ProductSpec_RTC-S1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | SENTINEL-1A_SLC v— | SENTINEL-1A_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1B_SLC v— | SENTINEL-1B_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1C_SLC v— | SENTINEL-1C_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1D_SLC v— | SENTINEL-1D_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |

## SENTINEL-1C_DP_GRD_HIGH v1 (`C3486566209-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_DP_GRD_HIGH v— | SENTINEL-1A_DP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_DP_GRD_HIGH v— | SENTINEL-1B_DP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | SENTINEL-1C_DP_META_GRD_HIGH v— | SENTINEL-1C_DP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1C_DP_GRD_MEDIUM v1 (`C3486605959-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_DP_GRD_MEDIUM v— | SENTINEL-1A_DP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_DP_GRD_MEDIUM v— | SENTINEL-1B_DP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | SENTINEL-1C_DP_META_GRD_MEDIUM v— | SENTINEL-1C_DP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1C_DP_META_GRD_HIGH v1 (`C3486580531-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_DP_META_GRD_HIGH v— | SENTINEL-1A_DP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_DP_META_GRD_HIGH v— | SENTINEL-1B_DP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | SENTINEL-1C_DP_GRD_HIGH v— | SENTINEL-1C_DP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1C_DP_META_GRD_MEDIUM v1 (`C3486616327-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_DP_META_GRD_MEDIUM v— | SENTINEL-1A_DP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_DP_META_GRD_MEDIUM v— | SENTINEL-1B_DP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | SENTINEL-1C_DP_GRD_MEDIUM v— | SENTINEL-1C_DP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1C_META_OCN v1 (`C3484670556-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_META_OCN v— | SENTINEL-1A_META_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_META_OCN v— | SENTINEL-1B_META_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | SENTINEL-1C_OCN v— | SENTINEL-1C_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1C_META_RAW v1 (`C3486527075-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_META_RAW v— | SENTINEL-1A_META_RAW v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_META_RAW v— | SENTINEL-1B_META_RAW v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | SENTINEL-1C_RAW v— | SENTINEL-1C_RAW v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1C_META_SLC v1 (`C3484561061-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_META_SLC v— | SENTINEL-1A_META_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_META_SLC v— | SENTINEL-1B_META_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | SENTINEL-1C_SLC v— | SENTINEL-1C_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1C_OCN v1 (`C3484661603-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_OCN v— | SENTINEL-1A_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_OCN v— | SENTINEL-1B_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | SENTINEL-1A_META_OCN v— | SENTINEL-1A_META_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1C_SP_GRD_HIGH v1 (`C3488402208-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_SP_GRD_HIGH v— | SENTINEL-1A_SP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_SP_GRD_HIGH v— | SENTINEL-1B_SP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | SENTINEL-1C_SP_META_GRD_HIGH v— | SENTINEL-1C_SP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1C_SP_GRD_MEDIUM v1 (`C3488414315-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_SP_GRD_MEDIUM v— | SENTINEL-1A_SP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_SP_GRD_MEDIUM v— | SENTINEL-1B_SP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | SENTINEL-1C_SP_META_GRD_MEDIUM v— | SENTINEL-1C_SP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1C_SP_META_GRD_HIGH v1 (`C3488406939-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_SP_META_GRD_HIGH v— | SENTINEL-1A_SP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_SP_META_GRD_HIGH v— | SENTINEL-1B_SP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | SENTINEL-1C_SP_GRD_HIGH v— | SENTINEL-1C_SP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1C_SP_META_GRD_MEDIUM v1 (`C3488417229-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_SP_META_GRD_MEDIUM v— | SENTINEL-1A_SP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_SP_META_GRD_MEDIUM v— | SENTINEL-1B_SP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | SENTINEL-1C_SP_GRD_MEDIUM v— | SENTINEL-1C_SP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_DP_GRD_HIGH v1 (`C4163054563-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_DP_GRD_HIGH v— | SENTINEL-1A_DP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_DP_GRD_HIGH v— | SENTINEL-1B_DP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_DP_GRD_HIGH v— | SENTINEL-1C_DP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | SENTINEL-1D_DP_META_GRD_HIGH v— | SENTINEL-1D_DP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_DP_GRD_MEDIUM v1 (`C4174076966-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_DP_GRD_MEDIUM v— | SENTINEL-1A_DP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_DP_GRD_MEDIUM v— | SENTINEL-1B_DP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_DP_GRD_MEDIUM v— | SENTINEL-1C_DP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | SENTINEL-1D_DP_META_GRD_MEDIUM v— | SENTINEL-1D_DP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_DP_META_GRD_HIGH v1 (`C4171102786-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_DP_META_GRD_HIGH v— | SENTINEL-1A_DP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_DP_META_GRD_HIGH v— | SENTINEL-1B_DP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_DP_META_GRD_HIGH v— | SENTINEL-1C_DP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | SENTINEL-1D_DP_GRD_HIGH v— | SENTINEL-1D_DP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_DP_META_GRD_MEDIUM v1 (`C4174076945-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_DP_META_GRD_MEDIUM v— | SENTINEL-1A_DP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_DP_META_GRD_MEDIUM v— | SENTINEL-1B_DP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_DP_META_GRD_MEDIUM v— | SENTINEL-1C_DP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | SENTINEL-1D_DP_GRD_MEDIUM v— | SENTINEL-1D_DP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_META_OCN v1 (`C4162996551-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_META_OCN v— | SENTINEL-1A_META_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_META_OCN v— | SENTINEL-1B_META_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_META_OCN v— | SENTINEL-1C_META_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | SENTINEL-1D_OCN v— | SENTINEL-1D_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_META_RAW v1 (`C4175250286-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_META_RAW v— | SENTINEL-1A_META_RAW v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_META_RAW v— | SENTINEL-1B_META_RAW v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_META_RAW v— | SENTINEL-1C_META_RAW v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | Sentinel-1D_RAW v— | SENTINEL-1D_RAW v1 | case_normalized / unique_in_cmr | HIGH | identifier case_normalized; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_META_SLC v1 (`C4175278190-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_META_SLC v— | SENTINEL-1A_META_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_META_SLC v— | SENTINEL-1B_META_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_META_SLC v— | SENTINEL-1C_META_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | Sentinel-1D_SLC v— | SENTINEL-1D_SLC v1 | case_normalized / unique_in_cmr | HIGH | identifier case_normalized; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_OCN v1 (`C4162942865-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_OCN v— | SENTINEL-1A_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_OCN v— | SENTINEL-1B_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_OCN v— | SENTINEL-1C_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | SENTINEL-1D_META_OCN v— | SENTINEL-1D_META_OCN v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_SP_GRD_HIGH v1 (`C4174044457-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_SP_GRD_HIGH v— | SENTINEL-1A_SP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_SP_GRD_HIGH v— | SENTINEL-1B_SP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_SP_GRD_HIGH v— | SENTINEL-1C_SP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | SENTINEL-1D_SP_META_GRD_HIGH v— | SENTINEL-1D_SP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_SP_GRD_MEDIUM v1 (`C4175200051-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_SP_GRD_MEDIUM v— | SENTINEL-1A_SP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_SP_GRD_MEDIUM v— | SENTINEL-1B_SP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_SP_GRD_MEDIUM v— | SENTINEL-1C_SP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| SCIENCE ASSOCIATED | SENTINEL-1D_SP_META_GRD_MEDIUM v— | SENTINEL-1D_SP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_SP_META_GRD_HIGH v1 (`C4174044493-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_SP_META_GRD_HIGH v— | SENTINEL-1A_SP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_SP_META_GRD_HIGH v— | SENTINEL-1B_SP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_SP_META_GRD_HIGH v— | SENTINEL-1C_SP_META_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | SENTINEL-1D_SP_GRD_HIGH v— | SENTINEL-1D_SP_GRD_HIGH v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_SP_META_GRD_MEDIUM v1 (`C4175200042-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | SENTINEL-1A_SP_META_GRD_MEDIUM v— | SENTINEL-1A_SP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1B_SP_META_GRD_MEDIUM v— | SENTINEL-1B_SP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| RELATED | SENTINEL-1C_SP_META_GRD_MEDIUM v— | SENTINEL-1C_SP_META_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |
| DEPENDENT | SENTINEL-1D_SP_GRD_MEDIUM v— | SENTINEL-1D_SP_GRD_MEDIUM v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1_BURSTS v1 (`C2709161906-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1-Bursts/Sentinel-1-Bursts-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | SENTINEL-1A_SLC v— | SENTINEL-1A_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENTINEL-1B_SLC v— | SENTINEL-1B_SLC v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR ok |
| INPUT | SENIINEL-1C_SLC v— | SENTINEL-1C_SLC v1 | typo_corrected / unique_in_cmr | MEDIUM | identifier: typo_corrected |
| INPUT | SENIINEL-1D_SLC v— | SENTINEL-1D_SLC v1 | typo_corrected / unique_in_cmr | MEDIUM | identifier: typo_corrected |

## UAVSAR_POLSAR v1 (`C4261555796-ASF`)

* Document (priority 4, not valid): https://uavsar.jpl.nasa.gov/science/documents/polsar-format.html

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | UAVSAR_RPI v— | UAVSAR_RPI v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## UAVSAR_RPI v1 (`C4261689115-ASF`)

* Document (priority 4, not valid): https://uavsar.jpl.nasa.gov/science/documents/rpi-format.html

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | UAVSAR_POLSAR v— | UAVSAR_POLSAR v1 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## VJ114IMG_NRT v2 (`C1907902788-LANCEMODIS`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | VJ114 v— | VJ114 v002 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## VJ146A1G_NRT v2 (`C2781431577-LANCEMODIS`)

* Document (priority 4, valid): https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/Black-Marble_v2.0_UG_2024.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | VNP46A1_1 v— | VNP46A1 v2 | embedded_split / unique_in_cmr | MEDIUM | identifier: embedded_split; document evidence |

> **VNP46A1_1** — Black-Marble_v2.0_UG_2024.pdf, p. 4: "iv List of Tables Table 1 Black Marble VNP46A1 product input files ...................................................................................."

## VJ146A1_NRT v2 (`C2781438623-LANCEMODIS`)

* Document (priority 4, valid): https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/Black-Marble_v2.0_UG_2024.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | VNP46A1_2 v— | VNP46A1 v2 | embedded_verified / original_verified | HIGH | identifier embedded_verified; version original_verified; CMR not_applicable; document evidence |

> **VNP46A1_2** — Black-Marble_v2.0_UG_2024.pdf, p. 4: "iv List of Tables Table 1 Black Marble VNP46A1 product input files ...................................................................................."

## VJ214IMG_NRT v2 (`C2837613056-LANCEMODIS`)

* Document (priority 4, valid): https://viirsland.gsfc.nasa.gov/PDF/VIIRS_activefire_User_Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | VJ114 v— | VJ114 v002 | exact / unique_in_cmr | HIGH | identifier exact; version unique_in_cmr; CMR not_applicable |

## VNP46A1G_NRT v2 (`C2780764136-LANCEMODIS`)

* Document (priority 4, valid): https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/Black-Marble_v2.0_UG_2024.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | VNP46A1_1 v— | VNP46A1 v2 | embedded_split / unique_in_cmr | MEDIUM | identifier: embedded_split; document evidence |

> **VNP46A1_1** — Black-Marble_v2.0_UG_2024.pdf, p. 4: "iv List of Tables Table 1 Black Marble VNP46A1 product input files ...................................................................................."

## VNP46A1_NRT v2 (`C2780753001-LANCEMODIS`)

* Document (priority 4, valid): https://landweb.modaps.eosdis.nasa.gov/data/userguide/BlackMarbleUserGuide_Collection2.0_20241203.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | VNP46A1_2 v— | VNP46A1 v2 | embedded_verified / original_verified | HIGH | identifier embedded_verified; version original_verified; CMR not_applicable; document evidence |

> **VNP46A1_2** — BlackMarbleUserGuide_Collection2.0_20241203.pdf, p. 4: "iv List of Tables Table 1 Black Marble VNP46A1 product input files ...................................................................................."

## VNP46A2_NRT v2 (`C3363944097-LANCEMODIS`)

* Document (priority 4, valid): https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/Black-Marble_v2.0_UG_2024.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | VNP46A2_2 v— | VNP46A2 v2 | embedded_verified / original_verified | HIGH | identifier embedded_verified; version original_verified; CMR not_applicable; document evidence |

> **VNP46A2_2** — Black-Marble_v2.0_UG_2024.pdf, p. 31: "25 NTL composite, the associated the number of valid observations used for the composite, and quality flags generated from daily lunar-BRDF-corrected NTL product (VNP46A2) for tile h06v05 in 2016."
