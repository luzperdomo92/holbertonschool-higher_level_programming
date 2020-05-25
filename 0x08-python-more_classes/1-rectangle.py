#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Class to handle rectangle objects"""

    def __init__(self, width=0, height=0):
        """
        Constructor for rectangle class.

        Parameters:
           height (int): height of the rectangle.
           width (int): width of the rentangle.
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """ methot to get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ method to set value of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ methot to get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ method to set value of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
