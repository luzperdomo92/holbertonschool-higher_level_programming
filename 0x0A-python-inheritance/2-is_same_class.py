#!/usr/bin/python3
"""Defining a new Method"""


def is_same_class(obj, a_class):
    """
    methot to check if object
    is exactly an instance of
    the specified class
    """
    if type(obj) is a_class:
        return True
    return False
