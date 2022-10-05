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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """ private instance attribute of height """
        """ get the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set value of height """
        self.__height = value
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """ private instance attribute of x """
        """ get the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set value of x """
        self.__x = value
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """ private instance attribute of y """
        """ get the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set value of y """
        self.__y = value
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """
        public method that returns the area value of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        public method that prints in stdout
        the Rectangle instance with the character #
        """
        if (self.y > 0):
            print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ overriding the __str__ method """
        Id, x, y, wid, hei = self.id, self.x, self.y, self.width, self.height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(Id, x, y, wid, hei))

    def update(self, *args, **kwargs):
        """ public method that assigns an argument to each attribute """
        if len(args) != 0:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ public method that returns the dictionary
            representation of a Rectangle
        """
        Rect_Dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return Rect_Dict
