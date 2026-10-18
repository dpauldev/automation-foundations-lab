# Downloads Organiser (scaffold)

Will sort files in a folder (default: `~/Downloads`) into category subfolders by file extension. Scaffold exercise from my automation learning plan: argparse setup, config-file shape, folder structure. **No full build yet.**

## Status
Scaffold only. Argparse and the config shape are done. The config loader and the file mover are not built yet.

## Layout
- `organiser.py`: behaviour (how to organise); currently parses arguments and prints them
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
- Each extension may appear in only one category; the loader must check this and stop with a clear error, because JSON validity does not catch it.
- Anything in `ignore` is never touched.
- Dry run is a rehearsal that changes nothing.
- Test against a throwaway sandbox folder, never the real Downloads.

## AI Disclosure
Building along with Claude: designed and written by me, with Claude AI used as a first-principles teaching tool and reviewer throughout (argparse, config design, repo layout). The code is my own; this README was drafted by Claude from decisions we made together.
