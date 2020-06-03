#!/usr/bin/python3
"""Defining read_file Function"""


def read_file(filename=""):
    """
    Function to read a file
    and print it in the STOUT
    """
    with open(filename, "r") as fl:
        print(fl.read())
