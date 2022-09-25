#!/usr/bin/python3
"""Define an empty class rectangle"""


class Rectangle():
    def __init__(self, width=0, height=0):
        """define private instance attributes width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """method to get value of width"""
        return self.__width

    @property
    def height(self):
        """method to get value of height"""
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
