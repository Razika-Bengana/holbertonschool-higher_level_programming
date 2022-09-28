#!/usr/bin/python3
"""define an empty class"""


class BaseGeometry:
    """class defined"""

    def area(self):
        """
            public instance methode that raises an exception
            with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
