"""Find MetadataAssociations that fail the new schema rules, formatted for the Jupyter notebook.

New rules: the association identifier is the collection ShortName (replaces EntryId), and Version
is mandatory. Based on find_version.py, but every identifier is checked against CMR instead of
guessing from the '_' in it (ShortNames such as MOD08_D3 or GPM_3IMERGHH already contain one).

Writes two files in the find_version.py notebook format (concept_id, atbd_url, target_collection,
lineage_data.parent_collections):
  - SHORTNAME_MISMATCH_FILE: associations whose identifier is not a CMR ShortName
  - MISSING_VERSION_FILE:    associations with no Version
An association can appear in both (e.g. 'VNP46A1_2': not a ShortName, and no Version field).
"""
import json
import re
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import requests

GRAPHQL_URL = "https://graphql.earthdata.nasa.gov/api"
ALLOWED_TYPES = [
    "SCIENCE ASSOCIATED", "DEPENDENT", "INPUT",
    "PARENT", "CHILD", "RELATED", "LARGER CITATION WORKS"
]

SHORTNAME_MISMATCH_FILE = "collections_shortname_mismatchOct22.json"
MISSING_VERSION_FILE = "collections_missing_versionOct22.json"

# Version values that are present but carry no real version
PLACEHOLDER_VERSIONS = {"", "not provided", "not applicable", "n/a", "na", "none", "null", "unknown"}

HIDDEN_VERSION_PATTERN = re.compile(r'_(v?\d[\w.]*)$', re.IGNORECASE)

PAGE_SIZE = 1000       # collections per page in the light scan
DETAIL_BATCH = 50      # collections per request when fetching full metadata for flagged collections
REQUEST_TIMEOUT = 120  # seconds
REQUEST_RETRIES = 4    # retries for 502/503/504 and network errors
LOOKUP_WORKERS = 8     # concurrent ShortName lookups
LOOKUP_RETRIES = 3

RETRY_STATUS = {429, 500, 502, 503, 504}


def graphql(query: str, variables: dict, retries: int = REQUEST_RETRIES) -> dict:
    """POST a query to CMR GraphQL and return its `data` block.

    Gateway timeouts and network errors are retried with exponential backoff; other HTTP or
    GraphQL errors raise immediately.
    """
    for attempt in range(retries + 1):
        try:
            resp = requests.post(GRAPHQL_URL, json={"query": query, "variables": variables},
                                 timeout=REQUEST_TIMEOUT)
            if resp.status_code in RETRY_STATUS and attempt < retries:
                raise requests.exceptions.HTTPError(f"{resp.status_code} {resp.reason}", response=resp)
            resp.raise_for_status()
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout,
                requests.exceptions.HTTPError) as exc:
            status = getattr(getattr(exc, "response", None), "status_code", None)
            if attempt == retries or (status is not None and status not in RETRY_STATUS):
                raise
            wait = 5 * 2 ** attempt
            print(f"    [retry] {exc} -- waiting {wait}s (attempt {attempt + 1}/{retries})")
            time.sleep(wait)
            continue
        payload = resp.json()
        if payload.get("errors"):
            raise RuntimeError(payload["errors"])
        return payload.get("data") or {}


def fetch_collections() -> list:
    """Page through every EOSDIS collection with granules (same filters as find_version.py).

    Only the fields needed to classify associations are requested here; asking for abstracts,
    relatedUrls etc. on every page makes the API time out (504). See fetch_details().
    """
    query = """
    query provenanceQuery($params: CollectionsInput) {
      collections(params: $params) {
        cursor
        items {
          conceptId
          entryId
          shortName
          versionId
          metadataAssociations
        }
      }
    }
    """
    collections = []
    cursor = None
    while True:
        variables = {
            "params": {"limit": PAGE_SIZE, "cursor": cursor, "hasGranules": True, "consortium": "EOSDIS"}
        }
        data = graphql(query, variables)
        page = data.get("collections") or {}
        items = page.get("items") or []
        if not items:
            break
        collections.extend(items)
        print(f"  fetched {len(collections)} collections...")
        cursor = page.get("cursor")
        if not cursor:
            break
    return collections


