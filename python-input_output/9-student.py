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

    def to_json(self):
        """
        public method that retrieves a dictionary representation
        of a 'Student' instance
        """
        return self.__dict__
