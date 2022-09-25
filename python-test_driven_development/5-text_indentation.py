#!/usr/bin/python3
"""define a function that prints a text with special characters"""


def text_indentation(text):
    """
    prints text with 2 new lines after characters ".", "?", and ":"
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for special_char in ".?:":
        if (special_char == '.' or special_char == '?' or special_char == ':'):
            text = (special_char + "\n\n").join(
                [lines.strip(' ') for lines in text.split(special_char)])
    print("{}".format(text), end="")
