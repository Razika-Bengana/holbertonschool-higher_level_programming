#!/usr/bin/python3
"""
define a new class that will represent the base
of the other classes in this project
"""


class Base:
    """ define this class """
    __nb_objects = 0
    """ private class attribute """

    def __init__(self, id=None):
        """ class constructor """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
