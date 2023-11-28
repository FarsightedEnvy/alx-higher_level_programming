#!/usr/bin/python3

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test case 1: List with positive integers
        self.assertEqual(max_integer([1, 3, 5, 7]), 7)

        # Test case 2: List with negative integers
        self.assertEqual(max_integer([-1, -3, -5, -7]), -1)

        # Test case 3: List with mixed positive and negative integers
        self.assertEqual(max_integer([-1, 3, -5, 7]), 7)

        # Test case 4: List with repeated integers
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

        # Test case 5: Empty list
        self.assertIsNone(max_integer([]))

        # Test case 6: List with one element
        self.assertEqual(max_integer([42]), 42)

        # Test case 7: List with zero
        self.assertEqual(max_integer([0, -3, 5, 7]), 7)

        # Test case 8: List with decimal numbers
        self.assertEqual(max_integer([1.5, 3.2, 5.7, 7.9]), 7.9)

        # Test case 9: List with a mix of integers and decimal numbers
        self.assertEqual(max_integer([1, 3.2, 5, 7.9]), 7.9)

    def test_max_integer_empty_list(self):
        # Test case: Empty list should return None
        self.assertIsNone(max_integer([]))

    def test_max_integer_invalid_input(self):
        # Test case: Invalid input (not a list)
        with self.assertRaises(TypeError):
            max_integer("not_a_list")

if __name__ == '__main__':
    unittest.main()
