# Skill: Collection Lineage CSV Export

## Overview
This skill extends **Collection_Lineage_via_ATBD_Skill** by writing a collection's lineage to a CSV file. Each row describes one relationship between two collection versions and the confidence in that relationship. The CSV is a flat, tabular view of lineage for spreadsheets, databases and graph tools. It can hold several levels of lineage (parents of parents) in one file.

**Skill Type:** Data Provenance Documentation & Tabular Export
**Difficulty Level:** Advanced
**Parent Skills:**
- Collection_Lineage_via_ATBD_Skill (lineage discovery, Steps 1–7)
- Collection_Lineage_Generation_Skill (relationship definitions, Step 1a–1c)
**Use Cases:**
- Lineage inventories across many collections
- Loading lineage into a database or graph tool
- Reviewing lineage before it becomes UMM-C MetadataAssociations
- Finding low-confidence relationships that need a curator's review

## Key Innovation
**Output Format:** One CSV row per relationship, with an explicit, rule-based **confidence level** for each.

---

## Input Parameters

| Parameter | Type | Required | Example | Description |
|-----------|------|----------|---------|-------------|
| `collection_short_name` | string | Yes | `MOD02QKM` | CMR ShortName of the target collection |
| `collection_version` | string | Yes | `7` | CMR Version of the target collection |
| `atbd_search_depth` | integer | No | `1` | Lineage levels to include (1 = the target's own relationships; 2 = also its parents' relationships, and so on). Default `1` |
| `include_low_confidence` | boolean | No | `true` | Write LOW rows (default `true`; set `false` for a curated-only file) |
| `write_evidence_sidecar` | boolean | No | `true` | Also write a JSON file with the evidence behind each row (default `true`) |

---

## CSV Specification

### Columns

| Column | Required | Description | Example |
|---|---|---|---|
| `shortname` | Yes | ShortName of the subject collection (the target at depth 1; a parent at depth 2+) | `MOD02QKM` |
| `version` | Yes | Version of the subject collection, exactly as in CMR | `7` |
| `association_type` | Yes | UMM-C MetadataAssociation Type: how the related collection relates to the subject (see below) | `PARENT` |
| `related_shortname` | Yes | ShortName of the related collection, exactly as in CMR | `MOD01` |
| `related_version` | Yes | Version of the related collection; `Unknown` when it cannot be determined (see Step 2) | `7` |
| `confidence` | Yes | `HIGH`, `MEDIUM` or `LOW` (see Step 3) | `HIGH` |
| `lineage_relationship` | Yes* | The detailed lineage relationship the `association_type` was assigned from (Collection_Lineage_Generation_Skill Step 1a). *Blank only for types set by hand (SCIENCE ASSOCIATED, DEPENDENT, LARGER CITATION WORKS) | `derived_from` |

### Format rules
- UTF-8, comma-delimited, RFC 4180 quoting (quote a field only when it contains a comma, quote or newline)
- The first row is the header, exactly: `shortname,version,association_type,related_shortname,related_version,confidence,lineage_relationship`
- `lineage_relationship` is the last column, so the first six columns keep their positions
- `version` and `related_version` are never blank. When a version cannot be determined, write `Unknown`
- One row per (`shortname`, `version`, `related_shortname`) pair; no duplicates
- No self-relations (`related_shortname` ≠ `shortname`)
- Rows are sorted by depth (target first), then `association_type` in the order of the table below, then `related_shortname`
- File name: `{shortname}_V{version}_lineage.csv`, for example `MOD02QKM_V7_lineage.csv`

### `association_type` values
Values are the UMM-C v1.18.6 `MetadataAssociateTypeEnum`, so each row corresponds to a MetadataAssociation in the subject's record. Each row reads: **"in `shortname`'s record, `related_shortname` is its `association_type`"**. The type describes the related collection X relative to the subject T.

Assign the type in two stages, using **Collection_Lineage_Generation_Skill Step 1**:
1. Classify the relationship as a lineage relationship (Step 1a definitions, Step 1b decision procedure, Step 1c rules).
2. Map it to the UMM-C Type (Step 1d).

Write the lineage relationship to the `lineage_relationship` column. It must be one that maps to the row's `association_type` in the table below. The confidence rules (Step 3) also depend on it.

