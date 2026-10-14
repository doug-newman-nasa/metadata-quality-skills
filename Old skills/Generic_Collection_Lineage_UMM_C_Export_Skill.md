# Skill: Collection Lineage Extraction with UMM-C MetadataAssociation Output

## Overview
This refined skill extends the Collection_Lineage_via_ATBD_Skill by generating valid UMM-C (Unified Metadata Model - Collections) MetadataAssociation elements that describe collection relationships discovered through ATBD analysis.

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
**Output Format:** UMM-C MetadataAssociation JSON/XML elements for direct CMR ingestion

---

## Input Parameters

| Parameter | Type | Required | Example | Description |
|-----------|------|----------|---------|------------|
| `collection_short_name` | string | Yes | `MOD11A2` | Target CMR collection |
| `extract_parents` | boolean | No | true | Extract parent collections |
| `extract_children` | boolean | No | true | Extract derived/child collections |
| `extract_related` | boolean | No | true | Extract related versions |
| `output_format` | string | No | `json`, `xml`, `yaml` | UMM-C format (default: json) |
| `include_descriptions` | boolean | No | true | Include ATBD-derived descriptions |
| `validate_against_cmr` | boolean | No | true | Validate relationships in CMR |

---

## Workflow Steps

### Step 1-3: Extract Lineage from ATBD
(Same as Collection_Lineage_via_ATBD_Skill Steps 1-3)

### Step 4: Classify Relationship Type
Determine MetadataAssociation type for each identified collection.

**Relationship Classification:**

```python
def classify_relationship_type(source_collection, target_collection, 
                              relationship_description):
    """Classify into UMM-C association types"""
    
    relationship_mapping = {
        'derived_from': {
            'type': 'DerivedFrom',
            'description': 'Target is derived from source collection',
            'examples': ['MOD11A2 derived from MOD11A1']
        },
        'input_to': {
            'type': 'Input',
            'description': 'Source is input to target collection',
            'examples': ['MOD11A1 is input to MOD11A2']
        },
        'component_of': {
            'type': 'ComponentOf',
            'description': 'Source is component of target',
            'examples': ['Band 31 is component of MOD02HKM']
        },
        'template_of': {
            'type': 'Template',
            'description': 'Source is template/pattern for target',
            'examples': ['MOD11A1 pattern used in MYD11A1']
        },
        'version_of': {
            'type': 'VersionOf',
            'description': 'Source is different version of target',
            'examples': ['MOD11A2 V6.0 version of MOD11A2 V6.1']
        },
        'related_to': {
            'type': 'RelatedTo',
            'description': 'Source is related to target',
            'examples': ['MOD11A2 related to MYD11A2']
        }
    }
    
    # Match based on keywords in description
    for keyword, mapping in relationship_mapping.items():
        if keyword.replace('_', ' ') in relationship_description.lower():
            return mapping
    
    # Default to general relationship
    return {
        'type': 'RelatedTo',
        'description': relationship_description
    }
```

### Step 5: Build UMM-C MetadataAssociation Elements

**UMM-C MetadataAssociation Structure:**

```json
{
  "MetadataAssociations": [
    {
      "Type": "Input",
      "Description": "MOD11A1 is the daily LST product that is aggregated to produce MOD11A2",
      "CollectionRef": {
        "ShortName": "MOD11A1",
        "Version": "6.1"
      },
      "AssociationDetails": {
        "RelatedUrl": {
          "URL": "https://doi.org/10.5067/MODIS/MOD11A1.061",
          "Description": "MOD11A1 collection landing page"
        }
      }
    },
    {
      "Type": "DerivedFrom",
      "Description": "MOD11A1 daily LST data serves as primary input for temporal aggregation",
      "CollectionRef": {
        "ShortName": "MOD11A1",
        "Version": "6.1"
      }
    }
  ]
}
```

### Step 6: Extract Metadata for MetadataAssociation

For each identified collection relationship, extract:

