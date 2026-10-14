# Skill: Extract Collection Documentation and Suggest Science Keywords for Any CMR Collection

## Overview
This skill demonstrates how to extract public documentation for any NASA Earth science collection in the CMR (Common Metadata Repository) and use the Earthdata keyword tool to suggest appropriate science keywords.

**Skill Type:** Data Discovery & Metadata Enhancement  
**Difficulty Level:** Intermediate  
**Use Cases:** 
- Metadata enrichment and validation
- Collection keyword discovery
- Science terminology standardization
- Collection documentation review

## Prerequisites
- Access to Earthdata `collections` tool
- Access to Earthdata `keywords` tool
- Target collection short name (e.g., MOD02HKM, VJ217A2, MOD44B)
- Network access to fetch public documentation URLs

## Input Parameters

| Parameter | Type | Required | Example | Description |
|-----------|------|----------|---------|-------------|
| `collection_short_name` | string | Yes | `MOD02HKM` | CMR collection short name |
| `provider_id` | string | No | `LPCLOUD`, `LAADS`, `ORNL_CLOUD` | Optional: specific data provider |
| `doc_type` | string | No | `ATBD`, `USER_GUIDE`, `LANDING_PAGE` | Documentation type preference |
| `limit_keywords` | integer | No | 10 | Max keywords to suggest (default: 10) |

## Workflow Steps

### Step 1: Retrieve Collection Metadata
Use the **collections tool** to locate and extract the collection record.

**Tool:** `earthdata_mcp_get_collections`

**Parameters:**
```
short_name: [collection_short_name]
provider: [provider_id] (optional)
fields: [
  "concept_id",
  "entry_title",
  "abstract",
  "doi",
  "related_urls",
  "science_keywords",
  "platforms",
  "instruments",
  "processing_level_id",
  "temporal_resolution",
  "spatial_resolution"
]
```

**Expected Output:**
- Collection concept ID
- Collection title
- Abstract/summary
- DOI and documentation links
- Current science keywords (if indexed)
- Processing level, resolution, platforms, instruments

**Troubleshooting:**
- If no exact match: try `short_name: [collection_short_name]*` with wildcard
- If multiple results: filter by `provider_id` or review all candidates

### Step 2: Extract Documentation URLs
From the `related_urls` field, identify public documentation.

**Priority order for documentation:**
1. **ATBD (Algorithm Theoretical Basis Document)** - Most detailed technical content
   - Type: `VIEW RELATED INFORMATION`
   - Subtype: `ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)`

2. **User Guide** - Application-focused documentation
   - Type: `VIEW RELATED INFORMATION`
   - Subtype: `USER'S GUIDE`

3. **Landing Page** - High-level overview
   - Type: `DATA SET LANDING PAGE`
   - Provides DOI and collection overview

4. **General Documentation** - Additional context
   - Type: `VIEW RELATED INFORMATION`
   - Subtype: `GENERAL DOCUMENTATION`

**Extraction Logic:**
```python
def extract_doc_urls(related_urls, priority=['ATBD', 'USER_GUIDE', 'LANDING_PAGE']):
    docs = {}
    for url_obj in related_urls:
        doc_type = url_obj.get('subtype') or url_obj.get('type')
        docs[doc_type] = url_obj['url']
    return docs
```

### Step 3: Fetch and Parse Documentation
Use the **fetch_url_content** tool to retrieve documentation.

**Tool:** `fetch_url_content`

**URL Priority:**
1. ATBD PDF (most comprehensive)
2. User Guide PDF
3. DOI landing page (fallback)

**Expected Content from Documentation:**
- Product description and purpose
- Data types and measurements
- Wavelength/frequency ranges
- Processing methodology
- Spatial and temporal characteristics
- Quality assurance details
- Related environmental phenomena

### Step 4: Extract Scientific Concepts
Analyze documentation to identify key scientific concepts.

**Key Information to Extract:**

| Category | Examples | Extraction Method |
|----------|----------|-------------------|
| **Measurement Types** | Radiance, reflectance, temperature, precipitation | Search documentation abstract/intro |
| **Wavelength Ranges** | Visible, infrared, microwave, thermal | Look for band definitions |
| **Earth System Domain** | Atmosphere, land surface, ocean, cryosphere | Review title and keywords |
| **Physical Phenomena** | Fire, vegetation, snow cover, water vapor | Search abstract and methods |
| **Processing Concepts** | Calibration, classification, composite, aggregation | Review algorithm section |
| **Spatial/Temporal Info** | Resolution, coverage, compositing period | Technical specifications |

