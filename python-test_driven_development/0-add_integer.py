#!/usr/bin/python3
def add_integer(a, b=98):
    """return the sum of two integers,
    otherwise an error if arguments are not int or float"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
