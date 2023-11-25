#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A unittest testmaxinteger class defined"""

    def test_non_empty_list(self):
        """max_integer for non empty list of integers"""
        regval = max_integer([1, 5, 6, 7, 8])
        self.assertEqual(regval, 8)

    def test_neg_values(self):
        """max_integer for neg value integers"""
        negval = max_integer([-5, -4, -3, -2, -1])
        self.assertEqual(negval, -1)

    def test_single_value(self):
        """max_integer for single value"""
        sngval = max_integer([10])
        self.assertEqual(sngval, 10)

    def test_float_values(self):
        """max_integer test for float values"""
        fltval = max_integer([1.2, 7.8, 5.6, 9.2])
        self.assertEqual(fltval, 9.2)

    def test_ints_floats(self):
        """max_integer test for integers and floats values"""
        intfloat = max_integer([3.4, 7, 8.9, -6, 9.2, 10.65])
        self.assertEqual(intfloat, 10.65)

    def test_empty_list(self):
        """max_integer test for emplty list"""
        emplist = max_integer([])
        self.assertEqual(emplist, None)


if __name__ == '__main__':
    unittest.main()
