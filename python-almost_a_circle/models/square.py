#!/usr/bin/python3
""" define the class Square that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the overloading method __str__ """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    @property
    def size(self):
        """ private instance attribute of size """
        """ get the value of size """
        return self.width

    @size.setter
    def size(self, value):
        """ set the value of size """
        self.width = value
        self.height = value
