#!/usr/bin/env python3
"""Validate the structure of Lite behavioral evaluation cases."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ALLOWED_CATEGORIES = {
    "draft",
    "zh-edit",
    "en-edit",
    "claim-boundary",
    "bilingual",
    "citation-safety",
}
REQUIRED_FIELDS = {
    "id",
    "category",
    "input",
    "context",
    "expected_findings",
    "forbidden_changes",
}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    count = 0
    for line_number, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            case = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: invalid JSON: {exc}")
            continue
        count += 1
        missing = REQUIRED_FIELDS - case.keys()
        if missing:
            errors.append(f"line {line_number}: missing fields: {sorted(missing)}")
            continue
        case_id = case["id"]
        if case_id in seen_ids:
            errors.append(f"line {line_number}: duplicate id {case_id!r}")
        seen_ids.add(case_id)
        if case["category"] not in ALLOWED_CATEGORIES:
            errors.append(f"line {line_number}: unsupported category {case['category']!r}")
        for field in ("expected_findings", "forbidden_changes"):
            if not isinstance(case[field], list) or not case[field]:
                errors.append(f"line {line_number}: {field} must be a non-empty list")
        for field in ("input", "context"):
            if not isinstance(case[field], str) or not case[field].strip():
                errors.append(f"line {line_number}: {field} must be a non-empty string")
    if count < 20:
        errors.append(f"expected at least 20 cases, found {count}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_file", type=Path)
    args = parser.parse_args(argv)
    if not args.case_file.is_file():
        parser.error(f"file not found: {args.case_file}")
    errors = validate(args.case_file)
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Validated behavioral evaluation cases: {args.case_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
