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

    @staticmethod
    def from_json_string(json_string):
        """
            static method that returns the list of the JSON string
            representation json_string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            class method that returns an instance
            with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ class method that returns a list of instances """
        name_of_file = cls.__name__ + ".json"
        json_obj = []
        try:
            with open(name_of_file, 'r', encoding='utf-8') as file:
                json_obj = cls.from_json_string(file.read())
            for key, value in enumerate(json_obj):
                json_obj[key] = cls.create(**json_obj[key])
        except Exception:
            pass
        return json_obj
