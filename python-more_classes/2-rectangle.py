#!/usr/bin/python3
"""Define an empty class rectangle"""


class Rectangle():
    """define private instance attributes width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """method to get the value of width"""
        return self.__width

    @property
    def height(self):
        """method to get the value of height"""
        return self.__height

    @width.setter
    def width(self, value):
        """method to set the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """method to set the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """define the area rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """define the perimeter rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
