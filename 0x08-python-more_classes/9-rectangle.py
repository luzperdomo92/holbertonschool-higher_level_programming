#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Class to handle rectangle objects"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor for rectangle class.

        Parameters:
           height (int): height of the rectangle.
           width (int): width of the rentangle.
        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ method to calculate the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """ method to calculate the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0

        return (self.width + self.height) * 2

    def __str__(self):
        """ method that returns the string representation of the object"""
        if self.width == 0 or self.height == 0:
            return ""
        horiz = self.width * str(self.print_symbol)
        horiz += '\n'
        horiz *= self.height
        horiz = horiz[:-1]
        return horiz

    def __repr__(self):
        """ method that returns the string representation"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ method that deletes an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ method to compare the values"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ method to return a Rectangle with the same width and height"""
        return Rectangle(size, size)
