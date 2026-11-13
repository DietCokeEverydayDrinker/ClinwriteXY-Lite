from __future__ import annotations

import json
import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw"
REPORT = ROOT / "scores" / "deterministic-checks.json"

NUMBER_CHECKS = {
    1: ["1,702", "851", "0.72", "0.63", "0.81", "0.64", "0.58", "0.70"],
    2: [
        "220,089",
        "8,459",
        "3.84%",
        "11.6",
        "1.30",
        "1.11",
        "1.52",
        "1.62",
        "1.32",
        "1.99",
        "13.5%",
    ],
    3: ["32", "53.1%", "21.9%", "25.0%", "58.3%", "65.0%", "50.0%", "72.2%"],
    4: [
        "30",
        "4.77%",
        "20",
        "66.7%",
        "10",
        "33.3%",
        "26",
        "86.7%",
        "4",
        "13.3%",
        "28/30",
        "93.3%",
        "64",
        "3/30",
        "10.0%",
        "56.5%",
        "45.9%",
        "37.5%",
    ],
    5: [
        "30",
        "4.77%",
        "20/30",
        "66.7%",
        "10/30",
        "33.3%",
        "26/30",
        "86.7%",
        "4/30",
        "13.3%",
        "28/30",
        "93.3%",
        "64",
        "3/30",
        "10.0%",
        "56.5%",
        "45.9%",
        "37.5%",
    ],
}

CONCEPT_CHECKS = {
    1: {
        "internal-validation": ["internal validation", "internal-validation"],
        "external-validation": ["external validation", "external-validation"],
        "no-clinical-utility": ["clinical utility", "decision", "workflow"],
    },
    2: {
        "observational": ["observational", "cohort"],
        "residual-confounding": ["confound"],
        "non-causal": ["causal", "causation", "causal pathway"],
    },
    3: {
        "retrospective": ["retrospective"],
        "single-centre": ["single-centre", "single center"],
        "small-sample": ["sample size", "32 patients"],
    },
    4: {
        "claim-boundary": ["回顾性", "单中心", "证据", "不能"],
    },
    5: {
        "sample-size-error": ["32", "30"],
        "efs-error": ["45.9%", "37.5%"],
        "claim-strength": ["cure", "standard treatment", "durable"],
    },
}


def normalise(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = text.replace("\u2212", "-")
    return re.sub(r"\s+", " ", text)


def case_sections(text: str) -> dict[int, str]:
    matches = list(re.finditer(r"(?im)^#+\s*Case\s*([1-5])\s*$", text))
    sections: dict[int, str] = {}
    for index, match in enumerate(matches):
        case = int(match.group(1))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[case] = text[match.end() : end].strip()
    return sections


def word_count(text: str) -> int:
    return len(re.findall(r"\b[A-Za-z0-9][A-Za-z0-9'’-]*\b", text))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=RAW)
    parser.add_argument("--output", type=Path, default=REPORT)
    args = parser.parse_args()
    raw = args.input.resolve()
    report = args.output.resolve()
    results = {}
    for path in sorted(raw.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        sections = case_sections(text)
        arm = {
            "bytes": path.stat().st_size,
            "cases_present": sorted(sections),
            "cases": {},
        }
        for case, body in sections.items():
            body_norm = normalise(body)
            checks = []
            for token in NUMBER_CHECKS.get(case, []):
                checks.append(
                    {
                        "type": "number",
                        "token": token,
                        "present": token.lower() in body_norm.lower(),
                    }
                )
            for label, alternatives in CONCEPT_CHECKS.get(case, {}).items():
                checks.append(
                    {
                        "type": "concept",
                        "token": label,
                        "present": any(
                            alternative.lower() in body_norm.lower()
                            for alternative in alternatives
                        ),
                    }
                )
            arm["cases"][str(case)] = {
                "word_count": word_count(body),
                "character_count": len(body),
                "checks": checks,
                "missing": [
                    check["token"] for check in checks if not check["present"]
                ],
            }
        results[path.name] = arm

    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {report}")
    for name, arm in results.items():
        missing = sum(len(case["missing"]) for case in arm["cases"].values())
        widths = {
            case: details["word_count"]
            for case, details in arm["cases"].items()
            if case in {"1", "2", "3"}
        }
        print(f"{name}: cases={arm['cases_present']} word_counts={widths} missing={missing}")


if __name__ == "__main__":
    main()
