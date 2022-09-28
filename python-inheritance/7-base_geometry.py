#!/usr/bin/python3
"""define an empty class"""


class BaseGeometry:
    """class defined"""

    def area(self):
        """public instance method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
