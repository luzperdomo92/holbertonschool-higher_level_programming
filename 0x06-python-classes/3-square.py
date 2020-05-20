#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class to handle square objects"""
    def __init__(self, size):
        """
        Constructor for Square class.

        Parameters:
           size (int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
