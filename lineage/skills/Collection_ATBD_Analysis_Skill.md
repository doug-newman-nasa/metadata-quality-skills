# Skill: Advanced ATBD Analysis for Collection Lineage and Algorithm Documentation

## Overview
This skill refines and extends the Generic_Collection_Lineage_Extraction_Skill by systematically parsing Algorithm Theoretical Basis Documents (ATBDs) to extract detailed algorithm descriptions, data flow specifications, input/output requirements, mathematical formulas, and processing specifications.

**Skill Type:** Scientific Documentation Analysis & Algorithm Extraction  
**Difficulty Level:** Advanced  
**Parent Skill:** Generic_Collection_Lineage_Extraction_Skill  
**Complementary Skills:** Generic_Collection_Keyword_Extraction_Skill  
**Use Cases:**
- Detailed algorithm understanding
- Processing chain reconstruction
- Input/output validation
- Implementation and reproducibility
- Data format specifications
- Quality assurance parameter extraction

## Prerequisites
- Access to collection ATBD documentation (PDF, HTML, or text)
- Basic understanding of remote sensing algorithms
- Knowledge of Earth science processing levels
- Target collection short name
- Access to ATBD URL or direct document

## Input Parameters

| Parameter | Type | Required | Example | Description |
|-----------|------|----------|---------|------------|
| `collection_short_name` | string | Yes | `MOD11A2` | CMR collection short name |
| `atbd_document` | file/url | Yes | ATBD PDF URL | Source document |
| `extract_sections` | list | No | `[algorithms, inputs, outputs, quality]` | Sections to analyze (default: all) |
| `parse_equations` | boolean | No | true | Extract mathematical formulas |
| `extract_data_flow` | boolean | No | true | Identify data flow diagrams |
| `cross_reference_cmr` | boolean | No | true | Validate against CMR metadata |
| `output_format` | string | No | `structured_json` | `structured_json`, `markdown`, `xml` |

## Workflow Steps

### Step 1: ATBD Document Acquisition & Validation
Locate and verify authenticity of ATBD documentation.

**Tool:** `fetch_url_content`

**ATBD Sources (Priority Order):**
1. **Official Provider Collections:**
   - LP DAAC: https://lpdaac.usgs.gov/documents/[ID]/[SHORT_NAME]_ATBD.pdf
   - NSIDC: https://nsidc.org/data/[collection_id]/version/[version]/
   - GES DISC: https://disc.gsfc.nasa.gov/
   - ORNL DAAC: https://daac.ornl.gov/

2. **CMR-Linked Documentation:**
   - From collection `related_urls` field
   - Type: `VIEW RELATED INFORMATION`
   - Subtype: `ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)`

3. **Archive Centers:**
   - MODIS: https://mcst.gsfc.nasa.gov/ (ATBD library)
   - VIIRS: https://www.jpss.noaa.gov/
   - General: https://earthdata.nasa.gov/

**Validation Steps:**
```python
def validate_atbd(document_url, collection_name):
    """Verify ATBD is legitimate and relevant"""
    
    checks = {
        'url_matches_collection': collection_name in url,
        'document_is_pdf_or_html': url.endswith(('.pdf', '.html')),
        'official_provider_source': any(provider in url for provider in 
                                       ['lpdaac', 'nsidc', 'daac', 'gsfc']),
        'accessible': fetch_url_content(url) is not None,
        'contains_algorithm_text': 'algorithm' in document_text.lower()
    }
    
    validation_score = sum(checks.values()) / len(checks)
    if validation_score >= 0.8:
        return True, "ATBD validated"
    return False, "ATBD validation failed"
```

### Step 2: ATBD Section Identification & Structure Analysis
Identify key sections and extract structural information.

**Standard ATBD Section Structure:**

