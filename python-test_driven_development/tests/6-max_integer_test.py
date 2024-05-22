#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer function."""

    def test_ordered_list(self):
        """Test with a list of ordered integers."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_unordered_list(self):
        """Test with a list of unordered integers."""
        self.assertEqual(max_integer([1, 3, 4, 2, 5]), 5)

    def test_all_negative(self):
        """Test with a list of all negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_negative_and_positive(self):
        """Test with a list containing both positive and negative integers."""
        self.assertEqual(max_integer([-1, 1, -2, 2, 0]), 2)

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.8, 3.1, 0.5]), 3.1)

    def test_mixed_types(self):
        """Test with a list containing integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 4.4]), 4.4)

    def test_identical_elements(self):
        """Test with a list containing identical elements."""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
