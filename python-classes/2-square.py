#!/usr/bin/python3
"""Define a class for Square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """define the private instance attribute size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
