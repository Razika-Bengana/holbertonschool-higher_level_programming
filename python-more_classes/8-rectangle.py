#!/usr/bin/python3
"""Define an empty class rectangle"""


class Rectangle():
    """define private instance attributes width and height"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """method to get the value of width"""
        return self.__width

    @property
    def height(self):
        """method to get the value of height"""
        return self.__height

    @width.setter
    def width(self, value):
        """method to set the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """method to set the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """public instance method to determine the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """public instance method to determine the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Print rectangle with #'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = (str(self.print_symbol) * self.__width + '\n') * self.__height
        return rec[:-1]

    def __repr__(self):
        """ String representation to recreate a new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Delete instance of class"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to return the bigger instance"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