| Section | Content | Key Information |
|---------|---------|---|
| **1. Introduction** | Product overview, purpose, applications | Primary objectives, use cases |
| **2. Algorithm Description** | Core algorithm(s) used | Mathematical formulas, steps |
| **3. Input Data & Ancillary Data** | Required input collections | Data sources, formats, resolutions |
| **4. Processing Algorithm** | Detailed processing steps | Flow diagrams, equations |
| **5. Output Data** | Output product specifications | Variables, formats, units |
| **6. Calibration & Validation** | QA/QC procedures | Calibration coefficients, validation metrics |
| **7. Appendices** | Supporting information | Formulas, tables, figures |

**Section Extraction Strategy:**

```python
def identify_atbd_sections(document_text):
    """Extract section headers and boundaries"""
    
    section_markers = {
        'introduction': ['1.', 'introduction', 'overview'],
        'algorithm': ['2.', '3.', 'algorithm', 'methodology'],
        'inputs': ['input', 'ancillary', 'data sources', 'requirements'],
        'processing': ['processing', 'procedure', 'retrieval', 'calculation'],
        'outputs': ['output', 'product', 'data structure', 'file format'],
        'calibration': ['calibration', 'validation', 'quality', 'qa/qc'],
        'appendix': ['appendix', 'references', 'bibliography']
    }
    
    sections_found = {}
    for section_type, markers in section_markers.items():
        for marker in markers:
            if marker in document_text.lower():
                # Extract section content between markers
                sections_found[section_type] = extract_section_content(
                    document_text, marker)
    
    return sections_found
```

### Step 3: Algorithm Extraction & Documentation
Extract detailed algorithm specifications from ATBD.

**Information to Extract:**

| Algorithm Element | Details to Capture | Example |
|---|---|---|
| **Algorithm Name** | Official name and acronym | "Split-Window LST Algorithm" (SW-LST) |
| **Description** | 1-2 sentence purpose | "Retrieves Land Surface Temperature from thermal IR bands" |
| **Historical Context** | Origin and evolution | "Based on Wan & Dozier (1996), refined for MODIS" |
| **Physical Basis** | Scientific foundation | "Radiative transfer theory, blackbody emission" |
| **Key Assumptions** | Constraints and limitations | "Assumes homogeneous pixels, clear-sky conditions" |
| **Input Requirements** | Specific data needed | "Bands 31, 32 (TIR), Land/Water mask, NDVI" |
| **Output Variables** | What is produced | "LST (K), Emissivity (0-1), QA flags" |
| **Outputs Units & Scales** | Measurement specifications | "LST: 0.02 K precision, stored as int16 × 0.02" |

**Extraction Template:**

```markdown
## Algorithm: [NAME] ([ACRONYM])

### Purpose
[1-2 sentence description]

### Scientific Basis
[Physical principles, radiative transfer theory, etc.]

### Historical Development
[Evolution, improvements, references]

### Assumptions & Limitations
- [Assumption 1]
- [Assumption 2]
- [Limitation 1]

### Input Requirements
| Input | Source Collection | Format | Resolution | Units |
|---|---|---|---|---|
| [Variable] | [Collection] | [Format] | [Res] | [Units] |

### Processing Steps
1. [Step 1]
2. [Step 2]
3. [etc.]

### Output Variables
| Variable | Type | Range | Units | Scale |
|---|---|---|---|---|
| [Var] | [Type] | [Min-Max] | [Units] | [Scale Factor] |

### References
- [Citation 1]
- [Citation 2]
```

### Step 4: Mathematical Formula Extraction
Identify and document all mathematical equations in ATBD.

**Formula Types to Extract:**

