#!/usr/bin/python3
"""Module that returns the dictionary description for JSON serialization"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure"""
    return obj.__dict__
