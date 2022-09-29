#!/usr/bin/python3
"""
define a function that writes a string to a text file
and returns the number of character written
"""


def write_file(filename="", text=""):
    """define this function"""
    with open(filename, "w", encoding="utf-8") as file_w:
        return (file_w.write(text))
