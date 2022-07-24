#!/usr/bin/python3
"""
   Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    # valid inputs
    def test_is_max(self):
        """ tests for max int """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        self.assertEqual(max_integer([1, 2, -3, -4]), 2)
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_is_none(self):
        self.assertIsNone(max_integer([]))

    # edge cases
    def test_is_raises(self):
        """ensure tests raises on error input"""
        self.assertRaises(TypeError, max_integer, {1, 2, 3})

        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 5)

    def test_wrong_element(self):
        self.assertRaises(TypeError, max_integer, [1, '2', 3, None])