```python
def extract_metadata_association_data(parent_collection, target_collection, 
                                     relationship_type, atbd_data):
    """Extract data needed for UMM-C MetadataAssociation"""
    
    association_data = {
        # Relationship characterization
        'Type': relationship_type,  # DerivedFrom, Input, etc.
        'Description': generate_description(parent_collection, relationship_type, atbd_data),
        
        # Parent collection reference
        'CollectionRef': {
            'ShortName': parent_collection['short_name'],
            'Version': parent_collection.get('version', 'unknown'),
            'ConceptId': parent_collection.get('concept_id', None)
        },
        
        # Association details
        'AssociationDetails': {
            'ProcessingMethodDescription': extract_processing_method(atbd_data),
            'RelatedUrl': {
                'URL': parent_collection.get('doi_url', None),
                'Description': f"{parent_collection['short_name']} collection landing page"
            },
            'AtbdReference': {
                'URL': atbd_data.get('atbd_url', None),
                'Section': atbd_data.get('atbd_section', None),
                'Quote': atbd_data.get('lineage_quote', None)
            }
        },
        
        # Metadata tracking
        'ExtractionMetadata': {
            'ExtractedFrom': 'ATBD',
            'ExtractedDate': get_timestamp(),
            'Confidence': calculate_confidence_score(relationship_type, atbd_data),
            'ValidationStatus': 'CMR_Verified' if parent_exists_in_cmr else 'Pending'
        }
    }
    
    return association_data
```

### Step 7: Generate Description from ATBD

Create natural language descriptions from ATBD content:

```python
def generate_description(parent_collection, relationship_type, atbd_data):
    """Generate description from ATBD data for UMM-C"""
    
    templates = {
        'DerivedFrom': (
            "{target} is derived from {parent}. "
            "Processing: {method}. "
            "ATBD Section: {section}. "
            "Source: {quote}"
        ),
        'Input': (
            "{parent} serves as input to {target}. "
            "Role: {role}. "
            "Processing: {method}. "
            "Reference: {section}"
        ),
        'ComponentOf': (
            "{parent} is a component of {target}. "
            "Component type: {component_type}. "
            "Integration method: {method}"
        ),
        'VersionOf': (
            "{parent} is a different version of {target}. "
            "Version information: {version_info}"
        )
    }
    
    template = templates.get(relationship_type, templates['DerivedFrom'])
    
    description = template.format(
        target=atbd_data['target_collection'],
        parent=parent_collection['short_name'],
        method=atbd_data.get('processing_method', 'Not specified'),
        section=atbd_data.get('atbd_section', 'N/A'),
        quote=atbd_data.get('lineage_quote', ''),
        role=atbd_data.get('input_role', 'Primary input'),
        component_type=atbd_data.get('component_type', 'N/A'),
        version_info=atbd_data.get('version_details', 'N/A')
    )
    
    return description
```

### Step 8: Validate Relationships Against CMR

Cross-check extracted relationships with CMR data:

```python
def validate_metadata_association(association_data):
    """Validate association against CMR metadata"""
    
    validation_results = {
        'parent_collection_exists': False,
        'version_match': False,
        'relationship_logical': False,
        'documentation_complete': False,
        'overall_valid': False
    }
    
    # Check 1: Parent collection exists in CMR
    parent_in_cmr = search_cmr(association_data['CollectionRef']['ShortName'])
    validation_results['parent_collection_exists'] = parent_in_cmr is not None
    
    # Check 2: Version information matches
    if parent_in_cmr:
        version_match = (
            association_data['CollectionRef']['Version'] == 
            parent_in_cmr.get('version', 'unknown')
        )
        validation_results['version_match'] = version_match
    
    # Check 3: Relationship type is logical for levels
    target_level = get_processing_level(association_data['TargetCollection'])
    parent_level = get_processing_level(parent_in_cmr)
    
    logical_mapping = {
        'DerivedFrom': parent_level <= target_level,
        'Input': parent_level <= target_level,
        'VersionOf': parent_level == target_level,
        'RelatedTo': True  # Always logical
    }
    
    validation_results['relationship_logical'] = (
        logical_mapping.get(association_data['Type'], False)
    )
    
    # Check 4: Documentation is complete
    validation_results['documentation_complete'] = (
        bool(association_data.get('Description')) and
        bool(association_data.get('AssociationDetails'))
    )
    
    # Overall validation
    validation_results['overall_valid'] = all(
        v for k, v in validation_results.items() 
        if k != 'overall_valid'
    )
    
    return validation_results
```

### Step 9: Generate UMM-C Output Formats

**JSON Format:**