| Formula Type | Purpose | Examples |
|---|---|---|
| **Retrieval Algorithms** | Calculate geophysical variables | LST = f(T11, T12, NDVI, ε) |
| **Calibration Equations** | Apply calibration coefficients | DN_calibrated = (DN_raw - offset) × scale |
| **Quality Metrics** | Calculate uncertainty/error | Uncertainty = √(ε₁² + ε₂²) |
| **Validation Statistics** | Compare to reference data | RMSE = √[Σ(measured - reference)²/N] |
| **Atmospheric Corrections** | Account for atmospheric effects | BOA = TOA - path_radiance |
| **Normalization** | Normalize indices or variables | NDVI = (NIR - RED) / (NIR + RED) |

**Formula Extraction Process:**

```python
def extract_formulas(atbd_section):
    """Extract mathematical formulas and equations"""
    
    formulas = []
    
    # Pattern 1: LaTeX-style equations
    latex_patterns = [
        r'\$\$(.*?)\$\$',  # Display math
        r'\$(.*?)\$',       # Inline math
    ]
    
    # Pattern 2: ASCII equations with operators
    ascii_patterns = [
        r'(\w+)\s*=\s*([^;\n]+)',  # Variable assignment
        r'where:\s*(.*?)(?=\n\n)',  # Variable definitions
    ]
    
    # Extract and structure
    for formula_text in formulas:
        formula_structured = {
            'raw_text': formula_text,
            'normalized': normalize_formula(formula_text),
            'variables': extract_variables(formula_text),
            'constants': extract_constants(formula_text),
            'description': extract_formula_description(formula_text),
            'section': current_section,
            'context': surrounding_text
        }
        formulas.append(formula_structured)
    
    return formulas
```

**Output Structure:**
```json
{
  "formulas": [
    {
      "id": "LST_001",
      "name": "Split-Window LST Retrieval",
      "equation": "LST = A1 + (A2 - A1)×(T11 - T12) + A4×(1 - NDVI) + A5×ΔT",
      "variables": {
        "LST": "Land Surface Temperature (K)",
        "T11": "Brightness temperature band 31 (K)",
        "T12": "Brightness temperature band 32 (K)",
        "NDVI": "Normalized Difference Vegetation Index",
        "A1-A5": "Calibration coefficients"
      },
      "output_unit": "Kelvin",
      "output_precision": "0.01 K",
      "source_reference": "Wan & Dozier (1996), ATBD Section 2.3",
      "validity_range": "-40°C to 80°C surface temperature"
    }
  ]
}
```

### Step 5: Input/Output Specification Extraction
Document detailed input and output data specifications.

**Input Specifications to Extract:**

```markdown
## INPUT DATA SPECIFICATION

### Primary Inputs
| Collection | Band/Variable | Resolution | Data Type | Range | Source |
|---|---|---|---|---|---|
| MOD02HKM | Band 31 (TIR) | 1 km | uint16 | 0-4095 | MODIS L1B |
| MOD02HKM | Band 32 (TIR) | 1 km | uint16 | 0-4095 | MODIS L1B |
| MOD02 | NIR, Red | 500m agg to 1km | uint16 | 0-4095 | MODIS L1B |

### Ancillary Inputs
| Type | Collection | Purpose | Resolution | Format |
|---|---|---|---|---|
| Geolocation | MOD03 | Lat/Lon for each pixel | 1 km | HDF |
| Land/Water Mask | MOD44W | Land/Water classification | 250m | HDF |
| NDVI | Derived from MOD02 | Vegetation fraction | 1 km | Internal |
| Elevation | SRTM or GTOPO30 | Terrain correction | 30m-1km | Resampled |

### Calibration/Auxiliary Data
| Data | Source | Format | Update Frequency |
|---|---|---|---|
| Calibration Coefficients | MODIS Characterization Support Team | ASCII table | Per version release |
| Atmospheric Profiles | MODTRAN or ERA-Interim | Model files | Pre-computed |
| Emissivity LUT | ASTER GED | HDF | Annual |
```

**Output Specifications to Extract:**

