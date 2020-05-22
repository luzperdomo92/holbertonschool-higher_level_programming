#!/usr/bin/python3
"""
    print_square: prints a square with the character #
    Return square made by #
"""


def print_square(size):
    """
    TypeError: If either of element is a non-integer.
    ValueError:  if size in less than cero.
    """
    if size:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
