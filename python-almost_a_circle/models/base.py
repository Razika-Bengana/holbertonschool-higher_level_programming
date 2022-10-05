#!/usr/bin/python3
"""
define a new class that will represent the base
of the other classes in this project
"""
import json

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

    def to_json_string(list_dictionaries):
        """
            static method that returns the JSON string
            representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
