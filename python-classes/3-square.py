#!/usr/bin/python3
"""Define a class for Square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """initialization of a new square"""
        self.__size = size
        """define the private instance attribute size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        def area(self):
            """Public instance method that returns the current square area"""
            return (self.__size)**2
