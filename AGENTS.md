# Repository Guidelines

## Project Structure & Module Organization
The CLI entry point `kemono-dl.py` forwards to `src.main.main()`. Core modules live in `src/`: `args.py` defines CLI defaults, `main.py` hosts the `downloader` workflow, `helper.py` supplies filesystem and pattern helpers, `logger.py` configures structured logging, `my_yt_dlp.py` wraps embed downloads, and `version.py` tracks the release string. Reference notes sit in `api.md`, and `coomer.st_cookies.txt` provides a sample cookie jar. Downloads write to user-defined paths computed by the templates inside `helper.py`.

## Build, Test, and Development Commands
- `python -m pip install -r requirements.txt` installs requests, BeautifulSoup, Pillow, and yt_dlp.
- `python kemono-dl.py --help` confirms the CLI surface and argument wiring.
- `python kemono-dl.py --simulate --cookies coomer.st_cookies.txt --links https://kemono.cr/SERVICE/user/USERID` dry-runs the downloader without writing files; swap the URL for a safe fixture.
- `python kemono-dl.py --verbose ...` pipes debug logs to stdout and the rotating file defined in `logger.configure_logger`.

## Coding Style & Naming Conventions
Use Python 3.10+ with PEP 8 defaults: 4-space indents, `snake_case` for functions and variables, `CamelCase` for classes. Rely on f-strings for templating and keep imports ordered standard, third-party, local. Log through `src.logger.logger` so verbosity flags and file handlers remain consistent. Keep filename templates ASCII-safe unless you explicitly disable `--restrict-names`.

## Testing Guidelines
No automated suite ships yet. Combine `--simulate` and `--verbose` to inspect control flow, rate limiting, and pattern rendering without touching disk. When introducing regression coverage, add `tests/test_<feature>.py` using `pytest` (install locally via `python -m pip install pytest`) and mock HTTP calls with fixtures shaped like the `/api/v1` payloads in `api.md`.

## Commit & Pull Request Guidelines
Keep commits focused and titled in the imperative mood (`Add Accept header`, `Update requirements.txt`) without trailing periods. Reference related issues in parentheses when relevant. Pull requests should describe behavior changes, list manual verification commands, and mention any impact to download destinations or API limits.

## Security & Configuration Tips
Never commit live cookie files; `.gitignore` already excludes them. Scrub user IDs and titles from examples. Prefer increasing `--ratelimit-sleep` over custom retry loops when services throttle requests, and note any such adjustments in reviews.
