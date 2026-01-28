#!/usr/bin/python3
"""This module defines a Square class that can be positioned and printed."""


class Square:
    """This class represents a square with a size and a position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance with a size and a position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square after validating the input."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using the # character at the correct position."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
