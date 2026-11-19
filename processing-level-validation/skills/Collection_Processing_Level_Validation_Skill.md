# Skill: Collection Processing Level Validation via ATBD and User Guides

## Overview
This skill validates the `ProcessingLevel` declared in a collection's CMR metadata. It retrieves the collection with the Earthdata MCP `get_collections` tool, finds any Algorithm Theoretical Basis Documents (ATBDs) and User Guides in the collection's `related_urls`, and reads those documents for evidence of the true processing level. It then compares that evidence with the declared `processing_level_id`. The result is a verdict (CONFIRMED, MISMATCH, AMBIGUOUS, or UNVERIFIABLE), a recommended level, and quoted evidence a metadata curator can act on.

**Skill Type:** Metadata Quality Validation & Documentation Analysis
**Difficulty Level:** Intermediate
**Complementary Skills:** Collection_ATBD_Analysis_Skill, Generic_Collection_Keyword_Extraction_Skill, Collection_Lineage_via_ATBD_Skill
**Use Cases:**
- Finding collections whose declared processing level is missing, malformed, or wrong
- Normalizing non-standard level values (e.g., `"Level 3"`, `"L3"`, `"3"`, `"NA"`)
- Supporting metadata curation and UMM-C correction requests
- Checking consistency across a product family (e.g., L1B → L2 → L3 → L4)

## Prerequisites
- Access to the Earthdata MCP server (`get_collections`)
- Ability to fetch documents by URL (`WebFetch`, or a PDF reader for PDF ATBDs)
- A target collection short name (and version) or a CMR concept ID
- Familiarity with the NASA EOSDIS data processing level definitions (below)

## Input Parameters

| Parameter | Type | Required | Example | Description |
|-----------|------|----------|---------|-------------|
| `collection_short_name` | string | One of these two | `MOD11A2` | CMR collection short name |
| `concept_id` | string | One of these two | `C2269056084-LPCLOUD` | Exact CMR collection concept ID (preferred when known) |
| `version` | string | No | `061` | Used to disambiguate when several versions are returned |
| `include_general_documentation` | boolean | No | `true` | Also inspect `GENERAL DOCUMENTATION`, `PRODUCT HISTORY`, and `DATA SET LANDING PAGE` links when no ATBD or User Guide exists (default: `true`) |
| `output_format` | string | No | `markdown` | `markdown` or `structured_json` |

---

## Reference: NASA EOSDIS Data Processing Levels

Use these definitions (from NASA Earthdata, *Data Processing Levels*) as the classification rubric.

| Level | Definition | Typical Document Signals |
|-------|-----------|--------------------------|
| **Level 0** | Reconstructed, unprocessed instrument and payload data at full resolution, with all communication artifacts (sync frames, headers, duplicates) removed. | "raw telemetry", "instrument packets", "CCSDS packets", "unprocessed", "Level 0 data" |
| **Level 1A** | Reconstructed, unprocessed instrument data at full resolution, time-referenced and annotated with ancillary information (radiometric and geometric calibration coefficients, georeferencing parameters) that is *computed and appended but not applied*. | "raw counts", "digital numbers (DN)", "calibration coefficients appended", "not applied" |
| **Level 1B** | Level 1A data that have been processed to sensor units (e.g., radar backscatter cross section, brightness temperature). Not all instruments have Level 1B data. | "calibrated radiance", "brightness temperature", "sensor units", "geolocated", "top-of-atmosphere (TOA) radiance/reflectance" |
| **Level 1C** | Level 1B data that include new variables to describe the spectra; resampled, or orthorectified onto a common grid (used by some missions, e.g., Sentinel-2, GPM). | "resampled", "orthorectified TOA reflectance", "intercalibrated brightness temperatures" |
| **Level 2** | Derived geophysical variables at the same resolution and location as the Level 1 source data, in the native swath / observation geometry. | "retrieved", "geophysical parameter", "per-pixel retrieval", "swath", "orbit", "granule = 5-minute scene", "same resolution as L1B" |
| **Level 2A/2B** | Mission-specific subdivisions of Level 2 (e.g., surface reflectance vs. derived products). Treat as Level 2 for validation unless the mission defines them. | Mission-specific naming |
| **Level 3** | Variables mapped on uniform space-time grid scales, usually with some completeness and consistency (e.g., missing points interpolated, complete regions mosaicked from multiple orbits). | "gridded", "composite", "daily/8-day/monthly average", "mosaic", "mapped to a global grid", "sinusoidal grid", "CMG", "binned" |
| **Level 4** | Model output or results from analyses of lower-level data (i.e., variables not directly measured by the instruments, but derived from those measurements), often through data assimilation. | "model output", "data assimilation", "reanalysis", "land surface model", "derived from multiple sensors and models", "value-added analysis" |

