#!/usr/bin/python3
"""
    say_my_name: print the name and last name
    Return print diferents name
"""


def say_my_name(first_name, last_name=""):
    """
    TypeError: If either of element is a non-string.
    """
    if not isinstance(first_name, str) or first_name is None::
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
