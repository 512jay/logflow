import pytest
from pathlib import Path
from logflow.init import initialize_logflow
import os

@pytest.fixture
def test_logflow_env(tmp_path):
    test_root = tmp_path
    os.chdir(test_root)
    initialize_logflow(force=True)
    return test_root / "logflow"

