#!/usr/bin/python3
"""
    add_integer: Check input if correct, Float arguments are
    typecasted to ints before addition is performed.
    Return the integer addition of a and b by default return 98.
"""


def add_integer(a, b=98):
    """
    TypeError: If either of a or b is a non-integer and non-float.
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return (a + b)
