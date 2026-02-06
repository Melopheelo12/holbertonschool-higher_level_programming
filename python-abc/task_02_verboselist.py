#!/usr/bin/env python3
"""VerboseList module"""


class VerboseList(list):
    """List subclass that prints notifications on modification"""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]  # get item to print
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
