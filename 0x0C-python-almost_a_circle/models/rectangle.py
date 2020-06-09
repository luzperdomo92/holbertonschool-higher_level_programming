#!/usr/bin/python3
"""Creating a new Rectangle class"""
from .base import Base


class Rectangle(Base):
    """ class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor to define values"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Method to get the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Method to set value of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Method to get the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method to set value of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Method to get the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Method to set value of x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Method to get the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Method to set value of y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method that return the area value"""
        return (self.width * self.height)

    print_symbol = "#"

    def display(self):
        """
        Method to print in stdout the Rectangle
        instance with the character #
        """
        if self.width == 0 or self.height == 0:
            return ""
        for _ in range(0, self.y):
            print("")
        display = self.x * (" ")
        display += self.width * str(self.print_symbol)
        display += '\n'
        display *= self.height
        display = display[:-1]
        print(display)

    def __str__(self):
        """Method that return a new string"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        Method that assigns
        a key/value argument to attributes
         """
        iter = 0

        for arg in args:
            if iter == 0:
                self.id = arg
            elif iter == 1:
                self.width = arg
            elif iter == 2:
                self.height = arg
            elif iter == 3:
                self.x = arg
            elif iter == 4:
                self.y = arg
            iter += 1

        if args is not None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        Method that return the dictionary
        representations of class rectangle
        """
        dictio = {}
        dictio["id"] = self.id
        dictio["width"] = self.width
        dictio["height"] = self.height
        dictio["x"] = self.x
        dictio["y"] = self.y
        return (dictio)
