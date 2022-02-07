"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import sys

sys.path.append('../2_python_part_2')
import task_read_write_2
import os
# print(task_read_write_2.generate_words(5))
# task_read_write_2.write_to_file()

CONTENT = "content"


def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    task_read_write_2.write_to_file(p)
    print(p.read_text())


    #assert p.read_text() == CONTENT
    #assert len(list(tmp_path.iterdir())) == 1

