"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""
import sys

sys.path.append('../2_python_part_2')
import task_exceptions


def test_division_ok(capsys):
    task_exceptions.division(4, 2)
    captured = capsys.readouterr()
    str = ('2\nDivision finished\n')
    assert captured.out == str


def test_division_by_zero(capfd):
    task_exceptions.division(1, 0)
    out, err = capfd.readouterr()
    assert out == "Division by 0\n"


def test_division_by_one(capfd):
    task_exceptions.division(1, 1)
    out, err = capfd.readouterr()
    str = ('DivisionByOneException("Deletion on 1 get the same result")\n')
    assert out == str
