from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw-clean"
BLIND = ROOT / "blind-clean"
SCORES = ROOT / "scores"

LABELS = {
    "A": "pro-full",
    "B": "flash-lite",
    "C": "pro-raw",
    "D": "flash-full",
    "E": "pro-lite",
    "F": "flash-raw",
}


def main() -> None:
    missing = [
        source
        for source in LABELS.values()
        if not (RAW / f"{source}.md").is_file()
    ]
    if missing:
        raise SystemExit(f"Missing clean outputs: {', '.join(missing)}")

    BLIND.mkdir(parents=True, exist_ok=True)
    for label, source in LABELS.items():
        text = (RAW / f"{source}.md").read_text(encoding="utf-8")
        text = text.replace("ClinwriteXY Lite", "the assigned workflow")
        text = text.replace("ClinwriteXY", "the assigned workflow")
        (BLIND / f"{label}.md").write_text(text.rstrip() + "\n", encoding="utf-8")

    SCORES.mkdir(parents=True, exist_ok=True)
    (SCORES / "blind-clean-key.json").write_text(
        json.dumps(LABELS, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Prepared {len(LABELS)} clean blind outputs")


if __name__ == "__main__":
    main()
