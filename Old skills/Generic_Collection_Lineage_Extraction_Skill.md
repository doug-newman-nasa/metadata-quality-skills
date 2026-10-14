# Skill: Extract Collection Lineage and Determine Parent/Input Collections

## Overview
This skill determines what CMR collections were used to produce a derived collection. It identifies the data provenance chain, input collections, processing hierarchy, and relationships between collections.

**Skill Type:** Data Provenance & Lineage Discovery  
**Difficulty Level:** Advanced  
**Parent Skill:** Generic_Collection_Keyword_Extraction_Skill  
**Use Cases:**
- Understanding data derivation chains
- Tracing data source authenticity
- Identifying required input collections for processing
- Documentation of processing hierarchy
- Quality assurance and lineage validation

## Prerequisites
- Access to Earthdata `collections` tool
- Access to `fetch_url_content` for documentation
- Target collection short name
- Understanding of CMR processing levels (L1A, L1B, L2, L3, L4)

## Input Parameters

| Parameter | Type | Required | Example | Description |
|-----------|------|----------|---------|-------------|
| `collection_short_name` | string | Yes | `MOD11A2` | CMR collection short name |
| `search_lineage_depth` | integer | No | 3 | How many levels up/down to search (default: 3) |
| `include_related_versions` | boolean | No | true | Include different versions of same collection |
| `output_format` | string | No | `tree`, `list`, `graph` | How to display lineage (default: tree) |

## Workflow Steps

### Step 1: Analyze Collection Processing Level
Determine where the collection sits in the processing hierarchy.

**Processing Level Classification:**

| Level | Type | Characteristics | Examples |
|-------|------|---|---|
| **L0** | Raw Data | Direct instrument output, no processing | Native satellite telemetry |
| **L1A** | Reformatted Raw | Reformatted, geolocated but not radiometrically calibrated | MOD01 (MODIS raw radiance) |
| **L1B** | Calibrated Radiance | Radiometrically calibrated at-aperture radiance | MOD02HKM, MOD02QKM |
| **L2** | Geophysical Variables | Retrieved geophysical variables from L1B | MOD06 (cloud properties), MOD11A1 (LST daily) |
| **L3** | Gridded/Composite | Spatially and/or temporally composited L2 data | MOD11A2 (LST 8-day), MOD09A1 (surface reflectance 8-day) |
| **L4** | Model Output | Data assimilation or model-generated products | GLDAS, MERRA-2 |

**Tool:** `earthdata_mcp_get_collections`  
**Query:** Extract `processing_level_id` field

**Processing Level Logic:**
```
IF processing_level_id IN [L3, L4]:
    → Likely derived from lower-level collections
    → Search for related L2, L1B, or L0 collections
    
IF processing_level_id IN [L1B, L1A, L0]:
    → Likely input collection
    → Search for L2/L3 products derived from this
    
IF processing_level_id == L2:
    → May be both input and output
    → Could derive from L1B or feed into L3
```

**Example: MOD11A2**
```
Input Processing Level: L3 (Level 3 - Gridded/Composite)
→ Indicator: Derived product likely created from L2 data
→ Expected parent: MOD11A1 (L2 - daily LST)
```

### Step 2: Extract Lineage Information from Documentation
Search collection documentation for explicit lineage/provenance statements.

**Documentation Search Terms:**

| Search Term | Purpose |
|---|---|
| "derived from" | Identifies source collections |
| "input data" | Lists required inputs |
| "based on" | References source product |
| "aggregated from" | Indicates temporal/spatial aggregation |
| "composite of" | Shows what's combined to create this collection |
| "uses" / "incorporates" | Input dependencies |
| "predecessor" / "successor" | Collection version relationships |
| "L2 product" / "L1B data" | Direct level references |

**Tool:** `fetch_url_content` for ATBD, User Guide, Landing Page

**Example from MOD11A2 documentation:**
```
"Each pixel value in the MOD11A2 is a simple average of all the 
corresponding MOD11A1 LST pixels collected within that 8-day period."

Extracted: MOD11A2 is derived from MOD11A1
```

### Step 3: Query CMR for Related Collections
Search CMR for collections with related naming/properties.

**Tool:** `earthdata_mcp_get_collections`

**Search Strategy A - By Short Name Pattern:**
```python
# Example: For MOD11A2, search for related patterns
patterns_to_search = [
    "MOD11*",      # Same product family
    "MYD11*",      # Aqua equivalent (if Terra)
    "MOD11A1",     # Explicit parent product
    "*11A2*",      # Temporal variation
    "*11*",        # Broader family search
]
```

**Search Strategy B - By Processing Level:**
```
For collection X with processing_level = L3:
  Search for collections where:
    - short_name contains base product name
    - processing_level IN [L1B, L2]
    - platform IN [same platform or related]
    - time_start <= X.time_start (predecessor)
```

