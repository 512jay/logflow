````md
# 🚀 Logflow Quickstart

Welcome to **Logflow CLI** — a focused journaling and ideation loop for developers.

---

## 📦 Installation (Recommended via pipx)

```bash
pip install pipx
pipx ensurepath
pipx install logflow-cli[rich,slugify]
````

This installs Logflow globally with optional extras:

* `rich` → beautiful terminal formatting
* `python-slugify` → emoji- and symbol-safe filenames

---

## 🧪 First Commands to Try

```bash
logflow init
logflow add "Set up Logflow on my new machine"
logflow focus
logflow pause
logflow status
```

These commands will:

* Create your config
* Add your first idea
* Start a dev session
* End a session
* Show current task

---

## 🗂 Where Data is Stored

By default, Logflow uses:

```bash
~/.logflow/
```

This includes:

* `daily_logs/` – your developer logs
* `idea_log.md` – list of quick thoughts
* `ideas/` – structured idea files
* `ideas/completed/` – done ideas
* `ideas/trash/` – soft-deleted ideas

Customize with:

* `LOGFLOW_HOME` env var
* Or `config.toml` inside your repo/project

---

## 🛠 Customize Your Workflow

Set aliases in your shell config:

```bash
alias lf="logflow focus"
alias la="logflow add"
alias ls="logflow status"
```

Or add a VS Code task:

```json
{
  "label": "Logflow: Focus",
  "type": "shell",
  "command": "logflow focus"
}
```

---

## 📚 Want More?

* [📘 PyPI Project Page](https://pypi.org/project/logflow-cli/)
* [💻 GitHub Repository](https://github.com/512jay/logflow)
* Run `logflow help` to see the full command list

✨ Enjoy the flow.

```
---

### ✨ New in v0.1.5

- `logflow export` for table or CSV exports
- `logflow note` to log timestamped thoughts
- YAML frontmatter metadata for all ideas