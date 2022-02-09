"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    >>>is_http_domain('http://wikipedia.org')
    True
    >>>is_http_domain('https://ru.wikipedia.org/')
    True
    >>>is_http_domain('griddynamics.com')
    False
"""
import re

import pytest


def is_http_domain(domain: str) -> bool:
    # return print('http' in domain)
    regex = r"(http)"
    url = re.findall(regex, domain)
    if len(url) > 0:
        if str(url[0]) == 'http':
            return True
    else:
        return False


# is_http_domain('http://wikipedia.org')
# is_http_domain('https://ru.wikipedia.org/')
# is_http_domain('griddynamics.com')
"""
write tests for is_http_domain function
"""


@pytest.mark.parametrize("a", ['http://wikipedia.org', 'https://ru.wikipedia.org/', 'griddynamics.com'])
def test_is_http_domain(a):
    assert (True == is_http_domain(a))
