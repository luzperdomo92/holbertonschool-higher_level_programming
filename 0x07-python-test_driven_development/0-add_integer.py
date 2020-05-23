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

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
