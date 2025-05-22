import pytest
from pathlib import Path
from logflow.idea import log, complete, delete, purge_trash
from logflow.paths import get_base

def test_idea_add_complete_delete_purge(tmp_path):
    # Set up
    base = get_base()
    idea_dir = base / "ideas"
    trash_dir = idea_dir / "trash"
    completed_dir = idea_dir / "completed"

    log("Test idea", title="Lifecycle Test", tag="pytest")

    matches = list(idea_dir.glob("*_test_idea.md"))
    assert matches, "Idea not created"
    idea_file = matches[0]

    complete(idea_file.stem.split("_")[0])
    completed_file = completed_dir / idea_file.name
    assert completed_file.exists()

    delete(completed_file.stem.split("_")[0])
    trashed_file = trash_dir / idea_file.name
    assert trashed_file.exists()

    purge_trash()
    assert not trashed_file.exists()