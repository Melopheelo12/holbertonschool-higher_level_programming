#!/usr/bin/python3
"""module that writes a string to a UTF8 text"""


def write_file(filename="", text=""):
    """Write a string to text file (UTF-8)"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
