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
    tmp_path = tmp_path / "sub"
    tmp_path2 = tmp_path / "sub2"
    tmp_path.mkdir()
    tmp_path2.mkdir()
    file_path = tmp_path2 / "file1.txt"
    file_path2 = tmp_path2 / "file2.txt"
    task_read_write_2.write_to_file(file_path, file_path2)
    assert (os.path.exists(file_path))
    assert (os.path.exists(file_path2))
