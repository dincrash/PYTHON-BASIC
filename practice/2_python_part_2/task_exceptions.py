"""
Write a function which divides x by y.
If y == 0 it should print "Division by 0" and return None
elif y == 1 it should raise custom Exception with "Deletion on 1 get the same result" text
else it should return the result of division
In all cases it should print "Division finished"
   # >>> division(1, 0)
    Division by 0
    Division finished
   # >>> division(1, 1)
    Division finished
    DivisionByOneException("Deletion on 1 get the same result")
  #  >>> division(2, 2)
    1
    Division finished
"""
import typing


def division(x: int, y: int) -> typing.Union[None, int]:
    """division"""
    try:
        if y == 0:
            print("Division by 0")
            return None
        elif y == 1:
            raise DivisionByOneException
        else:
            print("Division finished")
            return int(x / y)
    except DivisionByOneException:
        return print('DivisionByOneException("Deletion on 1 get the same result")')


class DivisionByOneException(Exception):
    """DivisionByOneException"""


division(1, 0)
division(1, 1)
division(2, 2)
