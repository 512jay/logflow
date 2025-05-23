import pytest
from logflow.devloop import log_focus_task
from logflow.status import log_pause
from logflow.paths import get_base
from datetime import datetime

def test_focus_and_pause_logged():
    base = get_base()
    today = datetime.now().date().isoformat()
    log_file = base / "daily_logs" / f"{today}.md"

    log_focus_task("pytest focus")
    log_pause()

    content = log_file.read_text()
    assert "pytest focus" in content
    assert "paused session" in content

# def test_focus_inline_parsing(test_logflow_env):
#     from logflow.idea_utils import get_metadata
#     from logflow.devloop import run_focus
#     import rich.console
#     import builtins
#     import logflow.paths

#     # Patch get_base to use the test directory
#     logflow.paths.get_base = lambda: test_logflow_env

#     user_input = "Fix bug --title BugFix --tag cli bug"
#     builtins.input = lambda _: user_input
#     rich.console.Console.input = lambda self, *a, **k: user_input

#     run_focus()

#     ideas = list((test_logflow_env / "ideas").glob("*.md"))
#     assert ideas, "No idea files created"
#     meta = get_metadata(ideas[-1])
#     assert meta["title"] == "BugFix"
#     assert set(meta["tags"]) == {"cli", "bug"}





