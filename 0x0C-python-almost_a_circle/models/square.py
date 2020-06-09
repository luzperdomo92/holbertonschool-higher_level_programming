#!/usr/bin/python3
"""Creating a new Square class"""
from .rectangle import Rectangle


class Square(Rectangle):
    """ Constructor to define values"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that return a new string"""
        return("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """ Method to get the value of size """
        return self.width

    @size.setter
    def size(self, value):
        """ Method to set value of size """
        self.width = value
        self.height = value

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
                self.size = arg
            elif iter == 2:
                self.x = arg
            elif iter == 3:
                self.y = arg
            iter += 1

        if args is not None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        Method that return the dictionary
        representations of class Square
        """
        dictio = {}
        dictio["id"] = self.id
        dictio["size"] = self.size
        dictio["x"] = self.x
        dictio["y"] = self.y
        return (dictio)
