"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""

from datetime import datetime, date

import pytest


def calculate_days(from_date: str) -> int:
    try:
        d1 = datetime.strptime(from_date, "%Y-%m-%d")
        d2 = datetime.now()
        if d2 < d1:
            return -(abs((d1 - d2).days))
        else:
            return abs((d2 - d1).days)
    except ValueError:
        print(("WrongFormatException"))


calculate_days('2021-10-07')
calculate_days('2022-10-01')
calculate_days('10-07-2021')
"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""

@pytest.fixture
def current_date():
    return date.today()


@pytest.mark.freeze_time
def test_changing_date(current_date, freezer):
    calc = ((current_date - date(2021, 10, 7)).days)
    calc2 = calculate_days('2021-10-07')
    assert calc == calc2

@pytest.mark.freeze_time
def test_changing_not_correct_date(current_date, freezer):
    calc = ((current_date - date(2020, 10, 7)).days)
    calc2 = calculate_days('2021-10-07')
    assert calc == calc2