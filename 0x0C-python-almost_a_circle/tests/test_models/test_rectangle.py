#!/usr/bin/python3
"""Unittest for rectangle.py is defined"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstance(unittest.TestCase):
    """Unittest for creating instances of the Rectangle class"""

    def testbaseinstance(self):
        """test to ensure rectangle is an instance of Base class"""
        self.assertIsInstance(Rectangle(13, 5), Base)

    def testnoarguments(self):
        """test to check when Rectangle has no argument"""
        with self.assertRaises(TypeError):
            Rectangle()

    def testoneargument(self):
        """test to check when rectangle has one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def testtwoarguments(self):
        """test to check when rectangle has two arguments"""
        rec1 = Rectangle(2, 12)
        rec2 = Rectangle(12, 2)
        self.assertEqual(rec1.id, rec2.id - 1)

    def testthreearguments(self):
        """test to check when rectangle has three arguments"""
        rec1 = Rectangle(2, 12, 5)
        rec2 = Rectangle(12, 2, 6)
        self.assertEqual(rec1.id, rec2.id - 1)

    def testfourarguments(self):
        """test to check when rectangle has four arguments"""
        rec1 = Rectangle(2, 12, 5, 9)
        rec2 = Rectangle(12, 2, 6, 5)
        self.assertEqual(rec1.id, rec2.id - 1)

    def testfivearguments(self):
        """test to check when rectangle has five arguments"""
        self.assertEqual(9, Rectangle(11, 4, 6, 8, 9).id)

    def testabovefiveargs(self):
        """test to check when rectangle has more than five arguments"""
        with self.assertRaises(TypeError):
            Rectangle(3, 5, 7, 9, 2, 4,)

    def testprivatewidth(self):
        """test to check when accessing __width"""
        with self.assertRaises(AttributeError):
            print(Rectangle(7, 7, 2, 3, 8).__width)

    def testprivateheight(self):
        """test to check when accessing __height"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 7, 4, 1).__height)

    def testprivatex(self):
        """test to check when accessing __x"""
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 6, 2, 3).__x)

    def testprivatey(self):
        """test to check when accessing __y"""
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 6, 7, 9, 2).__y)

    def testwidthgetter(self):
        """test to get the width"""
        rec = Rectangle(9, 6, 3, 2, 1)
        self.assertEqual(9, rec.width)

    def testheightgetter(self):
        """test to get the height"""
        rec = Rectangle(9, 6, 3, 2, 1)
        self.assertEqual(6, rec.height)

    def testxgetter(self):
        """test to get the x coordinate"""
        rec = Rectangle(9, 6, 3, 2, 1)
        self.assertEqual(3, rec.x)

    def testygetter(self):
        """test to get the y coordinate"""
        rec = Rectangle(9, 6, 3, 2, 1)
        self.assertEqual(2, rec.y)

    def testwidthsetter(self):
        """test to set the width"""
        rec = Rectangle(9, 6, 3, 2, 1)
        rec.width = 12
        self.assertEqual(12, rec.width)

    def testheightsetter(self):
        """test to set the height"""
        rec = Rectangle(9, 6, 3, 2, 1)
        rec.height = 8
        self.assertEqual(8, rec.height)

    def testxsetter(self):
        """test to set the x coordinate"""
        rec = Rectangle(9, 6, 3, 2, 1)
        rec.x = 5
        self.assertEqual(5, rec.x)

    def testysetter(self):
        """test to set the y coordinate"""
        rec = Rectangle(9, 6, 3, 2, 1)
        rec.y = 4
        self.assertEqual(4, rec.y)
