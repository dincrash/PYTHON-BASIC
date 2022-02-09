"""
Write function which updates dictionary with defined values but only if new value more than in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)
    # only b updated because new value for a less than original value
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {a: 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""
from typing import Dict


def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    """
    set_to_dict
    """
    for k_d1 in items_to_set.items():
        if k_d1 in dict_to_update:
            if dict_to_update[str(k_d1)] < items_to_set[str(k_d1)]:
                dict_to_update[str(k_d1)] = items_to_set[str(k_d1)]
        if k_d1 not in dict_to_update:
            dict_to_update[str(k_d1)] = items_to_set.get(str(k_d1))
    return dict_to_update


set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)
set_to_dict({}, a=0)
set_to_dict({'a': 5})
