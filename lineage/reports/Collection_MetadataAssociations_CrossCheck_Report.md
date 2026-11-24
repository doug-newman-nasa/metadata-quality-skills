# Collection Lineage vs. CMR `metadataAssociations` Cross-Check Report

**Analysis Date:** 2026-11-24  
**Data Source:** CMR GraphQL API (`https://graphql.earthdata.nasa.gov/api`), queried live. Retrieved at 2026-11-24 22:35 UTC  
**Notebook:** [`lineage/notebooks/Collection_MetadataAssociations_CrossCheck.ipynb`](../notebooks/Collection_MetadataAssociations_CrossCheck.ipynb)  
**Scope:** `lineage/metrics/{ASF,GES_DISC,GHRC_DAAC,LANCEMODIS,LARC_CLOUD,LPCLOUD,LPDAAC_ECS}/*_lineage.csv`  

---

## 1. Executive Summary

The ATBD-derived lineage CSVs were checked against the `metadataAssociations` that CMR holds for each source
collection. That covers 51 files, 3,039 associations and 734 source collections. The results went
into a new `match` column in every CSV.

| Result | Rows | Share |
|---|---:|---:|
| `true` (same related collection, same type) | 199 | 6.5% |
| Same related collection, **different type** (CMR type recorded) | 178 | 5.9% |
| `false` (related collection not in the CMR record) | 2,662 | 87.6% |
| **Total** | **3,039** |  |

**Key findings**
1. **The CSVs and CMR mostly describe different links.** Only 12.4% of CSV associations appear in CMR at all.
   Almost every `false` row (2,634 of 2,662) names a related
   collection that **does exist in CMR**, but the source record doesn't link to it. CMR's association metadata is
   sparse, and the CSV names are generally valid.
2. **Type disagreements are a convention mismatch.** The CSVs use `PARENT`/`CHILD` for processing lineage, while
   CMR providers use `INPUT`/`DEPENDENT` (118 of 178 type differences). In CMR, `PARENT`/`CHILD` mostly
   link versions of the same collection.
3. **CMR has 1,307 associations the CSVs don't list.**
   - 468 are self-references, mostly version-succession links and GES_DISC self-loop placeholders.
   - 839 link to other collections, 811 of them in LARC_CLOUD (mostly MISR `INPUT` lists).
     These are candidates to add to the lineage CSVs.
4. **CMR association metadata has quality problems.**
   - 445 association entries point to 103 short names that
     public CMR doesn't have.
   - There are likely typos, such as `ASF_ECMWF_TROPO`, `SENIINEL-1C_SLC`, `PREFIRE_SAT1-2B-SFC`.
   - Some entries put the version inside the entry ID, have stray whitespace, are free text, or have no type.

---

## 2. Inputs

| Provider | CSV files | Rows | Source collections |
|---|---:|---:|---:|
| ASF | 6 | 267 | 41 |
| GES_DISC | 9 | 812 | 157 |
| GHRC_DAAC | 1 | 2 | 1 |
| LANCEMODIS | 4 | 104 | 20 |
| LARC_CLOUD | 29 | 1,836 | 510 |
| LPCLOUD | 1 | 14 | 3 |
| LPDAAC_ECS | 1 | 4 | 2 |
| **All** | **51** | **3,039** | **734** |

- Each directory name is a CMR provider ID. All 787 CMR records
  retrieved belong to the EOSDIS consortium.
- Any existing `match`/`Match` column was **dropped on read and never used**. The new column was computed only from CMR.
- `LARC_CLOUD/SCAR_A_lineage.csv` has only a header row. It got the `match` column but has no data.

---

## 3. Method

### 3.1 Query strategy

Three options were evaluated for getting `metadataAssociations` for 734 collections:

| Strategy | Requests | Records downloaded | Measured / estimated time |
|---|---:|---:|---|
| A. One request per collection | 734 | 734 | Mean 0.45 s per request (max 0.73 s) in this run, so about 5.5 min sequentially |
| B. Whole provider (paged) | 7+ | 5,610 | Downloads 7.6× more records than needed (e.g. GHRC_DAAC: 703 records for 1 collection) |
| **C. Batched: provider + `shortNames` list (chosen)** | **12** | **787** | **11.2 s in this run** |

Why option C:
- **Fewest requests and least wasted data.** `CollectionsInput.shortNames` accepts a list, so one request covers up to
  100 short names.
- **Querying by short name, not entry ID, returns every version.** That makes it possible to recover from a wrong
  version in a CSV (section 3.2).
- **Robust.** It retries with exponential backoff, and it pages with `cursor` until `count` items are received.
- **Lighter on CMR.** It sends 12 requests to a shared public service instead of 734.