**Search Strategy C - By Instrument/Platform:**
```
For MOD11A2:
  - Instrument: MODIS
  - Platform: Terra
  
Search for:
  - Other MODIS/Terra products
  - Aqua equivalents (MYD11*)
  - Related instruments on same platform
```

**Query Parameters:**
```
keyword: [base_product_name] [processing_level_name]
instrument: [instrument_name]
platform: [platform_name]
processing_level_id: [adjacent_levels]
limit: 20 (allow more results for comprehensive search)
```

### Step 4: Identify Parent Collections
Filter results to identify actual parent/input collections.

**Criteria for Parent Collection:**

| Criterion | Check | Example |
|---|---|---|
| **Processing Level** | Lower than target OR same but different temporal resolution | MOD11A2 (L3, 8-day) ← MOD11A1 (L2, daily) |
| **Product Family** | Same scientific variable/product name base | MOD11* (all LST products) |
| **Temporal Coverage** | Overlaps or precedes target collection | MOD11A1 starts before MOD11A2 |
| **Instrument Match** | Same or complementary instrument | MODIS Terra for MODIS Terra products |
| **Documentation Reference** | Explicitly mentioned in ATBD or user guide | "Derived from MOD11A1" |
| **Versioning** | Consistent or documented upgrade path | MOD11A2 V6.1 uses MOD11A1 V6.1 |

**Elimination Criteria (NOT parent):**
- Higher processing level (e.g., L4 is not parent of L3)
- Different instrument (e.g., ASTER not parent of MODIS)
- Distinct scientific purpose (e.g., cloud mask not parent of LST)
- Later time start (temporal precedent required)

**Example: MOD11A2 Parent Search**
```
Candidate: MOD11A1
✓ Lower processing level (L2 vs L3)
✓ Same product family (MOD11)
✓ Same instrument/platform (MODIS/Terra)
✓ Time coverage overlaps
✓ Documentation states: "average of MOD11A1 LST"
→ CONFIRMED as parent

Candidate: MOD03 (Geolocation)
✓ Lower processing level (L1B geolocation)
✓ Same platform
✓ Used in processing pipeline
~ Supporting collection, not primary input
→ SECONDARY parent
```

### Step 5: Identify Child/Derived Collections
Search for collections produced FROM the target collection.

**Tool:** `earthdata_mcp_get_collections`

**Search Strategy:**
```
For MOD11A2, search for:
  - Higher processing levels (L4 products using L3 LST)
  - Aggregations or composites of MOD11A2
  - Products with MOD11A2 in ATBD as input
  - Climate/model products using MOD11A2
```

**Typical Derivation Chains:**
```
L1B → L2 → L3 → L4
MOD02HKM (L1B) → MOD11A1 (L2) → MOD11A2 (L3) → Climate Models (L4)
```

### Step 6: Build Collection Lineage Graph
Construct the derivation hierarchy.

**Data Structure:**
```python
lineage = {
    "target_collection": {
        "short_name": "MOD11A2",
        "processing_level": "L3",
    },
    "parents": [
        {
            "short_name": "MOD11A1",
            "processing_level": "L2",
            "relationship": "primary_input",
            "method": "8-day_temporal_average",
            "documentation": "ATBD Section 2.3"
        },
        {
            "short_name": "MOD03",
            "processing_level": "L1B",
            "relationship": "supporting_input",
            "method": "geolocation",
            "documentation": "User Guide Appendix B"
        }
    ],
    "children": [
        {
            "short_name": "MOD11C1",
            "processing_level": "L3",
            "relationship": "aggregated_derivative",
            "method": "global_0.05_degree_grid"
        }
    ],
    "related_versions": [
        {
            "short_name": "MYD11A2",
            "platform": "Aqua",
            "description": "Equivalent product from Aqua platform"
        }
    ]
}
```

**Visualization - Tree Format:**
```
MOD11A2 (L3, 8-day LST composite)
├── PRIMARY INPUTS
│   ├── MOD11A1 (L2, daily LST)
│   │   ├── MOD02HKM (L1B, 500m radiance)
│   │   │   └── MOD01 (L1A, raw radiance)
│   │   └── MOD03 (L1B, geolocation)
│   └── MOD43B (L3, BRDF parameters)
├── SUPPORTING INPUTS
│   ├── MOD03 (Geolocation)
│   └── Ancillary data (DEM, land cover)
├── RELATED VERSIONS
│   └── MYD11A2 (Aqua equivalent)
└── DERIVED PRODUCTS
    ├── MOD11C1 (L3, 0.05° grid)
    ├── MOD11C2 (L3, 0.05° monthly)
    └── Climate models (L4)
```

