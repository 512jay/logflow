# 📦 Changelog

All notable changes to this project will be documented here.

## [v0.1.5] - 2025-05-23

Logflow reaches its first public-ready milestone with export support, notes, and a full metadata system. 🎉

### ✨ New Features
- ✅ Added `logflow export` with markdown/CSV output, filtering by tag/status
- ✅ Added `logflow note` to log timestamped notes and append to idea files
- ✅ `logflow status` now reliably shows the current task or paused state
- ✅ Ideas now include YAML frontmatter with metadata (ID, Title, Tags, Status)
- ✅ `logflow add` auto-generates clean metadata using YAML block
- ✅ Legacy `.md` files are gracefully skipped with warnings during export
- ✅ CLI now supports safe ID sequencing (no reuse after deletes)
- ✅ `logflow purge`, `history`, `focus`, and `index` fully verified
- ✅ Future roadmap added internally as ideas using Logflow itself

### 🔧 Improvements
- Improved CLI error messages and fallback behaviors
- Added debug output for export filters
- Gracefully skips and logs issues with broken idea files
- Confirmed compatibility with pipx and poetry workflows

### 📁 Developer Experience
- Roadmap logged using Logflow itself
- Supports rich + slugify optional dependencies
- Clean YAML metadata in all idea files


## [v0.1.4] – Docs & Publishing Polish

📘 **Docs:**
- Fixed broken Quickstart Guide link on PyPI
- Added PyPI, Downloads, CI, and License badges to `README.md`
- Clarified install instructions with `pipx` recommendation

🚀 **Release:**
- Confirmed GitHub Actions workflow triggers on tag
- Verified `release.yml` supports publishing to PyPI via secrets

✨ **Other:**
- Cleaned up CLI output for `init` and `focus`
- Confirmed pipx install works reliably from PyPI

## [v0.1.3] – Bootstrap Fix & pipx Compatibility

🛠 **Bugfix:**
- Fixed critical import-time crash when running `logflow init` before a config file existed
- Now fully supports first-time installs via PyPI and pipx without errors

✨ **Improvements:**
- Deferred config loading until needed (`devloop.py` patched)
- Added support for safe fresh installs on managed Python environments (PEP 668)
- Compatible with pipx and PyPI global usage

---

## [v0.1.2] – (Skipped / Tag Correction)

- Tag correction from previous typo commit (`Realase v0.1.2`)

## [v0.1.0] – Initial Release

🎉 First public release of Logflow — a focused journaling and idea-tracking CLI for developers.

### ✨ Features

- `logflow add` – Add quick thoughts or structured ideas with title/body/tag
- `logflow focus` – Start a dev session with idea tracking and git status
- `logflow status` – Show current task + time tracking
- `logflow pause` – Mark end of work session
- `logflow history` – Browse previous tasks
- `logflow index` – View all structured ideas
- `logflow complete` / `delete` / `purge` – Manage idea lifecycle
- `logflow help` – Built-in command list

### 🧩 Optional Extras

- `rich` for colorized CLI output
- `python-slugify` for emoji-safe filenames

### 🧪 Testing

- Lifecycle tests for add → complete → delete → purge
- Config resolution and nested directory awareness
- Index filtering by status

### 🛠 Dev Tools

- Poetry-based project structure
- Optional extras defined in `pyproject.toml`

---

This version is ready for personal use and early contributors. Feedback welcome!