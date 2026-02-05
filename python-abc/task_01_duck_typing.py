#!/usr/bin/env python3
"""Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Return area of shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter of shape"""
        pass


class Circle(Shape):
    """Circle shape"""

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        """Area of circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Perimeter (circumference) of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter using duck typing.
    No type checking: we assume the object
    has area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
