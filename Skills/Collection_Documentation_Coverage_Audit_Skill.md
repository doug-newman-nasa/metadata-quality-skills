# Skill: Collection Documentation Coverage Audit (ATBD & User's Guide)

## Overview
This skill audits a set of CMR collections, by default every collection in the EOSDIS consortium, to find which ones have no Algorithm Theoretical Basis Document (ATBD) and no User's Guide in their `RelatedUrls`. It fetches the full result set straight from the CMR Search API, excludes Level 0 collections, and puts each remaining collection into one coverage class. It then writes three outputs: a CSV of the collections that are missing both documents, a JSON summary, and a Markdown report broken down by provider, processing level, and data type.

**Skill Type:** Metadata Quality Audit (bulk / catalog-wide)
**Difficulty Level:** Beginner–Intermediate
**Complementary Skills:** Collection_Processing_Level_Validation_Skill, Collection_ATBD_Analysis_Skill, Collection_Lineage_via_ATBD_Skill
**Use Cases:**
- Measuring ATBD and User's Guide coverage across EOSDIS, or for a single DAAC
- Building per-provider worklists of collections that need documentation links
- Finding documents that exist but carry the wrong `Subtype` (mis-tagged links)
- Screening collections before running the ATBD-based skills, which need an ATBD or User's Guide to work

## Prerequisites
- Network access to `https://cmr.earthdata.nasa.gov` (public metadata, so no token is needed)
- Python 3 (standard library only)
- The Earthdata MCP tools are **not** suitable here: `get_collections` returns at most 10 results per call, while a catalog-wide audit covers about 11,000 records. Use MCP only to spot-check individual collections (Step 5).

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `cmr_filter` | list of `key=value` | No | `consortium=EOSDIS` | CMR collection search parameters that define the population. `consortium=EOSDIS` is how this skill decides whether a collection counts as ESDIS/EOSDIS. Add `provider=GES_DISC` (for example) to audit one DAAC. |
| `exclude_levels` | list | No | `["0"]` | Normalized processing levels to leave out of the audit |
| `required_subtypes` | list | No | `ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)`, `USER'S GUIDE` | A collection is **covered** if it has a RelatedUrl with either Subtype |
| `report_name` | string | No | `EOSDIS` | Prefix for the output files in `Reports/` |

> **Note on "ESDIS" vs. "EOSDIS":** CMR also has a *provider* called `ESDIS`, which hosts about 327 CIESIN/SEDAC records. That is a different and much smaller population. Always state which filter was used. This skill uses `consortium=EOSDIS` unless the user asks for something else.

---

## Coverage Classes

Each assessed (non-Level 0) collection gets exactly one class. Rules are applied in order:

| Class | Rule | Counted as missing? |
|-------|------|---------------------|
| `BOTH` | Has both an ATBD and a USER'S GUIDE RelatedUrl | No |
| `ATBD_ONLY` | Has an ATBD RelatedUrl only | No |
| `USER_GUIDE_ONLY` | Has a USER'S GUIDE RelatedUrl only | No |
| `MISSING_POSSIBLE_MISTAG` | Neither Subtype is present, but a RelatedUrl's URL or Description matches `atbd`, `algorithm theoretical`, `user's guide`, `users_guide`, or `user manual`. The document probably exists but has the wrong Subtype. | Yes |
| `MISSING_ALT_DOCS` | Neither Subtype is present, but the record has a closely related document Subtype: `ALGORITHM DOCUMENTATION`, `PI DOCUMENTATION`, `PRODUCT USAGE`, `DATA PRODUCT SPECIFICATION`, `READ-ME`, `SCIENCE DATA PRODUCT SOFTWARE DOCUMENTATION`, or `HOW-TO` | Yes |
| `MISSING_GENERAL_DOCS_ONLY` | Has only other `VIEW RELATED INFORMATION` links (e.g., `GENERAL DOCUMENTATION`, `PUBLICATIONS`, or no Subtype) | Yes |
| `MISSING_NO_DOCS` | Has no `VIEW RELATED INFORMATION` links at all | Yes |

The classes show how much work each fix needs. `MISSING_POSSIBLE_MISTAG` usually needs only a Subtype change. `MISSING_ALT_DOCS` needs a curator to decide whether the existing document can serve as a guide. `MISSING_NO_DOCS` needs new documentation, or a new link to it.

Processing levels are normalized the same way as in `Collection_Processing_Level_Validation_Skill` (Step 2), so `0`, `L0`, and `Level 0` are all treated as `0` and excluded.

---

## Workflow Steps

Follow the repository's handling rules for untrusted data: keep downloaded data and scripts in separate directories, and run Python with `-I`.

```bash
mkdir -p /tmp/doccov/scripts /tmp/doccov/data
# write the two scripts below into /tmp/doccov/scripts/
```

### Step 1: Fetch the Collection Population from CMR
`scripts/fetch_collections.py` pages through `collections.umm_json` 2,000 records at a time. It uses the `CMR-Search-After` header to get the next page and retries transient errors. It keeps only the fields the audit needs.

```python
"""Fetch all CMR collections matching a filter (default consortium=EOSDIS), paging with CMR-Search-After.
Usage: python3 -I fetch_collections.py OUT.json [extra CMR query params, e.g. consortium=EOSDIS provider=GES_DISC]"""
import json, sys, time, urllib.parse, urllib.request

CMR = "https://cmr.earthdata.nasa.gov/search/collections.umm_json"
out = sys.argv[1]
params = [tuple(a.split("=", 1)) for a in sys.argv[2:]] or [("consortium", "EOSDIS")]
url = CMR + "?" + urllib.parse.urlencode(params + [("page_size", "2000")])

records, search_after, hits = [], None, None
while True:
    headers = {"CMR-Search-After": search_after} if search_after else {}
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=300) as r:
                hits = int(r.headers.get("CMR-Hits", 0))
                search_after = r.headers.get("CMR-Search-After")
                page = json.load(r)
            break
        except Exception as e:  # transient CMR errors: retry with backoff
            if attempt == 2: raise
            time.sleep(5 * (attempt + 1))
    if not page["items"]:
        break
    for it in page["items"]:
        u, m = it["umm"], it["meta"]
        records.append({
            "concept_id": m["concept-id"], "provider": m["provider-id"],
            "short_name": u.get("ShortName"), "version": u.get("Version"),
            "entry_title": u.get("EntryTitle"),
            "processing_level": (u.get("ProcessingLevel") or {}).get("Id"),
            "data_type": u.get("CollectionDataType"),
            "related_urls": [{k: r.get(k) for k in ("URLContentType", "Type", "Subtype", "URL", "Description")}
                             for r in (u.get("RelatedUrls") or [])],
        })
    print(f"{len(records)} / {hits}", file=sys.stderr)
    if not search_after:
        break

json.dump({"query": dict(params), "cmr_hits": hits, "fetched": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "collections": records}, open(out, "w"))
```

```bash
python3 -I /tmp/doccov/scripts/fetch_collections.py /tmp/doccov/data/eosdis.json consortium=EOSDIS
# one DAAC only:
python3 -I /tmp/doccov/scripts/fetch_collections.py /tmp/doccov/data/gesdisc.json consortium=EOSDIS provider=GES_DISC
```

Check that the final `fetched / hits` line shows the two numbers as equal. If they differ, the paging was interrupted, so run the fetch again.

### Step 2: Classify Coverage
`scripts/audit_doc_coverage.py` excludes Level 0, applies the coverage classes, and writes the CSV and the summary JSON.

```python
"""Classify collections by ATBD / User's Guide coverage.
Usage: python3 -I audit_doc_coverage.py IN.json OUT_PREFIX
Writes OUT_PREFIX.csv (collections missing both documents) and OUT_PREFIX_summary.json."""
import collections, csv, json, re, sys