**Example: MOD02HKM**
```
From documentation:
- "calibrated and geolocated at-aperture radiances"
- "reflective solar bands"
- "visible, near-infrared, and shortwave infrared"
- "500-meter spatial resolution"
- "5-minute swaths"

Extracted Concepts:
→ Visible radiance, Infrared radiance, Reflected infrared
```

**Example: VJ217A2**
```
From documentation:
- "Gross Primary Productivity (GPP)"
- "Net Photosynthesis (PSN)"
- "radiation use efficiency"
- "8-day composite"
- "vegetation"

Extracted Concepts:
→ Vegetation productivity, Gross primary productivity, Photosynthesis
```

### Step 5: Query Keyword Tool for Each Concept
Use the **keywords tool** to find official Earthdata vocabulary matches.

**Tool:** `earthdata_mcp_get_keywords`

**Parameters for each concept:**
```
query: [extracted_concept]
scheme: "sciencekeywords"
fields: [
  "prefLabel",
  "definition",
  "uuid",
  "scheme"
]
limit: [limit_keywords]
```

**Search Strategy:**
- Start with exact terminology from documentation
- If no results, try broader terms
- Try singular and plural forms
- Search related concepts (e.g., "evaporation" if "evapotranspiration" not found)

**Example Queries for MOD02HKM:**
```
1. Query: "visible radiance"     → Result: VISIBLE RADIANCE
2. Query: "infrared radiance"    → Result: INFRARED RADIANCE
3. Query: "reflected infrared"   → Result: REFLECTED INFRARED
4. Query: "reflectance"          → Result: REFLECTANCE (multiple variants)
```

**Example Queries for VJ217A2:**
```
1. Query: "gross primary productivity" → Result: (no direct match)
2. Query: "vegetation productivity"    → Result: VEGETATION PRODUCTIVITY
3. Query: "photosynthesis"             → Result: (no direct match - use VEGETATION PRODUCTIVITY)
4. Query: "evapotranspiration"         → Result: EVAPOTRANSPIRATION
5. Query: "latent heat flux"           → Result: LATENT HEAT FLUX
```

### Step 6: Validate and Prioritize Keywords
Compare suggested keywords against:

**Validation Checks:**
- [ ] Keywords found in official KMS (not arbitrary terms)
- [ ] Keywords align with collection abstract/title
- [ ] Keywords match processing level (L1B vs L3, etc.)
- [ ] Keywords are distinct (no redundancy)
- [ ] Keywords cover primary measurements (80% of collection content)

**Prioritization Criteria:**

| Priority | Criteria | Examples |
|----------|----------|----------|
| **Tier 1** | Primary measurement or product output | VISIBLE RADIANCE for MOD02HKM; VEGETATION PRODUCTIVITY for VJ217A2 |
| **Tier 2** | Supporting measurements or processes | REFLECTANCE for MOD02HKM; LATENT HEAT FLUX for VJ217A2 |
| **Tier 3** | Related concepts or quality indicators | (rarely assigned) |

### Step 7: Cross-Reference Related Collections
Look for similar collections to validate keyword consistency.

**Find Related Collections:**
- Same instrument, different platform (e.g., MOD vs MYD for MODIS)
- Same processing level, different product (e.g., MOD02QKM vs MOD02HKM)
- Derived products from the same input (e.g., MOD02HKM → MOD09A1)

**Validation Question:** 
Do keywords align with related collections' science keywords?

### Step 8: Compile Final Keyword Recommendation
Create prioritized, validated keyword set.

**Output Format:**

```markdown
## Recommended Science Keywords for [COLLECTION_SHORT_NAME]

### Collection Summary
- **Title:** [entry_title]
- **Concept ID:** [concept_id]
- **DOI:** [doi]
- **Processing Level:** [processing_level_id]
- **Platforms:** [platforms]
- **Instruments:** [instruments]

### Primary Keywords (Tier 1)
1. [KEYWORD_1] - [definition]
2. [KEYWORD_2] - [definition]

### Supporting Keywords (Tier 2)
1. [KEYWORD_3] - [definition]

### Documentation Sources
- ATBD: [url]
- User Guide: [url]
- Landing Page: [doi_url]
```

## Execution Template

```python
def extract_and_suggest_keywords(collection_short_name, provider_id=None):
    """
    Master function for keyword extraction workflow
    """
    
    # Step 1: Get collection metadata
    collection = get_collection_metadata(collection_short_name, provider_id)
    
    # Step 2: Extract documentation URLs
    doc_urls = extract_documentation_urls(collection['related_urls'])
    
    # Step 3: Fetch documentation
    documentation = fetch_documentation(doc_urls)
    
    # Step 4: Extract scientific concepts
    concepts = extract_scientific_concepts(documentation)
    
    # Step 5-6: Query keywords and validate
    keywords = []
    for concept in concepts:
        kw_results = query_keyword_tool(concept)
        keywords.extend(kw_results)
    
    # Step 7: Cross-reference
    validate_against_related(collection_short_name, keywords)
    
    # Step 8: Compile results
    final_recommendations = prioritize_keywords(keywords)
    
    return final_recommendations
```

