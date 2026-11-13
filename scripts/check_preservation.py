#!/usr/bin/env python3
"""Report numeric and citation-token changes between two text files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


CITATION_PATTERNS = [
    re.compile(r"<!--\s*(?:ref|anchor):[^>]+-->", re.IGNORECASE),
    re.compile(r"\[[0-9][0-9,\-–\s]*\]"),
    re.compile(
        r"\([A-Z][A-Za-z&.\s'’-]+,\s*(?:19|20)\d{2}[a-z]?"
        r"(?:\s*;\s*[A-Z][A-Za-z&.\s'’-]+,\s*(?:19|20)\d{2}[a-z]?)*\)"
    ),
]

NUMBER_PATTERN = re.compile(
    r"(?<![\w.])[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:\s?(?:%|‰))?"
)


def _citation_spans(text: str) -> list[tuple[int, int, str]]:
    spans: list[tuple[int, int, str]] = []
    occupied: list[tuple[int, int]] = []
    for pattern in CITATION_PATTERNS:
        for match in pattern.finditer(text):
            if any(match.start() < end and match.end() > start for start, end in occupied):
                continue
            token = re.sub(r"\s+", " ", match.group(0)).strip()
            spans.append((match.start(), match.end(), token))
            occupied.append((match.start(), match.end()))
    return sorted(spans)


def extract_tokens(text: str) -> dict[str, Counter[str]]:
    """Return multiset counters for citation and number tokens."""
    citations = _citation_spans(text)
    numbers: list[str] = []
    for match in NUMBER_PATTERN.finditer(text):
        if any(match.start() < end and match.end() > start for start, end, _ in citations):
            continue
        token = re.sub(r"\s+", "", match.group(0))
        numbers.append(token)
    return {
        "numbers": Counter(numbers),
        "citations": Counter(token for _, _, token in citations),
    }


def compare(original: str, revised: str) -> dict[str, object]:
    """Compare two texts and return missing or added tokens."""
    before = extract_tokens(original)
    after = extract_tokens(revised)
    result: dict[str, object] = {"status": "pass", "differences": {}}
    for kind in ("numbers", "citations"):
        missing = before[kind] - after[kind]
        added = after[kind] - before[kind]
        if missing or added:
            result["differences"][kind] = {
                "missing": dict(sorted(missing.items())),
                "added": dict(sorted(added.items())),
            }
    if result["differences"]:
        result["status"] = "review-required"
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path)
    parser.add_argument("revised", type=Path)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args(argv)

    for path in (args.original, args.revised):
        if not path.is_file():
            parser.error(f"file not found: {path}")

    result = compare(
        args.original.read_text(encoding="utf-8-sig"),
        args.revised.read_text(encoding="utf-8-sig"),
    )
    result["original"] = str(args.original)
    result["revised"] = str(args.revised)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif result["status"] == "pass":
        print("PASS: numeric and citation tokens are unchanged.")
    else:
        print("REVIEW REQUIRED: numeric or citation-token differences were found.")
        for kind, changes in result["differences"].items():
            print(f"{kind}:")
            print(f"  missing: {changes['missing']}")
            print(f"  added:   {changes['added']}")

    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
