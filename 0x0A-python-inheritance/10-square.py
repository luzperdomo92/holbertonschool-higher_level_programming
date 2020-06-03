#!/usr/bin/python3
"""Class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits
    from class 'Rectangle'
    """
    def __init__(self, size):
        """constructor to define superclass in square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