**Key discriminators** (the most common sources of misclassification):
- **L1B vs. L2:** L1B stays in *sensor units* (radiance, brightness temperature, backscatter). L2 converts those to *geophysical variables* (temperature, reflectance after atmospheric correction, soil moisture, aerosol optical depth).
- **L2 vs. L3:** L2 keeps the *native swath or observation geometry*. L3 is *resampled onto a regular space-time grid*. A gridded L2 product ("L2G") is still usually declared L2 by the mission, so record it as a note rather than a mismatch.
- **L3 vs. L4:** L3 is a gridded version of *observed* variables. L4 adds *model or assimilation* steps, or estimates variables the instrument cannot observe directly.

---

## Workflow Steps

### Step 1: Retrieve the Collection Metadata
Use the Earthdata MCP `get_collections` tool.

**Tool:** `get_collections`

```
# Preferred: exact lookup
get_collections(concept_id="C2269056084-LPCLOUD")

# Otherwise: short name lookup
get_collections(short_name="MOD11A2")
```

If more than one collection is returned (several versions or providers), pick the one that matches `version`. If no version was given, pick the latest active one (`collection_progress = ACTIVE`) and record the choice in the report.

**Fields to capture from the response:**

| Field | Purpose |
|-------|---------|
| `concept_id`, `short_name`, `version`, `provider_id` | Identify the collection |
| `processing_level_id` | **The declared value under test** |
| `entry_title` | Often contains an embedded level (e.g., "8-Day **L3** Global 1km") |
| `abstract` | Secondary evidence (e.g., "gridded", "average of daily") |
| `spatial_resolution`, `temporal_resolution` | Supporting evidence (grids and composite periods suggest L3+) |
| `instruments`, `platforms` | Context for interpreting mission-specific level schemes |
| `related_urls` | **Source of ATBD and User Guide links** |

If the collection cannot be found, stop and report `UNVERIFIABLE` with the reason `COLLECTION_NOT_FOUND`.

### Step 2: Normalize the Declared Processing Level
CMR `processing_level_id` is free text, and providers store it inconsistently. Normalize it before comparing.

| Raw Value Examples | Normalized |
|--------------------|-----------|
| `0`, `L0`, `Level 0` | `0` |
| `1A`, `L1A`, `Level 1A` | `1A` |
| `1B`, `L1B`, `Level 1B` | `1B` |
| `1`, `L1`, `Level 1` | `1` (flag: sub-level unspecified) |
| `1C`, `L1C` | `1C` |
| `2`, `L2`, `Level 2`, `2A`, `2B`, `L2G` | `2` (keep the suffix as a note) |
| `3`, `L3`, `Level 3`, `3A` | `3` |
| `4`, `L4`, `Level 4` | `4` |
| `NA`, `Not Provided`, `N/A`, empty, missing | `MISSING` |
| Anything else | `NON_STANDARD` (record the raw value) |

```python
import re

def normalize_level(raw):
    if raw is None or str(raw).strip().upper() in {"", "NA", "N/A", "NOT PROVIDED", "NOT APPLICABLE"}:
        return "MISSING", None
    m = re.fullmatch(r"\s*(?:LEVEL|L)?\s*-?\s*([0-4])\s*([A-C]|G)?\s*", str(raw).upper())
    if not m:
        return "NON_STANDARD", raw
    level, suffix = m.group(1), m.group(2)
    if level == "1" and suffix in {"A", "B", "C"}:
        return f"1{suffix}", None
    return level, suffix  # suffix kept as a note (e.g., 2A, L2G)
```

Also pull any level that appears in `entry_title` (regex `\bL(?:evel)?\s?([0-4][A-C]?)\b`) and record it as `title_level`. A disagreement between `title_level` and `processing_level_id` is a finding in itself.

