# Shortname Mismatch — lineage repair report

Generated 2026-10-22 20:13 UTC from `collections_shortname_mismatchOct22.json` following *Collection_Lineage_via_ATBD_Skill*.

* Collections: 210  · associations: 470
* Resolved: 51  · unresolved: 419
* Confidence: HIGH 14 · MEDIUM 37 · LOW 419
* Documents fetched: 68 (valid for lineage: 42)

## SENTINEL-1D_SLC v1 (`C4175278193-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | Sentinel-1D_META_SLC v— | SENTINEL-1D_META_SLC v1 | case_normalized / unique_in_cmr | HIGH | identifier case_normalized; version unique_in_cmr; CMR not_applicable |

## CAL_LID_L2_01kmCLay-Standard-V5-00 vV5-00 (`C3463063995-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/calipso/CALIPSO_DPC_Rev5x00.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/calipso/user_guides/CALIPSO_Data_Users_Guide_FAQ_mod2.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CAL_LID_L2_01kmCLay-Standard-V4-21 vV4-21 | CAL_LID_L2_01kmCLay-Standard-V4-51 vV4-51 | versioned_family / unique_in_cmr | MEDIUM | identifier: versioned_family |

## CAL_LID_L2_05kmAPro-Standard-V5-00 vV5-00 (`C3551627908-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/calipso/CALIPSO_DPC_Rev5x00.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/calipso/user_guides/CALIPSO_Data_Users_Guide_FAQ_mod2.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CAL_LID_L2_05kmAPro-Standard-V4-21 vV4-21 | CAL_LID_L2_05kmAPro-Standard-V4-51 vV4-51 | versioned_family / unique_in_cmr | MEDIUM | identifier: versioned_family |

## OPERA_L4_TROPO-ZENITH_V1 v1 (`C3717139408-ASF`)

* Document (priority 4, valid): https://d2pn8kiwq2w21t.cloudfront.net/documents/OPERA_TROPO_CalVal_Product_Spec.pdf
* Document (priority 4, not valid): https://www.ecmwf.int/en/forecasts/datasets/set-i/

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | ASF_ECMWF_TROPO v1 | ASF_ECMWF_TROP v1 | typo_corrected / original_verified | MEDIUM | identifier: typo_corrected |

## CAL_IIR_L2_Track-Standard-V5-00 vV5-00 (`C3964849248-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/calipso/user_guides/CALIPSO_Data_Users_Guide_Payload.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/calipso/user_guides/CALIPSO_Data_Users_Guide_Peer_Reviewed_Bibliography.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CAL_IIR_L2_Track-Beta-V4-51 vV4-51 | CAL_IIR_L2_Track-Standard-V4-51 vV4-51 | versioned_family / unique_in_cmr | MEDIUM | identifier: versioned_family |

## CAL_LID_L2_VFM-Standard-V5-00 vV5-00 (`C3463064020-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/calipso/CALIPSO_DPC_Rev5x00.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/calipso/user_guides/CALIPSO_Data_Users_Guide_FAQ_mod2.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CAL_LID_L2_VFM-Standard-V4-21 vV4-21 | CAL_LID_L2_VFM-Standard-V4-51 vV4-51 | versioned_family / unique_in_cmr | MEDIUM | identifier: versioned_family |

## MIL3DAEN v004 (`C2873769854-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIL3SAE v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3DAL v006 (`C2873770054-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIL3SAL v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3DCFA v001 (`C2873770864-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_CFbA_Product.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIL3SCFA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3DCOD v001 (`C2873771242-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIL3SCOD v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3MAEN v004 (`C2873771604-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3MAL v006 (`C2873771775-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3QAE v004 (`C3387017698-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3QAEN v004 (`C2873773600-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3QAL v006 (`C2873773796-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3YAE v004 (`C3387017703-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3YAL v006 (`C2873775162-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## SENTINEL-1D_RAW v1 (`C4175250274-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | Sentinel-1D_META_RAW v— | SENTINEL-1D_META_RAW v1 | case_normalized / unique_in_cmr | HIGH | identifier case_normalized; version unique_in_cmr; CMR not_applicable |

## AIRMISR_KONVEX v1 (`C3880545201-LARC_CLOUD`)

* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/airmisr/airmisr_read_software.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/airmisr/readme/readme_airmisr_konvex

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | AIRMISR v1 | *ambiguous* | — / — | LOW | not resolved (ambiguous) |

> **AIRMISR** — readme_airmisr_konvex: "The read_airmisr.pro program can be used to read any of the AIRMISR_KONVEX Georectified radiance product files, i.e., "GP" files."

## AIRMISR_LUNAR_LAKE_2000 v1 (`C3880545252-LARC_CLOUD`)

* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/airmisr/airmisr_read_software.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/airmisr/readme/readme_airmisr_lunar_lake_2000

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | AIRMISR v1 | *ambiguous* | — / — | LOW | not resolved (ambiguous) |

