#!/usr/bin/python3
"""Defining  number_of_lines Function"""


def number_of_lines(filename=""):
    """
    Function that returns the number
    of lines of a text file:
    """
    line_number = 0
    with open(filename, "r") as fl:
        for line in fl:
            line_number += 1
        return line_number