### Step 3: Identify ATBDs and User Guides in `related_urls`
Filter `related_urls` by `type` and `subtype`. Rank sources by how authoritative they are:

| Priority | `type` | `subtype` | Document Class |
|----------|--------|-----------|----------------|
| 1 | `VIEW RELATED INFORMATION` | `ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)` | ATBD |
| 2 | `VIEW RELATED INFORMATION` | `USER'S GUIDE` | User Guide |
| 3 | `VIEW RELATED INFORMATION` | `PRODUCT USAGE`, `DATA PRODUCT SPECIFICATION`, `READ-ME` | Product documentation |
| 4 | `VIEW RELATED INFORMATION` | `GENERAL DOCUMENTATION`, `PRODUCT HISTORY` | General docs (only if `include_general_documentation`) |
| 5 | `DATA SET LANDING PAGE` | any | Landing page (only if `include_general_documentation`, and mainly to find ATBD/User Guide links that are not in CMR) |

Also check the `description` text and the URL itself for `ATBD`, `Algorithm Theoretical Basis`, `User Guide`, `User's Guide`, or `Users_Guide`, because providers sometimes mis-tag the subtype.

```python
DOC_PRIORITY = {
    "ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)": ("ATBD", 1),
    "USER'S GUIDE": ("USER_GUIDE", 2),
    "PRODUCT USAGE": ("PRODUCT_DOC", 3),
    "DATA PRODUCT SPECIFICATION": ("PRODUCT_DOC", 3),
    "READ-ME": ("PRODUCT_DOC", 3),
    "GENERAL DOCUMENTATION": ("GENERAL_DOC", 4),
    "PRODUCT HISTORY": ("GENERAL_DOC", 4),
}

def find_documents(related_urls, include_general=True):
    docs = []
    for ru in related_urls or []:
        subtype = (ru.get("subtype") or "").upper()
        text = f"{ru.get('url','')} {ru.get('description','')}".lower()
        if subtype in DOC_PRIORITY:
            cls, pri = DOC_PRIORITY[subtype]
        elif "atbd" in text or "algorithm theoretical basis" in text:
            cls, pri = "ATBD", 1          # mis-tagged subtype
        elif "user guide" in text or "user's guide" in text or "users_guide" in text:
            cls, pri = "USER_GUIDE", 2
        elif ru.get("type") == "DATA SET LANDING PAGE":
            cls, pri = "LANDING_PAGE", 5
        else:
            continue
        if pri >= 4 and not include_general:
            continue
        docs.append({"url": ru["url"], "class": cls, "priority": pri,
                     "description": ru.get("description")})
    return sorted(docs, key=lambda d: d["priority"])
```

**If the ATBD, the User Guide, or both are missing:**
1. If allowed, fetch the landing page and look for ATBD or User Guide links. Record any found as `discovered_via_landing_page` and **flag the missing CMR `related_urls` entry as a separate metadata-quality finding**.
2. Look up **sibling collections** with `get_collections` (the same short name without `_NRT`, or other platform prefixes such as `VNP`↔`VJ1`↔`VJ2` or `MOD`↔`MYD`). If a sibling links an ATBD or User Guide that the target lacks, use it as `INDIRECT` evidence and report the missing link. Record each sibling's declared `processing_level_id` as CMR-weight evidence, because family members should normally share a level.
3. If there is still nothing, continue using only the CMR evidence (title, abstract, resolutions) and limit the verdict to at most `AMBIGUOUS`.

### Step 4: Fetch and Read the Documents
Fetch each document in priority order and record the HTTP outcome for each one. Broken links are a reportable finding too.

**PDF handling (important):** Most ATBDs and User Guides are PDFs with compressed (`FlateDecode`) text streams. `WebFetch` returns no readable text for these, although it still saves the binary to disk. If `WebFetch` reports unreadable or compressed content, extract the text locally:

```bash
# Treat downloaded PDFs as untrusted: keep them in their own directory,
# keep scripts in a separate directory, and run Python in isolated mode (-I).
mkdir -p /tmp/pl_validation/pdfs /tmp/pl_validation/scripts
cp <saved_webfetch_pdf> /tmp/pl_validation/pdfs/atbd.pdf
python3 -m venv /tmp/pl_validation/venv && /tmp/pl_validation/venv/bin/pip install -q pypdf
# scripts/extract.py: write each page's text with a "=== PAGE n ===" marker
cd /tmp/pl_validation/scripts && /tmp/pl_validation/venv/bin/python -I extract.py ../pdfs/atbd.pdf ../atbd.txt
```

