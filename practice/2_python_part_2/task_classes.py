"""
Create 3 classes with interconnection between them (Student, Teacher,
Homework)
Use datetime module for working with date/time
1. Homework takes 2 attributes for __init__: tasks text and number of days to complete
Attributes:
    text - task text
    deadline - datetime.timedelta object with date until task should be completed
    created - datetime.datetime object when the task was created
Methods:
    is_active - check if task already closed
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - request Homework object and returns it,
    if Homework is expired, prints 'You are late' and returns None
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - request task text and number of days to complete, returns Homework object
    Note that this method doesn't need object itself
PEP8 comply strictly.
"""
import datetime


class Teacher:
    """
    class Teacher
    """

    def __init__(self, last_name, first_name):
        self.text = None
        self.deadline = None
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, deadline):
        """create homework"""
        self.text = text
        self.deadline = deadline
        return Homework(text, deadline)


class Student:
    """class Student"""

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework):
        """ check if homework is active"""
        if homework.is_active():
            print("You are late")
            return None


class Homework:
    """class Homework"""

    def __init__(self, text, deadline):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    def is_active(self):
        """return Homework is active"""
        if self.deadline < 0:
            return True
        date_now = datetime.datetime.now() - datetime.timedelta(days=3)
        date_deadline = datetime.datetime.now() - datetime.timedelta(days=self.deadline)
        if (date_now - date_deadline).days >= 0:
            return True


if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Ivanov')
    student = Student('Vladislav', 'Popov')

    expired_homework = teacher.create_homework('Learn functions', 0)

    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
