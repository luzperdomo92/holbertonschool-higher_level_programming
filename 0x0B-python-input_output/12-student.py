#!/usr/bin/python3
"""Defining new class Student"""


class Student():
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """constructor to define parameters"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that return dictionary representation"""

        new_dict = {}
        if attrs is None:
            return (self.__dict__)

        for iter in attrs:
            if hasattr(self, iter):
                new_dict[iter] = getattr(self, iter)
        return (new_dict)
