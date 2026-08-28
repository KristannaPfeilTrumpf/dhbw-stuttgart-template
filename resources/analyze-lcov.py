#!/usr/bin/env python3
"""Aggregiert eine LCOV-Datei nach den Frontend-Bereichen der Arbeit."""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Coverage:
    files: int = 0
    lines_found: int = 0
    lines_hit: int = 0
    functions_found: int = 0
    functions_hit: int = 0
    branches_found: int = 0
    branches_hit: int = 0

    def add_record(self, record: dict[str, object]) -> None:
        self.files += 1
        self.lines_found += int(record.get("LF", 0))
        self.lines_hit += int(record.get("LH", 0))
        self.functions_found += int(record.get("FNF", 0))
        self.functions_hit += int(record.get("FNH", 0))
        self.branches_found += int(record.get("BRF", 0))
        self.branches_hit += int(record.get("BRH", 0))

    @staticmethod
    def percentage(hit: int, found: int) -> float:
        return 100.0 * hit / found if found else 0.0

    def percentages(self) -> tuple[float, float, float]:
        return (
            self.percentage(self.branches_hit, self.branches_found),
            self.percentage(self.functions_hit, self.functions_found),
            self.percentage(self.lines_hit, self.lines_found),
        )


def parse_value(line: str) -> tuple[str, int] | None:
    key, separator, value = line.partition(":")
    if not separator:
        return None
    try:
        return key, int(value.split(",", 1)[0])
    except ValueError:
        return None


def parse_lcov(path: Path) -> list[tuple[str, Coverage]]:
    records: list[tuple[str, Coverage]] = []
    current_path: str | None = None
    current_values: dict[str, object] = {}

    def finish_record() -> None:
        nonlocal current_path, current_values
        if current_path is not None:
            coverage = Coverage()
            coverage.add_record(current_values)
            records.append((current_path, coverage))
        current_path = None
        current_values = {}

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise RuntimeError(f"LCOV-Datei konnte nicht gelesen werden: {error}") from error

    for line in lines:
        if line.startswith("SF:"):
            if current_path is not None:
                finish_record()
            current_path = line[3:].replace("\\", "/")
        elif line == "end_of_record":
            finish_record()
        else:
            parsed = parse_value(line)
            if parsed is not None:
                key, value = parsed
                current_values[key] = value

    finish_record()
    return records


AREA_ORDER = [
    "Shared",
    "Guards",
    "features/experiment-dashboard",
    "features/experiment-report-preview",
    "features/experiment-wizard",
    "features/search-strategie",
    "features/tools",
    "services",
    "layout",
    "UI-Components",
]


def classify(source_path: str) -> str | None:
    """Ordnet einen Pfad einer der vorgegebenen Architekturgruppen zu."""
    parts = [part for part in source_path.split("/") if part]
    try:
        app_index = parts.index("app")
    except ValueError:
        return None

    app_parts = parts[app_index + 1 :]
    if not app_parts:
        return None

    first = app_parts[0]
    if first == "features" and len(app_parts) > 1:
        feature = f"features/{app_parts[1]}"
        return feature if feature in AREA_ORDER else None
    if first == "components":
        return "UI-Components"
    if first == "shared":
        return "Shared"
    if first == "guards":
        return "Guards"
    if first in {"services", "layout"}:
        return first
    return None


def aggregate(records: list[tuple[str, Coverage]]) -> dict[str, Coverage]:
    result = {area: Coverage() for area in AREA_ORDER}
    for source_path, coverage in records:
        group = classify(source_path)
        if group is None:
            continue
        result[group].files += coverage.files
        result[group].lines_found += coverage.lines_found
        result[group].lines_hit += coverage.lines_hit
        result[group].functions_found += coverage.functions_found
        result[group].functions_hit += coverage.functions_hit
        result[group].branches_found += coverage.branches_found
        result[group].branches_hit += coverage.branches_hit
    return result


def format_percentage(value: float) -> str:
    return f"{value:.1f}%"


def rows(aggregated: dict[str, Coverage]) -> list[list[str]]:
    result: list[list[str]] = []
    for group in AREA_ORDER:
        coverage = aggregated[group]
        branches, functions, lines = coverage.percentages()
        result.append(
            [
                group,
                str(coverage.files),
                format_percentage(branches),
                format_percentage(functions),
                format_percentage(lines),
                f"{coverage.lines_hit}/{coverage.lines_found}",
            ]
        )
    return result


def print_table(aggregated: dict[str, Coverage]) -> None:
    header = ["Bereich", "Dateien", "Branches", "Functions", "Lines", "Lines (getroffen/gesamt)"]
    table = [header, *rows(aggregated)]
    widths = [max(len(row[index]) for row in table) for index in range(len(header))]
    for row_index, row in enumerate(table):
        print("  ".join(value.ljust(widths[index]) for index, value in enumerate(row)))
        if row_index == 0:
            print("  ".join("-" * width for width in widths))


def write_csv(aggregated: dict[str, Coverage], path: Path) -> None:
    try:
        with path.open("w", newline="", encoding="utf-8") as output:
            writer = csv.writer(output)
            writer.writerow(["Bereich", "Dateien", "Branches", "Functions", "Lines", "Lines getroffen", "Lines gesamt"])
            for row, coverage in zip(rows(aggregated), (aggregated[group] for group in AREA_ORDER)):
                writer.writerow([row[0], row[1], row[2], row[3], row[4], coverage.lines_hit, coverage.lines_found])
    except OSError as error:
        raise RuntimeError(f"CSV-Datei konnte nicht geschrieben werden: {error}") from error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lcov", type=Path, help="Pfad zur lcov.info-Datei")
    parser.add_argument("--csv", type=Path, help="Optionaler Pfad fuer eine CSV-Ausgabe")
    args = parser.parse_args()

    try:
        records = parse_lcov(args.lcov)
        if not records:
            raise RuntimeError("Die LCOV-Datei enthaelt keine Quelldatei-Datensaetze.")
        aggregated = aggregate(records)
        print_table(aggregated)
        if args.csv:
            write_csv(aggregated, args.csv)
            print(f"\nCSV-Ausgabe: {args.csv}")
    except RuntimeError as error:
        print(f"Fehler: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
