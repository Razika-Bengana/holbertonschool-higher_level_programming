#!/usr/bin/python3
"""define a class that inherits from a list"""


class MyList(list):
    """define the subclass of 'list'"""
    pass

    def print_sorted(self):
        """public instance method that prints the list in sorted order"""
        print(sorted(self))
