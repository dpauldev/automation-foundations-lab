import argparse
import json
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Organise a folder of files into subfolders by file type."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path.home() / "Downloads",
        help="Folder to organise (default: the Downloads folder).",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).parent / "config.json",
        help="Path to the config file (default: config.json in the same folder as this script).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="If set, the script will only print what it would do without making any changes.",
    )
    return parser


def check_extension(ext: str, where: str) -> None:
    if not isinstance(ext, str):
        raise ValueError(f"Extension {ext!r} of category {where} is not a String")

    if not ext.startswith("."):
        raise ValueError(
            f"Extension {ext!r} of category {where} does not start with a dot"
        )

    if len(ext) < 2:
        raise ValueError(
            f"Extension {ext!r} of category {where} has nothing after the dot"
        )

    if ext != ext.lower():
        raise ValueError(f"Extension {ext!r} of category {where} is not lower case")


def read_config(path: Path) -> dict:
    file_text = path.read_text(encoding="utf-8")
    data = json.loads(file_text)

    if not isinstance(data, dict):
        raise ValueError("Top level of the config file must be a JSON object")

    return data


def build_lookup(categories: dict) -> dict[str, str]:
    result = {}

    for folder, extensions in categories.items():
        for extn in extensions:
            check_extension(extn, folder)
            if extn in result:
                raise ValueError(
                    f"Extension {extn!r} exists in both {result[extn]} and {folder}"
                )
            result[extn] = folder

    return result


def load_rules(path: Path) -> tuple[dict[str, str], set[str]]:
    data = read_config(path)

    if "categories" not in data:
        raise ValueError("Missing the 'categories' JSON key in config file.")

    if "ignore" not in data:
        raise ValueError("Missing the 'ignore' JSON key in config file.")

    for extn in data["ignore"]:
        check_extension(extn, "ignore")

    lookup = build_lookup(data["categories"])
    ignore_set = set(data["ignore"])

    return lookup, ignore_set


def main() -> None:
    args = build_parser().parse_args()
    print(f"Source: {args.source}")
    print(f"Config: {args.config}")
    print(
        f"Dry run: {args.dry_run}"
    )  # Hyphen isn’t legal inside a Python name. argparse converts it as args.dry_run (with an underscore).
    try:
        lookup, ignore_set = load_rules(args.config)
    except (ValueError, FileNotFoundError) as err:
        print(f"Config error in {args.config}: {err}", file=sys.stderr)
        sys.exit(1)

    print(f"lookup: total number of extension(s) taken care of - {len(lookup)}")
    print(f"ignore set: total number of extension(s) ignored - {len(ignore_set)}")


if __name__ == "__main__":
    main()
