#!/usr/bin/python3
"""Additionne 2 entiers.
Prototype : def add_integer(a, b=98) :
- a et b doivent être des entiers ou des nombres à virgule flottante, sinon lever une TypeError
- a et b doivent d’abord être convertis en entiers (s’ils sont des flottants)
- Retourne un entier : la somme de a et b
"""


def add_integer(a, b=98):
    """Adds two integers.
    Args: a: First number. b:Second number (default 98).
    Returns: int: Sum of a and b."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
