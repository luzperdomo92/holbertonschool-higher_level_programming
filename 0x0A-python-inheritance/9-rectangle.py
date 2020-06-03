#!/usr/bin/python3
"""Class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits
    from class 'BaseGeometry'
    """
    def __init__(self, width, height):
        """constructor to define atributes width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ method to define an area """
        return self.__width * self.__height

    def __str__(self):
        """method to return  a string"""
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string
