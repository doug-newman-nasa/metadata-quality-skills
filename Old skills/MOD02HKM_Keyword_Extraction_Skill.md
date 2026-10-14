# Skill: Extract Collection Documentation and Suggest Science Keywords for MOD02HKM

## Overview
This skill demonstrates how to extract public documentation for a NASA Earth science collection (MOD02HKM) and use the Earthdata keyword tool to suggest appropriate science keywords.

## Prerequisites
- Access to Earthdata collections tool
- Access to Earthdata keyword tool
- Target collection short name (MOD02HKM)
- Public documentation URL (DOI or landing page)

## Workflow Steps

### Step 1: Retrieve Collection Metadata
Use the **collections tool** to locate the collection by short name.

**Tool:** `earthdata_mcp_get_collections`
**Parameters:**
- `short_name`: `MOD02HKM`
- `fields`: Include `related_urls`, `doi`, `entry_title`, `abstract`, `science_keywords`

**Expected Output:**
- Collection concept ID
- DOI URL
- Related documentation links (ATBD, User Guide)
- Current science keywords (if any)

### Step 2: Fetch Public Documentation
Access the public ATBD (Algorithm Theoretical Basis Document) or landing page using the fetched URL.

**Tool:** `fetch_url_content`
**URL sources:**
- DOI landing page: `https://doi.org/10.5067/MODIS/MOD02HKM.007`
- ATBD PDF: From `related_urls` field (typically MCST or GSFC links)

**Extract Key Information:**
- Processing level and type (e.g., Level-1B, Calibrated Radiances)
- Wavelength bands and ranges
- Measurement types (visible, infrared, reflected)
- Data product characteristics
- Spatial/temporal resolution

### Step 3: Identify Core Scientific Concepts
From the documentation, extract the primary science concepts:

For **MOD02HKM** example:
- Visible radiance measurements
- Infrared radiance measurements
- Reflected infrared (solar) bands
- Near-infrared and shortwave infrared ranges
- Calibrated reflectance/radiance values

### Step 4: Query the Keyword Tool
Use the **keyword tool** to retrieve official Earthdata science keywords matching identified concepts.

**Tool:** `earthdata_mcp_get_keywords`
**Parameters:**
- `query`: Science concept from documentation
- `scheme`: `sciencekeywords`
- `fields`: `prefLabel`, `definition`, `scheme`

**Queries to run:**
```
1. "visible radiance"
2. "infrared radiance"
3. "reflected infrared"
4. "reflectance"
5. [Any other relevant terms from documentation]
```

### Step 5: Validate Keywords Against Collection
Compare suggested keywords with:
- Existing science keywords in collection metadata
- Documentation terminology
- Related collections in similar domains

### Step 6: Compile Recommended Keyword Set
Create a prioritized list of science keywords:

**For MOD02HKM:**
1. **Primary Keywords** (highest relevance):
   - VISIBLE RADIANCE
   - INFRARED RADIANCE
   - REFLECTED INFRARED

2. **Supporting Keywords** (additional context):
   - REFLECTANCE

3. **Metadata Keywords** (instrument/platform):
   - MODIS (instrument)
   - Terra (platform)

## Key Findings for MOD02HKM

### Collection Characteristics
- **Type:** Terra MODIS Level-1B 500 m Calibrated Radiances
- **Spatial Resolution:** 500 meters
- **Temporal Resolution:** 5-minute swaths
- **Data Format:** netCDF4
- **Bands Covered:** 5 reflective solar bands (Blue, Green, NIR, SWIR)

### Recommended Science Keywords
Based on public documentation analysis:

| Priority | Keyword | Definition | Relevance |
|----------|---------|-----------|-----------|
| 1 | VISIBLE RADIANCE | Radiant intensity in visible wavelengths (W·sr⁻¹·m⁻²) | Direct measurement in product |
| 1 | INFRARED RADIANCE | Radiant intensity in infrared wavelengths (W·sr⁻¹·m⁻²) | Direct measurement in product |
| 1 | REFLECTED INFRARED | Solar-generated IR radiation reflected from objects (0.7-3 µm) | Covers NIR and SWIR bands |
| 2 | REFLECTANCE | Radiation reflected from surface vs. incident radiation | Data convertible to reflectance |

## Quality Assurance Checklist

- [ ] Collection metadata retrieved successfully
- [ ] Public documentation fetched and readable
- [ ] All documentation sources identified (ATBD, User Guide, Landing Page)
- [ ] Key scientific concepts extracted from documentation
- [ ] Keyword tool queries executed for all identified concepts
- [ ] Returned keywords validated against documentation
- [ ] Keywords checked for consistency with related collections
- [ ] Prioritized keyword list created
- [ ] Supporting instrument/platform keywords identified

## Related Skills
- [Extract Collection Description and Suggest Keywords - Generic](./Extract_Collection_Keywords_Generic.md)
- [Query Earthdata Keyword Management System](./KMS_Keyword_Query.md)
- [Validate Science Keywords Against Collection](./Validate_Keywords.md)

## Tools Used
- `earthdata_mcp_get_collections` - Collection discovery and metadata
- `fetch_url_content` - Public documentation retrieval
- `earthdata_mcp_get_keywords` - Keyword vocabulary lookup

## References
- MOD02HKM DOI: `10.5067/MODIS/MOD02HKM.007`
- MODIS L1B ATBD: https://mcst.gsfc.nasa.gov/sites/default/files/file_attachments/MODIS_L1B_ATBD_C7_v7.pdf
- Earthdata Keyword Management System: https://earthdata.nasa.gov/about/science-system-description/eosdis-components/cmr/keywords

## Example Output

### Input
```
Collection Short Name: MOD02HKM
Documentation: Public ATBD and landing page
```

### Output
```
Suggested Science Keywords:
1. VISIBLE RADIANCE
2. INFRARED RADIANCE
3. REFLECTED INFRARED
4. REFLECTANCE (optional)

Collection Details:
- Concept ID: C3861634092-LAADS
- DOI: 10.5067/MODIS/MOD02HKM.007
- Platform: Terra
- Instrument: MODIS
- Processing Level: Level-1B
```

## Notes
- Always fetch fresh documentation; do not rely on cached abstracts
- Validate keywords are from official Earthdata KMS, not arbitrary terms
- Consider related/companion collections (MOD02QKM, MOD021KM) for context
- Update keywords if collection reprocessing changes data characteristics
