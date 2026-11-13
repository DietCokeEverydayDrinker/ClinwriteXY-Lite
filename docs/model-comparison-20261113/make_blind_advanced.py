from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw"
BLIND = ROOT / "blind"
SCORES = ROOT / "scores"

LABELS = {
    "G": "pro-raw-advanced",
    "H": "pro-lite-advanced",
    "I": "pro-full-advanced",
    "J": "flash-raw-advanced",
    "K": "flash-lite-advanced",
    "L": "flash-full-advanced",
}


def anonymise(text: str) -> str:
    replacements = {
        "ClinwriteXY Lite": "the assigned workflow",
        "ClinwriteXY Full": "the assigned workflow",
        "ClinwriteXY": "the assigned workflow",
        "Lite scope boundary": "Scope boundary",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    text = re.sub(r"\bLite\b", "the assigned workflow", text)
    return text


def main() -> None:
    missing = [
        source
        for source in LABELS.values()
        if not (RAW / f"{source}.md").is_file()
    ]
    if missing:
        raise SystemExit(f"Missing advanced outputs: {', '.join(missing)}")

    BLIND.mkdir(parents=True, exist_ok=True)
    for label, source in LABELS.items():
        text = (RAW / f"{source}.md").read_text(encoding="utf-8")
        (BLIND / f"{label}.md").write_text(
            anonymise(text).rstrip() + "\n",
            encoding="utf-8",
        )

    SCORES.mkdir(parents=True, exist_ok=True)
    (SCORES / "blind-advanced-key.json").write_text(
        json.dumps(LABELS, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Prepared {len(LABELS)} advanced blind outputs")


if __name__ == "__main__":
    main()
