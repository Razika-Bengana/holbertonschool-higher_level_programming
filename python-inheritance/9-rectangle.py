#!/usr/bin/python3
"""define an empty class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class defined that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
            instantiation with width and height that must be private,
            and must be positive integers
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Public instance method that return the area"""
        return self.__width * self.__height

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