ATBD = "ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)"
GUIDE = "USER'S GUIDE"
ALT_DOC_SUBTYPES = {"ALGORITHM DOCUMENTATION", "PI DOCUMENTATION", "PRODUCT USAGE", "DATA PRODUCT SPECIFICATION",
                    "READ-ME", "SCIENCE DATA PRODUCT SOFTWARE DOCUMENTATION", "HOW-TO"}
MISTAG_RE = re.compile(r"atbd|algorithm[ _-]?theoretical|user'?s?[ _-]?guide|users?_?guide|user[ _-]?manual", re.I)

def normalize_level(raw):
    if raw is None or str(raw).strip().upper() in {"", "NA", "N/A", "NOT PROVIDED", "NOT APPLICABLE"}:
        return "MISSING"
    m = re.fullmatch(r"\s*(?:LEVEL|L)?\s*-?\s*([0-4])\s*([A-C]|G)?\s*", str(raw).upper())
    if not m:
        return "NON_STANDARD"
    lvl, sfx = m.groups()
    return f"1{sfx}" if lvl == "1" and sfx in {"A", "B", "C"} else lvl

def classify(c):
    subs = {(r.get("Subtype") or "").upper() for r in c["related_urls"]}
    has_atbd, has_guide = ATBD in subs, GUIDE in subs
    if has_atbd or has_guide:
        return ("BOTH" if has_atbd and has_guide else "ATBD_ONLY" if has_atbd else "USER_GUIDE_ONLY"), []
    hints = [r["URL"] for r in c["related_urls"]
             if MISTAG_RE.search(f"{r.get('URL') or ''} {r.get('Description') or ''}")]
    if hints:
        return "MISSING_POSSIBLE_MISTAG", hints
    if subs & ALT_DOC_SUBTYPES:
        return "MISSING_ALT_DOCS", sorted(subs & ALT_DOC_SUBTYPES)
    if any((r.get("Type") or "").upper() == "VIEW RELATED INFORMATION" for r in c["related_urls"]):
        return "MISSING_GENERAL_DOCS_ONLY", []
    return "MISSING_NO_DOCS", []

data = json.load(open(sys.argv[1])); prefix = sys.argv[2]
rows, excluded = [], 0
for c in data["collections"]:
    lvl = normalize_level(c["processing_level"])
    if lvl == "0":
        excluded += 1
        continue
    status, detail = classify(c)
    rows.append({**c, "level_norm": lvl, "status": status, "detail": detail})

missing = [r for r in rows if r["status"].startswith("MISSING")]
by_prov = collections.defaultdict(collections.Counter)
by_level = collections.defaultdict(collections.Counter)
by_type = collections.defaultdict(collections.Counter)
for r in rows:
    m = "missing" if r["status"].startswith("MISSING") else "covered"
    by_prov[r["provider"]][m] += 1; by_level[r["level_norm"]][m] += 1; by_type[r["data_type"] or "NOT SET"][m] += 1

summary = {
    "query": data["query"], "fetched": data["fetched"], "cmr_hits": data["cmr_hits"],
    "total": len(data["collections"]), "excluded_level0": excluded, "assessed": len(rows),
    "status_counts": dict(collections.Counter(r["status"] for r in rows)),
    "missing": len(missing),
    "by_provider": {k: dict(v) for k, v in sorted(by_prov.items(), key=lambda kv: -kv[1]["missing"])},
    "by_level": {k: dict(v) for k, v in sorted(by_level.items())},
    "by_data_type": {k: dict(v) for k, v in by_type.items()},
    "possible_mistag_examples": [{"short_name": r["short_name"], "version": r["version"], "provider": r["provider"],
                                  "urls": r["detail"][:2]} for r in missing if r["status"] == "MISSING_POSSIBLE_MISTAG"][:25],
}
json.dump(summary, open(prefix + "_summary.json", "w"), indent=2)

