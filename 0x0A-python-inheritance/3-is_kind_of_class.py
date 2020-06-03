#!/usr/bin/python3
"""Defining a new Method"""


def is_kind_of_class(obj, a_class):
    """
    methot to check if  the object
    is an instance of, or if the object
    is an instance of a class that inherited
    from, the specified class
    """
    return isinstance(obj, a_class)