def fetch_details(concept_ids: list) -> dict:
    """{conceptId: full metadata} for the flagged collections only, in small batches.

    A batch that still fails after retries is split in half; a single collection that fails
    is skipped (its record is written with the light-scan fields only).
    """
    query = """
    query collectionDetails($params: CollectionsInput) {
      collections(params: $params) {
        items {
          conceptId
          title
          abstract
          doi
          processingLevel
          platforms
          scienceKeywords
          relatedUrls
        }
      }
    }
    """
    details = {}
    pending = [concept_ids[i:i + DETAIL_BATCH] for i in range(0, len(concept_ids), DETAIL_BATCH)]
    while pending:
        batch = pending.pop(0)
        try:
            data = graphql(query, {"params": {"conceptId": batch, "limit": len(batch)}})
        except Exception as exc:
            if len(batch) > 1:
                half = len(batch) // 2
                pending[:0] = [batch[:half], batch[half:]]
            else:
                print(f"    [warn] could not fetch details for {batch[0]}: {exc}")
            continue
        for it in (data.get("collections") or {}).get("items") or []:
            details[it["conceptId"]] = it
        print(f"  fetched details for {len(details)}/{len(concept_ids)} collections...")
    return details


def lookup_short_name(short_name: str):
    """All CMR collections whose ShortName equals short_name (case-insensitive).

    Returns a list (possibly empty), or None if CMR could not be reached.
    """
    query = """
    query getVersions($params: CollectionsInput) {
      collections(params: $params) {
        items { conceptId shortName versionId }
      }
    }
    """
    for attempt in range(LOOKUP_RETRIES):
        try:
            data = graphql(query, {"params": {"shortName": short_name, "limit": 100}})
            items = (data.get("collections") or {}).get("items") or []
            key = short_name.lower()
            return [c for c in items if (c.get("shortName") or "").lower() == key]
        except Exception as exc:
            if attempt == LOOKUP_RETRIES - 1:
                print(f"    [warn] CMR lookup failed for '{short_name}': {exc}")
                return None
            time.sleep(2 ** attempt)


def lookup_all(short_names) -> dict:
    """Look up many ShortNames concurrently. Returns {lowercase short_name: candidates or None}."""
    unique = sorted({s for s in short_names if s}, key=str.lower)
    with ThreadPoolExecutor(max_workers=LOOKUP_WORKERS) as pool:
        results = list(pool.map(lookup_short_name, unique))
    return {s.lower(): r for s, r in zip(unique, results)}


def norm_version(v) -> str:
    """Loose comparison form: 'v002' == '002' == '2'."""
    s = str(v or "").strip().lower().lstrip("v")
    return s.lstrip("0") or "0"


def matching_version(candidates: list, version):
    """The CMR spelling of `version` among the candidates, or None."""
    return next((c.get("versionId") for c in candidates
                 if norm_version(c.get("versionId")) == norm_version(version)), None)


def clean_version(assoc: dict):
    """The association's Version as a string, or None if absent or a placeholder."""
    v = assoc.get("version")
    if v is None or str(v).strip().lower() in PLACEHOLDER_VERSIONS:
        return None
    return str(v).strip()


def clean_identifier(assoc: dict) -> str:
    """ShortName under the new schema, EntryId under the current one."""
    v = assoc.get("shortName") or assoc.get("entryId")
    return str(v).strip() if v is not None else ""


def best_doc_url(related_urls: list):
    """Best ATBD / documentation URL, using find_version.py's priority order."""
    best_url, best_priority = None, 99
    for link in related_urls or []:
        if not isinstance(link, dict):
            continue
        url_type = str(link.get("type", link.get("Type", ""))).upper()
        subtype = str(link.get("subtype", link.get("Subtype", ""))).upper()
        url = str(link.get("url", link.get("URL", "")))

        if "ATBD" in subtype or "ATBD" in url.upper():
            priority = 1
        elif ("GUIDE" in subtype or "DOC" in subtype or "TECH" in subtype) and url.lower().endswith(".pdf"):
            priority = 2
        elif "VIEW RELATED INFORMATION" in url_type and url.lower().endswith(".pdf"):
            priority = 3
        else:
            continue
        if priority < best_priority:
            best_url, best_priority = url, priority
    return best_url


def target_collection_block(item: dict) -> dict:
    """target_collection in the find_version.py format (instruments are nested in platforms)."""
    doi_data = item.get("doi")
    doi_str = doi_data.get("doi") if isinstance(doi_data, dict) else doi_data

    proc_data = item.get("processingLevel")
    proc_id = proc_data.get("id", "Unknown") if isinstance(proc_data, dict) else "Unknown"

    p_names, i_names = [], []
    for p in item.get("platforms") or []:
        if isinstance(p, dict):
            if p.get("shortName"):
                p_names.append(p.get("shortName"))
            for inst in p.get("instruments") or []:
                if isinstance(inst, dict) and inst.get("shortName"):
                    i_names.append(inst.get("shortName"))

    return {
        "short_name": item.get("shortName"),
        "version": item.get("versionId"),
        "entry_title": item.get("title"),
        "abstract": item.get("abstract") or "",
        "doi": doi_str,
        "processing_level_id": proc_id,
        "platforms": sorted(set(p_names)),
        "instruments": sorted(set(i_names)),
        "science_keywords": item.get("scienceKeywords") or [],
    }


