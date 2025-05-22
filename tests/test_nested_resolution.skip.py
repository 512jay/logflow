from pathlib import Path
from logflow.paths import get_base

def test_nested_directory_resolution():
    base = get_base()
    config_path = base / "config.toml"
    base.mkdir(parents=True, exist_ok=True)
    config_path.write_text(f"[paths]\nlog_dir = '{base.as_posix()}'")
    result = get_base()
    assert result == base
    assert config_path.exists()