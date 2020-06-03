#!/usr/bin/python3
"""Defining read_file Function"""


def read_file(filename=""):
    """
    Function to read a file
    and print it in the STOUT
    """
    with open("my_file_0.txt", "r") as fl:
        print(fl.read())
