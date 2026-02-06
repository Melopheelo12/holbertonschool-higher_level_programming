#!/usr/bin/python3
"""Module Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize square with size"""
        self.integer_validator("size", size)
        self.__size = size
        # Call Rectangle constructor with width = height = size
        super().__init__(size, size)

    def area(self):
        """Return area of square"""
        return self.__size * self.__size

    def __str__(self):
        """Return string representation of Square (as Rectangle)"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