The same batched pattern was reused for the extra analysis lookups: 827 related short names in
9 requests, all self-referenced versions, and 149 association targets.

### 3.2 Resolving source collections

| Resolution | Collections |
|---|---:|
| Exact match (provider + short name + version) | 730 |
| Single-version fallback: CSV version not in CMR, but only one version exists, so it was used | 2 (`VNP46A1G_NRT`: CSV v2, CMR v1; `VNP46A1_NRT`: CSV v2, CMR v1) |
| Not in CMR (all rows `false`) | 2 (`VNP14IMGTDL_NRT`, `VNP46A2_NRT`) |

### 3.3 Matching rules

1. Find the source record's `metadataAssociations` entries whose `entryId` equals the CSV `related_shortname`. The
   comparison ignores case and surrounding whitespace.
2. If several entries share that `entryId`, keep the one whose `version` equals the CSV `related_version`. CMR often
   links several versions of one short name with different types.
3. If the type is the same, the value is `true`. If the type differs, the value is the CMR type (several types are
   joined with `|`). If there's no entry, the value is `false`.

---

## 4. Results

### 4.1 By provider

| Provider | Rows | `true` | Type differs | `false` | % `true` | % found in CMR |
|---|---:|---:|---:|---:|---:|---:|
| ASF | 267 | 78 | 48 | 141 | 29.2% | 47.2% |
| GES_DISC | 812 | 0 | 10 | 802 | 0.0% | 1.2% |
| GHRC_DAAC | 2 | 0 | 0 | 2 | 0.0% | 0.0% |
| LANCEMODIS | 104 | 0 | 0 | 104 | 0.0% | 0.0% |
| LARC_CLOUD | 1,836 | 121 | 117 | 1,598 | 6.6% | 13.0% |
| LPCLOUD | 14 | 0 | 3 | 11 | 0.0% | 21.4% |
| LPDAAC_ECS | 4 | 0 | 0 | 4 | 0.0% | 0.0% |
| **All** | **3,039** | **199** | **178** | **2,662** | **6.5%** | **12.4%** |

### 4.2 Collection suites with the most agreement

| File | Rows | `true` | Type differs | `false` |
|---|---:|---:|---:|---:|
| LARC_CLOUD/MISR | 383 | 88 | 37 | 258 |
| ASF/SENTINEL-1D | 98 | 42 | 14 | 42 |
| ASF/SENTINEL-1C | 100 | 28 | 13 | 59 |
| LARC_CLOUD/PREFIRE | 166 | 21 | 44 | 101 |
| LARC_CLOUD/TEMPO | 169 | 7 | 0 | 162 |
| ASF/OPERA | 40 | 6 | 17 | 17 |

Several large suites have **no** exact CMR agreement, including
GES_DISC/SNDR (476 rows, of which 7 differ by type), LARC_CLOUD/CERES (268 rows), LARC_CLOUD/CALIPSO (219 rows, of which 22 differ by type).
The per-file table for all 51 files is in notebook section 7b.

### 4.3 By CSV association type

| CSV type | Rows | `true` | Type differs | `false` |
|---|---:|---:|---:|---:|
| RELATED | 1,336 | 82 | 42 | 1,212 |
| PARENT | 615 | 2 | 90 | 523 |
| CHILD | 584 | 0 | 46 | 538 |
| INPUT | 504 | 115 | 0 | 389 |

`INPUT` is the CSV type that agrees with CMR best (22.8% `true`). `CHILD` never matches exactly.

### 4.4 Type differences (CSV type → CMR type)

| CSV type | CMR type | Count |
|---|---|---:|
| PARENT | INPUT | 71 |
| CHILD | DEPENDENT | 33 |
| RELATED | PARENT | 19 |
| PARENT | DEPENDENT | 14 |
| CHILD | SCIENCE ASSOCIATED | 13 |
| RELATED | SCIENCE ASSOCIATED | 12 |
| RELATED | CHILD | 11 |
| PARENT | SCIENCE ASSOCIATED | 4 |
| PARENT | RELATED | 1 |

PARENT→INPUT and CHILD→DEPENDENT together account for 104 of the 178
differences. Adopting CMR's convention in the lineage skill (upstream = `INPUT`, downstream = `DEPENDENT`) would turn
most of these rows into `true`.

### 4.5 Why rows are `false`

| Reason | Rows |
|---|---:|
| Related collection exists in CMR, but the source record doesn't link to it | 2,634 |
| Related collection doesn't exist in CMR | 22 |
| Source collection not in CMR | 6 |

The 22 rows with a non-existent related collection use 8 short
names. These are probably guessed product names in the CSVs:

