"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

import sys
import os

sys.path.append('../2_python_part_2')
import task_read_write

def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "result.txt"
    task_read_write.read_write(p)
    assert (os.path.exists(p))