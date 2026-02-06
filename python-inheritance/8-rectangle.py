#!/usr/bin/python3
"""Module Rectangle inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle instance

        Args:
            width (int): width of the rectangle (private)
            height (int): height of the rectangle (private)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
