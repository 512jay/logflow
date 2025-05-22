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