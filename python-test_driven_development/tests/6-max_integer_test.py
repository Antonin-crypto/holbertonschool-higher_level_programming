#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer()"""

    def test_start_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_end_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_mid_list(self):
        self.assertEqual(max_integer([3, 2, 4, 5]), 5)

    def test_positive_list(self):
        self.assertEqual(max_integer([1, 100]), 100)

    def test_negative_list(self):
        self.assertEqual(max_integer([1, -100]), 1)

    def test_one_number_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_not_start_list(self):
        self.assertNotEqual(max_integer([1, 2, 3, 4]), 1)

    def test_not_end_list(self):
        self.assertNotEqual(max_integer([4, 3, 2, 1]), 1)

    def test_not_mid_list(self):
        self.assertNotEqual(max_integer([3, 2, 4, 5]), 4)

    def test_not_positive_list(self):
        self.assertNotEqual(max_integer([1, 100]), 1)

    def test_not_negative_list(self):
        self.assertNotEqual(max_integer([1, -100]), -100)

    def test_not_one_number_list(self):
        self.assertNotEqual(max_integer([1]), 0)

    def test_duplication_list(self):
        self.assertEqual(max_integer([15, 15]), 15)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_unmodified_list(self):
        test_list = [873, 5654, 465, -389, 0]
        test_copy = list(test_list)
        self.assertTrue(len(test_copy) == len(test_list))
        for i in range(len(test_copy)):
            self.assertTrue(test_copy[i] == test_list[i])


