#!/usr/bin/env python3
"""CountedIterator module"""

class CountedIterator:
    """Iterator that counts how many items have been iterated"""

    def __init__(self, iterable):
        """Initialize with an iterable and counter"""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return next item and increment the counter"""
        item = next(self.iterator)  # may raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated"""
        return self.count

    def __iter__(self):
        """Iterator object returns self"""
        return self