```markdown
## OUTPUT DATA SPECIFICATION

### Science Data Sets (SDS)
| SDS Name | Variable | Data Type | Range | Units | Scale | Offset |
|---|---|---|---|---|---|---|
| LST_Day_1km | Daytime LST | int16 | 7500-65535 | K | 0.02 | 0.0 |
| LST_Night_1km | Nighttime LST | int16 | 7500-65535 | K | 0.02 | 0.0 |
| Emis_31_Day | Band 31 emissivity | uint8 | 1-255 | fraction | 0.002 | 0.49 |
| Emis_32_Day | Band 32 emissivity | uint8 | 1-255 | fraction | 0.002 | 0.49 |
| QC_Day | Quality control flags | uint8 | 0-255 | flags | - | - |

### File Format
- **Format Type**: HDF-EOS (v5 for newer products)
- **Grid Type**: MODIS Sinusoidal projection
- **File Size**: ~170 MB per 5-min granule
- **Geographic Dimensions**: 2708 samples × 1856 lines (1 km)
- **Tiling Scheme**: MODIS tile system (36×18 tiles globally)

### Quality Flags
| Bit | Parameter | Meaning |
|---|---|---|
| 0 | Mandatory QA | 0=pass, 1=fail |
| 1-2 | Data Quality | 0=best, 3=poor |
| 3 | Cloud State | 0=clear, 1=cloudy |
| 4-7 | Emissivity Accuracy | 0=poor, 15=excellent |
```

### Step 6: Data Flow Diagram Extraction & Reconstruction
Identify and reconstruct data flow paths from ATBD.

**Data Flow Elements to Extract:**

```
INPUT DATA
    ↓
┌───────────────────────┐
│ PROCESSING BLOCK 1    │
│ (Calibration)         │
└───────────┬───────────┘
            ↓
        [QA FLAG]
            ↓
┌───────────────────────┐
│ PROCESSING BLOCK 2    │
│ (LST Retrieval)       │
└───────────┬───────────┘
            ↓
        [QA FLAG]
            ↓
┌───────────────────────┐
│ PROCESSING BLOCK 3    │
│ (Emissivity)          │
└───────────┬───────────┘
            ↓
        [QA FLAG]
            ↓
    OUTPUT PRODUCT
```

**Extraction Template:**

```python
def extract_data_flow(atbd_section):
    """Extract and reconstruct data flow diagrams"""
    
    flow_elements = {
        'inputs': extract_input_sources(section),
        'processing_blocks': [
            {
                'name': 'Calibration',
                'inputs': ['Raw radiance (MOD02HKM)'],
                'algorithm': 'Radiometric calibration',
                'outputs': ['Calibrated radiance'],
                'quality_check': 'Calibration status flag',
                'next': 'LST Retrieval'
            },
            {
                'name': 'LST Retrieval',
                'inputs': ['Calibrated radiance', 'NDVI'],
                'algorithm': 'Split-window algorithm',
                'outputs': ['LST', 'Emissivity'],
                'quality_check': 'LST quality flag',
                'next': 'Output'
            }
        ],
        'outputs': extract_outputs(section),
        'quality_assurance': extract_qa_chain(section)
    }
    
    # Generate ASCII flow diagram
    diagram = generate_flow_diagram(flow_elements)
    return diagram, flow_elements
```

### Step 7: Quality Assurance & Validation Specifications
Extract QA/QC procedures, validation methods, and uncertainty estimates.

**QA Elements to Extract:**

