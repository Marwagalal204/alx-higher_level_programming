#!/usr/bin/python3
"""
divide matrix module This module defines a function,
matrix_divided(matrix, div), which divide 2 list
"""


def matrix_divided(matrix, div):
    """divide matric function"""
    resuled_list = []

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, int):
        raise TypeError("div must be a number")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            res = []
            for item in row:
                if not isinstance(item, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists)"
                                    "of integers/floats")
                divide = item / div
                diev_rounded = round(divide, 2)
                res.append(diev_rounded)
            resuled_list.append(res)
    return resuled_list