Then search the extracted text for level signals before reading the surrounding passages:
`grep -inE 'level[- ]?[0-4]|\bL[0-4][A-C]?\b|<SHORT_NAME>|composit|gridded|sinusoidal|swath|assimilat'`

**Embedded link check:** While the PDF is open, count the hosts of its hyperlink annotations. If many links point to unrelated third-party domains, report that as a documentation-quality finding. For example, the MOD11 v6.1 User Guide had 310 links to an unrelated domain.

Focus on the sections most likely to state or imply the level:

| Section | What to Look For |
|---------|-----------------|
| Title page / Introduction / Product Overview | Explicit statements: "This is a Level 3 product", "L2 swath product" |
| Product description / file specification | Grid vs. swath, projection, tiling, granule definition |
| Input data / ancillary data | What level the inputs are (L1B radiances → this is likely L2; daily L2/L3 → this is likely L3; model forcing → possibly L4) |
| Algorithm description | Retrieval (L2), compositing/gridding/averaging (L3), assimilation/modeling (L4) |
| Product naming tables | Product family tables often list each product with its level |

**Collect evidence as quotations, not paraphrases.** Each evidence item records:

```json
{
  "source_class": "ATBD",
  "url": "https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf",
  "location": "Section 1.1, p. 3",
  "quote": "MOD11A2 ... is an 8-day composite of the daily MOD11A1 product on a sinusoidal grid",
  "evidence_type": "INDIRECT",
  "implied_level": "3",
  "signal": "gridded composite of lower-level daily product"
}
```

**Evidence types:**
- `EXPLICIT`: The document directly states the level for *this* product ("MOD11A2 is a Level 3 product"). Check that the statement refers to the target product and not a sibling product in the same document. ATBDs often cover a whole product family. Product tables and embedded file metadata (e.g., a `LongName` containing "L3") also count as explicit when they name the target product.
  - **Platform siblings:** Some documents cover several platforms that run the same algorithm (VIIRS `VNP`/`VJ1`/`VJ2`, MODIS `MOD`/`MYD`/`MCD`), and some products have NRT variants (`_NRT`). If the *target collection's own `related_urls`* link to the document, and the named product differs from the target only by platform prefix or an `_NRT` suffix, score the statement as `EXPLICIT`. Add the note "platform-sibling attribution". In any other case, a statement about a sibling product is `INDIRECT`.
  - **Legacy names:** Older ATBDs often predate current short names. For example, the MOD11 ATBD v3.3 never says "MOD11A2" and calls the product `MOD.AM1.V2.lst_8dy.L3`. If a level is attached only to a legacy or internal name, score it as `INDIRECT` and explain the name mapping in a footnote.
- `INDIRECT`: The level is implied by processing characteristics (gridding, compositing, retrieval from radiances, model assimilation).
- `INPUT_BASED`: The level is inferred from the declared inputs (output level ≥ highest input level, and usually exactly one level above it for a single processing step).

### Step 5: Determine the Evidence-Based Processing Level
Weight the evidence and pick the best-supported level.

| Evidence | Weight |
|----------|--------|
| ATBD `EXPLICIT` statement for this product | 5 |
| User Guide `EXPLICIT` statement for this product | 4 |
| Product doc / general doc `EXPLICIT` statement | 3 |
| ATBD or User Guide `INDIRECT` evidence | 2 |
| `INPUT_BASED` inference | 2 |
| CMR `entry_title` level | 1 |
| CMR abstract / resolution signals | 1 |

```python
from collections import defaultdict

WEIGHTS = {("ATBD", "EXPLICIT"): 5, ("USER_GUIDE", "EXPLICIT"): 4,
           ("PRODUCT_DOC", "EXPLICIT"): 3, ("GENERAL_DOC", "EXPLICIT"): 3,
           ("LANDING_PAGE", "EXPLICIT"): 3}

def score_levels(evidence):
    scores = defaultdict(int)
    for e in evidence:
        w = WEIGHTS.get((e["source_class"], e["evidence_type"]))
        if w is None:
            w = 1 if e["source_class"] == "CMR" else 2
        scores[e["implied_level"]] += w
    return dict(scores)

def evidence_level(scores):
    if not scores:
        return None, 0.0
    ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    best, best_score = ranked[0]
    total = sum(scores.values())
    return best, best_score / total   # (level, share of total weight)
```

