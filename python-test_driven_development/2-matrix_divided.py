#!/usr/bin/python3
"""define a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix"""
    if type(matrix) is not list and type(matrix) is not float:
        raise TypeError("matrix must be a matrix (list of lists) of\
integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda x: list(map(lambda y: round(y / div, 2),
                                             x)), matrix))
    return new_matrix
