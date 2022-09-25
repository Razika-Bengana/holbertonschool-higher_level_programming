#!/usr/bin/python3
"""Define a class for Square"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Instanciation with options size and position"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position) is not tuple or len(position) != 2 \
            or type(position[0]) is not int or position[0] < 0 \
               or type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
        if type(value) is not tuple or len(value) != 2 \
           or type(value[0]) is not int or value[0] < 0 \
               or type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Public instance method that returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Public instance method that prints in stdout the square with #"""
        if self.__size == 0:
            print()
        else:
            for line in range(self.__position[1]):
                print()
            for size1 in range(self.__size):
                for space1 in range(self.__position[0]):
                    print(" ", end="")
                for diez in range(self.__size):
                    print("#", end="")
                print()
