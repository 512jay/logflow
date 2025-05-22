import pytest
from pathlib import Path
from logflow.paths import get_base

def test_nested_directory_resolution(tmp_path, monkeypatch):
    nested = tmp_path / "level1" / "level2"
    nested.mkdir(parents=True)
    base = tmp_path / "logflow"
    (base / "config.toml").parent.mkdir(parents=True, exist_ok=True)
    (base / "config.toml").write_text("[paths]\nlog_dir = '{}'".format(base.as_posix()))

    monkeypatch.chdir(nested)
    assert get_base().as_posix() == base.as_posix()