> **AIRMISR** — readme_airmisr_lunar_lake_2000: "The read_airmisr.pro program can be used to read any of the AIRMISR_LUNAR_LAKE_2000 Georectified radiance product files, i.e., "GP" files."

## ARESE_ER2_MAS v1 (`C3880547116-LARC_CLOUD`)

* Document (priority 4, not valid): https://eosweb.larc.nasa.gov/sites/default/files/project/arese/guide/arese_project.pdf
* Document (priority 4, not valid): https://eosweb.larc.nasa.gov/sites/default/files/project/arese/guide/base_arese_er2_mas_dataset.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | MAS v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## ATOST_ER2_MAS v1 (`C3880547171-LARC_CLOUD`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | MAS v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## ATSM2AEF v001 (`C3417608766-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## ATSM2LSF v001 (`C3417608836-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## ATSM2STF v001 (`C3417608893-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## ATSMIB2E v003 (`C3417608963-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MI1B2EP v1 | MI1B2E v003 | typo_corrected / matches_target | MEDIUM | identifier: typo_corrected |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## ATSMIB2T v003 (`C3417609031-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MI1B2TP v1 | MI1B2T v003 | typo_corrected / matches_target | MEDIUM | identifier: typo_corrected |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## ATSMIGEO v002 (`C3417609127-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MISANCGM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## AirMSPI_SEAC4RS_Terrain-projected_Georegistered_Radiance_Data v5 (`C3986090252-LARC_CLOUD`)

* Document (priority 1, not valid): https://eosweb.larc.nasa.gov/project/airmspi/guide/AirMSPI_Cloud_Droplet_ATBD.20180117.pdf
* Document (priority 4, not valid): https://eosweb.larc.nasa.gov/project/airmspi/quality_summaries/AirMSPI_L1B2_Quality.SEAC4RS-20180205.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | AirMSPI v1 | *ambiguous* | — / — | LOW | not resolved (ambiguous) |
| PARENT | SEAC4RS v1 | *ambiguous* | — / — | LOW | not resolved (ambiguous) |

## CAL_IIR_L2_Swath-Standard-V4-51 vV4-51 (`C3880518673-LARC_CLOUD`)

* Document (priority 4, not valid): https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x96.pdf
* Document (priority 4, not valid): https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CAL_IIR_L2_Swath-Standard-V4-20 vV4-20 | CAL_IIR_L2_Swath-Standard-V5-00 vV5-00 | versioned_family / unique_in_cmr | MEDIUM | identifier: versioned_family |

## CAL_IIR_L2_Track-Standard-V4-51 vV4-51 (`C3880518924-LARC_CLOUD`)

* Document (priority 4, not valid): https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x96.pdf
* Document (priority 4, not valid): https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CAL_IIR_L2_Track-Beta-V3-45 vV3-45 | CAL_IIR_L2_Track-Standard-V5-00 vV5-00 | versioned_family / unique_in_cmr | MEDIUM | identifier: versioned_family |
| PARENT | OPeNDAP data access for CAL_IIR_L2_Track-Standard-V4-20 vV4-20 | CAL_IIR_L2_Track-Standard-V5-00 vV5-00 | versioned_family / unique_in_cmr | MEDIUM | identifier: versioned_family |

## CAL_LID_L1-Standard-V4-51 vV4-51 (`C3880519157-LARC_CLOUD`)

* Document (priority 4, not valid): https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/
* Document (priority 4, not valid): https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x95.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | CAL_LID_L1-Standard-V4-10 vV4-10 | CAL_LID_L1-Standard-V5-00 vV5-00 | versioned_family / unique_in_cmr | MEDIUM | identifier: versioned_family |
| RELATED | CAL_LID_L1-Standard-V4-11 vV4-11 | CAL_LID_L1-Standard-V5-00 vV5-00 | versioned_family / unique_in_cmr | MEDIUM | identifier: versioned_family |

## CAL_LID_L2_05kmCPro-Standard-V5-00 vV5-00 (`C3551627896-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/calipso/CALIPSO_DPC_Rev5x00.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/calipso/user_guides/CALIPSO_Data_Users_Guide_FAQ_mod2.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CAL_LID_L2_05kmAPro-Standard-V4-21 vV4-21 | CAL_LID_L2_05kmAPro-Standard-V4-51 vV4-51 | versioned_family / unique_in_cmr | MEDIUM | identifier: versioned_family |

## CAL_LID_L2_333mMLay-Standard-V5-00 vV5-00 (`C3551627915-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/calipso/CALIPSO_DPC_Rev5x00.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/calipso/user_guides/CALIPSO_Data_Users_Guide_FAQ_mod2.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CAL_LID_L2_333mMLay-Standard-V4-21 vV4-21 | CAL_LID_L2_333mMLay-Standard-V4-51 vV4-51 | versioned_family / unique_in_cmr | MEDIUM | identifier: versioned_family |

## CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-20 vV4-20 (`C3880523630-LARC_CLOUD`)

