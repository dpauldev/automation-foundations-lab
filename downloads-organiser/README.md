# Downloads Organiser (work in progress)

Will sort files in a folder (default: `~/Downloads`) into category subfolders by file extension. Started as a scaffold exercise from my automation learning plan (argparse setup, config-file shape, folder structure) and is now being built up step by step.

## Status
Done: argparse setup, config file shape, and the config loader (reads and validates `config.json`, with clear one-line errors and a non-zero exit code on failure).
To do: scan the source folder, classify each file (move, ignore or unknown), and move files (with `--dry-run` support).

## Layout
- `organiser.py`: behaviour (how to organise); currently parses arguments, loads and validates the config, and prints a summary
- `config.json`: data (what goes where)
- `README.md`: intent (why it works this way)

## Usage
uv run downloads-organiser/organiser.py [--source FOLDER] [--config FILE] [--dry-run]

| Argument | Default | Meaning |
|---|---|---|
| `--source` | `~/Downloads` | Folder to organise |
| `--config` | `config.json` beside the script | Rules file |
| `--dry-run` | off | Print what would happen; change nothing |

## Config shape
`config.json` has two top-level sections:
- `categories`: folder name -> list of extensions (lowercase, with the leading dot)
- `ignore`: extensions that are never touched (half-finished browser downloads)

## Design decisions
- Unknown extensions are flagged in a report, never moved.
- Folders are skipped; files with no extension count as unknown.
- Extensions are compared in lowercase (`HEIC` matches `.heic`).
- Each extension may appear in only one category; the loader checks this and stops with a clear error naming both categories, because JSON validity does not catch it.
- Anything in `ignore` is never touched.
- Dry run is a rehearsal that changes nothing.
- Test against a throwaway sandbox folder, never the real Downloads.

## AI Disclosure
Building along with Claude: designed and written by me, with Claude AI used as a first-principles teaching tool and reviewer throughout (argparse, config design, repo layout). The code is my own; this README was drafted by Claude from decisions we made together.
