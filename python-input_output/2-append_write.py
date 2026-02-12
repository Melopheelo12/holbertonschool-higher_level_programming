#!/usr/bin/python3
"""Module that append a string to a UTF-8 text file"""


def append_write(filename="", text=""):
    """append a string at the end of a text"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
