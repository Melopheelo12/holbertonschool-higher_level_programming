#!/usr/bin/python3
""" if the object is exactly an instance of the specified class that will
    return true otherwise that will return false"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class."""

    return type(obj) is a_class
