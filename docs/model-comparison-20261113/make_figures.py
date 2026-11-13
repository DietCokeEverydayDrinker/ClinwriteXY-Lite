from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


ROOT = Path(__file__).resolve().parent
SCORES = ROOT / "scores"
DATA = ROOT / "data"
ASSETS = ROOT / "assets"

mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "font.size": 7,
        "axes.titlesize": 8,
        "axes.labelsize": 7,
        "xtick.labelsize": 6.5,
        "ytick.labelsize": 6.5,
        "legend.fontsize": 6.5,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.linewidth": 0.7,
        "legend.frameon": False,
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


ARMS = [
    {
        "blind": "C",
        "advanced_blind": "G",
        "model": "V4 Pro",
        "condition": "Raw",
        "label": "Pro Raw",
        "basic_file": "pro-raw.md",
        "advanced_file": "pro-raw-advanced.md",
    },
    {
        "blind": "E",
        "advanced_blind": "H",
        "model": "V4 Pro",
        "condition": "Lite",
        "label": "Pro Lite",
        "basic_file": "pro-lite.md",
        "advanced_file": "pro-lite-advanced.md",
    },
    {
        "blind": "A",
        "advanced_blind": "I",
        "model": "V4 Pro",
        "condition": "Full",
        "label": "Pro Full",
        "basic_file": "pro-full.md",
        "advanced_file": "pro-full-advanced.md",
    },
    {
        "blind": "F",
        "advanced_blind": "J",
        "model": "V4 Flash",
        "condition": "Raw",
        "label": "Flash Raw",
        "basic_file": "flash-raw.md",
        "advanced_file": "flash-raw-advanced.md",
    },
    {
        "blind": "B",
        "advanced_blind": "K",
        "model": "V4 Flash",
        "condition": "Lite",
        "label": "Flash Lite",
        "basic_file": "flash-lite.md",
        "advanced_file": "flash-lite-advanced.md",
    },
    {
        "blind": "D",
        "advanced_blind": "L",
        "model": "V4 Flash",
        "condition": "Full",
        "label": "Flash Full",
        "basic_file": "flash-full.md",
        "advanced_file": "flash-full-advanced.md",
    },
]

CONDITION_COLORS = {
    "Raw": "#8A8A8A",
    "Lite": "#2A9D8F",
    "Full": "#E76F51",
}