| Provider | CSV `related_shortname` | Rows |
|---|---|---:|
| LANCEMODIS | VNP02DNB_NRT | 4 |
| LANCEMODIS | VNP02MOD_NRT | 4 |
| LANCEMODIS | VNP03DNB_NRT | 2 |
| LANCEMODIS | VNP03MOD_NRT | 2 |
| LANCEMODIS | VNP14IMGTDL_NRT | 2 |
| LANCEMODIS | VNP14IMG_NRT | 2 |
| LANCEMODIS | VNP46A2_NRT | 2 |
| LARC_CLOUD | CER_ES9_Terra+Aqua | 4 |

### 4.6 Provider notes

- **GES_DISC (0.0% `true`):** CMR associations are mostly `SCIENCE ASSOCIATED` entries that point to the
  record itself or to its `_NRT` twin. There are 146 self-loops. They rarely name the upstream products the CSVs list.
- **LANCEMODIS (0.0% `true`):** CMR links NRT products to *standard* products, often with the version
  inside the entry ID (e.g. `VJ146A2_2`, `VNP46A1_1`, `VNP46A1_2`).
  The CSVs link NRT products to other NRT products.
- **ASF (29.2% `true`):** the best agreement, mainly from the SENTINEL-1C/1D suites.

---

## 5. CMR Associations Not in the CSVs

The `match` column only shows CSV rows. Going the other way, CMR has **1,307** associations on the source
records that no CSV row names.

| Provider | Self-references | To another collection |
|---|---:|---:|
| ASF | 0 | 9 |
| GES_DISC | 146 | 7 |
| GHRC_DAAC | 1 | 0 |
| LANCEMODIS | 6 | 10 |
| LARC_CLOUD | 315 | 811 |
| LPCLOUD | 0 | 0 |
| LPDAAC_ECS | 0 | 2 |
| **All** | **468** | **839** |

### 5.1 Self-referencing associations (468 entries, 449 collections)

The `entryId` is the record's own short name. The CSVs contain **no**
self-references, because ATBD-based lineage doesn't model version succession.

| Kind | Entries | Notes |
|---|---:|---|
| Links to another version that exists in CMR | 93 | Version-succession links, e.g. `CER_BDS_NPP-FM5` Edition2 → Edition1-CV, `CER_CRS_Terra-FM1-MODIS` Edition4A → Edition2G |
| Links to a version public CMR doesn't have | 217 | e.g. `glmmth` 1 → 3, `AirMSPI_ORACLES_Ellipsoid-projected_Georegistered_Radiance_Data` 6 → 1, `CERES_EBAF` Edition4.2.1 → Edition4.2, `CER_BDS_Aqua-FM3` Edition4 → Edition3. Probably retired versions, so the links can't be followed |
| Points to the record itself (same version) | 152 | 146 are GES_DISC placeholders. They carry no lineage information |
| No version given | 6 | LANCEMODIS. The target can't be told apart from the record itself |

Another 20 self-references write the version differently from CMR, e.g.
`EDITION2A` for version `Edition2B` (CER_SSF_NPP-FM5-VIIRS), `02` for version `2` (SNDRJ1ATMSL1B). They resolve once versions are normalized,
but they would fail an exact-match lookup.

### 5.2 Associations to a different collection (839 entries, 228 collections)

These are lineage links already in CMR that the ATBD-derived CSVs missed. **They're the main candidates to add to the
lineage CSVs.**

- By type: `INPUT` 730, `PARENT` 52, `SCIENCE ASSOCIATED` 27, `RELATED` 14, `DEPENDENT` 11, `CHILD` 5.
- 811 are in LARC_CLOUD. The most-linked targets are `MICNFG` (132), `MIANCAGP` (54), `MIANCARP` (47), `MIANLDBM` (33), `MI1B2T` (32), `MI1B2E` (31).
- 454 of the 839 have an `entryId` that doesn't resolve to a CMR collection: the
  target isn't in CMR, or the ID has a version inside it or is free text (section 6). Adding those to the CSVs as-is
  would produce links that can't be resolved.

---

## 6. CMR Association Data Quality

All 1,685 association entries on the 730 resolved records were checked:

