# tests/test_idea.py

import pytest
from pathlib import Path
from logflow import idea

@pytest.fixture
def patch_base(monkeypatch, tmp_path):
    """Force get_base() to return temp path for tests."""
    monkeypatch.setattr("logflow.idea.get_base", lambda: tmp_path)
    return tmp_path


def test_log_creates_file(patch_base):
    idea.log("Test summary", title="Test Idea", body="This is a body.", tag="unit")

    idea_dir = patch_base / "ideas"
    files = list(idea_dir.glob("*.md"))
    assert len(files) == 1

    content = files[0].read_text()
    assert "# Test Idea" in content
    assert "Tags: unit" in content
    assert "Status: Active" in content
    assert "Hash:" in content
    assert "---" in content
    assert "Test summary" in content
    assert "This is a body." in content

def test_get_next_id_increments(patch_base):
    idea.log("First idea")
    id1 = idea.get_next_id()
    idea.log("Second idea")
    id2 = idea.get_next_id()
    assert id2 == id1 + 1

