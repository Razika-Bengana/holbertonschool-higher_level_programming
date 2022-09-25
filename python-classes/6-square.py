#!/usr/bin/python3
"""Define a class for Square"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """class instantiation with option size and also position"""
        self.__size = size
        """define the private instance attribute size"""
        self.__position = position
        """define the private instance attribute position"""

    @property
    def size(self):
        """proprety setter to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """proprety setter to set the size"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """proprety setter to retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """proprety setter to set the position"""
        if type(value) is tuple and len(value) is 2 and \
           type(value[0]) is int and type(value[1]) is int and \
           value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Public instance method that returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Public instance method that prints in stdout the square with #"""
        if (self.__size):
            for i in range(self.__position[1]):
                print()
            for k in range(self.__size):
                print('{}{}'.format(' ' * self.position[0], '#' * self.__size))
        else:
            print()
