"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     #>>> make_request('https://www.google.com')
     200, 'response data'
"""
import urllib.request
from typing import Tuple
from unittest.mock import Mock


def make_request(url: str) -> Tuple[int, str]:
    urlcode = urllib.request.urlopen(url)
    return urlcode.getcode(), urlcode.read().decode('utf8')


#make_request("https://www.google.com")
"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""

def test_make_request():
    mr = make_request("https://www.google.com")
    m = Mock()
    m.make_request.return_value = 200
    m.make_request()
    assert(m.make_request())


