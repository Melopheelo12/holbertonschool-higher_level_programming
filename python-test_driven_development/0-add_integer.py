#!/usr/bin/python3
"""Adds 2 integers.
Prototype: def add_integer(a, b=98):
- a and b must be integers or floats, otherwise raise a TypeError
- a and b must be first casted to integers (if they are floats)
- Returns an integer: the addition of a and b"""


def add_integer(a, b=98):
    """Adds two integers.
    Args: a: First number. b:Second number (default 98).
    Returns: int: Sum of a and b."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
