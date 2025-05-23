````md
# Logflow

[![PyPI version](https://img.shields.io/pypi/v/logflow-cli.svg)](https://pypi.org/project/logflow-cli/)  
[![PyPI - Downloads](https://img.shields.io/pypi/dm/logflow-cli.svg)](https://pypi.org/project/logflow-cli/)  
[![CI](https://github.com/512jay/logflow/actions/workflows/release.yml/badge.svg)](https://github.com/512jay/logflow/actions/workflows/release.yml)  
[![License](https://img.shields.io/github/license/512jay/logflow.svg)](https://github.com/512jay/logflow/blob/main/LICENSE)

[📘 Quickstart Guide](https://github.com/512jay/logflow/blob/main/docs/quickstart.md) – Learn how to install and use Logflow in minutes.


💡 **Tip:** For the best experience, install with extras:

```bash
pipx install logflow-cli[rich,fancy_slugs]
```

This enables rich terminal output and emoji-safe filenames.

---

## 🧠 How Logflow Stores Data

By default, Logflow stores all your developer thoughts in:

```bash
./logflow/
```

This directory includes:

- `daily_logs/` – developer check-ins
- `ideas/` – structured Markdown idea files
- `idea_log.md` – append-only quick thought list
- `completed_log.md` – a snapshot of done ideas
- `next_id.txt` – internal idea counter
- `config.toml` – optional config file

### Example Config:

```toml
[paths]
log_dir = "logflow"
scan_root = "parent"
max_recent_ideas = 5
```

Run `logflow init` to generate this layout and config.

---

Or forcibly regenerate:

```bash
logflow init --force
```

---

## 💡 Use Cases

* Solo dev journaling
* Idea tracking across projects
* Developer time tracking & status reporting
* Task queue for future sprints

---

## 📘 Command Cheat Sheet

```bash
logflow add "Idea"               # Quick log
logflow add "X" --title T --body B --tag TAG

logflow recent                   # Show recent ideas
logflow index                    # Structured idea index

logflow focus                    # Start dev work
logflow status                   # What am I working on?
logflow pause                    # Mark break/end of session

logflow complete 007             # Mark done
logflow delete slug_or_id        # Soft delete
logflow purge                    # Trash cleanup

logflow history --summary        # View logs
logflow init --force             # Regenerate config & folders
logflow help                     # Command list
```

---

## 🎯 Philosophy

Logflow is designed to:

* Work with or without Git
* Require zero setup, but allow full config
* Help developers reflect, prioritize, and focus

It's built for long-term sustainability of developer thought.

---

## 🔓 License

MIT

---

### 📣 Maintained by [Oravox LLC](mailto:oravoxco@gmail.com) — freely available for solo devs, teams, and contributors.

```

---

Let me know if you'd like:
- A PR-ready version of this
- The `quickstart.md` file scaffolded and saved
- A next-version dev checklist for `v0.1.5` planning
```


### ✨ New in v0.1.5

#### `logflow export`
Export your backlog or roadmap to a markdown table or CSV file.

```bash
logflow export --tag internal --format table
logflow export --format csv --output backlog.csv
```

#### `logflow note`
Log mid-task notes to the daily log, and optionally append them to an idea file.

```bash
logflow note "Clarified export logic"
logflow note "Linked to issue" --id 002
```

#### YAML Frontmatter Metadata
All idea files now include structured frontmatter:

```yaml
---
ID: 002
Title: Export feature
Tags: internal
Status: Active
Created: 2025-05-22 20:58
---
```