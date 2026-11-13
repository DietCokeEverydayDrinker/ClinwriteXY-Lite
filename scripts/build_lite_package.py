#!/usr/bin/env python3
"""Build the minimal installable ClinwriteXY Lite Skill archive."""

from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "SKILL.md",
    "VERSION",
    "LICENSE",
    "README.md",
    "agents/openai.yaml",
    "references/bilingual-abstract-alignment.md",
    "references/claim-and-evidence-boundary.md",
    "references/clinical-writing-contract.md",
    "references/zh-clinical-micro-edit.md",
    "scripts/check_preservation.py",
    "scripts/test_check_preservation.py",
)


def build(output: Path) -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    output.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for relative_path in FILES:
            source = ROOT / relative_path
            if not source.is_file():
                raise FileNotFoundError(f"required package file missing: {relative_path}")
            archive.write(source, f"clinwritexy-lite/{relative_path}")
        archive.writestr(
            "clinwritexy-lite/PACKAGE-MANIFEST.txt",
            "\n".join(
                (
                    f"ClinwriteXY Lite {version}",
                    "Minimal installable Skill package.",
                    "Benchmark materials, Full-condition outputs, evaluation data,",
                    "and repository history are intentionally excluded.",
                    "",
                    *FILES,
                    "PACKAGE-MANIFEST.txt",
                    "",
                )
            ),
        )


def main() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "dist" / f"ClinwriteXY-Lite-{version}-minimal.zip",
    )
    args = parser.parse_args()
    output = args.output.resolve()
    build(output)
    print(f"Built {output} ({output.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