* Document (priority 4, not valid): https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/
* Document (priority 4, not valid): https://atrain.nasa.gov/publications/CALIPSO.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CAL_LID_L3_APro_AllSky-Standard-V3-10 vV3-10 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20 vV4-20 (`C3880523637-LARC_CLOUD`)

* Document (priority 4, not valid): https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/calipso/TiltModeGeometry.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CAL_LID_L3_APro_CloudFree-Standard-V3-10 vV3-10 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CAL_LID_L3_Tropospheric_APro_CloudySkyOpaque-Standard-V4-20 vV4-20 (`C3880523648-LARC_CLOUD`)

* Document (priority 4, not valid): https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/calipso/TiltModeGeometry.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CAL_LID_L3_APro_CloudySkyOpaque-Standard-V3-00 vV3-00 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| PARENT | CAL_LID_L3_APro_CloudySkyOpaque-Standard-V3-10 vV3-10 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CAL_LID_L3_Tropospheric_APro_CloudySkyOpaque-Standard-V4-21 vV4-21 (`C3880523651-LARC_CLOUD`)

* Document (priority 4, not valid): https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf
* Document (priority 4, not valid): https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CAL_LID_L3_APro_CloudySkyOpaque-Standard-V4-20 vV4-20 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CARMIAAE v002 (`C3417609165-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CARMITST v002 (`C3417609182-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CAR_KUWAITOILFIRE_BRDF v2 (`C1617621689-GES_DISC`)

* Document (priority 4, valid): https://docserver.gesdisc.eosdis.nasa.gov/public/project/CAR/CAR_BRDF_README-v2.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | KUWAITOILFIRE_BRDF.2 v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CATS-ISS_L1B_D-M7.1-V3-00 vV3-00 (`C3880592074-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf
* Document (priority 4, valid): https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CATS-ISS_L1B_D-M7.1-V2-08 vV2-08 | *self_reference* | typo_corrected / self_reference | LOW | not resolved (self_reference) |

## CATS-ISS_L1B_D-M7.2-V3-00 vV3-00 (`C3880592401-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf
* Document (priority 4, valid): https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CATS-ISS_L1B_D-M7.2-V2-08 vV2-08 | *self_reference* | typo_corrected / self_reference | LOW | not resolved (self_reference) |

## CATS-ISS_L1B_N-M7.1-V3-00 vV3-00 (`C3880592530-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf
* Document (priority 4, valid): https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CATS-ISS_L1B_N-M7.1-V2-08 vV2-08 | *self_reference* | typo_corrected / self_reference | LOW | not resolved (self_reference) |

## CATS-ISS_L1B_N-M7.2-V3-00 vV3-00 (`C3880592741-LARC_CLOUD`)

* Document (priority 4, valid): https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/cats/quality_summaries/CATS_Release_Notes6_v2.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CATS-ISS_L1B_N-M7.2-V2-08 vV2-08 | *self_reference* | typo_corrected / self_reference | LOW | not resolved (self_reference) |

## CATS-ISS_L2O_D-M7.1-V3-01_05kmLay vV3-01 (`C3880592769-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf
* Document (priority 4, valid): https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CATS-ISS_L2O_D-M7.1-V3-00_05kmLay vV3-00 | *documented_not_in_cmr* | — / — | LOW | not resolved (documented_not_in_cmr) |

> **CATS-ISS_L2O_D-M7.1-V3-00_05kmLay** — CATS_Data_Products_Catalog.pdf, p. 29: "October 01, 2018 V1-02 Corresponds to V3_00 L2 Product Software Data File Name: 5 km Layer: CATS-ISS_L2O_D-M7.1-V3-00_05kmLay.2014-09-17T00-31-01UTC.hdf5 Table 1: CATS-ISS 5 km Layer Record Summary for Mode 7.1 Table 2: CATS-ISS 5 km Layer Record Summary for Mode 7.2 Record Name Reference Table Record Size (Bytes) Records/File File Size (Bytes) Metadata Table 4 2,504 1 2,504 Geolocation and Viewin"

## CATS-ISS_L2O_D-M7.1-V3-01_05kmPro vV3-01 (`C3880592830-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf
* Document (priority 4, valid): https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CATS-ISS_L2O_D-M7.1-V3-00_05kmPro vV3-00 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CATS-ISS_L2O_D-M7.2-V3-00_05kmLay vV3-00 (`C3880593042-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf
* Document (priority 4, valid): https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CATS-ISS_L2O_D-M7.2-V2-01_05kmLay vV2-01 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CATS-ISS_L2O_D-M7.2-V3-00_05kmPro vV3-00 (`C3880593077-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf
* Document (priority 4, valid): https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CATS-ISS_L2O_D-M7.2-V2-01_05kmPro vV2-01 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CATS-ISS_L2O_N-M7.1-V3-01_05kmLay vV3-01 (`C3880593136-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/cats/quality_summaries/CATS_Release_Notes6_v2.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CATS-ISS_L2O_N-M7.1-V3-00_05kmLay vV3-00 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CATS-ISS_L2O_N-M7.1-V3-01_05kmPro vV3-01 (`C3880593151-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/cats/quality_summaries/CATS_QS_L2O_Profile_2.01.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CATS-ISS_L2O_N-M7.1-V3-00_05kmPro vV3-00 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CATS-ISS_L2O_N-M7.2-V3-00_05kmLay vV3-00 (`C3880593171-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf
* Document (priority 4, valid): https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CATS-ISS_L2O_N-M7.2-V2-01_05kmLay vV2-01 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CATS-ISS_L2O_N-M7.2-V3-00_05kmPro vV3-00 (`C3880593201-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf
* Document (priority 4, valid): https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CATS-ISS_L2O_N-M7.2-V2-01_05kmPro vV2-01 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CER_BDS_Aqua-FM3 vEdition1-CV (`C3880454566-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_BDS_R6V1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CER_BDS_Aqua-FM3_Edition1 v1 | CER_BDS_Aqua-FM3 vEdition4 | embedded_split / unique_in_cmr | MEDIUM | identifier: embedded_split |

## CER_BDS_Aqua-FM4 vEdition1-CV (`C3880454812-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_BDS_Aqua_Edition1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| CHILD | CER_BDS_Aqua-FM4_Edition2 v2 | CER_BDS_Aqua-FM4 vEdition4 | embedded_split / unique_in_cmr | MEDIUM | identifier: embedded_split |

## CER_BDS_Terra-FM1 vEdition1-CV (`C3880455569-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/ceres/guide/cer_bds.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CER_BDS_Terra-FM1_Edition1 v1 | CER_BDS_Terra-FM1 vEdition4 | embedded_split / unique_in_cmr | MEDIUM | identifier: embedded_split |
| CHILD | CER_BDS_Terra-FM1_Edition2 v2 | CER_BDS_Terra-FM1 vEdition4 | embedded_split / unique_in_cmr | MEDIUM | identifier: embedded_split |

## CER_BDS_Terra-FM2 vEdition1-CV (`C3880455643-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/ceres/guide/cer_bds.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CER_BDS_Terra-FM2_Edition1 v1 | CER_BDS_Terra-FM2 vEdition4 | embedded_split / unique_in_cmr | MEDIUM | identifier: embedded_split |
| CHILD | CER_BDS_Terra-FM2_Edition2 v2 | CER_BDS_Terra-FM2 vEdition4 | embedded_split / unique_in_cmr | MEDIUM | identifier: embedded_split |

## CER_CCCM_Aqua-FM3-MODIS-CAL-CS vRelD2 (`C3880454265-LARC_CLOUD`)

* Document (priority 4, valid): https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_CCCM_DQS_RelD2.pdf
* Document (priority 4, valid): https://ceres.larc.nasa.gov/documents/DPC/DPC_current/pdfs/DPC_SSF_CRS_C3M_RelD1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CER_CCCM_Aqua-FM3-MODIS-CAL-CS_RelD1 vRelD1 | *self_reference* | embedded_split / self_reference | LOW | not resolved (self_reference) |

## CER_CRS_Aqua-FM3-MODIS vEdition4A (`C3880455907-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/ceres/examples.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CER_SSF_Aqua-FM3-MODIS_Edition4A vEdition4A | CER_SSF_Aqua-FM3-MODIS vEdition4A | embedded_verified / original_verified | HIGH | identifier embedded_verified; version original_verified; CMR ok |

## CER_CRS_Terra-FM1-MODIS vEdition2G (`C3880455936-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_CRS_R5V1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CER_CRS_Terra-FM1-MODIS_Edition2A v2A | CER_CRS_Terra-FM1-MODIS vEdition4A | embedded_split / unique_in_cmr | MEDIUM | identifier: embedded_split |

## CER_ES4_TRMM-PFM vEdition2 (`C3880499915-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, valid): https://ceres.larc.nasa.gov/documents/collect_guide/pdf/ES4_CG_R1V1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CER_ES4_TRMM-PFM_Edition1 v1 | *self_reference* | embedded_split / self_reference | LOW | not resolved (self_reference) |

## CER_ES8_TRMM-PFM vEdition2 (`C3880499656-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_ES8_R7V1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CER_ES8_TRMM-PFM_Transient-Ops2 v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CER_ES9_TRMM-PFM vEdition2 (`C3880500188-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_ES9_R7V1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CER_ES9_TRMM-PFM_Edition1 v1 | *self_reference* | embedded_split / self_reference | LOW | not resolved (self_reference) |

## CER_SSF1deg-Month_NOAA20-VIIRS vEdition1C (`C3425515481-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, valid): https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SSF1deg_Ed4A_DQS.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CER_SSF1DEG-MONTH_NOAA20-VIIRS vEDITION1A | *self_reference* | case_normalized / self_reference | LOW | not resolved (self_reference) |

## CER_SSF1deg-Month_NPP-VIIRS vEdition2B (`C4232284622-LARC_CLOUD`)

* Document (priority 4, valid): https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SSF1deg_Ed4A_DQS.pdf
* Document (priority 4, valid): https://ceres.larc.nasa.gov/documents/DPC/DPC_current/pdfs/DPC_SSF1deg-Month_R5V1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CER_SSF1DEG-MONTH_NPP-VIIRS vEdition2A | CER_SSF1deg-Month_NPP-VIIRS vEdition2A | case_normalized / original_verified | HIGH | identifier case_normalized; version original_verified; CMR ok |

## CER_SSF1deg-Month_NPP-VIIRS vEdition2A (`C3880507073-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, valid): https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SSF1deg_Ed4A_DQS.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CER_SSF1DEG-MONTH_NPP-VIIRS vEDITION1A | CER_SSF1deg-Month_NPP-VIIRS vEdition2B | case_normalized / unique_in_cmr | HIGH | identifier case_normalized; version unique_in_cmr; CMR ok |

## CER_SYN1deg-Day_Terra-Aqua-NOAA20 vEdition4B (`C3880454279-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/ceres/guide/cer_syn1deg.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | CER_SYN1deg-Day_Terra-Aqua-MODIS vEdition4A | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CER_SYN1deg-MHour_Terra-Aqua-NOAA20 vEdition4B (`C3181056152-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/ceres/guide/cer_syn1deg.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | CER_SYN1deg-M1Hour_Terra-Aqua-MODIS vEdition4A | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CER_SYN1deg-Month_Terra-Aqua-NOAA20 vEdition4B (`C3880454295-LARC_CLOUD`)

* Document (priority 1, not valid): https://asdc.larc.nasa.gov/documents/ceres/CERES_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/ceres/guide/cer_syn1deg.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | CER_SYN1deg-Month_Terra-Aqua vVersion4A | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CLAMS_CERES_CHESLIGHT_SONDE v1 (`C3880593267-LARC_CLOUD`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CLAMS v0 | *ambiguous* | — / — | LOW | not resolved (ambiguous) |

## CLAMS_ER2_MAS v1 (`C3880593293-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/clams/readme/readme_clams_mas.txt

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | MAS v1 | *documented_not_in_cmr* | — / — | LOW | not resolved (documented_not_in_cmr) |
| PARENT | CLAMS v1 | *ambiguous* | — / — | LOW | not resolved (ambiguous) |

> **MAS** — readme_clams_mas.txt: "2.2 Data Quality Note that spectral response curves used for processing raw MAS instrument counts to calibrated radiances were "atmospherically corrected" and smoothed."

> **CLAMS** — readme_clams_mas.txt: "The clams_mas_read_idl.pro program will read data from the input file and write it out in ASCII format to a file with the same name but with .rpt as the extension."

## CLAMS_MODIS_L2_AEROSOL_PRODUCTS v1 (`C3880593388-LARC_CLOUD`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | CLAMS v0 | *ambiguous* | — / — | LOW | not resolved (ambiguous) |

## CMRMIAAE v002 (`C3422083483-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CMRMIALS v002 (`C3422083504-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CMRMIGEO v002 (`C3422083610-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MISANCGM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## CMRMITST v002 (`C3422083715-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## DSCOVR_EPIC_L2_COMPOSITE v02 (`C3860110047-LARC_CLOUD`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | DSCOVR_EPIC_L2_COMPOSITE_01 v01 | *self_reference* | embedded_split / self_reference | LOW | not resolved (self_reference) |

## ERBE_S10N_WFOV_SF_ERBS_AreaAverageTimeSeries vEdition4 (`C3880595228-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/measures/quality_summaries/ERBE-Measures_DQS.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | ERBE_S10N_WFOV_SF_Edition3 v3 | ERBE_S10N_WFOV_SF vEdition3 | embedded_verified / original_verified | HIGH | identifier embedded_verified; version original_verified; CMR not_applicable |
| RELATED | ERBE_S10N_WFOV_SF_ERBS_REGIONAL_EDITION4 v4 | ERBE_S10N_WFOV_SF_ERBS_Regional vEdition4 | embedded_verified / original_verified | HIGH | identifier embedded_verified; version original_verified; CMR not_applicable |

## ERBE_S10N_WFOV_SF_ERBS_Regional vEdition4 (`C3880596832-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/measures/quality_summaries/ERBE-Measures_DQS.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | ERBE_S10N_WFOV_SF_Edition3 v3 | ERBE_S10N_WFOV_SF vEdition3 | embedded_verified / original_verified | HIGH | identifier embedded_verified; version original_verified; CMR not_applicable |
| RELATED | ERBE_S10_WFOV_SF_ERBS_AREAAVERAGETIMESERIES_EDITION4 v4 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## GOMI2AE v002 (`C3417609211-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/GoMACCS/gomaccs_lm_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## GOMI2LS v002 (`C3417609217-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/GoMACCS/gomaccs_lm_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## GOMI2ST v002 (`C3417609252-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## GOMIB2E v003 (`C3417609305-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/GoMACCS/gomaccs_lm_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MI1B2EP v1 | MI1B2E v003 | typo_corrected / matches_target | MEDIUM | identifier: typo_corrected |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## GOMIB2T v003 (`C3417609355-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/GoMACCS/gomaccs_lm_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MI1B2TP v1 | MI1B2T v003 | typo_corrected / matches_target | MEDIUM | identifier: typo_corrected |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## GOMIGEO v002 (`C3417609359-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/GoMACCS/gomaccs_lm_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MISANCGM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## IXBMI2AE v002 (`C3422083722-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## IXBMI2LS v002 (`C3422083724-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## IXBMI2ST v002 (`C3422083726-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## IXBMIB2E v003 (`C3422083734-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | IXBMIB2EP v1 | *self_reference* | typo_corrected / self_reference | LOW | not resolved (self_reference) |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## IXBMIB2T v003 (`C3422083818-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | IXBMIB2TP v1 | *self_reference* | typo_corrected / self_reference | LOW | not resolved (self_reference) |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## IXBMIGEO v002 (`C3422083875-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MISANCGM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MB2LME v002 (`C2854334785-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/DPS_GRP_V030.20240624.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MISANCGM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIAA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIAF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIAN v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIBA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIBF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOICA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOICF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIDA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIDF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPAA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPAF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPAN v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPBA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPBF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPCA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPCF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPDA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPDF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRCCT v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI1B1 v002 (`C2873768416-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MISL0AN v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0DF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0CF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0BF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0AF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0AA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0BA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0CA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0DA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI1B2E v003 (`C3257326597-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/observing_concept.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MI1B2EP v4 | MI1B2E v004 | typo_corrected / original_verified | MEDIUM | identifier: typo_corrected; document evidence |
| CHILD | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

> **MI1B2EP** — L1_Products.pdf, p. 1: "GRP_ELLIPSOID_GM, MI1B2E) (from MISR PGE22) (Stage 3 Validated) L1B2 Terrain Local Mode (a.k.a."

## MI1B2T v004 (`C2854334658-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/DPS_v50_RevS.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| RELATED | MI1B2_ELLIPSOID_NRT v001 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI1B2T v003 (`C3257326624-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MI1B2TP v1 | MI1B2T v004 | typo_corrected / unique_in_cmr | MEDIUM | identifier: typo_corrected |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3DAEF v002 (`C3387017290-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3DAENF v002 (`C2854338720-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3DALF v002 (`C2854337789-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3DALNF v002 (`C2854338447-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3DCDF v002 (`C2854338179-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3DCDNF v002 (`C2854338573-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3DLSF v002 (`C3387017341-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3DLSNF v002 (`C2854338930-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3DRDF v002 (`C2854337331-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3MAEF v002 (`C3387017425-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3MAENF v002 (`C2854339684-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3MALF v002 (`C2854339252-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3MALNF v002 (`C2854339491-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3MCDF v002 (`C2854339370-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3MCDNF v002 (`C2854339578-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3MCLDN v002 (`C2873768742-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3MLSF v002 (`C3387017544-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3MRDF v002 (`C2854339112-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3MRDR v002 (`C3417609404-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3QCLDN v002 (`C2873769069-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MI3YCLDN v002 (`C2873769466-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIB1LM v002 (`C2854334270-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MISL0AN v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0DF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0CF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0BF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0AF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0AA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0BA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0CA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MISL0DA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIB2GEOP v002 (`C3257326645-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MISANCGM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2ASAE v002 (`C3417629474-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L2_AS_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2ASAF v002 (`C2873769608-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2ASLF v002 (`C2854335482-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCRT v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2ASLS v003 (`C2854337125-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCRT v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2TCAF v001 (`C3387017704-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2TCAL v002 (`C2854336695-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2TCCF v002 (`C2854335355-LARC_CLOUD`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2TCCF v001 (`C3387017705-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2TCCL v003 (`C2854336390-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2TCSF v001 (`C3387017709-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2TCSP v002 (`C2854336257-LARC_CLOUD`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v002 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2TCSP v001 (`C2854335956-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL2TCST v002 (`C2854335636-LARC_CLOUD`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3DALN v006 (`C2873770629-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIL3SAL v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3DCLD v002 (`C2873771124-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3DLS v004 (`C3387017654-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIL3SLS v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3DLSN v004 (`C2873771301-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIL3SLS v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3DRD v004 (`C2873771503-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIL3SRD v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3MALN v006 (`C2873772253-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3MCLD v002 (`C2873772597-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3MLS v004 (`C3387017684-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3MLSN v004 (`C2873773072-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3MRD v005 (`C2873773424-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3QALN v006 (`C2873773976-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3QCLD v002 (`C2873774382-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3QLS v004 (`C3387017702-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3QLSN v004 (`C2873774574-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3QRD v005 (`C2873774681-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3YAEN v004 (`C2873774819-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3YALN v006 (`C2873775262-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3YCLD v002 (`C2873775633-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3YLSN v004 (`C2873775922-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIL3YRD v005 (`C2873776171-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIRCCM v004 (`C2951415957-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRCCT v4 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANRCCH v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIRCCMF v002 (`C2854335241-LARC_CLOUD`)

* No lineage document linked in CMR or the input file

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRCCT v4 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRCCHF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## MIRCCMF v001 (`C3387017710-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRCCT v4 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRCCHF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## PREFIRE_SAT1_3-SFC-SORTED-ALLSKY vR01 (`C3544479147-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/prefire/guide/PREFIRE_Data_User_Guide_3-SFC-SORTED-ALLSKY_R01-20250430.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | PREFIRE_SAT1-2B-SFC vR00 | PREFIRE_SAT1_2B-SFC vR01 | typo_corrected / unique_in_cmr | MEDIUM | identifier: typo_corrected |

## PREFIRE_SAT2_3-SFC-SORTED-ALLSKY vR01 (`C3544479139-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/prefire/guide/PREFIRE_Data_User_Guide_3-SFC-SORTED-ALLSKY_R01-20250430.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | PREFIRE_SAT2-2B-SFC vR00 | PREFIRE_SAT2_2B-SFC vR01 | typo_corrected / unique_in_cmr | MEDIUM | identifier: typo_corrected |

## RICMIAAE v002 (`C3417609406-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## RICMIB2E v002 (`C3417609407-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## RICMIRCM v004 (`C3417609410-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRCCT v4 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANRCCH v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## RICMITAL v002 (`C3417609472-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## RICMITCL v003 (`C3417609654-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## RICMITST v002 (`C3417609763-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## SAGE2_AEROSOL_O3_NO2_H2O_BINARY vV7.0 (`C3880792530-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/sage2/sage2_release_v7_notes.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | SAGE2_V6.20_AEROSOL_O3_NO2_H2O_BINARY v1 | *self_reference* | typo_corrected / self_reference | LOW | not resolved (self_reference) |

## SAMMI2AE v002 (`C3422083912-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## SAMMI2LS v002 (`C3422083921-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## SAMMI2ST v002 (`C3422083926-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## SAMMIB2E v003 (`C3422083933-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MI1B2EP v1 | MI1B2E v003 | typo_corrected / matches_target | MEDIUM | identifier: typo_corrected |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## SAMMIB2T v003 (`C3422083935-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MI1B2TP v1 | MI1B2T v003 | typo_corrected / matches_target | MEDIUM | identifier: typo_corrected |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## SAMMIGEO v002 (`C3422083942-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MISANCGM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## SCAR_A_ER2_MAS v1 (`C3880795271-LARC_CLOUD`)

* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/scara/guide/base_scar_a_er2_mas_dataset.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/scara/guide/scar_project.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| PARENT | MAS v0 | *documented_not_in_cmr* | — / — | LOW | not resolved (documented_not_in_cmr) |

> **MAS** — base_scar_a_er2_mas_dataset.pdf, p. 2: "The MAS spectrometer was mated to a scanner subassembly which collected image data with an IFOV of 2.5 mrad, giving a ground resolution of 50 meters from 20000 meters altitude, and a cross track scan width of 85.92 degrees."

## SENTINEL-1D_META_RAW v1 (`C4175250286-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| DEPENDENT | Sentinel-1D_RAW v— | SENTINEL-1D_RAW v1 | case_normalized / unique_in_cmr | HIGH | identifier case_normalized; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1D_META_SLC v1 (`C4175278190-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1/Sentinel-1-User-Guide.pdf
* Document (priority 4, not valid): https://webdocs.asf.alaska.edu/Sentinel-1/ASF_SAR_Sentinel-1_product_specification_v1.1.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| DEPENDENT | Sentinel-1D_SLC v— | SENTINEL-1D_SLC v1 | case_normalized / unique_in_cmr | HIGH | identifier case_normalized; version unique_in_cmr; CMR not_applicable |

## SENTINEL-1_BURSTS v1 (`C2709161906-ASF`)

* Document (priority 4, valid): https://webdocs.asf.alaska.edu/Sentinel-1-Bursts/Sentinel-1-Bursts-User-Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | SENIINEL-1C_SLC v— | SENTINEL-1C_SLC v1 | typo_corrected / unique_in_cmr | MEDIUM | identifier: typo_corrected |
| INPUT | SENIINEL-1D_SLC v— | SENTINEL-1D_SLC v1 | typo_corrected / unique_in_cmr | MEDIUM | identifier: typo_corrected |

## UAEM1LME v002 (`C3417609862-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/UAE/UAE_LM_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MISANCGM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIAA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIAF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIAN v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIBA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIBF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOICA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOICF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIDA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIDF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPAA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPAF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPAN v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPBA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPBF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPCA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPCF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPDA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPDF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRCCT v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEM1LMT v002 (`C3417609933-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/UAE/UAE_LM_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MISANCGM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIAA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIAF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIAN v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIBA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIBF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOICA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOICF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIDA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRFOIDF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPAA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPAF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPAN v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPBA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPBF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPCA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPCF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPDA v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANPPDF v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRCCT v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMIAAE v002 (`C3417609986-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMIALS v002 (`C3417610039-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/UAE/UAE_LM_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMIB2E v003 (`C3417610135-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/UAE/UAE_LM_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | UAEMIB2EP v1 | UAEMIB2E v002 | typo_corrected / unique_in_cmr | MEDIUM | identifier: typo_corrected |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMIB2E v002 (`C3417610093-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/UAE/UAE_LM_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMIB2T v003 (`C3417610157-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/UAE/UAE_LM_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | UAEMIB2TP v1 | UAEMIB2T v002 | typo_corrected / unique_in_cmr | MEDIUM | identifier: typo_corrected |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMIB2T v002 (`C3417610141-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMIRCM v004 (`C3417610198-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRCCT v4 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANRCCH v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMIRCM v003 (`C3417610171-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/UAE/UAE_LM_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIRCCT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANRCCH v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMITAL v002 (`C3417610285-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/UAE/UAE_LM_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMITCL v003 (`C3417610439-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMITST v002 (`C3417610479-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMRDAE v004 (`C3417610543-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIL3SAE v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMRDLS v004 (`C3417610564-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/gallery/field_campaigns/UAE/UAE_LM_sites.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIL3SLS v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMRDRD v004 (`C3417610567-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIL3SRD v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMRMLS v004 (`C3417610569-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## UAEMRMRD v005 (`C3417610572-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## VBEMI2AE v002 (`C3417610573-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## VBEMI2LS v002 (`C3417610617-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANTOAC v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANSMT v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## VBEMI2ST v002 (`C3417610727-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MIANAZM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANCSSC v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MIANLDBM v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## VBEMIB2E v003 (`C3417610802-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MI1B2EP v1 | MI1B2E v003 | typo_corrected / matches_target | MEDIUM | identifier: typo_corrected |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## VBEMIB2T v003 (`C3417610851-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MI1B2TP v1 | MI1B2T v003 | typo_corrected / matches_target | MEDIUM | identifier: typo_corrected |
| INPUT | MIB2CORR v1 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## VBEMIGEO v002 (`C3417610912-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/misr/MISR_ATBDs.pdf
* Document (priority 4, not valid): https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2023.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| INPUT | MISANCGM v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| INPUT | MICNFG v2 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

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

## VJ146A2_NRT v2 (`C4193331158-LANCEMODIS`)

* Document (priority 4, valid): https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/Black-Marble_v2.0_UG_2024.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | VJ146A2_2 v2 | VJ146A2 v2 | embedded_verified / original_verified | HIGH | identifier embedded_verified; version original_verified; CMR not_applicable; document evidence |

> **VJ146A2_2** — Black-Marble_v2.0_UG_2024.pdf, p. 21: "15 QF_VIIRS_M16 512 = Missing_EV 1024 = Cal_Fail 2048 = Dead_Detector 5.2 The VNP46A2/VJ146A2 Daily Moonlight-adjusted Nighttime Lights (NTL) Product The daily moonlight and atmosphere-corrected NTL is available at 15 arc-second resolution from January 2012-present."

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

## g3acld v004 (`C3449081101-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/sage3/ATBDs/Cloud_Data_Products.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/sage3/guide/Data_Product_User_Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | g3arepc v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| SCIENCE ASSOCIATED | g3arepqc v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## g3acldb v004 (`C3449082507-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/sage3/ATBDs/Cloud_Data_Products.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/sage3/guide/Data_Product_User_Guide.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | g3arepc v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| SCIENCE ASSOCIATED | g3arepqc v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## g3alsp v003 (`C3215260899-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/sage3/ATBDs/Solar_and_Lunar_Algorithm.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/sage3/quality_summaries/sage3_quality_summary_v3.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | g3arep v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| SCIENCE ASSOCIATED | g3arepqa v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## g3alspb v003 (`C3215260968-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/sage3/ATBDs/Solar_and_Lunar_Algorithm.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/sage3/quality_summaries/sage3_quality_summary_v3.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | g3arep v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| SCIENCE ASSOCIATED | g3arepqa v3 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## g3assp v004 (`C3215264962-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/sage3/ATBDs/Solar_and_Lunar_Algorithm.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/sage3/quality_summaries/sage3_quality_summary_v3.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | g3arep v4 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| SCIENCE ASSOCIATED | g3arepqa v4 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |

## g3asspb v004 (`C3215261129-LARC_CLOUD`)

* Document (priority 1, valid): https://asdc.larc.nasa.gov/documents/sage3/ATBDs/Solar_and_Lunar_Algorithm.pdf
* Document (priority 4, valid): https://asdc.larc.nasa.gov/documents/sage3/quality_summaries/sage3_quality_summary_v3.pdf

| Type | Original | Repaired | Basis | Confidence | Note |
|---|---|---|---|---|---|
| SCIENCE ASSOCIATED | g3arep v4 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
| SCIENCE ASSOCIATED | g3arepqa v4 | *not_in_cmr* | — / — | LOW | not resolved (not_in_cmr) |
