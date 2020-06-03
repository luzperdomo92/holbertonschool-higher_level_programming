#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry
    Raises:
    Exception: area(self) method not implemented.
    TypeError: if value is not 'int' type.
    ValueError: if value is <= 0.
    """
    def area(self):
        """ method to define an area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method to validate value to integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
