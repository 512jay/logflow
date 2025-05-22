# 🚀 Logflow Quickstart

Welcome to **Logflow CLI** — a focused journaling and ideation loop for developers.

---

## 📦 Installation

You can install Logflow globally with:

```bash
pip install logflow-cli
```

Or with Poetry:

```bash
poetry add logflow-cli
```

---

## 🧪 First Commands to Try

```bash
logflow add "Set up Logflow on my new machine"
logflow focus
logflow pause
logflow status
```

These will log your first idea, start a dev session, stop it, and check your current task — all saved to markdown.

---

## 🗂 Where Data is Stored

By default, Logflow uses:

```
~/.logflow/
```

This includes:

- `daily_logs/` – your developer logs
- `idea_log.md` – list of quick thoughts
- `ideas/` – structured idea files
- `completed/` and `trash/` folders for status transitions

You can override the location via `LOGFLOW_HOME` or `config.toml`.

---

## 🛠 Customize Your Workflow

You can create aliases in your `.zshrc` or `.bashrc`:

```bash
alias lf="logflow focus"
alias la="logflow add"
alias ls="logflow status"
```

Or define a VS Code task:

```json
{
  "label": "Logflow: Focus",
  "type": "shell",
  "command": "logflow focus"
}
```

---

## 📚 Want More?

See:

- [PyPI page](https://pypi.org/project/logflow-cli/)
- [GitHub repo](https://github.com/512jay/logflow)
- `logflow help` for built-in commands

Enjoy the flow ✨