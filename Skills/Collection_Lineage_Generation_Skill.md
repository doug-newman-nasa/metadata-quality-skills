# Skill: Collection Lineage Generation (UMM-C MetadataAssociations)

## Overview
This refined skill extends the Collection_Lineage_via_ATBD_Skill by generating valid UMM-C (Unified Metadata Model - Collections) MetadataAssociation elements that describe collection relationships discovered through ATBD analysis, conforming to the official UMM-C v1.18.6 schema.

**Skill Type:** Data Provenance Documentation & Metadata Export  
**Difficulty Level:** Advanced  
**Parent Skills:**
- Collection_Lineage_via_ATBD_Skill
- Collection_ATBD_Analysis_Skill

**Use Cases:**
- CMR metadata update/enhancement
- Collection relationship documentation
- Automated metadata generation
- Data provenance standardization
- Interoperable collection descriptions

## Key Innovation
**Output Format:** UMM-C v1.18.6 MetadataAssociation JSON elements (CMR-compliant)

---

## UMM-C MetadataAssociation Schema (v1.18.6)

### Valid Association Types

According to UMM-C v1.18.6 schema, the following association types are supported:

```
MetadataAssociateTypeEnum:
├─ "SCIENCE ASSOCIATED"  - Related science metadata
├─ "DEPENDENT"           - Collection depends on another
├─ "INPUT"               - Used as input to another
├─ "PARENT"              - Parent collection
├─ "CHILD"               - Derived/child collection
├─ "RELATED"             - Generally related collection
└─ "LARGER CITATION WORKS" - Part of larger work
```

### Correct MetadataAssociation Structure

```json
{
  "Type": "PARENT",
  "Description": "Free-text description (max 4000 chars)",
  "EntryId": "MOD11A1",
  "Version": "6.1"
}
```

### Required Fields
- **EntryId** (required): ShortName of target collection
- **Type** (required): One of the enum values above
- **Description** (optional): Free-text description (1-4000 chars)
- **Version** (optional): Version of target collection

---

## Corrected Processing Steps

### Step 1: Classify Relationship Type

Classification happens in two stages:

1. **Documents → lineage relationship.** Assign each related collection one lineage relationship label, using the definitions and decision procedure below and supported by an evidence quote from the ATBD or User Guide.
2. **Lineage relationship → UMM-C Type.** Convert the label to a UMM-C `Type` with the fixed mapping table.

The UMM-C schema defines the `Type` enum but not what each value means. The definitions below are this skill's convention, and every association must follow them.

#### 1a. Lineage relationship definitions

Every relationship describes the **related collection X relative to the target collection T** (the collection whose record is being updated).

