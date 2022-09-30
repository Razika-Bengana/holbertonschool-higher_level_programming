#!/usr/bin/python3
""" Pascal's triangle """


def pascal_triangle(n):
    """ define a function that returns a list of lists of integers
        representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    pasc_triangle = [[1]]

    for rows in range(n - 1):
        line = [1]
        for i in range(rows):
            line.append(pasc_triangle[rows][i] + pasc_triangle[rows][i + 1])

        line.append(1)
        pasc_triangle.append(line)

    return pasc_triangle