| `association_type` | Assigned from lineage relationship | Meaning (X relative to T) |
|---|---|---|
| `PARENT` | `derived_from`, `aggregated_from` | T is produced directly from, or aggregates, X's data |
| `INPUT` | `input_to`, `component_of` | T's algorithm consumes X without reprocessing X's data, or assembles X as one component |
| `CHILD` | `downstream_product` | X is produced from T |
| `RELATED` | `parallel_product`, `equivalent_product`, `version_of`, `template_of`, `related_to` | Sibling from the same run, same product from another platform, or another documented relationship |
| `SCIENCE ASSOCIATED`, `DEPENDENT`, `LARGER CITATION WORKS` | — (never assigned automatically) | Valid UMM-C values; set by hand only when a data provider requires them |

Collapsing to UMM-C types merges some distinctions. A sibling product (`parallel_product`) and a platform counterpart (`equivalent_product`) are both `RELATED`. The `lineage_relationship` column keeps them apart.

The parent skill's keyword categories map onto the lineage relationships first: `composite_of` → `aggregated_from` (PARENT), and `input_data` → `derived_from` (PARENT) or `input_to` (INPUT), by the PARENT vs INPUT test in Collection_Lineage_Generation_Skill Step 1b.

---|---|---|
| `derived_from` | T is produced directly from X's data | PARENT |
| `aggregated_from` | T aggregates or composites X | PARENT |
| `input_to` | T's algorithm consumes X without reprocessing X's data | INPUT |
| `component_of` | T is assembled from X as one of several components | INPUT |
| `downstream_product` | X is produced from T | CHILD |
| `parallel_product` | X is produced by the same run as T | RELATED |
| `equivalent_product` | X is the same product from another platform/instrument | RELATED |
| `version_of` | X is a related product version (never another version of T itself) | RELATED |
| `template_of` | X shares T's format or template, with no data dependency | RELATED |
| `related_to` | Another documented relationship | RELATED |

The parent skill's keyword categories map onto this vocabulary: `composite_of` → `aggregated_from`, and `input_data` → `input_to` or `derived_from` (by the PARENT vs INPUT test in Collection_Lineage_Generation_Skill Step 1b).

---

## Processing Steps

### Step 1: Discover lineage (parent skill)
Run **Collection_Lineage_via_ATBD_Skill** Steps 1–7 for the target collection:
- retrieve the metadata and its ATBD/User Guide URLs
- fetch the documents and extract lineage statements and structured inputs
- validate against CMR and identify derived collections

For each related collection, keep the evidence the confidence rules need:

```python
relationship = {
    'shortname': 'MOD02QKM', 'version': '7', 'depth': 1,
    'related_shortname': 'MOD03',
    'lineage_relationship': 'input_to',       # Collection_Lineage_Generation_Skill Step 1a-1b
    'association_type': 'INPUT',              # Collection_Lineage_Generation_Skill Step 1d
    'evidence_source': 'user_guide',          # atbd | user_guide | other_doc | naming_convention | cmr_pattern
    'evidence_quote': 'Level 1B copies subsets of the geolocation data from the geolocation file ...',
    'evidence_section': '3.3.2',
    'quote_verified': True,                   # the quote was found in the document text
    'named_explicitly': False,                # the documents name the ShortName (False = mapped from a generic reference)
    'keyword_priority': 2,                    # parent skill Step 3 priority (1-3), or None
    'cmr_validation': {...},                  # parent skill Step 6 results for this collection
}
```

When `atbd_search_depth` > 1, repeat Step 1 for each `PARENT` and `INPUT` collection found at the previous depth, using it as the subject. Keep track of visited (`shortname`, `version`) pairs so each collection is processed once and cycles end.

### Step 2: Resolve versions
- **`version`:** the subject's version exactly as in CMR. At depth 1 this is the input `collection_version`. At depth 2+ it is the `related_version` resolved for that collection at the previous depth, including `Unknown`. A collection keeps the same version in every row.
- **`related_version`:** use the same rules as Collection_Lineage_Generation_Skill:
  1. the subject's version, if the related collection has it in CMR
  2. otherwise the latest non-NRT version in CMR (this lowers confidence; see Step 3)
  3. otherwise `Unknown`, when the version cannot be determined (for example, CMR has only NRT versions)
- If the related collection has **no CMR record at all**, do not write the row (Collection_Lineage_Generation_Skill rule 4). List it in the evidence sidecar instead.

```python
def resolve_related_version(related_shortname, subject_version):
    versions = cmr_versions(related_shortname)            # all versions in CMR
    if not versions:
        return None, 'not_in_cmr'                         # row is not written
    if subject_version in versions:
        return subject_version, 'matched'
    standard = [v for v in versions if 'NRT' not in v.upper()]
    if standard:
        return max(standard, key=version_key), 'substituted'
    return 'Unknown', 'nrt_only'                          # version cannot be determined
```

