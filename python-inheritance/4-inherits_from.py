#!/usr/bin/python3
"""Module with method inheritance"""


def inherits_from(obj, a_class):
    """return true if obj, a_class"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