with open(prefix + ".csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["short_name", "version", "provider", "concept_id", "processing_level", "data_type", "status", "detail"])
    for r in sorted(missing, key=lambda r: ((r["short_name"] or "").lower(), r["version"] or "")):
        w.writerow([r["short_name"], r["version"], r["provider"], r["concept_id"], r["processing_level"],
                    r["data_type"], r["status"], "; ".join(r["detail"])])
print(json.dumps({k: summary[k] for k in ("total", "excluded_level0", "assessed", "missing", "status_counts")}, indent=2))
```

```bash
python3 -I /tmp/doccov/scripts/audit_doc_coverage.py /tmp/doccov/data/eosdis.json /tmp/doccov/data/out
cp /tmp/doccov/data/out.csv          "Reports/<report_name>_Collections_Missing_ATBD_UserGuide.csv"
cp /tmp/doccov/data/out_summary.json "Reports/<report_name>_ATBD_UserGuide_Coverage_Summary.json"
```

**CSV columns:** `short_name, version, provider, concept_id, processing_level, data_type, status, detail`. `detail` holds the matching URLs for `MISSING_POSSIBLE_MISTAG` and the alternate Subtypes for `MISSING_ALT_DOCS`.

### Step 3: Sanity Checks
Before writing the report, confirm that:
1. `total == cmr_hits` (the fetch was complete).
2. `assessed + excluded_level0 == total`.
3. The `status_counts` for the `MISSING_*` classes add up to `missing`, and `missing` equals the number of CSV data rows.
4. Your Subtype matching is not missing variants. Count `VIEW RELATED INFORMATION` Subtypes across the population, and confirm that the required Subtypes appear spelled exactly as in the KMS vocabulary. Free-text Subtypes such as `Processing History` do occur.

### Step 4: Write the Report
Use the template below. Use the summary JSON for the numbers, and put per-collection lists in the CSV rather than the Markdown.

### Step 5 (optional): Spot-Check
Choose 3–5 collections from different `MISSING_*` classes and confirm them with the Earthdata MCP tool `get_collections(concept_id=...)`. Check that `related_urls` really has no ATBD or User's Guide. For `MISSING_POSSIBLE_MISTAG`, open the matching URL and confirm what kind of document it is.

---

## Report Template

```markdown
# ATBD & User's Guide Coverage Audit: [POPULATION]

**Skill:** Collection_Documentation_Coverage_Audit_Skill v1.0
**Run date:** [DATE]  |  **CMR filter:** `[cmr_filter]`  |  **Excluded levels:** [exclude_levels]

## Summary
[total] → [excluded] Level 0 → [assessed] assessed → **[missing] ([pct]%) missing both ATBD and User's Guide**

## Coverage Classes
[table of status_counts with % of assessed]

## By Provider
[table: provider, assessed, missing, % missing, dominant missing class]

## By Processing Level / Data Type
[tables]

## Findings
[numbered findings: concentration by provider, mis-tag patterns, zero-doc providers, level skew]

## Recommended Actions
[per-class remediation, prioritized by effort and impact]

## Method & Caveats
[filter definition, Subtype matching rules, known limitations]

## Output Files
[CSV and JSON paths]
```

---

## Known Limitations
- Coverage is based **only on the Subtype in metadata**. The skill does not fetch the documents, so a broken URL tagged as an ATBD still counts as covered.
- The mis-tag heuristic matches text in URLs and Descriptions. It can produce false positives (e.g., a README whose Description mentions a user guide) and false negatives (e.g., files with opaque names).
- Collections with no `ProcessingLevel` (`MISSING`) are kept in the audit. Some of them may be Level 0 data that was never labelled as such.
- CMR content changes daily, so always record the run date and `cmr_hits`.

## Worked Example
See `Reports/EOSDIS_ATBD_UserGuide_Coverage_Report.md` (run 2026-11-04): 11,388 EOSDIS collections, 103 Level 0 excluded, and 3,425 of the remaining 11,285 (30.3%) missing both an ATBD and a User's Guide.