When comparing levels, treat `1` as matching `1A` / `1B` / `1C` (and record "sub-level unspecified"), and treat `2` as matching `2A` / `2B` / `2G`.

### Step 6: Assign a Verdict

| Verdict | Condition |
|---------|-----------|
| ✅ **CONFIRMED** | Evidence level equals the declared level, at least one `EXPLICIT` or two independent `INDIRECT` items from an ATBD or User Guide support it, and no ATBD or User Guide evidence contradicts it. |
| ❌ **MISMATCH** | Evidence level differs from the declared level, has ≥ 70% of the total evidence weight, and is supported by at least one ATBD or User Guide `EXPLICIT` item, *or* by at least three independent `INDIRECT` / `INPUT_BASED` items from the collection's documents. |
| ⚠️ **AMBIGUOUS** | Evidence conflicts (no level reaches 70% of the weight), *or* only CMR-internal evidence is available, *or* the declared level is `MISSING` / `NON_STANDARD` and the evidence is not strong enough for a MISMATCH-grade recommendation. |
| ⛔ **UNVERIFIABLE** | The collection was not found, or there are no usable documents *and* no CMR signals. |

**Special cases:**
- **Declared level `MISSING` or `NON_STANDARD`:** Always report it as a metadata-quality finding. If the evidence would meet the MISMATCH threshold, report the verdict as `MISMATCH` and give the recommended value.
- **Sub-level imprecision:** A declared `1` with evidence for `1B` is reported as `CONFIRMED` with a recommendation to add the sub-level.
- **Title vs. declared disagreement:** Always report this, even when the documents confirm the declared level (the title may need fixing instead).

**Confidence:**

| Confidence | Criteria |
|------------|----------|
| HIGH | ATBD or User Guide `EXPLICIT` evidence for this specific product, with no contradictions |
| MEDIUM | Several agreeing `INDIRECT` / `INPUT_BASED` items from documents, no explicit statement |
| LOW | Only CMR-internal evidence, or conflicting document evidence |

### Step 7: Produce the Report
Report findings for a curator. **Do not modify CMR metadata.** This skill only recommends changes.

#### Markdown Report Template

```markdown
# Processing Level Validation: [SHORT_NAME] v[VERSION]

**Concept ID:** [concept_id]  |  **Provider:** [provider_id]
**Verdict:** [✅ CONFIRMED | ❌ MISMATCH | ⚠️ AMBIGUOUS | ⛔ UNVERIFIABLE]  |  **Confidence:** [HIGH|MEDIUM|LOW]

| | Value |
|---|---|
| Declared `ProcessingLevel.Id` (raw) | [raw] |
| Declared (normalized) | [normalized] |
| Level in Entry Title | [title_level or "none"] |
| Evidence-based level | [level] ([share]% of evidence weight) |
| **Recommended `ProcessingLevel.Id`** | [value, or "no change"] |

## Documents Assessed
| Class | URL | Status | Used |
|---|---|---|---|
| ATBD | [url] | 200 OK | ✓ |
| User Guide | [url] | 200 OK | ✓ |

## Evidence
| # | Source | Location | Quote | Type | Implies |
|---|---|---|---|---|---|
| 1 | ATBD | §1.1 p.3 | "…" | INDIRECT | L3 |

## Findings
- [e.g., Declared level matches ATBD and User Guide evidence.]
- [e.g., Entry title says "L2" but declared level is "3".]
- [e.g., No ATBD link in CMR related_urls; ATBD found only via landing page.]
- [e.g., User Guide link returns 404.]

## Recommended Actions
- [e.g., Update UMM-C `ProcessingLevel.Id` from "NA" to "3".]
- [e.g., Add a RelatedUrl with Subtype "ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)".]
```

#### Structured JSON Output

