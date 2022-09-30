#!/usr/bin/python3
"""
define a class student by:
first name, last name, and age
"""


class Student():
    """ class defined """

    def __init__(self, first_name, last_name, age):
        """ instantiation with first name, last name, and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        public method that retrieves a dictionary representation
        of a 'Student' instance
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            if i in self.__dict__:
                new_dict[i] = self.__dict__[i]
        return new_dict
