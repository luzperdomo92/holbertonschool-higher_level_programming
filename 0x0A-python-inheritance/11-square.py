#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size):
        """constructor to define superclass in square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """method to return  a string"""
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