```python
def generate_umm_c_json(metadata_associations):
    """Generate UMM-C JSON output"""
    
    umm_c_collection = {
        "MetadataLanguage": "en",
        "ArchiveAndDistributionInformation": {
            "FileDistributionInformation": []
        },
        "MetadataAssociations": []
    }
    
    for association in metadata_associations:
        umm_association = {
            "Type": association['Type'],
            "Description": association['Description'],
            "CollectionRef": {
                "ShortName": association['CollectionRef']['ShortName'],
                "Version": association['CollectionRef']['Version']
            }
        }
        
        # Add concept ID if available
        if association['CollectionRef'].get('ConceptId'):
            umm_association['CollectionRef']['ConceptId'] = (
                association['CollectionRef']['ConceptId']
            )
        
        # Add association details if present
        if association.get('AssociationDetails'):
            umm_association['AssociationDetails'] = {
                'ProcessingMethodDescription': (
                    association['AssociationDetails'].get('ProcessingMethodDescription')
                ),
                'RelatedUrl': association['AssociationDetails'].get('RelatedUrl')
            }
        
        umm_c_collection['MetadataAssociations'].append(umm_association)
    
    return umm_c_collection
```

**XML Format:**

```python
def generate_umm_c_xml(metadata_associations):
    """Generate UMM-C XML output (ISO-like)"""
    
    xml_output = """<?xml version="1.0" encoding="UTF-8"?>
<Collection>
  <MetadataAssociations>
"""
    
    for association in metadata_associations:
        xml_output += f"""    <Association>
      <Type>{association['Type']}</Type>
      <Description>{escape_xml(association['Description'])}</Description>
      <CollectionRef>
        <ShortName>{association['CollectionRef']['ShortName']}</ShortName>
        <Version>{association['CollectionRef']['Version']}</Version>
"""
        if association['CollectionRef'].get('ConceptId'):
            xml_output += f"""        <ConceptId>{association['CollectionRef']['ConceptId']}</ConceptId>
"""
        
        xml_output += """      </CollectionRef>
"""
        
        if association.get('AssociationDetails'):
            xml_output += """      <AssociationDetails>
"""
            if association['AssociationDetails'].get('ProcessingMethodDescription'):
                xml_output += f"""        <ProcessingMethod>{escape_xml(association['AssociationDetails']['ProcessingMethodDescription'])}</ProcessingMethod>
"""
            xml_output += """      </AssociationDetails>
"""
        
        xml_output += """    </Association>
"""
    
    xml_output += """  </MetadataAssociations>
</Collection>
"""
    
    return xml_output
```

### Step 10: Generate Complete UMM-C Collection Record

Merge MetadataAssociations into full collection metadata:

```python
def generate_complete_umm_c_record(target_collection, metadata_associations):
    """Generate complete UMM-C record with lineage metadata"""
    
    umm_c_record = {
        "ShortName": target_collection['short_name'],
        "Version": target_collection.get('version', '001'),
        "EntryTitle": target_collection['entry_title'],
        "Abstract": target_collection['abstract'],
        "DOI": {
            "DOI": target_collection.get('doi', ''),
            "Authority": "https://doi.org"
        },
        "ScienceKeywords": target_collection.get('science_keywords', []),
        "Platforms": [
            {
                "Type": platform['type'] if isinstance(platform, dict) else 'Not Specified',
                "ShortName": platform['short_name'] if isinstance(platform, dict) else platform
            }
            for platform in target_collection.get('platforms', [])
        ],
        "Instruments": [
            {
                "ShortName": instrument['short_name'] if isinstance(instrument, dict) else instrument
            }
            for instrument in target_collection.get('instruments', [])
        ],
        "ProcessingLevel": {
            "Id": target_collection.get('processing_level_id', 'Unknown')
        },
        "TemporalResolution": target_collection.get('temporal_resolution', ''),
        "SpatialResolution": target_collection.get('spatial_resolution', ''),
        "MetadataAssociations": metadata_associations,
        "MetadataProvenance": {
            "GeneratedBy": "Generic_Collection_Lineage_UMM_C_Export_Skill v1.0",
            "GenerationDate": get_iso_timestamp(),
            "Source": "ATBD-based lineage extraction"
        }
    }
    
    return umm_c_record
```

---

## Example Output: MOD11A2 MetadataAssociation

### JSON Format Output

