#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path


PACKAGE_ROOTS = ("low-code", "high-code")
REQUIRED_DOCS = ("DEVELOPMENT.md", "USAGE.md")


def package_directories(base_dir: Path) -> list[Path]:
    packages: list[Path] = []

    for root_name in PACKAGE_ROOTS:
        root_dir = base_dir / root_name
        if not root_dir.is_dir():
            continue

        packages.extend(
            sorted(
                child
                for child in root_dir.iterdir()
                if child.is_dir() and not child.name.startswith(".")
            )
        )

    return packages


def validate_package(package_dir: Path, base_dir: Path) -> list[str]:
    issues: list[str] = []

    for required_doc in REQUIRED_DOCS:
        if not (package_dir / required_doc).is_file():
            issues.append(f"missing {required_doc}")

    component_directories = [
        child
        for child in package_dir.iterdir()
        if child.is_dir() and not child.name.startswith(".")
    ]
    if not component_directories:
        issues.append("missing component directory")

    if issues:
        relative_path = package_dir.relative_to(base_dir).as_posix()
        return [f"{relative_path}: {issue}" for issue in issues]

    return []


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the minimum structure required for Salesforce sample packages."
    )
    parser.add_argument(
        "base_dir",
        nargs="?",
        default=".",
        help="Repository root to validate. Defaults to the current directory.",
    )
    args = parser.parse_args()

    base_dir = Path(args.base_dir).resolve()
    packages = package_directories(base_dir)

    if not packages:
        print("No packages found in low-code/ or high-code/.")
        return 0

    errors: list[str] = []
    for package_dir in packages:
        errors.extend(validate_package(package_dir, base_dir))

    if errors:
        print("Package validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(packages)} package(s) successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