MODEL_MARKERS = {"V4 Pro": "o", "V4 Flash": "s"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def mean(values: list[float]) -> float:
    return float(np.mean(values))


def collect_data() -> tuple[list[dict], list[dict]]:
    pro_basic = load_json(SCORES / "judge-pro-clean.json")
    flash_basic = load_json(SCORES / "judge-flash-clean.json")
    pro_advanced = load_json(SCORES / "judge-pro-advanced.json")
    flash_advanced = load_json(SCORES / "judge-flash-advanced.json")

    basic_rows = []
    advanced_rows = []
    for arm in ARMS:
        basic_cases = {}
        basic_dimensions = {}
        for case in range(1, 6):
            case_key = str(case)
            pro_case = pro_basic["arms"][arm["blind"]]["cases"][case_key]
            flash_case = flash_basic["arms"][arm["blind"]]["cases"][case_key]
            basic_cases[case_key] = mean([pro_case["total"], flash_case["total"]])
            for dimension in ["evidence", "preservation", "prose", "concision", "usefulness"]:
                basic_dimensions.setdefault(dimension, {})[case_key] = mean(
                    [pro_case[dimension], flash_case[dimension]]
                )

        pro_basic_total = pro_basic["arms"][arm["blind"]]["total"]
        flash_basic_total = flash_basic["arms"][arm["blind"]]["total"]
        pro_advanced_total = pro_advanced["arms"][arm["advanced_blind"]]["total"]
        flash_advanced_total = flash_advanced["arms"][arm["advanced_blind"]]["total"]

        basic_path = ROOT / "outputs" / "basic" / arm["basic_file"]
        advanced_path = ROOT / "outputs" / "advanced" / arm["advanced_file"]
        basic_rows.append(
            {
                **arm,
                "pro_score": pro_basic_total,
                "flash_score": flash_basic_total,
                "mean_score": mean([pro_basic_total, flash_basic_total]),
                "cases": basic_cases,
                "dimensions": basic_dimensions,
                "output_chars": len(basic_path.read_text(encoding="utf-8")),
            }
        )
        advanced_rows.append(
            {
                **arm,
                "pro_score": pro_advanced_total,
                "flash_score": flash_advanced_total,
                "mean_score": mean([pro_advanced_total, flash_advanced_total]),
                "output_chars": len(advanced_path.read_text(encoding="utf-8")),
            }
        )
    return basic_rows, advanced_rows


def write_source_data(basic_rows: list[dict], advanced_rows: list[dict]) -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    with (DATA / "scores.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "model",
                "condition",
                "basic_pro_judge",
                "basic_flash_judge",
                "basic_mean",
                "advanced_pro_judge",
                "advanced_flash_judge",
                "advanced_mean",
                "basic_output_chars",
                "advanced_output_chars",
            ]
        )
        for basic, advanced in zip(basic_rows, advanced_rows):
            writer.writerow(
                [
                    basic["model"],
                    basic["condition"],
                    basic["pro_score"],
                    basic["flash_score"],
                    basic["mean_score"],
                    advanced["pro_score"],
                    advanced["flash_score"],
                    advanced["mean_score"],
                    basic["output_chars"],
                    advanced["output_chars"],
                ]
            )

    with (DATA / "case_scores.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["model", "condition", *[f"case_{case}" for case in range(1, 6)]])
        for row in basic_rows:
            writer.writerow(
                [
                    row["model"],
                    row["condition"],
                    *[f"{row['cases'][str(case)]:.1f}" for case in range(1, 6)],
                ]
            )


def add_panel_label(axis: plt.Axes, label: str) -> None:
    axis.text(
        -0.16,
        1.08,
        label,
        transform=axis.transAxes,
        fontsize=10,
        fontweight="bold",
        ha="left",
        va="top",
    )


def style_axis(axis: plt.Axes) -> None:
    axis.tick_params(length=2.2, width=0.6, color="#333333")
    for spine in axis.spines.values():
        spine.set_color("#333333")


def make_figure_1(basic_rows: list[dict], advanced_rows: list[dict]) -> None:
    labels = [row["label"] for row in basic_rows]
    colors = [CONDITION_COLORS[row["condition"]] for row in basic_rows]
    y = np.arange(len(labels))

    fig = plt.figure(figsize=(7.2, 6.1), constrained_layout=True)
    grid = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.05], width_ratios=[1.1, 1.0])

    axis_a = fig.add_subplot(grid[0, 0])
    basic_scores = [row["mean_score"] for row in basic_rows]
    axis_a.barh(y, basic_scores, color=colors, height=0.62)
    axis_a.set_yticks(y, labels)
    axis_a.invert_yaxis()
    axis_a.set_xlim(0, 130)
    axis_a.set_xlabel("Blind score (maximum 125)")
    axis_a.set_title("Five basic writing cases")
    for yi, score in zip(y, basic_scores):
        axis_a.text(score + 1.5, yi, f"{score:.1f}", va="center", fontsize=6.5)
    axis_a.axvline(125, color="#B8B8B8", linewidth=0.6, linestyle=(0, (2, 2)))
    axis_a.text(124, -0.75, "Max", ha="right", va="bottom", color="#6B6B6B", fontsize=6)
    style_axis(axis_a)

    axis_b = fig.add_subplot(grid[0, 1])
    case_matrix = np.array([[row["cases"][str(case)] for case in range(1, 6)] for row in basic_rows])
    case_cmap = LinearSegmentedColormap.from_list(
        "case_score", ["#F3EEE8", "#D8C2AA", "#7FB7AE", "#216C66"]
    )
    image = axis_b.imshow(case_matrix, aspect="auto", cmap=case_cmap, vmin=15, vmax=25)
    axis_b.set_xticks(np.arange(5), [f"C{case}" for case in range(1, 6)])
    axis_b.set_yticks(np.arange(len(labels)), labels)
    axis_b.set_title("Case-level blind score")
    for row_index in range(case_matrix.shape[0]):
        for column_index in range(case_matrix.shape[1]):
            value = case_matrix[row_index, column_index]
            text_color = "white" if value >= 22.5 else "#252525"
            axis_b.text(
                column_index,
                row_index,
                f"{value:.1f}",
                ha="center",
                va="center",
                fontsize=6,
                color=text_color,
            )
    axis_b.tick_params(length=0)
    for spine in axis_b.spines.values():
        spine.set_visible(False)
    colorbar = fig.colorbar(image, ax=axis_b, fraction=0.035, pad=0.02)
    colorbar.set_label("Score / 25")
    colorbar.ax.tick_params(labelsize=6, length=2)
    colorbar.outline.set_linewidth(0.4)

    axis_c = fig.add_subplot(grid[1, 0])
    advanced_scores = [row["mean_score"] for row in advanced_rows]
    axis_c.barh(y, advanced_scores, color=colors, height=0.62)
    axis_c.set_yticks(y, labels)
    axis_c.invert_yaxis()
    axis_c.set_xlim(0, 78)
    axis_c.set_xlabel("Blind score (maximum 75)")
    axis_c.set_title("Three advanced integration cases")
    for yi, score in zip(y, advanced_scores):
        axis_c.text(score + 0.8, yi, f"{score:.1f}", va="center", fontsize=6.5)
    axis_c.axvline(75, color="#B8B8B8", linewidth=0.6, linestyle=(0, (2, 2)))
    axis_c.text(74.4, -0.75, "Max", ha="right", va="bottom", color="#6B6B6B", fontsize=6)
    style_axis(axis_c)

    axis_d = fig.add_subplot(grid[1, 1])
    x = np.arange(len(labels))
    basic_chars = np.array([row["output_chars"] for row in basic_rows])
    advanced_chars = np.array([row["output_chars"] for row in advanced_rows])
    width = 0.36
    axis_d.bar(x - width / 2, basic_chars / 1000, width, color="#C9C9C9", label="Basic cases")
    axis_d.bar(x + width / 2, advanced_chars / 1000, width, color="#333333", label="Advanced cases")
    axis_d.set_xticks(x, labels, rotation=35, ha="right")
    axis_d.set_ylabel("Output characters (thousands)")
    axis_d.set_title("Output volume")
    axis_d.legend(loc="upper left")
    axis_d.set_ylim(0, 14)
    style_axis(axis_d)

    for axis, panel in zip([axis_a, axis_b, axis_c, axis_d], ["a", "b", "c", "d"]):
        add_panel_label(axis, panel)

    fig.suptitle(
        "ClinwriteXY model comparison: quality gains depend on model and task scope",
        fontsize=10,
        fontweight="bold",
        x=0.02,
        ha="left",
    )
    fig.savefig(ASSETS / "figure-1-overall-performance.png", dpi=600, bbox_inches="tight")
    fig.savefig(ASSETS / "figure-1-overall-performance.svg", bbox_inches="tight")
    fig.savefig(ASSETS / "figure-1-overall-performance.pdf", bbox_inches="tight")
    plt.close(fig)


