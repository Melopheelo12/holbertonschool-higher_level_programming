#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test with a list of one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list of positive and negative integers"""
        self.assertEqual(max_integer([-10, 5, 3, -2]), 5)

    def test_max_at_beginning(self):
        """Test when max is the first element"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        """Test when max is the last element"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_duplicate_max(self):
        """Test with duplicate max values"""
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_floats(self):
        """Test with float values"""
        self.assertEqual(max_integer([1.5, 2.7, 3.1]), 3.1)


if __name__ == "__main__":
    unittest.main()
