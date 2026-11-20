# Skill: Collection Documentation Discovery (Find Missing ATBDs & User's Guides)

## Overview
This skill takes the collections that **Collection_Documentation_Coverage_Audit_Skill** flags as missing both an ATBD and a User's Guide, and tries to find those documents. It checks four sources, cheapest first:

1. Links already in the record that carry the wrong label
2. Sibling collections in CMR that already link the documents
3. The collection's own landing and project pages
4. Web search

Each candidate is ranked by domain, with **nasa.gov preferred**. It is then fetched to confirm it is the right document type for the right product. The output is a curator-ready list of `RelatedUrls` additions and re-tags.

**Skill Type:** Metadata Quality Remediation / Documentation Discovery (single or batch)
**Difficulty Level:** Intermediate
**Depends on:** Collection_Documentation_Coverage_Audit_Skill (population JSON + audit CSV)
**Complementary Skills:** Collection_Processing_Level_Validation_Skill, Collection_ATBD_Analysis_Skill, Collection_Lineage_via_ATBD_Skill. Those skills need an ATBD or User's Guide, and this skill supplies them.
**Use Cases:**
- Building per-DAAC lists of suggested ATBD and User's Guide links
- Turning `MISSING_POSSIBLE_MISTAG` and `MISSING_ALT_DOCS` audit results into concrete re-tag requests
- Finding documents for NRT, reprocessed, or platform-variant collections whose sibling already links them
- Preparing collections for the ATBD-based lineage, keyword, and processing-level skills

## Prerequisites
- Outputs of **Collection_Documentation_Coverage_Audit_Skill** Steps 1–2: the population JSON (`fetch_collections.py`) and the audit CSV (`audit_doc_coverage.py`). If they are missing or older than about a week, run that skill first.
- `WebSearch` with `allowed_domains` support (for Step 4), `WebFetch`, and `curl`
- Python 3; `pypdf` in an isolated venv for reading PDFs
- Optional: the Earthdata MCP tool `get_collections`, for spot-checking a sibling or the target record

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `population_json` | path | Yes | — | Population file from the audit skill |
| `audit_csv` | path | Yes | — | Missing-collections CSV from the audit skill |
| `provider` | string | No | all | Restrict to one provider (recommended for batches) |
| `status` | string | No | all | Restrict to one audit class, e.g. `MISSING_POSSIBLE_MISTAG` |
| `limit` | int | No | none | Maximum collections to process |
| `max_searches_per_family` | int | No | `4` | Web-search budget per product family (Step 4) |
| `min_tier` | int | No | `4` | Lowest domain tier that may be recommended (see the domain tier table) |

---

## Domain Priority Policy

Candidates are ranked by **domain tier first**, then by how specific the document is to the product. A lower tier number always wins when two candidates are equally valid.

| Tier | Domains | Examples | Use |
|------|---------|----------|-----|
| **1** | `nasa.gov` and all subdomains | earthdata.nasa.gov, disc.gsfc.nasa.gov, docserver.gesdisc.eosdis.nasa.gov, cddis.nasa.gov, ntrs.nasa.gov, modis-atmos.gsfc.nasa.gov, oceancolor.gsfc.nasa.gov, asdc.larc.nasa.gov, podaac.jpl.nasa.gov, espo.nasa.gov | **Preferred.** Always search here first |
| 2 | EOSDIS DAAC / SIPS hosts outside nasa.gov | lpdaac.usgs.gov, nsidc.org, asf.alaska.edu, ornldaac.ornl.gov, sedac.ciesin.columbia.edu, ssec.wisc.edu | Accept. Do one tier-1 equivalence check first (see below) |
| 3 | Partner agencies and mission bodies | usgs.gov, noaa.gov, esa.int, eumetsat.int, jaxa.jp, cnes.fr, dlr.de, copernicus.eu, ids-doris.org, igs.org | Accept for partner-mission products (e.g., JAXA ALOS, CNES DORIS) |
| 4 | Other `.gov`, `.edu`, `.mil`, `doi.org` | University PI sites, DOI landing pages | Accept only if the document is clearly the official product document |
| 5 | Everything else (journals, commercial sites) | mdpi.com, wiley.com | Do not recommend as an ATBD or User's Guide. Note it as a `PUBLICATIONS` candidate at most |
| 9 | Rejected | researchgate, scribd, academia.edu, docplayer, PDF mirror sites | Never recommend |