def make_figure_2(basic_rows: list[dict]) -> None:
    labels = [row["label"] for row in basic_rows]
    y = np.arange(len(labels))
    dimensions = [
        ("evidence", "Evidence and claim calibration"),
        ("preservation", "Number and denominator preservation"),
        ("concision", "Concision and template control"),
    ]
    score_cmap = LinearSegmentedColormap.from_list(
        "dimension_score", ["#F4E1DB", "#E8B39E", "#57A49A", "#1D615C"]
    )

    fig, axes = plt.subplots(
        1,
        3,
        figsize=(7.2, 3.25),
        sharey=True,
        constrained_layout=True,
    )
    for axis, (dimension, title) in zip(axes, dimensions):
        matrix = np.array(
            [
                [row["dimensions"][dimension][str(case)] for case in range(1, 6)]
                for row in basic_rows
            ]
        )
        image = axis.imshow(matrix, aspect="auto", cmap=score_cmap, vmin=1, vmax=5)
        axis.set_xticks(np.arange(5), [f"C{case}" for case in range(1, 6)])
        axis.set_yticks(y, labels)
        axis.set_title(title, pad=8)
        for row_index in range(matrix.shape[0]):
            for column_index in range(matrix.shape[1]):
                value = matrix[row_index, column_index]
                text_color = "white" if value >= 4.0 else "#252525"
                axis.text(
                    column_index,
                    row_index,
                    f"{value:.1f}",
                    ha="center",
                    va="center",
                    color=text_color,
                    fontsize=6,
                )
        axis.tick_params(length=0)
        for spine in axis.spines.values():
            spine.set_visible(False)

    colorbar = fig.colorbar(image, ax=axes, fraction=0.025, pad=0.02)
    colorbar.set_label("Score / 5")
    colorbar.ax.tick_params(labelsize=6, length=2)
    colorbar.outline.set_linewidth(0.4)

    for axis, panel in zip(axes, ["a", "b", "c"]):
        add_panel_label(axis, panel)

    fig.suptitle(
        "Case-level score profiles across all five clinical-writing cases",
        fontsize=10,
        fontweight="bold",
        x=0.02,
        ha="left",
    )
    fig.savefig(ASSETS / "figure-2-evidence-preservation.png", dpi=600, bbox_inches="tight")
    fig.savefig(ASSETS / "figure-2-evidence-preservation.svg", bbox_inches="tight")
    fig.savefig(ASSETS / "figure-2-evidence-preservation.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    basic_rows, advanced_rows = collect_data()
    write_source_data(basic_rows, advanced_rows)
    make_figure_1(basic_rows, advanced_rows)
    make_figure_2(basic_rows)


if __name__ == "__main__":
    main()
