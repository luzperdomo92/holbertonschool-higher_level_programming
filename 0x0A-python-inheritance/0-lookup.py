#!/usr/bin/python3
"""Defining a new Method"""


def lookup(obj):
    """
    methot that returns the
    list of available attributes
    and methods of an object:
    """
    return(list(dir(obj)))
