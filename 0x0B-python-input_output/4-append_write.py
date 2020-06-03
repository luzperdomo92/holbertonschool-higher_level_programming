#!/usr/bin/python3
"""Defining  append_write Function"""


def append_write(filename="", text=""):
    """
     Function that appends a string at the end of
     a text file and returns the number of
     characters added
    """
    with open(filename, "a") as fl:
        return (fl.write(text))
