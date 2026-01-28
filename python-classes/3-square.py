#!/usr/bin/python3
"""This module defines a Square class and provides methods to work with it."""


class Square:
    """This class represents a square defined by a validated size."""

    def __init__(self, size=0):
        """Initializes a Square instance with a validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size
