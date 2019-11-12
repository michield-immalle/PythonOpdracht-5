from typing import Dict


def tel_letters(string: str) -> Dict[str, int]:
    """
    >>> tel_letters("hallo!")
    {'h': 1, 'a': 1, 'l': 2, 'o': 1, '!': 1}
    >>> tel_letters("België")
    {'B': 1, 'e': 1, 'l': 1, 'g': 1, 'i': 1, 'ë': 1}
    """
    d = {}
    for i in range(len(string)):
        if string[i] in d:
            d[string[i]] += 1
        else:
            d.update({string[i]: 1})
    return d


if __name__ == "__main__":
    import doctest
    doctest.testmod()