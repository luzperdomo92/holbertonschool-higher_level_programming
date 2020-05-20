#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class to handle square objects"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor for Square class.

        Parameters:
           size (int): size of the square.
           position (tuple): position to print the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.position = position
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if ((not isinstance(value, tuple)) or
                len(value) != 2 or
                (not isinstance(value[0], int) or value[0] < 0) or
                (not isinstance(value[1], int) or value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        for _ in range(0, self.__position[1]):
            print("")
        for _ in range(0, self.__size):
            print((" " * self.__position[0]) + ("#" * self.__size))