### Step 3: Assign the confidence level
Assess each relationship on three criteria:

| Criterion | Strong | Weak |
|---|---|---|
| **Source** | ATBD or official product User Guide | Other documentation; naming conventions or CMR pattern search only |
| **Statement** | Names the related ShortName in an explicit lineage statement (parent skill keyword priority 1–2, or a product summary table), with a verified quote | Generic reference mapped to a ShortName ("the geolocation file" → MOD03), a priority-3 keyword, or an unverified quote |
| **CMR validation** (parent skill Step 6) | Found in CMR, processing levels progress correctly, `related_version` matched | `related_version` substituted or NRT-only, or a version-compatibility warning |

Then apply the first matching rule:

| Confidence | Rule |
|---|---|
| **LOW** | Any of: no document evidence (naming convention or CMR pattern only, parent skill Step 7); the quote could not be verified; the processing-level progression is invalid |
| **HIGH** | Source, statement and CMR validation are all **strong** |
| **MEDIUM** | Everything else: document-supported, with exactly one weak criterion, or several weak criteria that don't trigger LOW |

There are two exceptions:
- **Platform counterparts (`RELATED`, lineage relationship `equivalent_product`):** a counterpart (MOD↔MYD, VNP↔VJ1) identified only by naming convention is **MEDIUM**, not LOW, when the counterpart exists in CMR at the matching version. Algorithms and file formats are shared across such pairs by design. It is HIGH when a document also names it.
- **`CHILD`:** a downstream product found by CMR pattern search alone is **LOW**. It is HIGH or MEDIUM only when its own documentation, or the target's, names the relationship.

```python
def assess_confidence(rel):
    """Return HIGH, MEDIUM or LOW for one relationship (rules evaluated in order)"""
    cmr = rel['cmr_validation']
    documented = rel['evidence_source'] in ('atbd', 'user_guide', 'other_doc')

    # LOW
    if rel['lineage_relationship'] == 'equivalent_product' and not documented:
        return 'MEDIUM' if rel['version_status'] == 'matched' else 'LOW'
    if not documented or not rel['quote_verified'] or not cmr['level_progression_valid']:
        return 'LOW'

    # HIGH
    strong_source = rel['evidence_source'] in ('atbd', 'user_guide')
    strong_statement = rel['named_explicitly'] and (rel['keyword_priority'] or 3) <= 2
    strong_cmr = rel['version_status'] == 'matched' and cmr['version_compatible']
    if strong_source and strong_statement and strong_cmr:
        return 'HIGH'

    # MEDIUM
    return 'MEDIUM'
```

Product summary tables (for example "Table 1.2.1: Summary of Level 1B Products") count as `keyword_priority` 1 for the collections they list.

This rubric replaces the fixed confidence in the parent skill's Step 3 code. That code sets HIGH or MEDIUM from the keyword type alone and ignores source quality and CMR validation.

### Step 4: Write the CSV

```python
import csv

CSV_COLUMNS = ['shortname', 'version', 'association_type',
               'related_shortname', 'related_version', 'confidence', 'lineage_relationship']
# Collection_Lineage_Generation_Skill Step 1d
LINEAGE_TO_UMM_TYPE = {
    'derived_from': 'PARENT', 'aggregated_from': 'PARENT',
    'input_to': 'INPUT', 'component_of': 'INPUT',
    'downstream_product': 'CHILD',
    'parallel_product': 'RELATED', 'equivalent_product': 'RELATED', 'version_of': 'RELATED',
    'template_of': 'RELATED', 'related_to': 'RELATED',
}
MANUAL_ONLY_TYPES = {'SCIENCE ASSOCIATED', 'DEPENDENT', 'LARGER CITATION WORKS'}
# UMM-C v1.18.6 MetadataAssociateTypeEnum, in CSV sort order
ASSOCIATION_TYPE_ORDER = ['PARENT', 'INPUT', 'CHILD', 'RELATED',
                          'SCIENCE ASSOCIATED', 'DEPENDENT', 'LARGER CITATION WORKS']


def write_lineage_csv(relationships, path, include_low_confidence=True):
    rows, seen = [], set()
    for rel in sorted(relationships, key=lambda r: (r['depth'], ASSOCIATION_TYPE_ORDER.index(r['association_type']),
                                                    r['related_shortname'])):
        key = (rel['shortname'], rel['version'], rel['related_shortname'])
        if rel['version_status'] == 'not_in_cmr' or key in seen:
            continue
        if rel['confidence'] == 'LOW' and not include_low_confidence:
            continue
        seen.add(key)
        rows.append({col: rel.get(col) or '' for col in CSV_COLUMNS})

    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)
    return rows
```

