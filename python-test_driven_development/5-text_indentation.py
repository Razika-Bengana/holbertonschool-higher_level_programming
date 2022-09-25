#!/usr/bin/python3
"""define a function that prints a text with special characters"""


def text_indentation(text):
    """
    prints text with 2 new lines after characters ".", "?", and ":"
    """
    if (type(text) is not str or text is None):
        raise TypeError("text must be a string")
    for char in ".?:":
        if (char == '.' or char == '?' or char == ':'):
            text = text.replace(char, char + "\n\n")
            text_lines = [lines.strip(' ') for lines in text.split('\n')]
            new_text = "\n".join(text_lines)
            print(new_text, end="")
