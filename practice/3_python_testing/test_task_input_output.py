"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
import unittest
from unittest.mock import patch


class Test(unittest.TestCase):

    def test_read_numbers_without_text_input(self):
        string_input = "1 2 hello 2 world"
        string_output = "['1', '2', '2']"
        self.assertTrue(string_output == str(number_input(string_input)))

    @patch('builtins.input', side_effect=['1 2 hello 2 world'])
    def test_read_numbers_with_text_input(self, mock_input):
        calling_1 = mock_input()
        calling_1 = (' '.join(word for word in calling_1.split() if word.isdigit())).split()
        self.assertTrue(str(calling_1) == "['1', '2', '2']")


def number_input(s):
    # s="1 2 hello 2 world"
    s = (' '.join(word for word in s.split() if word.isdigit())).split()
    return s
