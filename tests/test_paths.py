from pathlib import Path
from logflow.paths import get_base

def test_get_base_resolves_correct_path():
    base = get_base()
    base.mkdir(parents=True, exist_ok=True)
    config_path = base / "config.toml"
    config_path.write_text(f"[paths]\nlog_dir = '{base.as_posix()}'")
    assert base.exists()
    assert config_path.exists()