| Check | Entries | Examples |
|---|---:|---|
| `entryId` not in CMR | 445 (103 distinct targets) | `MICNFG` (132), `MIANLDBM` (33), `MIANCSSC` (24), likely typos `ASF_ECMWF_TROPO`, `PREFIRE_SAT1-2B-SFC`, `PREFIRE_SAT2-2B-SFC`, `SAGE2_V6.20_AEROSOL_O3_NO2_H2O_BINARY`, `SENIINEL-1C_SLC`, `SENIINEL-1D_SLC` |
| Version inside `entryId` | 8 | `VNP46A1_2`, `VNP46A1_1` (×3), `VJ146A2_2`, `CER_CCCM_Aqua-FM3-MODIS-CAL-CS_RelD1`, `CER_SSF_Aqua-FM3-MODIS_Edition4A` |
| Leading/trailing whitespace in `entryId` | 5 | `"OPERA_L2_CSLC-S1-STATIC_V1 "`, `"MOD09A1N "`, `"CMRMIAAE "` (×2), `" TEMPO_CLDO4_L3_NRT"` |
| Missing `type` | 4 | `Global_Landslide_Exposure_Maps`, `Global_Landslide_Nowcast` (×2), `glmmth` |
| Free-text `entryId` | 1 | `"OPeNDAP data access for CAL_IIR_L2_Track-Standard-V4-20"` in `CAL_IIR_L2_Track-Standard-V4-51` |
| `type` not in the UMM-C enum | 0 |  |
| Duplicate entries | 0 |  |

Specific errors worth reporting to the DAACs:
- **ASF `OPERA_L4_TROPO-ZENITH_V1`:** `ASF_ECMWF_TROPO` is not in CMR, probably `ASF_ECMWF_TROP`. The CSV has the correct name.
- **ASF `SENTINEL-1_BURSTS`:** `SENIINEL-1C_SLC` is not in CMR, probably `SENTINEL-1C_SLC`; `SENIINEL-1D_SLC` is not in CMR, probably `SENTINEL-1D_SLC`. The CSV has the correct name.
- **LARC_CLOUD `PREFIRE_SAT1_3-SFC-SORTED-ALLSKY`:** `PREFIRE_SAT1-2B-SFC` is not in CMR, probably `PREFIRE_SAT1_2B-SFC`. The CSV has the correct name.
- **LARC_CLOUD `PREFIRE_SAT2_3-SFC-SORTED-ALLSKY`:** `PREFIRE_SAT2-2B-SFC` is not in CMR, probably `PREFIRE_SAT2_2B-SFC`. The CSV has the correct name.
- **LARC_CLOUD `SAGE2_AEROSOL_O3_NO2_H2O_BINARY`:** `SAGE2_V6.20_AEROSOL_O3_NO2_H2O_BINARY` is not in CMR, probably `SAGE2_AEROSOL_O3_NO2_H2O_BINARY`.
- **LARC_CLOUD `CAL_IIR_L2_Track-Standard-V4-51`:** the `PARENT` entry ID is a description, not a short name.
- **LANCEMODIS:** entry IDs with the version inside them (`VJ146A2_2`, `VNP46A1_1`, `VNP46A1_2`) should be split into short name + `Version`.
- **LARC_CLOUD:** entry IDs with the version inside them (`CER_CCCM_Aqua-FM3-MODIS-CAL-CS_RelD1`, `CER_SSF_Aqua-FM3-MODIS_Edition4A`, `DSCOVR_EPIC_L2_COMPOSITE_01`) should be split into short name + `Version`.

"Not in CMR" means that CMR GraphQL returned no collection with that short name under any provider. During development
a sample (e.g. `MICNFG`, `AIRMISR`, `ASF_ECMWF_TROPO`) was confirmed against the CMR Search API
(`collections.json?short_name=`), which returns nothing for them either.

---

## 7. Recommendations

**For the lineage CSV generation skill (`Collection_Lineage_via_ATBD_Skill`)**
1. Use CMR's type convention: upstream processing inputs = `INPUT`, downstream products = `DEPENDENT`. Keep
   `PARENT`/`CHILD` for version succession. This alone would resolve most of the 178 type differences.
2. Check every `related_shortname` against CMR before writing it. That would drop or fix the 8
   non-existent names.
3. Merge in the 385 CMR links to other collections whose target exists in CMR
   (section 5.2). Leave out, or first correct, the 454 whose `entryId` doesn't resolve.

**For the DAACs / CMR metadata**
1. Fix the likely typos and the free-text entry IDs listed in section 6.
2. Trim whitespace from entry IDs, and split versions out of entry IDs into the `Version` field.
3. Add `Type` to the 4 untyped associations.
4. Review the 217 version links to versions that no longer exist, and the
   146 GES_DISC self-loop placeholders.
5. Review the 103 association targets that public CMR doesn't have (most-linked:
   `MICNFG`, `MIANLDBM`, `MIANCSSC`).

---

## 8. Reproducing the Results

Run every cell of `lineage/notebooks/Collection_MetadataAssociations_CrossCheck.ipynb`. It uses the `uv_metadata` environment
(Python 3.14, `requests`) and needs no authentication. Step 9 of the notebook regenerates this report.
- `DRY_RUN = True` computes everything without rewriting the CSVs.
- `RUN_BENCHMARK = False` skips the query-strategy timing.
- `WRITE_REPORT = False` skips writing this report.

Results reflect CMR at the retrieval time shown at the top of this report.