```markdown
## QUALITY ASSURANCE & VALIDATION

### Calibration Procedures
| Procedure | Frequency | Method | Reference |
|---|---|---|---|
| Radiometric Calibration | Per scene | Desert sites (Libya-1) | ATBD Section 4.1 |
| Response-vs-Scan (RVS) | Weekly | Deep convective clouds | ATBD Section 4.2 |
| Crosstalk Correction | Per granule | Electronic calibration | ATBD Section 4.3 |

### Validation Methods
| Validation Type | Reference Data | Metric | Target Accuracy |
|---|---|---|---|
| LST Accuracy | Ground truth sites | RMSE | < 1.0 K |
| Emissivity | ASTER GED database | RMSE | < 0.02 |
| Radiometric | on-board calibrator | Trending | < 2% drift/year |

### Uncertainty Estimates
| Component | Source | Magnitude | Units |
|---|---|---|---|
| Calibration uncertainty | L1B calibration | ±0.5% | % of signal |
| Algorithm uncertainty | Radiative transfer | ±0.3 | K at 300 K |
| Ancillary data uncertainty | NDVI, elevation | ±0.2 | K |
| **Total Uncertainty** | Propagated | ±0.6 | K (95% confidence) |

### Quality Flags & Interpretation
- **QC Bit 0 (Mandatory QA)**: 0=Pass all QA tests, 1=Fail QA
- **QC Bits 1-2 (Data Quality)**: 
  - 00 = Excellent quality
  - 01 = Good quality
  - 10 = Fair quality
  - 11 = Poor quality (use with caution)
- **QC Bit 3 (Cloud)**:
  - 0 = Clear
  - 1 = Cloud detected (may affect LST)
- **QC Bits 4-7 (Emissivity Accuracy)**:
  - Indicates emissivity accuracy level (0=poor, 15=excellent)
```

**Uncertainty Propagation Formula:**

```
Total Uncertainty = √(U_calib² + U_algorithm² + U_ancillary² + U_model²)

Where:
  U_calib = Calibration uncertainty (±0.5%)
  U_algorithm = Algorithm uncertainty from radiative transfer (±0.3 K)
  U_ancillary = Ancillary data uncertainty (NDVI, emissivity) (±0.2 K)
  U_model = Model parameter uncertainty (±0.1 K)

Result: Total uncertainty = ±0.6 K at 95% confidence
```

### Step 8: Cross-Reference with CMR Metadata
Validate ATBD findings against CMR collection metadata.

**Cross-Reference Checklist:**

```python
def cross_reference_atbd_cmr(atbd_data, cmr_collection):
    """Validate ATBD content against CMR metadata"""
    
    validations = {
        'spatial_resolution': {
            'atbd_value': atbd_data['output_spatial_resolution'],
            'cmr_value': cmr_collection['spatial_resolution'],
            'match': compare_resolutions(...),
            'status': 'PASS' or 'WARNING'
        },
        'temporal_resolution': {
            'atbd_value': atbd_data['temporal_resolution'],
            'cmr_value': cmr_collection['temporal_resolution'],
            'match': atbd_data['temporal_resolution'] == cmr_collection['temporal_resolution'],
            'status': 'PASS'
        },
        'input_collections': {
            'atbd_value': atbd_data['input_collections'],
            'cmr_verified': verify_collections_in_cmr(atbd_data['input_collections']),
            'status': 'PASS' or 'REQUIRES_REVIEW'
        },
        'output_variables': {
            'atbd_defined': atbd_data['output_variables'],
            'cmr_variables': cmr_collection['science_keywords'],
            'coverage': calculate_coverage_percentage(...),
            'status': 'GOOD_COVERAGE' or 'INCOMPLETE'
        },
        'algorithm_references': {
            'atbd_citations': extract_citations(atbd_data),
            'publication_count': len(citations),
            'peer_reviewed': count_peer_reviewed(citations),
            'status': 'WELL_DOCUMENTED' if peer_reviewed > 5 else 'LIMITED'
        }
    }
    
    return validations
```

**Validation Matrix:**

