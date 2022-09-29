#!/usr/bin/python3
"""
define a function that returns an object(Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """define this function"""
    import json
    return json.loads(my_str)
