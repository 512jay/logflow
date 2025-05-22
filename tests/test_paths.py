import pytest
from logflow.paths import get_base
from pathlib import Path

def test_get_base_resolves_correct_path():
    base = get_base()
    assert base.exists()
    assert (base / "config.toml").exists()