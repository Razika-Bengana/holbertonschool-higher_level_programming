#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = 0
    result = 0
    while i < len(roman_string):
        if i < len(roman_string) - 1:
            if roman[roman_string[i]] < roman[roman_string[i + 1]]:
                result += roman[roman_string[i + 1]] - roman[roman_string[i]]
                i += 2
            else:
                result += roman[roman_string[i]]
                i += 1
        else:
            result += roman[roman_string[i]]
            i += 1
            return result