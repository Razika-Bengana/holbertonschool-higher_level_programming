#!/usr/bin/python3
"""
define a function that appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """define this function"""
    with open(filename, "a", encoding="utf-8") as file_a:
        return (file_a.write(text))
