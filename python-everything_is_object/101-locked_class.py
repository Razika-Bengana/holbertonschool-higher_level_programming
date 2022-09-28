#!/usr/bin/python3
"""
define a class with no class or object attribute,
that prevents the user from dynamically creating
new instance attributes, except if the new instance
attribute is called 'first_name'
"""


class LockedClass():
    """define this class"""
    __slots__ = "first_name"
