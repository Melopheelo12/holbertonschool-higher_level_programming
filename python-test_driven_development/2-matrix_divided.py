#!/usr/bin/python3
"""
Module that provides a function to divide all elements of a matrix.

The matrix_divided function returns a new matrix where each element
is divided by a given divisor and rounded to two decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    The matrix must be a list of lists of integers or floats.
    Each row must have the same size.
    The divisor must be a non-zero integer or float.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