| Lineage relationship | Definition | Typical evidence | Example (T ← X) |
|---|---|---|---|
| `derived_from` | T is produced **directly from X's data**: T is a reprocessing, calibration, retrieval or transformation of X. X is T's upstream product. | "generated from", "derived from", "converts X into", "X is the principal input" | MOD02QKM ← MOD01 (L1A counts calibrated into L1B radiances) |
| `aggregated_from` | T **temporally or spatially aggregates, averages or composites** X. | "average of all X pixels", "composited from", "8-day mean of daily X" | MOD11A2 ← MOD11A1 (8-day average of daily LST) |
| `input_to` | T's algorithm **consumes X as an input or ancillary input**, but T is **not** a reprocessing of X's data. | "X is used to", "inputs include", "requires X", "copied from the X file" | MOD02QKM ← MOD03 (geolocation input) |
| `component_of` | T is **assembled from X as one of several components or subsets**, for example a merged or multi-sensor product. | "combines X and Y", "X forms the … layer of T" | A merged product ← each contributing collection |
| `downstream_product` | X is **produced from T** (X is T's child). | "T is the input to X", "X is derived from T" | MOD02QKM → a named L2 product that cites it |
| `parallel_product` | X is **produced by the same processing run or algorithm alongside T** (a sibling). Neither is derived from the other. | "the process produces three files…", product summary tables | MOD02QKM ↔ MOD02HKM, MOD021KM |
| `equivalent_product` | X is **the same product from another platform or instrument**, made with the same algorithm. | Terra/Aqua (MOD/MYD), SNPP/NOAA-20 (VNP/VJ1) naming | MOD02QKM ↔ MYD02QKM |
| `version_of` | X is a **different version of a related product family**, discussed in the documents (for example a predecessor product with a different ShortName). Never list other versions of T itself. | "replaces", "supersedes", "successor to" | — |
| `template_of` | X **shares T's format, structure or processing template** without a data dependency. | "follows the same format as X" | — |
| `related_to` | Any other **documented** relationship that doesn't fit a type above. | Explicit cross-references | — |

#### 1b. Decision procedure

Apply the questions in order and stop at the first "yes":

1. Is X produced from T? → `downstream_product`
2. Is T produced directly from X's data?
   - by temporal or spatial aggregation → `aggregated_from`
   - by any other reprocessing or transformation → `derived_from`
3. Does T's algorithm consume X without reprocessing X's data?
   - X is one of several assembled components → `component_of`
   - otherwise (ancillary, geolocation, masks, auxiliary fields) → `input_to`
4. Is X produced by the same run as T? → `parallel_product`
5. Is X the same product from another platform or instrument? → `equivalent_product`
6. Otherwise, if the documents describe a relationship → `version_of`, `template_of` or `related_to`

**The PARENT vs INPUT test:** if X were reprocessed, would T change *because X's measurements changed*? If T is X's data carried forward (calibrated, retrieved, averaged), use PARENT. If X only supports T's processing (where pixels are, which are cloudy, what the surface is), use INPUT. When a collection serves both roles, choose PARENT.

#### 1c. Classification rules

1. **Direct relationships only.** List only collections T's own processing uses or produces. Inputs of T's parent are not inputs of T. MOD03 is an input to MOD11_L2, not to MOD11A2; when such a collection is still worth recording, use `related_to`.
2. **Evidence is required.** Every relationship needs a verbatim quote from the documentation, plus its section or page. The quote must be findable in the document text. Exception: `equivalent_product` may be inferred from platform naming conventions (MOD↔MYD, VNP↔VJ1) when the counterpart exists in CMR. Say so in the Description.
3. **Generic references.** When the documents describe an input generically ("the Level 1A granules", "the geolocation file"), map it to a ShortName only when the instrument, platform and processing level make the mapping unambiguous. State in the Description that the mapping was inferred.
4. **CMR collections only.** Skip look-up tables, software, ephemeris/attitude files and other inputs that are not distributed as CMR collections. If a named collection has no CMR record at all, omit it. If only NRT records exist, keep it and omit `Version`.
5. **One relationship per EntryId.** If several apply, use the most specific: the earliest match in the decision procedure.
6. **Precision over recall.** When the evidence is ambiguous, use RELATED, or omit the association, rather than overstating the relationship.

#### 1d. Mapping to UMM-C Type

```python
LINEAGE_TO_UMM_TYPE = {
    'derived_from': 'PARENT',
    'aggregated_from': 'PARENT',
    'input_to': 'INPUT',
    'component_of': 'INPUT',
    'downstream_product': 'CHILD',
    'parallel_product': 'RELATED',
    'equivalent_product': 'RELATED',
    'version_of': 'RELATED',
    'template_of': 'RELATED',
    'related_to': 'RELATED',
}


def map_to_umm_c_association_type(lineage_relationship):
    """Map a lineage relationship (X relative to the target T) to a UMM-C MetadataAssociation Type"""
    return LINEAGE_TO_UMM_TYPE.get(lineage_relationship.lower(), 'RELATED')
```

| Lineage relationship | UMM-C Type | Meaning in the target's record |
|---|---|---|
| `derived_from` | PARENT | X is T's upstream product |
| `aggregated_from` | PARENT | T aggregates X |
| `input_to` | INPUT | X is an input to T's algorithm |
| `component_of` | INPUT | X is a component T is assembled from |
| `downstream_product` | CHILD | X is produced from T |
| `parallel_product` | RELATED | Sibling from the same processing run |
| `equivalent_product` | RELATED | Same product, other platform/instrument |
| `version_of` | RELATED | Related product version |
| `template_of` | RELATED | Shared format/template |
| `related_to` | RELATED | Other documented relationship |

The skill does not assign `SCIENCE ASSOCIATED`, `DEPENDENT` or `LARGER CITATION WORKS` automatically. Set them by hand only when a data provider requires them. Unrecognized labels map to `RELATED`.

#### 1e. Worked example: MOD02QKM V7 (Terra MODIS L1B 250m)

| EntryId | Evidence (L1B ATBD C7 / User's Guide) | Lineage relationship | Type |
|---|---|---|---|
| MOD01 | "Each L1A granule contains 5 minutes of data… These are the principal inputs to the Level 1B (L1B) process." (ATBD §5.1) | `derived_from`: L1B is the L1A data, calibrated (mapping from "L1A" inferred) | PARENT |
| MOD03 | "Level 1B copies subsets of the geolocation data from the geolocation file to the Earth View products" (User's Guide §3.3.2) | `input_to`: geolocation supports processing; the radiances are not MOD03's data | INPUT |
| MOD02HKM, MOD021KM | Table 1.2.1: the four products of MOD_PR02 (User's Guide §1.2) | `parallel_product`: same run, from the same L1A input | RELATED |
| MYD02QKM | Table 1.2.1 lists MOD02QKM / MYD02QKM | `equivalent_product`: Aqua counterpart | RELATED |
| MOD02OBC | Table 1.2.1 | `parallel_product`, but it has no CMR record | omitted (rule 4) |

MOD02HKM is not a CHILD of MOD02QKM, even though it contains bands 1–2 aggregated to 500m. Both are produced from MOD01 in the same run; MOD02HKM is not made from MOD02QKM files.

### Step 2: Extract Metadata for MetadataAssociation

```python
def extract_umm_c_metadata_association(parent_collection, target_collection, 
                                     relationship_type, atbd_data):
    """Extract data for UMM-C MetadataAssociation"""
    
    association = {
        "Type": relationship_type,  # PARENT, INPUT, RELATED, etc.
        "Description": generate_description(parent_collection, relationship_type, atbd_data),
        "EntryId": parent_collection['short_name'],
        "Version": parent_collection.get('version', None)
    }
    
    return association


def generate_description(parent_collection, association_type, atbd_data):
    """Generate description from ATBD data for UMM-C"""
    
    base_description = f"{atbd_data['target_collection']} uses {parent_collection['short_name']}"
    
    if association_type == 'PARENT':
        desc = (
            f"{atbd_data['target_collection']} is derived from {parent_collection['short_name']}. "
            f"Processing: {atbd_data.get('processing_method', 'Not specified')}. "
        )
    elif association_type == 'INPUT':
        desc = (
            f"{parent_collection['short_name']} serves as input to {atbd_data['target_collection']}. "
            f"Role: {atbd_data.get('input_role', 'Primary input')}. "
        )
    elif association_type == 'CHILD':
        desc = (
            f"{parent_collection['short_name']} is derived from {atbd_data['target_collection']}. "
            f"Processing: {atbd_data.get('processing_method', 'Not specified')}. "
        )
    elif association_type == 'RELATED':
        desc = (
            f"{parent_collection['short_name']} is related to {atbd_data['target_collection']}. "
            f"Relationship: {atbd_data.get('relationship_description', 'Associated collection')}. "
        )
    else:
        desc = base_description
    
    # Add ATBD reference if available
    if atbd_data.get('atbd_section'):
        desc += f"ATBD Section: {atbd_data['atbd_section']}. "
    
    if atbd_data.get('lineage_quote'):
        desc += f"Source: '{atbd_data['lineage_quote']}'"
    
    # Ensure description is within 4000 char limit
    if len(desc) > 4000:
        desc = desc[:3997] + "..."
    
    return desc
```

### Step 3: Validate Against UMM-C Schema

```python
def validate_umm_c_association(association):
    """Validate association conforms to UMM-C schema"""
    
    validation = {
        'valid': True,
        'errors': []
    }
    
    # Check required fields
    if 'EntryId' not in association or not association['EntryId']:
        validation['valid'] = False
        validation['errors'].append("EntryId (ShortName) is required")
    
    if 'Type' not in association or not association['Type']:
        validation['valid'] = False
        validation['errors'].append("Type is required")
    
    # Validate Type is in enum
    valid_types = [
        "SCIENCE ASSOCIATED", "DEPENDENT", "INPUT", 
        "PARENT", "CHILD", "RELATED", "LARGER CITATION WORKS"
    ]
    
    if association.get('Type') not in valid_types:
        validation['valid'] = False
        validation['errors'].append(
            f"Type '{association.get('Type')}' not in valid enum: {valid_types}"
        )
    
    # Validate Description length
    if association.get('Description'):
        if len(association['Description']) > 4000:
            validation['valid'] = False
            validation['errors'].append(
                f"Description exceeds 4000 characters ({len(association['Description'])} chars)"
            )
        if len(association['Description']) < 1:
            validation['valid'] = False
            validation['errors'].append("Description must have at least 1 character")
    
    # Validate EntryId format
    if association.get('EntryId'):
        if len(association['EntryId']) > 80:
            validation['valid'] = False
            validation['errors'].append(
                f"EntryId exceeds 80 characters ({len(association['EntryId'])} chars)"
            )
    
    # Validate Version if present
    if association.get('Version'):
        if not isinstance(association['Version'], str):
            validation['valid'] = False
            validation['errors'].append("Version must be a string")
    
    return validation
```

### Step 4: Generate UMM-C JSON Output

```python
def generate_umm_c_json_associations(metadata_associations):
    """Generate UMM-C JSON output for MetadataAssociations array"""
    
    umm_c_associations = []
    
    for association in metadata_associations:
        umm_association = {
            "Type": association['Type'],
            "Description": association['Description'],
            "EntryId": association['EntryId']
        }
        
        # Add Version if available
        if association.get('Version'):
            umm_association['Version'] = association['Version']
        
        umm_c_associations.append(umm_association)
    
    return umm_c_associations
```

### Step 5: Merge Into Complete UMM-C Record

```python
def generate_complete_umm_c_record(target_collection, metadata_associations):
    """Generate complete UMM-C record with MetadataAssociations"""
    
    umm_c_record = {
        "ShortName": target_collection['short_name'],
        "Version": target_collection.get('version', '001'),
        "EntryTitle": target_collection['entry_title'],
        "Abstract": target_collection.get('abstract', ''),
        "DOI": {
            "DOI": target_collection.get('doi', ''),
            "Authority": "https://doi.org"
        } if target_collection.get('doi') else {
            "MissingReason": "Unknown"
        },
        "ProcessingLevel": {
            "Id": target_collection.get('processing_level_id', 'Unknown')
        },
        "Platforms": [
            {
                "Type": "Earth Observation Satellites",
                "ShortName": p if isinstance(p, str) else p.get('short_name', p)
            }
            for p in target_collection.get('platforms', [])
        ],
        "Instruments": [
            {
                "ShortName": i if isinstance(i, str) else i.get('short_name', i)
            }
            for i in target_collection.get('instruments', [])
        ],
        "ScienceKeywords": target_collection.get('science_keywords', []),
        "MetadataAssociations": metadata_associations
    }
    
    return umm_c_record
```

---

## Example Output: MOD11A2 (Corrected UMM-C)

```json
{
  "ShortName": "MOD11A2",
  "Version": "6.1",
  "EntryTitle": "MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V061",
  "Abstract": "The Terra Moderate Resolution Imaging Spectroradiometer (MODIS) Land Surface Temperature/Emissivity 8-Day (MOD11A2) Version 6.1 product provides an average 8-day per-pixel Land Surface Temperature and Emissivity (LST&E) with a 1 kilometer (km) spatial resolution in a 1,200 by 1,200 km grid.",
  "DOI": {
    "DOI": "10.5067/MODIS/MOD11A2.061",
    "Authority": "https://doi.org"
  },
  "ProcessingLevel": {
    "Id": "3"
  },
  "Platforms": [
    {
      "Type": "Earth Observation Satellites",
      "ShortName": "Terra"
    }
  ],
  "Instruments": [
    {
      "ShortName": "MODIS"
    }
  ],
  "ScienceKeywords": [
    {
      "Category": "EARTH SCIENCE",
      "Topic": "LAND SURFACE",
      "Term": "SURFACE THERMAL PROPERTIES",
      "VariableLevel1": "LAND SURFACE TEMPERATURE"
    },
    {
      "Category": "EARTH SCIENCE",
      "Topic": "LAND SURFACE",
      "Term": "SURFACE RADIATIVE PROPERTIES",
      "VariableLevel1": "EMISSIVITY"
    }
  ],
  "MetadataAssociations": [
    {
      "Type": "PARENT",
      "Description": "MOD11A2 is derived from MOD11A1. Processing: 8-day temporal averaging of daily LST pixels. ATBD Section: 2.4. Source: 'Each pixel value in the MOD11A2 is a simple average of all the corresponding MOD11A1 LST pixels collected within that 8-day period.' Processing Formula: MOD11A2[pixel] = mean(MOD11A1[pixel, day1:day8]) with minimum 4 valid days requirement.",
      "EntryId": "MOD11A1",
      "Version": "6.1"
    },
    {
      "Type": "RELATED",
      "Description": "MOD03 provides geolocation information required for spatial mapping and georeferencing of MOD11A2 pixels. Essential supporting data for pixel coordinate reference. Geolocation data includes latitude/longitude per pixel at 1 km resolution used for spatial mapping and geographic registration.",
      "EntryId": "MOD03",
      "Version": "6.1"
    },
    {
      "Type": "RELATED",
      "Description": "MYD11A2 is the equivalent product from the Aqua platform. Both collections provide global LST observations with identical processing algorithms and output structure, enabling inter-platform comparison and complementary spatial/temporal coverage.",
      "EntryId": "MYD11A2",
      "Version": "6.1"
    }
  ]
}
```

---

## Key Corrections from Original Skill

| Issue | Original | Corrected |
|---|---|---|
| **Association Types** | Custom types (DerivedFrom, Input, etc.) | UMM-C enum: PARENT, INPUT, RELATED, etc. |
| **Structure** | CollectionRef with nested properties | Simple EntryId (ShortName) field |
| **Fields** | Many optional fields (AtbdReference, etc.) | Only 4 fields: Type, Description, EntryId, Version |
| **Description** | Embedded in AssociationDetails | Single Description field with full details |
| **Schema Compliance** | Custom UMM model | Official UMM-C v1.18.6 |

---

## Execution Template (Corrected)

```python
def extract_lineage_and_export_umm_c_corrected(collection_short_name):
    """
    Complete workflow: Extract lineage and export as UMM-C MetadataAssociation
    (Conforms to UMM-C v1.18.6 schema)
    """
    
    # Step 1-3: Extract lineage from ATBD (unchanged)
    target_collection = get_collection_metadata(collection_short_name)
    atbd_document = fetch_atbd_from_metadata(target_collection)
    lineage_data = extract_lineage_from_atbd(atbd_document)
    
    # Step 4: Map to UMM-C association types and build associations
    metadata_associations = []
    
    # Each related collection carries its own classification (Step 1a-1c) and evidence:
    # {'short_name', 'version', 'relationship_type', 'lineage_quote', 'atbd_section', 'processing_method', ...}
    for parent_collection in lineage_data['parent_collections']:
        # Map this collection's relationship to a UMM-C type (Step 1d)
        umm_type = map_to_umm_c_association_type(
            parent_collection.get('relationship_type', 'related_to')
        )
        
        # Extract metadata, using this collection's evidence rather than collection-wide values
        association = extract_umm_c_metadata_association(
            parent_collection,
            target_collection,
            umm_type,
            {**lineage_data, **parent_collection}
        )
        
        # Validate UMM-C compliance
        validation = validate_umm_c_association(association)
        
        if validation['valid']:
            metadata_associations.append(association)
        else:
            print(f"Validation error: {validation['errors']}")
    
    # Step 5: Generate UMM-C JSON output
    umm_c_associations_array = generate_umm_c_json_associations(metadata_associations)
    
    # Step 6: Build complete UMM-C record
    umm_c_record = generate_complete_umm_c_record(
        target_collection,
        umm_c_associations_array
    )
    
    return json.dumps(umm_c_record, indent=2), umm_c_record
```

---

## Validation Checklist

- [ ] EntryId (ShortName) field is required and present
- [ ] Type field is required and matches enum
- [ ] Type is one of: SCIENCE ASSOCIATED, DEPENDENT, INPUT, PARENT, CHILD, RELATED, LARGER CITATION WORKS
- [ ] Description is 1-4000 characters (if provided)
- [ ] Version is optional string (if provided)
- [ ] No extra fields beyond Type, Description, EntryId, Version
- [ ] JSON validates against UMM-C v1.18.6 schema
- [ ] No nested CollectionRef object
- [ ] No AssociationDetails object

**Classification (Step 1):**
- [ ] Each association's Type comes from its own lineage relationship (Step 1a), not a collection-wide value
- [ ] The relationship was chosen with the decision procedure (Step 1b); PARENT vs INPUT passes the "is T X's data carried forward?" test
- [ ] The relationship is direct: no inputs of T's parent listed as INPUTs of T
- [ ] The Description includes a verbatim evidence quote and section/page that can be found in the source document
- [ ] Generic references mapped to a ShortName are marked "inferred" in the Description
- [ ] The EntryId has a CMR record; Version is omitted when only NRT versions exist
- [ ] Each EntryId appears at most once

---

## CMR API Compatibility

These MetadataAssociations conform to:
- **UMM-C Version:** 1.18.6
- **CMR API:** Ready for direct ingestion
- **Update Endpoint:** `/collections/{concept_id}`
- **Format:** JSON (preferred)

---

## Version History
- **v2.1** (2026-10-13): Defined relationship classification; renamed from `Generic_Collection_Lineage_UMM_C_Export_Skill_Corrected.md` to `Collection_Lineage_Generation_Skill.md`
  - Added Step 1a–1e: definitions for each lineage relationship (X relative to the target T), an ordered decision procedure, the PARENT vs INPUT test, classification rules (direct relationships only, evidence required, inferred mappings marked, CMR collections only, one relationship per EntryId) and a MOD02QKM V7 worked example
  - Added `downstream_product` → CHILD and `related_to` → RELATED to the mapping; the previous mapping had no way to produce CHILD
  - Added a CHILD branch to `generate_description`
  - Fixed the execution template: each related collection's Type now comes from its own `relationship_type`. Previously one `lineage_data['relationship_type']` was applied to every association, and its default `'related'` was not a mapping key.
  - Added classification items to the validation checklist
  - Reference implementation: `Collection_Lineage_UMM_C_Export.ipynb`
- **v2.0** (2025-09-11): Corrected to UMM-C v1.18.6 schema
  - Fixed association type enum
  - Simplified MetadataAssociation structure
  - Removed non-standard fields
  - Validated against official schema
  - All descriptions consolidated into single field
- **v1.0** (2025-09-11): Initial UMM-C export capability (non-compliant)

---

**Skill Status:** ✅ **CORRECTED & UMM-C COMPLIANT**  
**Schema Version:** UMM-C v1.18.6  
**Output Compatibility:** Official CMR specification  
**Ready for:** Direct CMR metadata ingestion and updates