```json
{
  "processing_level_validation": {
    "collection": {
      "concept_id": "C2269056084-LPCLOUD",
      "short_name": "MOD11A2",
      "version": "061",
      "provider_id": "LPCLOUD"
    },
    "declared": { "raw": "3", "normalized": "3", "title_level": "3" },
    "documents": [
      { "class": "ATBD", "url": "https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf", "status": "OK" },
      { "class": "USER_GUIDE", "url": "https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf", "status": "OK" }
    ],
    "evidence": [
      {
        "source_class": "USER_GUIDE",
        "location": "Product description",
        "quote": "<verbatim quote from document>",
        "evidence_type": "EXPLICIT",
        "implied_level": "3"
      }
    ],
    "level_scores": { "3": 9, "2": 0 },
    "evidence_level": "3",
    "verdict": "CONFIRMED",
    "confidence": "HIGH",
    "recommended_processing_level_id": null,
    "findings": [],
    "recommended_actions": []
  }
}
```

---

## Worked Example: MOD11A2 v061

**Step 1:** `get_collections(short_name="MOD11A2")` returns `C2269056084-LPCLOUD` with:
- `processing_level_id`: `"3"`
- `entry_title`: "MODIS/Terra Land Surface Temperature/Emissivity 8-Day **L3** Global 1km SIN Grid V061"
- `abstract`: "...Each pixel value in the MOD11A2 is a simple average of all the corresponding MOD11A1 LST pixels collected within that 8-day period..."
- `temporal_resolution`: `8 Day`; `spatial_resolution`: `1000x1000 Meters`

**Step 2:** Declared `"3"` normalizes to `3`. Title level is `3`. These agree.

**Step 3:** `related_urls` contains:
- ATBD: `https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf`
- User's Guide: `https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf`
- General Documentation (File Spec): `https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD11A2`

**Step 4:** `WebFetch` could not decode either PDF, so the text was extracted locally with pypdf (User Guide 37 pp., ATBD 77 pp.).

**Step 5 (actual evidence, run 2026-11-03):**

| Source | Location | Quote | Type | Weight |
|---|---|---|---|---|
| User Guide | p. 7, Table 1 | "MOD11A2 … L3 1200 rows by 1200 columns 1km (actual 0.928km) eight days Sinusoidal" | EXPLICIT | 4 |
| User Guide | p. 25, ArchiveMetadata | "LongName "MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid"" | EXPLICIT | 4 |
| User Guide | p. 7 | "MOD11A2, is an eight-day LST product by averaging from two to eight days of the MOD11A1 product" | INDIRECT | 2 |
| User Guide | p. 6–7 | Input MOD11A1 is listed as L3, and the operation is a temporal average | INPUT_BASED | 2 |
| ATBD | p. 53 | "MOD_PR11C MOD.AM1.V2.lst_8dy.L3" (legacy name; "MOD11A2" never appears) | INDIRECT | 2 |
| CMR | title / abstract | "8-Day L3 Global…", "simple average of … MOD11A1" | CMR | 1 + 1 |

**Step 6:** All 16 points of evidence weight are for L3, including explicit User Guide statements. The verdict is **✅ CONFIRMED, HIGH confidence**, with no change recommended. The run also found a separate documentation finding: 310 embedded links to an unrelated third-party domain in the User Guide PDF. Full report: [Reports/MOD11A2_Processing_Level_Validation_Report.md](../Reports/MOD11A2_Processing_Level_Validation_Report.md).

**Lessons from this run:** The User Guide, not the ATBD, was the decisive source. The ATBD is an at-launch document that uses legacy product names. PDF text extraction was required for both documents.

---

## Execution Template

```python
def validate_processing_level(short_name=None, concept_id=None, version=None,
                              include_general_documentation=True):
    # Step 1
    resp = get_collections(concept_id=concept_id) if concept_id \
        else get_collections(short_name=short_name)
    coll = select_collection(resp["collections"], version)
    if coll is None:
        return report(verdict="UNVERIFIABLE", reason="COLLECTION_NOT_FOUND")

    # Step 2
    declared, suffix = normalize_level(coll.get("processing_level_id"))
    title_level = extract_title_level(coll.get("entry_title", ""))

    # Step 3
    docs = find_documents(coll.get("related_urls"), include_general_documentation)

    # Step 4
    evidence = cmr_internal_evidence(coll, title_level)    # weight-1 signals
    for doc in docs:
        content, status = fetch_document(doc["url"])
        doc["status"] = status
        if content:
            evidence += extract_level_evidence(content, doc, coll["short_name"])

    # Step 5
    scores = score_levels(evidence)
    level, share = evidence_level(scores)

    # Step 6
    verdict, confidence = assign_verdict(declared, level, share, evidence)

    # Step 7
    return report(coll, declared, title_level, docs, evidence, scores,
                  level, verdict, confidence)
```

