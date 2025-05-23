from logflow.idea_utils import get_tag

def test_multi_tag_parsing(tmp_path):
    f = tmp_path / "001_test.md"
    f.write_text("""---
ID: 001
Title: Test
Tags:
  - cli
  - ux
  - error-handling
---

Some body
""")
    assert get_tag(f) == ["cli", "ux", "error-handling"]