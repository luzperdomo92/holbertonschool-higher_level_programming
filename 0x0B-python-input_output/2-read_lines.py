#!/usr/bin/python3
"""Defining  read_lines Function"""


def read_lines(filename="", nb_lines=0):
    """
    Function that reads n lines of a text file
    and prints it to STDOUT
    """
    with open(filename, mode='r', encoding='utf-8') as fl:
        if nb_lines <= 0:
            print(fl.read(), end="")
        else:
            for line in range(nb_lines):
                print(fl.readline(), end="")
