#!/usr/bin/python3
"""define a function that prints a string"""


def say_my_name(first_name, last_name=""):
    """function that prints first name and last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
