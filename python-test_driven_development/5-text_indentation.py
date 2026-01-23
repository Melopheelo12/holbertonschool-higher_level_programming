#!/usr/bin/python3
"""
Module that provides a function to print text with indentation.

The text_indentation function prints a text and adds two new lines
after each '.', '?' and ':' character.
"""


def text_indentation(text):
    """
    Print a text with two new lines after '.', '?' and ':'.

    text must be a string, otherwise a TypeError is raised.
    No line should start or end with a space.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ".?:"
    i = 0

    while i < len(text):
        print(text[i], end="")

        if text[i] in special_chars:
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1
