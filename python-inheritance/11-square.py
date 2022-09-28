#!/usr/bin/python3
"""define an empty class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class defined that inherits from Rectangle"""

    def __init__(self, size):
        """
            instantiation with size that must be private,
            and must be a positive integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Public instance method that return the area"""
        return self.__size ** 2

    def __str__(self):
        """prints [Square] <width>/<height>"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
