"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse
from unittest.mock import Mock
from faker import Faker


class Thingy:
    def __init__(self, name):
        self.name = name

    def print_name_address(self, parser: argparse.Namespace) -> None:

        parser.add_argument('integers', metavar='N', type=int)
        parser.add_argument('--fake-address', type=str)
        parser.add_argument('--some_name', type=str)
        args = parser.parse_args()

        fake = Faker()
        fake.name()
        fake.address()

        mydict = vars(args)
        mydict1 = {}
        for _ in range(args.integers):
            for arg in mydict:
                if getattr(args, arg) == "address":
                    mydict1[arg] = fake.address()
                if getattr(args, arg) == "name":
                    mydict1[arg] = fake.name()
            print(mydict1)


def main():
    pars = argparse.ArgumentParser()
    Thingy.print_name_address(pars)


if __name__ == '__main__':
    main()

"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""


def test_parser():
    m = Mock()
    m.Thingy.print_name_address = [4, '--fake-address=address', '--some_name=name']
    m.Thingy.print_name_address().assert_called()
