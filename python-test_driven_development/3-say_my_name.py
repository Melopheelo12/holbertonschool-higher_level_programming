#!/usr/bin/python3
"""
Module that provides a function to print a formatted name.

The function prints a sentence introducing a person using
their first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a formatted string with the first name and last name.

    first_name and last_name must be strings, otherwise a TypeError
    is raised.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
