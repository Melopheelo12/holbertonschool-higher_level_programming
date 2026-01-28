#!/usr/bin/python3
"""This module defines a Square class with a size property."""


class Square:
    """This class represents a square and controls access to its size."""

    def __init__(self, size=0):
        """Initializes a Square instance with a validated size."""
        self.size = size

    @property
    def size(self):
        """Retrieves the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