### Step 5: Write the evidence sidecar (optional)
When `write_evidence_sidecar` is true, write `{shortname}_V{version}_lineage_evidence.json`. It records:
- the source documents (title, URL)
- for each row: the evidence quote and section, `evidence_source`, `named_explicitly`, `version_status`, the CMR validation results, and the rule that set its confidence
- the related collections that were left out, with the reason (for example `not_in_cmr`)

The CSV holds the seven columns. Any row's confidence can be traced through the sidecar.

### Step 6: Validate the CSV

```python
VALID_CONFIDENCE = {'HIGH', 'MEDIUM', 'LOW'}


def validate_lineage_csv(path):
    errors = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != CSV_COLUMNS:
            errors.append(f'Header must be {",".join(CSV_COLUMNS)}; found {reader.fieldnames}')
        seen = set()
        for n, row in enumerate(reader, start=2):
            for col in ('shortname', 'version', 'association_type', 'related_shortname',
                        'related_version', 'confidence'):
                if not row.get(col):
                    errors.append(f'Line {n}: {col} is required')
            if row['association_type'] not in ASSOCIATION_TYPE_ORDER:
                errors.append(f"Line {n}: association_type '{row['association_type']}' is not a UMM-C MetadataAssociation Type")
            if row['confidence'] not in VALID_CONFIDENCE:
                errors.append(f"Line {n}: confidence must be HIGH, MEDIUM or LOW")
            lineage = row.get('lineage_relationship') or ''
            if not lineage and row['association_type'] not in MANUAL_ONLY_TYPES:
                errors.append(f'Line {n}: lineage_relationship is required for {row["association_type"]}')
            elif lineage and LINEAGE_TO_UMM_TYPE.get(lineage) != row['association_type']:
                errors.append(f"Line {n}: lineage_relationship '{lineage}' does not map to "
                              f"association_type '{row['association_type']}'")
            if row['related_shortname'] == row['shortname']:
                errors.append(f'Line {n}: self-relation')
            key = (row['shortname'], row['version'], row['related_shortname'])
            if key in seen:
                errors.append(f'Line {n}: duplicate relationship {key}')
            seen.add(key)
    return {'valid': not errors, 'errors': errors}
```

---

## Execution Example: MOD02QKM V7

Sources: the MODIS L1B ATBD (Collection 7) and the MODIS Level 1B Product User's Guide (MOD_PR02 V7.0.20), both linked from the collection's CMR metadata (C3861609263-LAADS).

**`MOD02QKM_V7_lineage.csv`**
```csv
shortname,version,association_type,related_shortname,related_version,confidence,lineage_relationship
MOD02QKM,7,PARENT,MOD01,Unknown,MEDIUM,derived_from
MOD02QKM,7,INPUT,MOD03,7,MEDIUM,input_to
MOD02QKM,7,RELATED,MOD021KM,7,HIGH,parallel_product
MOD02QKM,7,RELATED,MOD02HKM,7,HIGH,parallel_product
MOD02QKM,7,RELATED,MYD02QKM,7,HIGH,equivalent_product
```

**How each confidence was assigned:**

| Related | Lineage relationship → type | Evidence | Weak criteria | Confidence |
|---|---|---|---|---|
| MOD01 | `derived_from` → PARENT | ATBD §5.1: "Each L1A granule contains 5 minutes of data… These are the principal inputs to the Level 1B (L1B) process." | Statement: generic "L1A" mapped to MOD01. CMR: only 6.1NRT exists, so `related_version` is `Unknown`. | MEDIUM |
| MOD03 | `input_to` → INPUT | User's Guide §3.3.2: "Level 1B copies subsets of the geolocation data from the geolocation file to the Earth View products" | Statement: generic "geolocation file" mapped to MOD03 | MEDIUM |
| MOD021KM, MOD02HKM | `parallel_product` → RELATED | User's Guide Table 1.2.1 names both as MOD_PR02 products | none | HIGH |
| MYD02QKM | `equivalent_product` → RELATED | User's Guide Table 1.2.1 lists MOD02QKM / MYD02QKM; it is also the MOD↔MYD counterpart | none | HIGH |
| MOD02OBC | `parallel_product` → RELATED | User's Guide Table 1.2.1 | No CMR record, so no row is written. It is listed in the sidecar as `not_in_cmr`. | — |

