#!/usr/bin/python3
"""define a function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """define this function"""
    with open(filename, "r", encoding="utf-8") as file_r:
        print(file_r.read(), end='')
