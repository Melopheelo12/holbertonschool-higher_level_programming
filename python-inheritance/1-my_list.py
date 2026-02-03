#!/usr/bin/python3
class MyList(list):
    """Class that inherit in my list"""
    pass

    def print_sorted(self):
        """Print the list of ascending sort"""

        print(sorted(list(self)))
