#!/usr/bin/python3
"""Define a class for Square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """class instatiation with option"""
        self.__size = size
        """define the private instance attribute size"""

    @property
    def size(self):
        """proprety setter to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """proprety setter to set the size"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public instance method that returns the current square area"""
        return (self.__size)**2
