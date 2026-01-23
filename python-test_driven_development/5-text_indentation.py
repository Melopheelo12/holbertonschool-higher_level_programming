
#!/usr/bin/python3
"""
This module provides the function text_indentation
that prints a text with 2 new lines after each ., ?, or :.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each ., ?, or :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentence = ""
    for word in text:
        if word in ".?:":
            print(sentence.strip() + word)
            print()
            print()
            sentence = ""
        else:
            sentence += word
    if sentence.strip():
        print(sentence.strip())