**nasa.gov equivalence check:** If the best verified candidate is tier 2 or lower, run **one** nasa.gov-restricted search for the same document title. Prefer a tier-1 copy only if it is the *same document at the same or a newer version*. Do not swap in an older or different document just because it is on nasa.gov.

**Persistence tiebreakers (same tier):** prefer DOI-backed URLs, then document-ID URLs (e.g., `lpdaac.usgs.gov/documents/<id>/…`), then NTRS citations, then stable file paths, and last of all pages that load their content with JavaScript.

---

## Discovery Outcomes

Each collection gets one outcome **per document type** (ATBD and User's Guide):

| Outcome | Meaning | Recommended action |
|---------|---------|--------------------|
| `FOUND_RETAG` | The document is already in the record under another Subtype or as an untyped link, and has been verified | Change the Subtype on the existing RelatedUrl |
| `FOUND_SIBLING` | A sibling collection in CMR links it (another version, NRT ↔ science quality, or a platform variant), and it has been verified | Add the RelatedUrl, copied from the sibling |
| `FOUND_WEB` | Found on a landing page or through web search, and verified | Add the RelatedUrl |
| `CANDIDATE` | Plausible, but verification was partial (e.g., covers the product family but not this version; a product web page rather than a guide document) | Curator review |
| `NOT_APPLICABLE` | An ATBD is not expected (airborne, in-situ, cruise, or ground-station campaign data; ancillary or orbit files) | Look for a User's Guide or README only |
| `NOT_FOUND` | Nothing acceptable at or above `min_tier` after the search budget was used up | Ask the DAAC whether one exists |

**Confidence:** `HIGH` means verified type and product match and tier ≤ 2. `MEDIUM` means verified type but only a family-level or version-adjacent match, or tier 3–4. `LOW` applies to any `CANDIDATE`.

---

## Workflow Steps

Follow the repository's handling rules for untrusted data. Keep downloaded pages and PDFs in their own directory, keep scripts in a separate directory, and run Python with `-I`.

```bash
mkdir -p /tmp/docdisc/scripts /tmp/docdisc/data /tmp/docdisc/web /tmp/docdisc/pdfs
python3 -m venv /tmp/docdisc/venv && /tmp/docdisc/venv/bin/pip install -q pypdf
# write the three scripts below into /tmp/docdisc/scripts/
```

### Step 1: Build the Worklist (CMR only, no web traffic)
`build_worklist.py` joins the audit CSV to the population JSON. For each missing collection it records:
- **In-record candidates**: any RelatedUrl whose URL or description looks like an ATBD or guide, whatever its Subtype
- **Sibling candidates**: collections in the same *product family* that already link an ATBD or User's Guide. A family groups the same short name across versions, `_NRT` variants, the LANCE trailing-`N` convention (`MCD19A2N` → `MCD19A2`), and platform-prefix twins (`MOD`/`MYD`/`MCD`, `VNP`/`VJ1`/`VJ2`)
- **Landing and project pages**, to crawl in Step 3
- **`atbd_expected`**: false when the title or short name indicates aircraft, airborne, in-situ, cruise, ship, sonde, ground-based, or station data
- **`family_key`**: used to run web searches once per family rather than once per collection

```python
"""Build a documentation-discovery worklist from Coverage Audit outputs.
Usage: python3 -I build_worklist.py POPULATION.json AUDIT.csv OUT.json [--provider P] [--status S] [--limit N]
Adds, per missing collection: in-record candidates, CMR sibling candidates, landing pages,
a product-family key (for de-duplicating web searches), and whether an ATBD is expected."""
import argparse, collections, csv, json, re

ATBD = "ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)"
GUIDE = "USER'S GUIDE"
LANDING_TYPES = {"DATA SET LANDING PAGE", "HOME PAGE", "PROJECT HOME PAGE"}
DOC_HINT_RE = re.compile(r"atbd|algorithm[ _-]?theoretical|user'?s?[ _-]?guide|users?_?guide|user[ _-]?manual|_dug\b|product[ _-]?guide", re.I)
# Platform prefixes that share one algorithm (and usually one ATBD / user guide)
PREFIX_GROUPS = [("MOD", "MYD", "MCD"), ("VNP", "VJ1", "VJ2"), ("AST",), ("OMI", "OM")]
# Signals that a collection is airborne / in-situ campaign data, for which an ATBD is normally not expected
CAMPAIGN_RE = re.compile(r"\b(aircraft|airborne|in[- ]situ|cruise|field campaign|ship|sonde|ground[- ]based|station)\b", re.I)

def norm(s): return (s or "").strip().upper()

def family_key(short_name):
    sn = re.sub(r"_NRT$", "", norm(short_name))
    for grp in PREFIX_GROUPS:
        for p in sorted(grp, key=len, reverse=True):
            if sn.startswith(p) and len(sn) > len(p):
                return grp[0] + sn[len(p):]
    return sn

def family_keys(c):
    """Primary family key plus NRT alternates (LANCE NRT short names often append 'N', e.g. MCD19A2N -> MCD19A2)."""
    keys = [family_key(c["short_name"])]
    is_nrt = "NRT" in norm(c.get("version")) or norm(c.get("data_type")) in {"NEAR_REAL_TIME", "LOW_LATENCY", "EXPEDITED"}
    if is_nrt and keys[0].endswith("N") and len(keys[0]) > 4:
        keys.append(keys[0][:-1])
    return keys

def doc_links(c):
    out = {}
    for r in c["related_urls"]:
        st = norm(r.get("Subtype"))
        if st in (ATBD, GUIDE):
            out.setdefault("ATBD" if st == ATBD else "USER_GUIDE", []).append(r["URL"])
    return out

ap = argparse.ArgumentParser()
ap.add_argument("population"); ap.add_argument("audit_csv"); ap.add_argument("out")
ap.add_argument("--provider"); ap.add_argument("--status"); ap.add_argument("--limit", type=int)
a = ap.parse_args()

pop = json.load(open(a.population))["collections"]
by_cid = {c["concept_id"]: c for c in pop}
by_family = collections.defaultdict(list)
for c in pop:
    by_family[family_key(c["short_name"])].append(c)

targets = list(csv.DictReader(open(a.audit_csv)))
if a.provider: targets = [t for t in targets if t["provider"] == a.provider]
if a.status:   targets = [t for t in targets if t["status"] == a.status]
if a.limit:    targets = targets[: a.limit]

work = []
for t in targets:
    c = by_cid[t["concept_id"]]
    keys = family_keys(c); fam = keys[0]
    in_record = [{"url": r["URL"], "subtype": r.get("Subtype"), "description": r.get("Description")}
                 for r in c["related_urls"]
                 if DOC_HINT_RE.search(f"{r.get('URL') or ''} {r.get('Description') or ''}")]
    siblings = []
    seen = {c["concept_id"]}
    for s in (s for k in keys for s in by_family[k]):
        if s["concept_id"] in seen: continue
        seen.add(s["concept_id"])
        links = doc_links(s)
        if links:
            siblings.append({"concept_id": s["concept_id"], "short_name": s["short_name"], "version": s["version"],
                             "provider": s["provider"], "links": links})
    landing = sorted({r["URL"] for r in c["related_urls"] if norm(r.get("Type")) in LANDING_TYPES
                      or norm(r.get("URLContentType")) == "COLLECTIONURL"})
    text = f"{c.get('entry_title') or ''} {c['short_name']}"
    work.append({
        "concept_id": c["concept_id"], "short_name": c["short_name"], "version": c["version"],
        "provider": c["provider"], "entry_title": c.get("entry_title"), "processing_level": c["processing_level"],
        "data_type": c["data_type"], "audit_status": t["status"], "family_key": fam,
        "atbd_expected": not CAMPAIGN_RE.search(text),
        "in_record_candidates": in_record, "sibling_candidates": siblings, "landing_pages": landing,
    })

json.dump(work, open(a.out, "w"), indent=1)
fams = collections.Counter(w["family_key"] for w in work)
print(json.dumps({
    "targets": len(work),
    "product_families": len(fams),
    "with_in_record_candidates": sum(bool(w["in_record_candidates"]) for w in work),
    "with_sibling_candidates": sum(bool(w["sibling_candidates"]) for w in work),
    "with_landing_page": sum(bool(w["landing_pages"]) for w in work),
    "needs_web_search": sum(not w["in_record_candidates"] and not w["sibling_candidates"] for w in work),
    "atbd_not_expected": sum(not w["atbd_expected"] for w in work),
}, indent=2))
```

```bash
python3 -I /tmp/docdisc/scripts/build_worklist.py \
  /tmp/doccov/data/eosdis.json /tmp/doccov/data/out.csv /tmp/docdisc/data/worklist.json \
  --provider GES_DISC --limit 50
```

Full EOSDIS run (2026-11-05): 3,425 targets in 3,260 families; 99 with in-record candidates, 163 with sibling candidates, 2,845 with a landing page, 3,168 needing a web search, and 591 where an ATBD is not expected.

### Step 2: Resolve Cheap Candidates (in-record, then siblings)
For each worklist entry:
1. **In-record candidates.** Fetch each one and verify it (Step 5). A verified document becomes `FOUND_RETAG`. Many `READ-ME` PDFs are user guides in all but name; GES DISC READMEs, for example, usually have sections on file naming, format, data fields, and usage.
2. **Sibling candidates.** Verify the sibling's document against the *target* product: the target short name or its family name must appear in the document, and the version or collection must be compatible. A verified match becomes `FOUND_SIBLING`. Cache documents by URL, because one ATBD often covers a whole family.
3. If both document types are now resolved (or the ATBD is `NOT_APPLICABLE` and the guide is resolved), skip Steps 3–4.

### Step 3: Crawl Landing and Project Pages
Fetch each `landing_pages` URL and rank its links with `rank_links.py`. Follow at most **two levels** of links within the same site, and only follow links that look like product or documentation pages.

```python
"""Extract candidate documentation links from a saved HTML page and rank them by domain tier.
Usage: python3 -I rank_links.py PAGE.html BASE_URL [SHORT_NAME]
Prints JSON lines: tier, doc_hint, product_match, url, text (best first)."""
import html, json, re, sys
from urllib.parse import urljoin, urlparse

# Tier 1: NASA-owned domains (preferred). Tier 2: EOSDIS DAAC/SIPS hosts outside nasa.gov.
# Tier 3: partner space/science agencies and mission bodies. Tier 4: other .gov/.edu/DOI. Tier 9: rejected hosts.
TIER2 = {"lpdaac.usgs.gov", "nsidc.org", "asf.alaska.edu", "ornldaac.ornl.gov", "sedac.ciesin.columbia.edu",
         "earthdata.ciesin.columbia.edu", "www.ssec.wisc.edu", "sips.ssec.wisc.edu"}
TIER3 = ("usgs.gov", "noaa.gov", "esa.int", "eumetsat.int", "jaxa.jp", "cnes.fr", "dlr.de", "ids-doris.org",
         "igs.org", "copernicus.eu", "isro.gov.in")
REJECT = ("researchgate.net", "scribd.com", "academia.edu", "docplayer.", "pdfcoffee.", "yumpu.com", "dokumen.")

def domain_tier(url):
    host = (urlparse(url).hostname or "").lower()
    if not host: return 9
    if any(r in host for r in REJECT): return 9
    if host in TIER2: return 2
    if host == "nasa.gov" or host.endswith(".nasa.gov"): return 1
    if any(host == d or host.endswith("." + d) for d in TIER3): return 3
    if host.endswith((".gov", ".edu", ".mil")) or host in {"doi.org", "dx.doi.org"}: return 4
    return 5

ATBD_RE = re.compile(r"atbd|algorithm[ _-]?theoretical", re.I)
GUIDE_RE = re.compile(r"user'?s?[ _-]?guide|users?_?guide|_dug\b|product[ _-]?guide|handbook|user[ _-]?manual|readme", re.I)
SPEC_RE = re.compile(r"\bformats?\b|specification|\.fmt\b|file[ _-]?spec|data[ _-]?dictionary", re.I)

page, base = sys.argv[1], sys.argv[2]
short = (sys.argv[3] if len(sys.argv) > 3 else "").lower()
t = open(page, errors="replace").read()
seen, rows = set(), []
for href, inner in re.findall(r'<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>', t, re.S | re.I):
    url = urljoin(base, html.unescape(href))
    if url in seen or not url.startswith(("http", "ftp")): continue
    seen.add(url)
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", inner))).strip()
    blob = f"{url} {text}"
    hint = "ATBD" if ATBD_RE.search(blob) else "USER_GUIDE" if GUIDE_RE.search(blob) else \
           "SPEC" if SPEC_RE.search(blob) else ("PDF" if url.lower().endswith(".pdf") else None)
    if not hint: continue
    rows.append({"tier": domain_tier(url), "doc_hint": hint, "product_match": bool(short) and short in blob.lower(),
                 "url": url, "text": text[:120]})
order = {"ATBD": 0, "USER_GUIDE": 1, "SPEC": 2, "PDF": 3}
for r in sorted(rows, key=lambda r: (r["tier"], not r["product_match"], order[r["doc_hint"]])):
    if r["tier"] < 9: print(json.dumps(r))
```

```bash
cd /tmp/docdisc/web && curl -sL -m 60 -A "Mozilla/5.0" -o page.html -w "%{http_code} %{url_effective}\n" "<LANDING_URL>"
python3 -I /tmp/docdisc/scripts/rank_links.py /tmp/docdisc/web/page.html "<FINAL_URL>" "<SHORT_NAME>"
```

**Practical notes (from testing):**
- **Pages that load content with JavaScript** return no useful links to `curl` or `WebFetch`. Examples: GES DISC `datasets/.../summary` and the ESPO archive browser. Skip them and go to Step 4.
- **Bot blocks and redirects:** some sites return 403 to `curl`. Retry with `WebFetch`, which reports cross-host redirects. For example, ASF data-set pages now redirect to `earthdata.nasa.gov/data/instruments/...`, so follow the redirect, which also moves the candidate to tier 1.
- `doi.org` landing pages usually redirect to the DAAC page, so crawl the final URL.

### Step 4: Web Search (nasa.gov first)
Run searches once per `family_key`, using at most `max_searches_per_family` searches, in this order. Stop early once both document types are resolved at tier 1.

| # | `allowed_domains` | Query template |
|---|-------------------|----------------|
| 1 | `["nasa.gov"]` | `"<SHORT_NAME>" ATBD OR "algorithm theoretical basis"`, or `"<SHORT_NAME>" "user guide"` for the guide |
| 2 | `["nasa.gov"]` | `<instrument> <key words from entry_title> <document type>` (drop the version and NRT tokens) |
| 3 | tier-2 DAAC domain of the provider (e.g., `["lpdaac.usgs.gov"]`, `["nsidc.org"]`) | Same as #1 |
| 4 | none (open web) | `<entry_title without version> <document type>`; then apply the domain tiers to the results |

**Fallback when `WebSearch` is unavailable** (it was unavailable in the 2026-11-05 test environment):
- **NTRS API** (tier 1): `curl -G https://ntrs.nasa.gov/api/citations/search --data-urlencode "q=<terms>" --data-urlencode "page.size=10"`. It works well for older-mission ATBDs and campaign reports. Most hits are papers or presentations, so classify a hit as an ATBD only if its title says so.
- **Earthdata topic and instrument pages** (`earthdata.nasa.gov/data/instruments/<instrument>`, `.../space-geodesy-techniques/<technique>`): crawl them with Step 3.
- Record `search_method: fallback` in the results. Without a search engine, `NOT_FOUND` results are weaker evidence.

### Step 5: Verify Each Candidate
Fetch the document (PDFs go into `/tmp/docdisc/pdfs/`), extract the text, and check all of the following:

```python
"""Extract PDF text with page markers. Usage: pdf_text.py IN.pdf OUT.txt"""
import sys
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
with open(sys.argv[2], "w") as f:
    f.write(f"=== META pages={len(r.pages)} title={(r.metadata or {}).get('/Title')}\n")
    for i, p in enumerate(r.pages, 1):
        f.write(f"=== PAGE {i}\n{p.extract_text() or ''}\n")
```

| Check | Pass criteria |
|-------|---------------|
| Reachable | HTTP 200 after redirects; record the final URL |
| Document type: ATBD | Title or front matter says "Algorithm Theoretical Basis", or the content has sections on algorithm, physics, or retrieval theory |
| Document type: User's Guide | Title says "User's Guide", "User Guide", "Data User's Guide", or "Product Guide", **or** it is a README or product page covering file naming, format and structure, data fields, quality flags, and how to use the data. Score a README like that as a guide, and say so in the evidence |
| Product match | The text names the target short name, its family name (e.g., `MCD19A2` for `MCD19A2N`), or a documented legacy name. `grep -oE "<SHORT_NAME>\|<FAMILY>" doc.txt \| sort \| uniq -c` |
| Version match | The document's collection or version is the same as, or compatible with, the target's (e.g., a C6.1 guide for `6.1NRT`). An ATBD can be older than the product version; that is acceptable, but note it |
| Not a mirror | The host is not tier 9, and the document is the publisher's copy |

Record the evidence for each verified candidate: page title, the line naming the product, version, page count, final URL, and tier.

### Step 6: Choose the Recommendation and Write the Output
For each collection and document type, pick the best verified candidate, ordered by tier, then confidence, then persistence. Write the UMM-C changes:

```json
{
  "concept_id": "C2407807500-LANCEMODIS",
  "action": "ADD",
  "RelatedUrl": {
    "URL": "https://lpdaac.usgs.gov/documents/1500/MCD19_User_Guide_V61.pdf",
    "URLContentType": "PublicationURL",
    "Type": "VIEW RELATED INFORMATION",
    "Subtype": "USER'S GUIDE",
    "Description": "MODIS MAIAC (MCD19) Data User's Guide, Collection 6.1"
  },
  "outcome": "FOUND_SIBLING", "tier": 2, "confidence": "HIGH",
  "evidence": "Title page: 'MODIS Multi-Angle Implementation of Atmospheric Correction (MAIAC) Data User's Guide Collection 6.1'; names MCD19A2 11 times; linked by sibling MCD19A2 v061 (LPCLOUD)"
}
```

For `FOUND_RETAG`, use `"action": "RETAG"`, and include the existing URL with its `"from_subtype"` and `"to_subtype"`.

**Outputs:**
- `Reports/<NAME>_Documentation_Discovery_Report.md`: summary counts by outcome and tier, a per-collection table, and findings
- `Reports/<NAME>_Documentation_Discovery_Recommendations.json`: the UMM-C change list above

### Report Template

```markdown
# Documentation Discovery: [POPULATION / PROVIDER]

**Skill:** Collection_Documentation_Discovery_Skill v1.0  |  **Run date:** [DATE]
**Input audit:** [audit CSV path, audit run date]  |  **Search method:** WebSearch | fallback

## Summary
[n] collections, [f] families → ATBD: FOUND [x] / CANDIDATE [y] / NOT_APPLICABLE [z] / NOT_FOUND [w]
User's Guide: FOUND [..] / CANDIDATE [..] / NOT_FOUND [..]  |  Tier-1 share of recommendations: [..]%

## Results
| Short Name | Version | Provider | Doc | Outcome | Tier | Confidence | URL | Evidence |

## Findings
## Recommended Actions
## Method & Caveats
```

---

## Batch Guidance
- **Run by provider.** DAAC curators act on per-provider lists, and providers share landing page structures and document servers.
- **Search once per family.** Run Step 4 once per `family_key` and apply the verified results to every member, re-checking version compatibility for each one.
- **Cache documents by URL**, both the downloaded file and its verification result.
- **Budget:** about one fetch per in-record or sibling candidate, two or three page fetches per landing page, and at most `max_searches_per_family` searches. With 3,260 families EOSDIS-wide, a full run is large, so do it one provider at a time.
- **Order of work:** `MISSING_POSSIBLE_MISTAG` → `MISSING_ALT_DOCS` → collections with sibling candidates → everything else. This front-loads the fixes that need only a re-tag.

## Quality Assurance Checklist
- [ ] Audit inputs are recent (≤ 7 days) and their run date is recorded
- [ ] nasa.gov searched before any other tier; equivalence check done for tier-2+ picks
- [ ] Every recommended URL fetched (HTTP 200), with type, product, and version verified
- [ ] README-as-guide decisions justified with section evidence
- [ ] Sibling-derived documents confirmed to cover the *target* product and version
- [ ] `NOT_APPLICABLE` used only for ATBDs of campaign, in-situ, or ancillary data
- [ ] Search method (WebSearch or fallback) recorded; `NOT_FOUND` caveated when the fallback was used
- [ ] No CMR metadata modified; output is recommendations only

## Tools Used
- `build_worklist.py`, `rank_links.py`, `pdf_text.py` (above)
- `WebSearch` (with `allowed_domains`), `WebFetch`, `curl`
- NTRS Search API: `https://ntrs.nasa.gov/api/citations/search`
- Earthdata MCP `get_collections` (spot checks)

## Known Limitations
- Product-family matching is rule-based. It misses families whose names differ more than a version, `_NRT`, a trailing `N`, or a known platform prefix (e.g., CERES editions, mission renames).
- `atbd_expected` uses keywords in the title, so a campaign collection whose title doesn't say "aircraft" or "in-situ" will still be treated as needing an ATBD.
- Pages that load content with JavaScript can't be crawled without a browser.
- Scanned PDFs need OCR to be verified. Record them as `CANDIDATE` with a note.

## Test Results (2026-11-05, fallback search: `WebSearch` unavailable)
See `Reports/Documentation_Discovery_Test_Report.md`. Five collections, one from each route:

| Collection | Route | ATBD | User's Guide |
|---|---|---|---|
| MCD19A2N 6.1NRT (LANCEMODIS) | Sibling MCD19A2 v061 | FOUND_SIBLING, tier 2, HIGH | FOUND_SIBLING, tier 2, HIGH |
| AER_DBDT_D10KM_L3_MODIS_AQUA 001 (GES_DISC) | In-record README | NOT_FOUND | FOUND_RETAG, tier 1, HIGH |
| DORIS_data_cycle 1 (CDDIS) | Landing-page crawl | NOT_APPLICABLE | CANDIDATE, tier 1, LOW |
| AAOE_Aerosol_AircraftInSitu_ER2_Data 1 (LARC_CLOUD) | Crawl + NTRS | NOT_APPLICABLE | NOT_FOUND |
| ALOS_PSR_L1.1 1 (ASF) | Crawl (ASF → Earthdata redirect) | NOT_FOUND | NOT_FOUND (format spec only) |

Fixes made during testing: added the LANCE trailing-`N` NRT sibling rule (+9 sibling matches EOSDIS-wide); fixed `format` matching inside "information"; corrected nasa.gov hosts that had been placed in tier 2.

## Related Skills
- Collection_Documentation_Coverage_Audit_Skill: produces this skill's inputs
- Collection_Processing_Level_Validation_Skill and Collection_ATBD_Analysis_Skill: consume the documents found here

## Version History
- **v1.0** (2026-11-05): Initial skill; tested on five collections using fallback search

---

**Skill Status:** ✅ TESTED (5 collections, fallback search); WebSearch path not yet exercised
