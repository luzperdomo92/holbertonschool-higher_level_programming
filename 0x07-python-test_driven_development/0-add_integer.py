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

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
