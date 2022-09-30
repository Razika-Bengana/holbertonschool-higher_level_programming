#!/usr/bin/python3
"""
define a script that adds all arguments to a Python list
and save them in a file
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")

except:
    my_list = []
save_to_json_file(my_list + argv[1:], "add_item.json")