---

## Batch Mode
To validate many collections (e.g., every collection for an instrument or provider):
1. Use `get_collections` with `instrument`, `platform`, `provider`, or `keyword` filters and `has_granules=true`, paging with `next_cursor`.
2. Run Steps 2–3 for every collection first. These steps are cheap and need only CMR. Flag `MISSING` / `NON_STANDARD` levels and title disagreements right away.
3. Cache fetched documents by URL. Product families often share one ATBD (e.g., `MOD11_ATBD.pdf` covers MOD11A1, MOD11A2, MOD11B1, and MOD11C1–C3). Within one document, attribute each statement to the right product.
4. Produce a summary table: `concept_id, short_name, declared, evidence_level, verdict, confidence, recommended`.

---

## Quality Assurance Checklist

- [ ] Correct collection and version selected; selection recorded
- [ ] Declared `processing_level_id` captured raw and normalized
- [ ] Entry-title level extracted and compared
- [ ] All ATBD and User Guide `related_urls` identified (including mis-tagged subtypes)
- [ ] Each document fetched, with HTTP status recorded; broken links reported
- [ ] Evidence recorded as verbatim quotes with section/page locations
- [ ] Explicit statements checked against the *target* product, not a sibling product
- [ ] L1B/L2, L2/L3, and L3/L4 discriminators applied
- [ ] Verdict and confidence assigned per the rules in Step 6
- [ ] Recommended `ProcessingLevel.Id` given for MISMATCH / MISSING / NON_STANDARD
- [ ] Missing documentation links reported as separate findings
- [ ] No CMR metadata modified

---

## Tools Used
- `get_collections` (Earthdata MCP): retrieves collection metadata, `processing_level_id`, and `related_urls`
- `WebFetch`: retrieves HTML documents and landing pages, and saves PDF binaries to disk
- `pypdf` (in an isolated venv): extracts text and link annotations from PDF ATBDs and User Guides
- Regex / text analysis: normalizes levels and extracts evidence

## References
- NASA Earthdata, Data Processing Levels: https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/data-processing-levels
- UMM-C `ProcessingLevel` and `RelatedUrls` specification: https://www.earthdata.nasa.gov/unified-metadata-model-umm
- CMR Search API: https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html

## Related Skills
- Collection_ATBD_Analysis_Skill: deep ATBD parsing (inputs, algorithms, outputs)
- Collection_Lineage_via_ATBD_Skill: input collections, which support `INPUT_BASED` evidence
- Generic_Collection_Keyword_Extraction_Skill: a parallel metadata-quality skill for science keywords

## Notes
- Processing level schemes vary by mission (e.g., GPM 1C, SMAP L2/L3/L4, Sentinel-2 L1C/L2A). Accept a mission-defined level when the ATBD defines it, and note where it differs from the EOSDIS rubric.
- ATBDs are often older than the current product version. Prefer the User Guide for version-specific statements, and note when the two disagree.
- Scanned PDFs may need OCR. If a document cannot be read, record it as `UNREADABLE` rather than treating it as absent.

## Version History
- **v1.0** (2026-11-03): Initial processing level validation skill using `get_collections` and ATBD/User Guide evidence
- **v1.1** (2026-11-03): Tested on MOD11A2 v061 (CONFIRMED, HIGH). Added a local PDF text-extraction fallback, legacy product-name guidance, an embedded link check, and real worked-example evidence

- **v1.2** (2026-11-03): Tested on VJ209CMG_NRT (MISMATCH: declared 2, evidence L3). Added platform-sibling attribution, a sibling-collection lookup when documents are missing, and a MISMATCH path for three independent indirect items. Under v1.1, this case would have returned AMBIGUOUS despite unanimous L3 evidence

---

**Skill Status:** ✅ TESTED (MOD11A2: CONFIRMED; VJ209CMG_NRT: MISMATCH)
**Ready for:** Single-collection and batch processing level validation
