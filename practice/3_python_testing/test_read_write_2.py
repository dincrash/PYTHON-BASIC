"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import sys
import os

sys.path.append('../2_python_part_2')
import task_read_write_2


def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d2 = tmp_path / "sub2"
    d.mkdir()
    d2.mkdir()
    p = d / "file1.txt"
    p2 = d2 / "file2.txt"
    task_read_write_2.write_to_file(p, p2)
    assert (os.path.exists(p))
    assert (os.path.exists(p2))
