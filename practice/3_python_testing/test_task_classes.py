"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
import pytest
import sys

sys.path.append('../2_python_part_2')
import task_classes


def test_Teacher():
    tc = task_classes.Teacher("daniil", "test")
    crHomework = tc.create_homework("test", 2)
    assert ("test" == crHomework.text)
    assert (2 == crHomework.deadline)


def test_Student():
    ts = task_classes.Student("daniil", "test")
    tc = task_classes.Teacher("daniil", "test")
    expired_homework = tc.create_homework('Learn functions', 0)
    assert (ts.do_homework(expired_homework) == None)


def test_Negative_Number():
    hw = task_classes.Homework('Learn functions', 10)
    assert (hw.is_active() == False)


def test_Negative_Number():
    hw = task_classes.Homework('Learn functions', -5)
    assert (hw.is_active() == False)