**Visualization - Graph Format:**
```
MOD02HKM ──────┐
                │
MOD01 ─────────┤
                │
               MOD11A1 ──────┐
                │            │
                │           MOD11A2 ──┐
                │            │        │
            MOD03 ────────┘  │       MOD11C1
                             │        │
                        (temporal)   MOD11C2
                       (averaging)
                             │
                    Climate Model (L4)
```

### Step 7: Document Processing Methods
For each parent-child relationship, document HOW the collection is derived.

**Processing Method Classification:**

| Method | Example | Input → Output |
|---|---|---|
| **Temporal Aggregation** | 8-day composite | Daily (MOD11A1) → 8-day (MOD11A2) |
| **Spatial Aggregation** | 0.05° global grid | 1 km tile (MOD11A2) → 0.05° grid (MOD11C1) |
| **Retrieval Algorithm** | Physical inversion | L1B radiance → L2 geophysical variable |
| **Calibration** | Radiometric correction | L0 raw counts → L1B calibrated radiance |
| **Quality Filtering** | QA masking | Raw data → quality-controlled product |
| **Data Fusion** | Multi-source combination | Multiple L2 → L3 or L4 |
| **Modeling** | Assimilation/interpolation | Observations → model output (L4) |
| **Dimensionality Reduction** | Vegetation index calculation | Multi-spectral bands → single index |

**Documentation Format:**
```markdown
## MOD11A2 Processing Derivation

### Primary Parent: MOD11A1
- **Processing Method:** Temporal Aggregation
- **Specification:** Simple arithmetic mean of 8-day period
- **Equation:** MOD11A2[pixel,period] = mean(MOD11A1[pixel, day1..day8])
- **Quality Control:** QA flags inherited and aggregated
- **Documentation:** ATBD Section 2.3, Algorithm Theoretical Basis Document

### Supporting Input: MOD03 Geolocation
- **Method:** Geolocation and mapping
- **Role:** Pixel location reference
- **Resampling:** 1 km resolution maintained
- **Citation:** "Uses geolocation from MOD03 product"
```

### Step 8: Validate Lineage
Cross-check derived lineage against documentation and related products.

**Validation Checks:**

| Check | Purpose | Validation Method |
|---|---|---|
| **Documentation Consistency** | Parent/child relationships stated in docs | Compare extracted info with ATBD |
| **Version Alignment** | Version numbers logical progression | V6.1 parent → V6.1 child |
| **Temporal Continuity** | No gaps in data coverage | Parent time_end ≥ child time_start |
| **Related Product Consistency** | Similar products follow same pattern | MYD11A2 should also derive from MYD11A1 |
| **Scientific Validity** | Derivation method is scientifically sound | Temporal averaging preserves physical meaning |
| **Citation Network** | Other papers cite same lineage | Literature supports documented lineage |

**Validation Result Codes:**
```
✓ CONFIRMED - Explicitly documented and verified
◐ INFERRED - Logically derived from patterns and level
⚠ ASSUMED - Likely but not explicitly documented
✗ UNCONFIRMED - Cannot validate, requires manual review
```

---

## Execution Template

```python
def extract_collection_lineage(collection_short_name, search_depth=3):
    """
    Master function for collection lineage extraction
    """
    
    # Step 1: Analyze processing level
    collection = get_collection_metadata(collection_short_name)
    processing_level = collection['processing_level_id']
    
    # Step 2: Extract lineage from documentation
    documentation = fetch_collection_documentation(collection)
    explicit_parents = extract_explicit_lineage(documentation)
    
    # Step 3-4: Query CMR and identify parents
    potential_parents = search_related_collections(collection)
    confirmed_parents = filter_parent_collections(potential_parents, collection)
    
    # Step 5: Identify derived collections
    derived_products = search_derived_collections(collection)
    confirmed_children = filter_derived_collections(derived_products, collection)
    
    # Step 6: Build lineage graph
    lineage_graph = build_lineage_graph(
        target=collection,
        parents=confirmed_parents,
        children=confirmed_children
    )
    
    # Step 7: Document processing methods
    lineage_with_methods = add_processing_methods(lineage_graph, documentation)
    
    # Step 8: Validate
    validated_lineage = validate_lineage(lineage_with_methods)
    
    return validated_lineage
```

---

## Collection Lineage Analysis: MOD11A2 Example

### **Step 1: Processing Level Analysis**
- **MOD11A2 Level:** L3 (Level 3 - Gridded/Composite)
- **Indicator:** Derived from lower-level data

### **Step 2: Documentation Extraction**
From ATBD:
> "Each pixel value in the MOD11A2 is a simple average of all the corresponding MOD11A1 LST pixels collected within that 8-day period."

**Extracted:** MOD11A2 ← MOD11A1

### **Step 3-4: CMR Search Results**
```
Search for: MOD11* products on Terra
Results:
  - MOD11A1 (L2, daily LST) ✓ Parent candidate
  - MOD11C1 (L3, 0.05° grid) ✓ Child candidate
  - MOD11C2 (L3, monthly) ✓ Child candidate
  - MYD11A2 (Aqua, L3) ✓ Related version
```

