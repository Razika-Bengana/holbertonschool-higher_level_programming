#!/usr/bin/python3
""" define the class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ private instance attribute of width """
        """ get the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the value of width """
        self.__width = value

    @property
    def height(self):
        """ private instance attribute of height """
        """ get the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """set value of height"""
        self.__height = value

    @property
    def x(self):
        """ private instance attribute of x """
        """ get the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """set value of x"""
        self.__x = value

    @property
    def y(self):
        """ private instance attribute of y """
        """ get the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """set value of y"""
        self.__y = value
