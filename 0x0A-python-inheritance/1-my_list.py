#!/usr/bin/python3
"""Class MyList"""


class MyList(list):
    """Class MyList"""
    def __init__(self):
        """constructor to define superclass in MyList"""
        list.__init__(self)

    def print_sorted(self):
        """methot to prints the list sorted"""
        print(sorted(self))
