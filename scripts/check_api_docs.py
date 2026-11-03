#!/usr/bin/env python3
"""Check that the API docs match the live APIs.

For each project, download the server's /openapi.json and compare its
endpoints with the endpoint paths used in docs/apis/<Project>/*.md.

Reports:
  - endpoints used in the docs that the API does not have (e.g. typos)
  - endpoints the API has that the docs never mention

Exits with status 1 if anything does not match. Uses only the standard library.
"""

import json
import re
import sys
import urllib.request
from pathlib import Path

PROJECTS = {
    "Texas": "https://twdb.dri.edu",
    "Reclamation": "https://operevap.dri.edu",
    "Conus": "https://nasa-revap.dri.edu",
}

# Endpoint groups the docs use; anything else (e.g. /docs) is ignored.
ENDPOINT_PREFIXES = ("/auth/", "/info/", "/metadata/", "/timeseries/")

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs" / "apis"


def api_endpoints(base_url):
    with urllib.request.urlopen(f"{base_url}/openapi.json", timeout=30) as resp:
        spec = json.load(resp)
    return {path.rstrip("/") for path in spec.get("paths", {})}


def doc_endpoints(project, base_url):
    host = re.escape(base_url)
    patterns = [
        # Full URLs, e.g. "https://twdb.dri.edu/info/list_dates?..."
        re.compile(host + r"(/[A-Za-z0-9_/\-]+)"),
        # Python f-strings and shell variables, e.g. f"{BASE_URL}/info/..." or "${BASE_URL}/info/..."
        re.compile(r"\$?\{BASE_URL\}(/[A-Za-z0-9_/\-]+)"),
        # Paths in backticks, e.g. `/info/list_RES_NAMES`
        re.compile(r"`(/(?:auth|info|metadata|timeseries)/[A-Za-z0-9_/\-]+)`"),
    ]
    found = {}
    for md in sorted((DOCS_DIR / project).glob("*.md")):
        text = md.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), start=1):
            for pattern in patterns:
                for match in pattern.finditer(line):
                    path = match.group(1).rstrip("/")
                    if path.startswith(ENDPOINT_PREFIXES):
                        found.setdefault(path, []).append(f"{md.relative_to(DOCS_DIR.parent.parent)}:{lineno}")
    return found


def main():
    problems = 0
    for project, base_url in PROJECTS.items():
        print(f"== {project} ({base_url})")
        try:
            api = api_endpoints(base_url)
        except Exception as exc:  # network errors, bad JSON
            print(f"  ERROR: could not read {base_url}/openapi.json: {exc}")
            problems += 1
            continue
        docs = doc_endpoints(project, base_url)

        unknown = sorted(set(docs) - api)
        undocumented = sorted(api - set(docs))

        for path in unknown:
            print(f"  Not in API: {path}  (used at {', '.join(docs[path])})")
        for path in undocumented:
            print(f"  Not documented: {path}")
        if not unknown and not undocumented:
            print("  OK")
        problems += len(unknown) + len(undocumented)

    if problems:
        print(f"\n{problems} problem(s) found.")
        return 1
    print("\nAll API docs match the live APIs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