### **Step 5: Derived Products**
```
Collections derived from MOD11A2:
  - MOD11C1: 0.05° global daily grid
  - MOD11C2: 0.05° global monthly grid
  - GLDAS: Land data assimilation (uses LST)
  - Climate models: Various L4 products
```

### **Step 6: Lineage Graph**
```
MOD02HKM (L1B)
    ↓
MOD11A1 (L2, daily)
    ↓ [8-day temporal average]
MOD11A2 (L3, 8-day) ← TARGET
    ↓ [spatial aggregation]
MOD11C1 (L3, 0.05° daily)
    ↓ [monthly temporal aggregate]
MOD11C2 (L3, 0.05° monthly)
```

### **Step 7: Processing Methods**
| Derivation | Method | Formula |
|---|---|---|
| MOD02HKM → MOD11A1 | Physical retrieval (split-window LST algorithm) | Complex radiative transfer equations |
| MOD11A1 → MOD11A2 | Temporal averaging | Mean(MOD11A1[8 days]) |
| MOD11A2 → MOD11C1 | Spatial aggregation | Reproject to 0.05° grid |
| MOD11A2 → MOD11C2 | Temporal + spatial aggregation | Monthly mean of MOD11C1 |

### **Step 8: Validation**
- ✓ Documentation explicitly states MOD11A1 → MOD11A2 relationship
- ✓ Processing level hierarchy correct (L2 → L3)
- ◐ Related product MYD11A2 follows same pattern
- ✓ Temporal coverage continuous since 2000
- ✓ Version alignment: V6.1 MOD11A1 → V6.1 MOD11A2

---

## Quality Assurance Checklist

- [ ] Collection metadata retrieved (processing level identified)
- [ ] Documentation fetched and analyzed for lineage statements
- [ ] CMR search performed for related collections
- [ ] Parent collections identified and validated
- [ ] Child/derived collections identified
- [ ] Lineage graph constructed
- [ ] Processing methods documented with formulas
- [ ] Validation checks completed for all relationships
- [ ] Cross-referenced with related versions (e.g., Aqua equivalent)
- [ ] Temporal and version continuity confirmed
- [ ] Lineage visualization generated (tree/graph format)
- [ ] Report documented and formatted

---

## Common Lineage Patterns

### **Pattern 1: Temporal Aggregation**
```
L2 daily → L3 8-day → L3 monthly → L4 annual climate
Example: MOD11A1 → MOD11A2 → MOD11C2 → Climate record
```

### **Pattern 2: Spatial Aggregation**
```
L2 pixel → L3 tile → L3 grid → L4 global model
Example: MOD02HKM (1km tile) → MOD11A2 (1km grid) → MOD11C1 (0.05° grid)
```

### **Pattern 3: Multi-source Fusion**
```
L2 product A + L2 product B + Ancillary → L3 fusion → L4 model
Example: SMAP (soil moisture) + GEDI (vegetation) → L4 assimilation
```

### **Pattern 4: Complex Retrieval**
```
L1B calibrated radiance + Ancillary data → L2 geophysical variable → L3 composite
Example: MOD02HKM (radiance) + MOD03 (geolocation) → MOD11A1 (LST)
```

### **Pattern 5: Direct Derivative (same level)**
```
L3 product A → Processing → L3 product B (different variable)
Example: MOD11A2 (LST) → Emissivity extraction → MOD11A2 LST+Emissivity
```

---

## Tools Used
- `earthdata_mcp_get_collections` - Find related collections
- `fetch_url_content` - Extract documentation lineage info
- Pattern matching on short names and processing levels
- Temporal/version continuity validation

## References
- CMR Processing Levels: https://earthdata.nasa.gov/about/science-system-description/eosdis-components/cmr
- MODIS Collection: https://modis.gsfc.nasa.gov/
- ATBD Documentation Standards: https://earthdata.nasa.gov/

## Related Skills
- Generic_Collection_Keyword_Extraction_Skill (parent skill)
- Extract_Collection_Processing_Chain
- Validate_Data_Provenance
- Generate_Collection_Family_Report
- Create_Lineage_Visualization

---

## Notes
- Lineage extraction becomes more complex with multi-source products
- Some L4 model products may have implicit rather than explicit lineage
- Version compatibility should always be checked
- Temporal gaps can indicate breaks in derivation chain
- Documentation may not always explicitly state all lineage relationships
- Equivalent products (Terra/Aqua) follow parallel lineage chains

## Version History
- **v1.0** (2025-09-10): Initial lineage extraction skill
- Extends Generic_Collection_Keyword_Extraction_Skill
- Tested with MOD11A2 and related LST product family