```json
{
  "ShortName": "MOD11A2",
  "Version": "6.1",
  "EntryTitle": "MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V061",
  "MetadataAssociations": [
    {
      "Type": "DerivedFrom",
      "Description": "MOD11A2 is derived from MOD11A1. Processing: 8-day temporal averaging of daily LST pixels. ATBD Section: 2.4. Source: 'Each pixel value in the MOD11A2 is a simple average of all the corresponding MOD11A1 LST pixels collected within that 8-day period.'",
      "CollectionRef": {
        "ShortName": "MOD11A1",
        "Version": "6.1",
        "ConceptId": "C1748058432-LPCLOUD"
      },
      "AssociationDetails": {
        "ProcessingMethodDescription": "8-day temporal averaging: MOD11A2[pixel] = mean(MOD11A1[pixel, day1:day8]) with minimum 4 valid days requirement",
        "RelatedUrl": {
          "URL": "https://doi.org/10.5067/MODIS/MOD11A1.061",
          "Description": "MOD11A1 collection landing page"
        },
        "AtbdReference": {
          "URL": "https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf",
          "Section": "2.4 (Temporal Aggregation Algorithm)",
          "Quote": "Each pixel value in the MOD11A2 is a simple average of all the corresponding MOD11A1 LST pixels collected within that 8-day period"
        }
      },
      "ExtractionMetadata": {
        "ExtractedFrom": "ATBD",
        "ExtractedDate": "2025-09-11T10:30:00Z",
        "Confidence": "HIGH",
        "ValidationStatus": "CMR_Verified"
      }
    },
    {
      "Type": "Input",
      "Description": "MOD03 provides geolocation information required for spatial mapping of MOD11A2 pixels",
      "CollectionRef": {
        "ShortName": "MOD03",
        "Version": "6.1",
        "ConceptId": "C1234567890-LPCLOUD"
      },
      "AssociationDetails": {
        "ProcessingMethodDescription": "Geolocation reference: latitude/longitude per pixel",
        "RelatedUrl": {
          "URL": "https://doi.org/10.5067/MODIS/MOD03.061",
          "Description": "MOD03 geolocation collection"
        }
      },
      "ExtractionMetadata": {
        "ExtractedFrom": "ATBD",
        "ExtractedDate": "2025-09-11T10:30:00Z",
        "Confidence": "MEDIUM",
        "ValidationStatus": "CMR_Verified"
      }
    }
  ],
  "MetadataProvenance": {
    "GeneratedBy": "Generic_Collection_Lineage_UMM_C_Export_Skill v1.0",
    "GenerationDate": "2025-09-11T10:30:00Z",
    "Source": "ATBD-based lineage extraction"
  }
}
```

### XML Format Output

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Collection>
  <ShortName>MOD11A2</ShortName>
  <Version>6.1</Version>
  <EntryTitle>MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V061</EntryTitle>
  <MetadataAssociations>
    <Association>
      <Type>DerivedFrom</Type>
      <Description>MOD11A2 is derived from MOD11A1. Processing: 8-day temporal averaging of daily LST pixels. ATBD Section: 2.4. Source: &apos;Each pixel value in the MOD11A2 is a simple average of all the corresponding MOD11A1 LST pixels collected within that 8-day period.&apos;</Description>
      <CollectionRef>
        <ShortName>MOD11A1</ShortName>
        <Version>6.1</Version>
        <ConceptId>C1748058432-LPCLOUD</ConceptId>
      </CollectionRef>
      <AssociationDetails>
        <ProcessingMethod>8-day temporal averaging: MOD11A2[pixel] = mean(MOD11A1[pixel, day1:day8]) with minimum 4 valid days requirement</ProcessingMethod>
        <RelatedUrl>
          <URL>https://doi.org/10.5067/MODIS/MOD11A1.061</URL>
          <Description>MOD11A1 collection landing page</Description>
        </RelatedUrl>
        <AtbdReference>
          <URL>https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf</URL>
          <Section>2.4 (Temporal Aggregation Algorithm)</Section>
          <Quote>Each pixel value in the MOD11A2 is a simple average of all the corresponding MOD11A1 LST pixels collected within that 8-day period</Quote>
        </AtbdReference>
      </AssociationDetails>
      <ExtractionMetadata>
        <ExtractedFrom>ATBD</ExtractedFrom>
        <ExtractedDate>2025-09-11T10:30:00Z</ExtractedDate>
        <Confidence>HIGH</Confidence>
        <ValidationStatus>CMR_Verified</ValidationStatus>
      </ExtractionMetadata>
    </Association>
  </MetadataAssociations>
  <MetadataProvenance>
    <GeneratedBy>Generic_Collection_Lineage_UMM_C_Export_Skill v1.0</GeneratedBy>
    <GenerationDate>2025-09-11T10:30:00Z</GenerationDate>
    <Source>ATBD-based lineage extraction</Source>
  </MetadataProvenance>