**Depth 2 (illustrative).** With `atbd_search_depth = 2`, the parents' relationships are added below the depth-1 rows, with the parent as `shortname`. For example, rows describing MOD01's own inputs would read `MOD01,<version>,PARENT,<related>,...`. A parent whose version cannot be determined, like MOD01, has `related_version` `Unknown` at depth 1. Its depth-2 rows then use `Unknown` as `version` (for example `MOD01,Unknown,PARENT,<related>,...`), and the confidence rules apply unchanged.

---

## Validation Checklist

- [ ] The header is exactly `shortname,version,association_type,related_shortname,related_version,confidence,lineage_relationship`
- [ ] Every `association_type` is a UMM-C v1.18.6 MetadataAssociation Type, assigned through a lineage relationship (Collection_Lineage_Generation_Skill Step 1b) and the Step 1d mapping
- [ ] Every row's `lineage_relationship` maps to its `association_type` (blank only for types set by hand)
- [ ] Every `confidence` is HIGH, MEDIUM or LOW and was assigned with the Step 3 rules
- [ ] HIGH rows have a verified quote, from an ATBD or User Guide, that names the related ShortName
- [ ] Generic-reference mappings are no higher than MEDIUM
- [ ] Naming-convention-only and CMR-pattern-only rows are LOW (except platform counterparts that exist in CMR at the matching version)
- [ ] `version` and `related_version` are never blank; `Unknown` is used only when a version cannot be determined (for example, CMR has only NRT versions)
- [ ] Related collections with no CMR record are left out of the CSV and listed in the sidecar
- [ ] No duplicate (`shortname`, `version`, `related_shortname`) rows and no self-relations
- [ ] The evidence sidecar (if written) lets each row's confidence be traced

---

## Tools Used
- `earthdata_mcp_get_collections`: collection metadata, related URLs, and versions for related collections
- `fetch_url_content`: ATBD and User Guide documents
- Python `csv` module: CSV writing and validation

## Related Skills
- Collection_Lineage_via_ATBD_Skill (parent: lineage discovery)
- Collection_Lineage_Generation_Skill (relationship definitions; turns the same lineage into UMM-C MetadataAssociations)
- Collection_ATBD_Analysis_Skill

## Notes
- **Same lineage, two outputs:** this CSV and Collection_Lineage_Generation_Skill's MetadataAssociations come from the same classification. Each row's `shortname`, `version`, `association_type`, `related_shortname` and `related_version` match a MetadataAssociation's record, `Type`, `EntryId` and `Version`.
- **Review queue:** sort by `confidence` to find relationships that need a curator's review before they are ingested as MetadataAssociations.
- **Reproducibility:** keep the evidence sidecar with the CSV. Confidence depends on CMR state (versions present), so record when the file was generated.

## Version History
- **v1.3** (2026-10-14): Versions that cannot be determined are written as `Unknown` instead of left blank
  - `related_version` is now required. Depth-2+ rows use `Unknown` as `version` for such a parent, instead of its NRT version
- **v1.2** (2026-10-14): Added a seventh column, `lineage_relationship`
  - Records the detailed lineage relationship (`derived_from`, `parallel_product`, `equivalent_product`, …) behind each `association_type`, so rows of the same UMM-C type can be told apart
  - Appended as the last column, so the first six columns are unchanged
  - Validation checks that it maps to the row's `association_type`
- **v1.1** (2026-10-14): Replaced `relation_type` with `association_type`
  - The column holds UMM-C v1.18.6 MetadataAssociation Types (PARENT, INPUT, CHILD, RELATED, …) instead of lineage relationship labels
  - Lineage relationships are still used for classification and confidence, and are recorded in the evidence sidecar
  - Sort order and validation now use the UMM-C enum
- **v1.0** (2026-10-14): Initial CSV lineage export
  - Six-column CSV: shortname, version, relation_type, related_shortname, related_version, confidence
  - `relation_type` vocabulary shared with Collection_Lineage_Generation_Skill Step 1a
  - Rule-based HIGH / MEDIUM / LOW confidence from evidence source, statement strength and CMR validation
  - Multi-level lineage through `atbd_search_depth`
  - Optional JSON evidence sidecar

---

**Skill Status:** ✅ COMPLETE
**Output:** `{shortname}_V{version}_lineage.csv` (+ optional `{shortname}_V{version}_lineage_evidence.json`)
