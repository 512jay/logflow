import pytest
from pathlib import Path
from logflow.idea import log, complete, delete, purge_trash
from logflow.paths import get_base

def test_idea_add_complete_delete_purge(tmp_path):
    base = get_base()
    idea_dir = base / "ideas"
    trash_dir = idea_dir / "trash"
    completed_dir = idea_dir / "completed"

    idea_file = log("Test idea", title="Lifecycle Test", tag="pytest")
    idea_id = idea_file.stem.split("_")[0]

    complete(idea_id)
    completed_file = completed_dir / idea_file.name
    assert completed_file.exists()

    delete(idea_id)
    trashed_file = trash_dir / idea_file.name
    assert trashed_file.exists()

    purge_trash()
    assert not trashed_file.exists()

