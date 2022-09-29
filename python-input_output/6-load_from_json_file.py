#!/usr/bin/python3
""" function that creates an Object from a JSON file """


def load_from_json_file(filename):
    """ define this function """
    import json
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
