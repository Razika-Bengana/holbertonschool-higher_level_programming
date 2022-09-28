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