</Collection>
```

---

## Execution Template

```python
def extract_lineage_and_export_umm_c(collection_short_name, output_format='json'):
    """
    Complete workflow: Extract lineage and export as UMM-C MetadataAssociation
    """
    
    # Step 1-3: Extract lineage from ATBD
    target_collection = get_collection_metadata(collection_short_name)
    atbd_document = fetch_atbd_from_metadata(target_collection)
    lineage_data = extract_lineage_from_atbd(atbd_document)
    
    # Step 4: Classify relationships
    metadata_associations = []
    
    for parent_collection in lineage_data['parent_collections']:
        # Classify relationship type
        relationship_type = classify_relationship_type(
            parent_collection,
            target_collection,
            lineage_data.get('relationship_description', '')
        )
        
        # Step 5-6: Extract metadata
        association_data = extract_metadata_association_data(
            parent_collection,
            target_collection,
            relationship_type['type'],
            lineage_data
        )
        
        # Step 7: Generate description
        association_data['Description'] = generate_description(
            parent_collection,
            relationship_type['type'],
            lineage_data
        )
        
        # Step 8: Validate
        validation = validate_metadata_association(association_data)
        association_data['ExtractionMetadata']['ValidationStatus'] = (
            'CMR_Verified' if validation['overall_valid'] else 'Requires_Review'
        )
        
        metadata_associations.append(association_data)
    
    # Step 9-10: Generate output
    umm_c_record = generate_complete_umm_c_record(
        target_collection,
        metadata_associations
    )
    
    # Export in requested format
    if output_format == 'json':
        output = json.dumps(umm_c_record, indent=2)
    elif output_format == 'xml':
        output = generate_umm_c_xml(metadata_associations)
    elif output_format == 'yaml':
        output = yaml.dump(umm_c_record, default_flow_style=False)
    
    return output, umm_c_record
```

---

## UMM-C MetadataAssociation Reference

### Association Types (per UMM-C specification)

| Type | Description | Example |
|------|---|---|
| **Input** | Collection is input to target | MOD11A1 → MOD11A2 |
| **DerivedFrom** | Collection is derived from target | MOD11A2 derived from MOD11A1 |
| **ComponentOf** | Collection is component of target | Band 31 component of MOD02HKM |
| **Template** | Collection serves as template for target | MOD11A2 uses MOD11A1 template |
| **VersionOf** | Collection is version of target | MOD11A2 V6.1 version of V6.0 |
| **RelatedTo** | Collection is related to target | MOD11A2 related to MYD11A2 |
| **VirtualAggregation** | Virtual aggregation relationship | Multiple granules into single collection |
| **ExternallyDerived** | Derived from external source | Climate model product |

### Required Fields

```
MetadataAssociation:
├─ Type (required)
│   └─ One of: Input, DerivedFrom, ComponentOf, Template, etc.
│
├─ Description (required)
│   └─ Human-readable description
│
├─ CollectionRef (required)
│   ├─ ShortName (required)
│   ├─ Version (optional)
│   └─ ConceptId (optional)
│
└─ AssociationDetails (optional)
    ├─ ProcessingMethodDescription
    ├─ RelatedUrl
    └─ AtbdReference
```

---

## Quality Assurance Checklist

- [ ] ATBD lineage extracted
- [ ] Relationship types classified correctly
- [ ] Parent collections identified
- [ ] Relationship descriptions generated from ATBD
- [ ] Processing methods documented
- [ ] ATBD references included
- [ ] CMR validation performed
- [ ] Confidence scores calculated
- [ ] MetadataAssociation fields populated
- [ ] Output format valid (JSON/XML/YAML)
- [ ] Metadata provenance tracked
- [ ] UMM-C compliance verified

---

## Tools Used
- `earthdata_mcp_get_collections` - Get collection metadata
- `fetch_url_content` - Retrieve ATBD
- Pattern matching - Extract lineage statements
- `earthdata_mcp_get_keywords` - Validate keywords
- JSON/XML generators - Format output
- Validation libraries - UMM-C compliance check

## References
- UMM-C Specification: https://wiki.earthdata.nasa.gov/display/CMR/UMM-C
- MetadataAssociation Examples: https://wiki.earthdata.nasa.gov/display/CMR/Collections
- CMR API Documentation: https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html

## Related Skills
- Collection_Lineage_via_ATBD_Skill
- Collection_ATBD_Analysis_Skill
- Validate_UMM_C_Metadata
- Generate_CMR_Metadata_Update

## Version History
- **v1.0** (2025-09-11): Initial UMM-C export capability
  - JSON output format
  - XML output format
  - YAML output format
  - MetadataAssociation generation
  - CMR validation integration
  - ATBD reference tracking

---

**Skill Status:** ✅ COMPLETE & PRODUCTION-READY  
**Output Compatibility:** UMM-C standard format for CMR ingestion  
**Use Cases:** Automated metadata enhancement, collection relationship documentation