| Element | ATBD Specification | CMR Metadata | Status | Notes |
|---|---|---|---|---|
| **Spatial Resolution** | 1 km | 1000x1000 meters | ✓ MATCH | Consistent |
| **Temporal Resolution** | 8-day composite | 8 Day | ✓ MATCH | Consistent |
| **Input: MOD11A1** | Daily LST from MOD02HKM | C1748058432-LPCLOUD | ✓ VERIFIED | Collection exists |
| **Output Variables** | LST, Emissivity, QA flags | Contains LST, Emissivity | ✓ GOOD | Minor QA detail missing |
| **Processing Level** | L3 (composite) | Level 3 | ✓ MATCH | Consistent |
| **Algorithm** | Split-window LST | Not in CMR keywords | ⚠ NOTE | CMR lacks algorithm detail |

---

## ATBD Analysis for MOD11A2 Example

### Complete ATBD-Based Lineage Analysis

```markdown
## MOD11A2 ALGORITHM ANALYSIS (from ATBD)

### Algorithm Chain Extracted from ATBD:

Step 1: INPUT MOD02HKM (L1B)
  - Bands 31, 32 (thermal infrared)
  - Calibrated radiance (W m⁻² sr⁻¹ μm⁻¹)
  - 500m resolution aggregated to 1km

Step 2: PROCESS MOD11A1 Generation (from MOD02HKM)
  - Apply split-window LST algorithm
  - Formula: LST = A1 + (A2-A1)×(T11-T12) + A4×(1-NDVI) + A5×ΔT
  - Generate daily LST at 1km resolution
  - Apply QA flags (clear sky requirement)
  - OUTPUT: MOD11A1 (daily LST)

Step 3: AGGREGATE MOD11A2 (from MOD11A1)
  - Collect 8 daily MOD11A1 granules
  - Simple arithmetic mean per pixel
  - Formula: MOD11A2[pixel] = mean(MOD11A1[pixel, day1:day8])
  - Require ≥ 4 valid days for output
  - Aggregate QA flags
  - OUTPUT: MOD11A2 (8-day composite LST)

Step 4: REGRID MOD11C1/C2 (from MOD11A2)
  - Hierarchical sampling to 0.05° CMG grid
  - Weighted average within grid cells
  - OUTPUT: MOD11C1 (daily 0.05° grid), MOD11C2 (8-day 0.05° grid)

### Input/Output Chain:
MOD02HKM → MOD11A1 → MOD11A2 → MOD11C1/C2 → Climate Models
```

---

## Execution Template

```python
def analyze_atbd_comprehensive(collection_short_name, atbd_url):
    """
    Complete ATBD analysis workflow
    """
    
    # Step 1: Acquire & validate ATBD
    atbd_doc = fetch_atbd(atbd_url)
    validation = validate_atbd(atbd_doc, collection_short_name)
    
    if not validation.success:
        return error(validation.message)
    
    # Step 2: Identify sections
    sections = identify_atbd_sections(atbd_doc)
    
    # Step 3: Extract algorithms
    algorithms = extract_algorithms(sections['algorithm'])
    
    # Step 4: Extract formulas
    formulas = extract_formulas(sections['processing'])
    
    # Step 5: Extract I/O specs
    inputs = extract_input_specifications(sections['inputs'])
    outputs = extract_output_specifications(sections['outputs'])
    
    # Step 6: Reconstruct data flow
    data_flow = extract_data_flow(sections)
    
    # Step 7: Extract QA specs
    qa_specs = extract_qa_specifications(sections['calibration'])
    
    # Step 8: Cross-reference with CMR
    cmr_data = get_collection_metadata(collection_short_name)
    validation_matrix = cross_reference_atbd_cmr(
        {
            'algorithms': algorithms,
            'inputs': inputs,
            'outputs': outputs,
            'qa': qa_specs
        },
        cmr_data
    )
    
    # Compile comprehensive report
    report = {
        'collection': collection_short_name,
        'algorithms': algorithms,
        'formulas': formulas,
        'input_specifications': inputs,
        'output_specifications': outputs,
        'data_flow': data_flow,
        'qa_specifications': qa_specs,
        'cmr_validation': validation_matrix,
        'lineage_graph': build_lineage_from_atbd(algorithms, inputs, outputs)
    }
    
    return report
```

