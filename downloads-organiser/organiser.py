import argparse
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


def main() -> None:
    args = build_parser().parse_args()
    print(f"Source: {args.source}")
    print(f"Config: {args.config}")
    print(
        f"Dry run: {args.dry_run}"
    )  # Hyphen isn’t legal inside a Python name. argparse converts it as args.dry_run (with an underscore).


if __name__ == "__main__":
    main()
