#!/usr/bin/python3
"""Module that provide a function to list attribute"""


def lookup(obj):
    """return the list of available method of an object"""

    return dir(obj)