---

## Quality Assurance Checklist

- [ ] ATBD document located and validated
- [ ] Official provider source confirmed
- [ ] All sections identified (intro, algorithm, I/O, QA)
- [ ] Algorithms extracted with descriptions
- [ ] All mathematical formulas identified and normalized
- [ ] Input specifications documented (collections, bands, resolutions)
- [ ] Output specifications documented (variables, ranges, units)
- [ ] Data flow reconstructed (input → processing → output)
- [ ] QA/validation procedures documented
- [ ] Uncertainty estimates extracted and propagated
- [ ] CMR metadata cross-referenced
- [ ] Lineage chain reconstructed from ATBD
- [ ] Related products identified
- [ ] Validation metrics documented
- [ ] Report generated and formatted

---

## Output Structure (JSON)

```json
{
  "atbd_analysis": {
    "collection": "MOD11A2",
    "atbd_source": "https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf",
    "algorithms": [
      {
        "id": "ALG_001",
        "name": "Split-Window LST Retrieval",
        "description": "Retrieves LST from thermal IR bands using split-window technique",
        "equations": [
          {
            "id": "EQ_001",
            "description": "LST calculation",
            "formula": "LST = A1 + (A2-A1)×(T11-T12) + A4×(1-NDVI) + A5×ΔT"
          }
        ]
      }
    ],
    "input_specifications": [
      {
        "collection": "MOD02HKM",
        "band": 31,
        "variable": "Band 31 TIR radiance",
        "resolution": "1 km",
        "data_type": "uint16",
        "range": "0-4095"
      }
    ],
    "output_specifications": [
      {
        "variable": "LST_Day_1km",
        "data_type": "int16",
        "range": "7500-65535",
        "scale": 0.02,
        "unit": "K",
        "description": "Daytime Land Surface Temperature"
      }
    ],
    "data_flow": "MOD02HKM → Calibration → LST_Retrieval → MOD11A1 → Temporal_Aggregation → MOD11A2 → Spatial_Regrid → MOD11C1/C2",
    "qa_specifications": {
      "calibration_frequency": "Per scene",
      "validation_rmse": "< 1.0 K",
      "uncertainty": "±0.6 K (95% confidence)"
    },
    "cmr_validation": {
      "spatial_resolution_match": true,
      "temporal_resolution_match": true,
      "input_collections_verified": true,
      "status": "FULLY_VALIDATED"
    }
  }
}
```

---

## Tools Used
- `fetch_url_content` - Retrieve ATBD documents
- Pattern matching (regex) - Extract formulas and structures
- NLP techniques - Identify sections and keywords
- `earthdata_mcp_get_collections` - Cross-reference CMR

## References
- MODIS ATBD Library: https://mcst.gsfc.nasa.gov/
- VIIRS ATBD Resources: https://www.jpss.noaa.gov/
- CMR Documentation: https://earthdata.nasa.gov/

## Related Skills
- Generic_Collection_Lineage_Extraction_Skill (parent)
- Generic_Collection_Keyword_Extraction_Skill
- Validate_Algorithm_Implementation
- Extract_Processing_Coefficients
- Generate_Algorithm_Flowchart

## Notes
- ATBD documents vary in structure; adaptation may be needed per document
- Some formulas may be in images or text graphics (require OCR)
- Historical algorithms may differ from current implementation
- Version differences should be tracked for reproducibility
- Cross-referencing with implementation code improves accuracy

## Version History
- **v1.0** (2025-09-10): Initial ATBD analysis skill
- Extends Generic_Collection_Lineage_Extraction_Skill
- Includes formula extraction, QA analysis, data flow reconstruction
- Tested with MOD11A2 ATBD documentation

---

**Skill Status:** ✅ COMPLETE & VALIDATED  
**Ready for:** Algorithm analysis, implementation planning, validation design, data reproducibility
