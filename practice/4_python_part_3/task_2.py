"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math


def math_calculate(function: str, *args):
    if function == 'log':
        return log(*args)
    elif function == 'ceil':
        return ceil(*args)
    else:
        return "OperationNotFoundException"


def log(*args):
    return math.log(*args)


def ceil(*args):
    return math.ceil(*args)


# math_calculate('log', 1024, 2)
# math_calculate('log', 1024)
# math_calculate('ceil', 10.7)
# math_calculate('ceils', 10.7)
"""
Write tests for math_calculate function
"""


def test_log():
    assert math_calculate('log', 1024, 2) == math.log(1024, 2)


def test_ceil():
    assert math_calculate('ceil', 10.7) == math.ceil(10.7)
