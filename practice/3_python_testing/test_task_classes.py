"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
import sys

sys.path.append('../2_python_part_2')
import task_classes


def test_teacher():
    tc_teacher = task_classes.Teacher("daniil", "test")
    cr_homework = tc_teacher.create_homework("test", 2)
    assert "test" == cr_homework.text
    assert 2 == cr_homework.deadline


def test_student():
    tc_student = task_classes.Student("daniil", "test")
    tc_teacher = task_classes.Teacher("daniil", "test")
    expired_homework = tc_teacher.create_homework('Learn functions', 0)
    assert tc_student.do_homework(expired_homework) is None


def test_normal_number():
    hw = task_classes.Homework('Learn functions', 10)
    assert hw.is_active() is True


def test_negative_number():
    hw = task_classes.Homework('Learn functions', -5)
    assert hw.is_active() is False
