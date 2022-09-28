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
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
