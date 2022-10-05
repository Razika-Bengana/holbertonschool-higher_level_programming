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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            static method that returns the JSON string
            representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            class method that writes the JSON string
            representation of list_objs to a file
        """
        n_file = "{}.json".format(cls.__name__)
        list_of_dic = []

        if list_objs is not None:
            for element in list_objs:
                list_of_dic.append(cls.to_dictionary(element))
        with open(n_file, mode="w", encoding='utf-8') as my_file:
            my_file.write(cls.to_json_string(list_of_dic))
