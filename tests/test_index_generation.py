import pytest
from logflow.idea_index import generate
from logflow.paths import get_base

def test_index_file_created():
    base = get_base()
    generate()
    index_file = base / "idea_index.md"
    assert index_file.exists()
    assert "# 🧠 Idea Index" in index_file.read_text()