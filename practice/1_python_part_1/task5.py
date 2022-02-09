"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""


def remove_duplicated_words(line: str) -> str:
    """
    remove duplicated words
    """
    words = line.split()
    words = (" ".join(sorted(set(words), key=line.index)))
    return words


remove_duplicated_words('cat cat dog 1 dog 2')
remove_duplicated_words('cat cat cat')
remove_duplicated_words('1 2 3')
