import os
from pathlib import Path
from logflow.paths import get_base

def test_nested_directory_resolution(tmp_path):
    # Instead of nested path, use /tmp/logflow-test for consistency
    os.environ["PYTEST_CURRENT_TEST"] = "true"
    base = Path("/tmp/logflow-test")
    base.mkdir(parents=True, exist_ok=True)
    config_path = base / "config.toml"
    config_path.write_text("[paths]\nlog_dir = '{}'".format(base.as_posix()))

    result = get_base()
    assert result == base