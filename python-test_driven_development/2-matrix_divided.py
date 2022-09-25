#!/usr/bin/python3
"""define a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix"""
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if all(isinstance(elements, list) for elements in matrix) is False:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return list(map(lambda x:
                    list(map(lambda y: round(y / div, 2), x)), matrix))
