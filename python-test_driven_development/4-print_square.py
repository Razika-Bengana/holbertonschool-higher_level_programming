#!/usr/bin/python3
"""define a function that prints a square with the character #"""


def print_square(size):
    """print a square with # and size as the length of the square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is int and type(size) < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
