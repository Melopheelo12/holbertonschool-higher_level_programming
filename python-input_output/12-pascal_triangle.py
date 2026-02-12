#!/usr/bin/python3
"""Module that creates Pascal's triangle"""


def pascal_triangle(n):
    """Return a list of lists of integers representing
        Pascal's triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        prev_row = triangle[i - 1]

        # Compute the inner values
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
