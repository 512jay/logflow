# 📦 Changelog

All notable changes to this project will be documented here.

---

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