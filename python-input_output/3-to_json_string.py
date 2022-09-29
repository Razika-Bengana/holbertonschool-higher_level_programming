#!/usr/bin/python3
"""
define a function that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """define this function"""
    import json
    return json.dumps(my_obj)
