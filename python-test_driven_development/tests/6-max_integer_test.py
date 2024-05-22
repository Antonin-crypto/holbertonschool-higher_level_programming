#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([10, 20, 30]), 30)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -10, -2]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([5, -8, 12, 0]), 12)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([10, 20, 30, 30]), 30)