def notebook_record(item: dict, parent_collections: list) -> dict:
    """One collection in the find_version.py / notebook input format."""
    return {
        "concept_id": item.get("conceptId"),
        "atbd_url": best_doc_url(item.get("relatedUrls")),
        "target_collection": target_collection_block(item),
        "lineage_data": {
            "target_collection": item.get("shortName"),
            "processing_method": "Pending update",
            "atbd_section": None,
            "lineage_quote": None,
            "parent_collections": parent_collections,
        },
    }


def find_schema_issues():
    print("Fetching data from GraphQL... (This may take a few minutes)")
    collections = fetch_collections()

    # Pass 1: gather associations and resolve every identifier against CMR
    rows = []  # (collection item, index, association)
    for item in collections:
        for index, assoc in enumerate(item.get("metadataAssociations") or []):
            if isinstance(assoc, dict):
                rows.append((item, index, assoc))

    identifiers = {clean_identifier(a) for _, _, a in rows}
    print(f"Resolving {len(identifiers)} unique association identifiers against CMR...")
    lookups = lookup_all(identifiers)

    # Identifiers that are not a ShortName: try splitting off a trailing _<version>
    split_bases = set()
    for ident in identifiers:
        match = HIDDEN_VERSION_PATTERN.search(ident) if ident else None
        if match and lookups.get(ident.lower()) == []:
            split_bases.add(ident[:match.start()])
    print(f"Resolving {len(split_bases)} possible ShortName_Version identifiers...")
    lookups.update({k: v for k, v in lookup_all(split_bases).items() if k not in lookups})

    # Pass 2: classify
    total_collections_with_assocs = sum(1 for item in collections if item.get("metadataAssociations"))
    type_distribution = defaultdict(int)
    mismatch_by_concept = {}   # conceptId -> (item, [parent_collections])
    missing_by_concept = {}
    failing_collections = set()
    counts = defaultdict(int)

    for item, index, assoc in rows:
        assoc_type = assoc.get("type")
        type_distribution[assoc_type if assoc_type else "MISSING_TYPE_FIELD"] += 1

        ident = clean_identifier(assoc)
        version = clean_version(assoc)
        exact = lookups.get(ident.lower()) if ident else []

        # Version embedded in the identifier, e.g. VNP46A1_2 -> VNP46A1 v2
        base = extracted = base_candidates = None
        match = HIDDEN_VERSION_PATTERN.search(ident) if ident else None
        if match and exact == []:
            base, extracted = ident[:match.start()], match.group(1)
            base_candidates = lookups.get(base.lower())
        lookup_failed = exact is None or (base is not None and base_candidates is None)
        if lookup_failed:
            counts["lookup_failed"] += 1

        entry = {
            "association_index": index,
            "original_id": ident,
            "original_version": assoc.get("version"),
            "original_type": assoc_type,
            "original_description": assoc.get("description"),
        }

        # Rule 1: identifier must be a CMR ShortName
        mismatch_flags = []
        suggested = None
        if not ident:
            mismatch_flags.append("missing_identifier")
        elif lookup_failed:
            pass   # cannot tell; reported in the warning below
        elif exact:
            cmr_name = exact[0].get("shortName")
            if cmr_name != ident:
                mismatch_flags.append("shortname_case_differs")
                suggested = cmr_name
        elif base_candidates:
            mismatch_flags.append("version_embedded_in_identifier")
            suggested = base_candidates[0].get("shortName")
        else:
            mismatch_flags.append("identifier_not_in_cmr")

        if mismatch_flags:
            counts["shortname_mismatch"] += 1
            candidates = exact or base_candidates or []
            mismatch_by_concept.setdefault(item.get("conceptId"), (item, []))[1].append({
                **entry,
                "short_name": suggested or ident,
                "version": version,
                "relationship_type": assoc_type or "related",
                "suggested_short_name": suggested,
                "available_versions": sorted({str(c.get("versionId")) for c in candidates}),
                "flags": mismatch_flags,
                "description_override": f"Needs review. Flags: {', '.join(mismatch_flags)}.",
            })

        # Rule 2: Version is mandatory
        if not version:
            counts["missing_version"] += 1
            missing_flags = ["missing_version"]
            short_name, resolved = ident, None
            if base_candidates:
                short_name = base_candidates[0].get("shortName")
                resolved = matching_version(base_candidates, extracted)
                missing_flags.append("version_in_entryId" if resolved else "embedded_version_not_in_cmr")
                counts["embedded_verified" if resolved else "embedded_unverified"] += 1
            elif exact:
                counts["bare_shortname"] += 1
            elif lookup_failed:
                missing_flags.append("cmr_lookup_failed")
            else:
                counts["missing_not_in_cmr"] += 1

            if resolved:
                desc = f"Auto-fixed version. Extracted '{extracted}' from original ID '{ident}', verified in CMR."
            else:
                desc = f"Needs review. Flags: {', '.join(missing_flags)}."

            candidates = exact or base_candidates or []
            missing_by_concept.setdefault(item.get("conceptId"), (item, []))[1].append({
                **entry,
                "short_name": short_name,
                # Only a version verified in CMR is pre-filled; the notebook resolves the rest
                "version": resolved,
                "relationship_type": assoc_type or "related",
                "extracted_version": extracted,
                "available_versions": sorted({str(c.get("versionId")) for c in candidates}),
                "flags": missing_flags,
                "description_override": desc,
            })

        if mismatch_flags or not version or not assoc_type or assoc_type not in ALLOWED_TYPES:
            failing_collections.add(item.get("conceptId"))

    # Full metadata (abstract, DOI, relatedUrls, ...) only for the collections written out
    flagged = sorted(set(mismatch_by_concept) | set(missing_by_concept))
    print(f"Fetching full metadata for {len(flagged)} flagged collections...")
    details = fetch_details(flagged)

    def full(item):
        return {**item, **details.get(item.get("conceptId"), {})}

    mismatch_records = [notebook_record(full(item), pcs) for item, pcs in mismatch_by_concept.values()]
    missing_records = [notebook_record(full(item), pcs) for item, pcs in missing_by_concept.values()]
    missing_entirely = counts["bare_shortname"] + counts["missing_not_in_cmr"]

    # ==========================================
    # PRINT THE TERMINAL SUMMARY
    # ==========================================
    print("\n" + "=" * 60)
    print("SCHEMA CHANGE ANALYSIS: ShortName replaces EntryId, Version mandatory")
    print("=" * 60)
    print(f"Total Collections Scanned in CMR: {len(collections)}")
    print(f"Collections actually using MetadataAssociations: {total_collections_with_assocs}")
    print(f"Total Individual Associations Analyzed: {len(rows)}\n")

    print("--- DISTRIBUTION OF ASSOCIATION TYPES ---")
    for t_name, count in sorted(type_distribution.items(), key=lambda x: x[1], reverse=True):
        print(f"  {t_name.ljust(25)} : {count}")

    print("\n--- SCHEMA CHANGE IMPACT (Who needs to update?) ---")
    print(f"Collections that FAIL the new schema rules: {len(failing_collections)}")

    print("\n--- SHORTNAME CHECK ---")
    print(f"Associations whose identifier is not a CMR ShortName: {counts['shortname_mismatch']}")
    print(f"Collections affected: {len(mismatch_records)}  -> {SHORTNAME_MISMATCH_FILE}")

    print("\n--- VERSION CHECK ---")
    print(f"Associations missing the Version field: {counts['missing_version']}")
    print(f"  Version embedded in identifier, verified in CMR  : {counts['embedded_verified']}")
    print(f"  Version embedded in identifier, not found in CMR : {counts['embedded_unverified']}")
    print(f"  Identifier is a bare ShortName (no version)      : {counts['bare_shortname']}")
    print(f"  Identifier not found in CMR (manual review)      : {counts['missing_not_in_cmr']}")
    print(f"Associations missing version entirely (no field, none in identifier): {missing_entirely}")
    print(f"Collections affected: {len(missing_records)}  -> {MISSING_VERSION_FILE}")

    if counts["lookup_failed"]:
        print(f"\n[warn] CMR lookups failed for {counts['lookup_failed']} association(s); rerun to classify them.")

    # ==========================================
    # SAVE THE JSON FILES
    # ==========================================
    with open(SHORTNAME_MISMATCH_FILE, "w", encoding="utf-8") as f:
        json.dump(mismatch_records, f, indent=2)
    with open(MISSING_VERSION_FILE, "w", encoding="utf-8") as f:
        json.dump(missing_records, f, indent=2)

    print(f"\nSaved '{SHORTNAME_MISMATCH_FILE}' and '{MISSING_VERSION_FILE}'")


if __name__ == "__main__":
    find_schema_issues()
