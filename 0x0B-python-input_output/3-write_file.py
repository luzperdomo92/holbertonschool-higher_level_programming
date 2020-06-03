#!/usr/bin/python3
"""Defining  write_file Function"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file
    and returns the number of characters written
    """
    with open(filename, "w") as fl:
        return (fl.write(text))
