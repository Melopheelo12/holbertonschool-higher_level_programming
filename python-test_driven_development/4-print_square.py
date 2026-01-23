#!/usr/bin/python3
"""
This module provides the function print_square
that prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square of # characters of length 'size'.

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