## Quality Assurance Checklist

- [ ] Collection found in CMR with correct concept ID
- [ ] All documentation URLs identified and accessible
- [ ] Key scientific concepts extracted from documentation
- [ ] All concepts queried against KMS
- [ ] Returned keywords verified in official vocabulary
- [ ] Keywords match collection description and processing level
- [ ] Redundant or overlapping keywords removed
- [ ] Prioritized list created (Tier 1 → Tier 2)
- [ ] Related collections reviewed for consistency
- [ ] Output formatted and documented
- [ ] No proprietary or non-standard terms used

## Common Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| Collection not found by short name | Try with wildcard (*) or search by keyword/concept ID |
| Documentation URL broken or behind authentication | Use DOI landing page; contact collection provider |
| Concept has no exact KMS match | Search related/broader terms; check synonym vocabulary |
| Too many keyword matches | Use definition to disambiguate; check related collections |
| Keywords seem too specific or too broad | Cross-validate with collection abstract; compare to similar products |
| Conflicting keywords between sources | Prioritize ATBD terminology over other sources |

## Collection-Type Specific Guidance

### Level-1 (Raw Data) Collections
**Expected Keywords:** Radiance, brightness temperature, raw counts
**Typical Query Terms:** Instrument name + "radiance", "thermal", "visible"
**Examples:** MOD02HKM, VJ114IMG, SMAP_L1B_TB

### Level-2 (Geophysical) Collections
**Expected Keywords:** Temperature, reflectance, indices
**Typical Query Terms:** Measurement type + "surface", "land", "ocean"
**Examples:** MOD11A2, MOD09A1, MYD21A2

### Level-3 (Gridded/Composite) Collections
**Expected Keywords:** Composite, aggregated, processed product
**Typical Query Terms:** Product name + "productivity", "cover", "density"
**Examples:** MOD44B, VJ217A2, GFCC30TC

### Level-4 (Model Output/Analysis) Collections
**Expected Keywords:** Model results, derived product
**Typical Query Terms:** Model name + output type
**Examples:** GLDAS_NOAH, MiCASA, ECOSTRESS

## Tools Used
- `earthdata_mcp_get_collections` - Collection discovery and metadata retrieval
- `fetch_url_content` - Public documentation retrieval
- `earthdata_mcp_get_keywords` - Official Earthdata KMS keyword lookup

## References
- CMR Documentation: https://earthdata.nasa.gov/about/science-system-description/eosdis-components/cmr
- Earthdata Keyword Management System: https://earthdata.nasa.gov/about/science-system-description/eosdis-components/cmr/keywords
- Collection Metadata Standards: https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html

## Related Skills
- Validate Science Keywords Against Collection
- Query Earthdata Keyword Management System
- Cross-Reference Related Collections
- Extract Collection Variables and Dimensions
- Generate Collection Summary Report

## Example Executions

### Example 1: MODIS L1B Radiance (MOD02HKM)
```
Input: collection_short_name = "MOD02HKM"

Output:
✓ VISIBLE RADIANCE
✓ INFRARED RADIANCE
✓ REFLECTED INFRARED
✓ REFLECTANCE
```

### Example 2: VIIRS Productivity (VJ217A2)
```
Input: collection_short_name = "VJ217A2"

Output:
✓ VEGETATION PRODUCTIVITY
✓ EVAPOTRANSPIRATION
✓ LATENT HEAT FLUX
✓ EVAPORATION
```

### Example 3: MODIS Tree Cover (MOD44B)
```
Input: collection_short_name = "MOD44B"

Output:
✓ VEGETATION COVER
✓ CANOPY CHARACTERISTICS
✓ LAND USE/LAND COVER CLASSIFICATION
```

## Notes
- Always fetch fresh documentation; do not rely on cached abstracts
- Validate all keywords are from official Earthdata KMS
- Consider collection processing level when selecting keywords
- Review related/companion collections for consistency
- Document keyword selection rationale
- Revalidate if collection undergoes reprocessing
- Update skill with emerging collection types or keyword standards

## Version History
- **v1.0** (2025-01-XX): Initial generic skill creation
- Adapted from MOD02HKM-specific skill
- Tested with multiple collection types (L1B, L2, L3, L4)
