#!/usr/bin/python3
"""Module to serialize and deserialize a custom Python object using pickle"""

import pickle


class CustomObject:
    """Custom object with name, age, and is_student attributes"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle"""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except (OSError, pickle.PickleError, EOFError):
            return None
