#!/usr/bin/python3
"""Unittest for rectangle.py is defined"""
import unittest
import sys
from io import StringIO
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


class TestRectangleWidth(unittest.TestCase):
    """Unittest for Rectangle width attribute initialization"""

    def testinvalidwidthnone(self):
        """test to check for invalid width: None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 7)

    def testinvalidwidthstr(self):
        """test to check for invalid width: String"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("a_string", 4)

    def testinvalidwidthlist(self):
        """test to check for invalid width: List"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 4, 6], 8)

    def testinvalidwidthtuple(self):
        """test to check for invalid width: Tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 3, 5), 7)

    def testinvalidwidthdict(self):
        """test to check for invalid width: Dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"key": 9, "val": 4}, 7)

    def testinvalidwidthset(self):
        """test to check for invalid width: Set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 4, 7}, 2)

    def testinvalidwidthfrozenset(self):
        """test to check for invalid width: Frozenset"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({2, 5, 8}), 3)

    def testinvalidwidthfloat(self):
        """test to check for invalid width: Float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(9.8, 3)

    def testinvalidwidthinf(self):
        """test to check for invalid width: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 5)

    def testinvalidwidthnan(self):
        """test to check invalid width: nan"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 9)

    def testnegativewidth(self):
        """test to check width with negative value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-8, 6)

    def testzerowidth(self):
        """test to check width with zero value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)

    def testinvalidwidthcomplex(self):
        """test to check for invalid width: Complex number"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(4), 9)

    def testinvalidwidthbytes(self):
        """test to check for invalid width: Bytes"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Data', 1)

    def testinvalidwidthbytearray(self):
        """test to check for invalid width: Bytearray"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'barr'), 7)

    def testinvalidwidthmemoryview(self):
        """test to check for invalid width: Memoryview"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'memview'), 8)

    def testinvalidwidthrange(self):
        """test to check for invalid width: Range"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(4), 3)

    def testinvalidwidthbool(self):
        """test to check for invalid width: Bool"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 3)


class TestRectangleHeight(unittest.TestCase):
    """Unittest for Rectangle height attribute initialization"""

    def testinvalidheightnone(self):
        """test to check for invalid height: None"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, None)

    def testinvalidheightstr(self):
        """test to check for invalid height: String"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "a_string")

    def testinvalidheightlist(self):
        """test to check for invalid height: List"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, [2, 4, 6])

    def testinvalidheighttuple(self):
        """test to check for invalid height: Tuple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, (1, 3, 5))

    def testinvalidheightdict(self):
        """test to check for invalid height: Dictionary"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, {"key": 9, "val": 4})

    def testinvalidheightset(self):
        """test to check for invalid height: Set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 4, 7})

    def testinvalidheightfrozenset(self):
        """test to check for invalid height: Frozenset"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, frozenset({2, 5, 8}))

    def testinvalidheightfloat(self):
        """test to check for invalid height: Float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 9.8)

    def testinvalidheightinf(self):
        """test to check for invalid height: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('inf'))

    def testinvalidheightnan(self):
        """test to check invalid height: nan"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, float('nan'))

    def testnegativeheight(self):
        """test to check height with negative value"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(6, -8)

    def testzeroheight(self):
        """test to check height with zero value"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)

    def testinvalidheightcomplex(self):
        """test to check for invalid height: Complex number"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, complex(4))

    def testinvalidheightbytes(self):
        """test to check for invalid height: Bytes"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Data')

    def testinvalidheightbytearray(self):
        """test to check for invalid height: Bytearray"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, bytearray(b'barr'))

    def testinvalidheightmemoryview(self):
        """test to check for invalid height: Memoryview"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, memoryview(b'memview'))

    def testinvalidheightrange(self):
        """test to check for invalid height: Range"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, range(4))

    def testinvalidheightbool(self):
        """test to check for invalid height: Bool"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, True)


class TestRectangleXCoordinate(unittest.TestCase):
    """Unittest for Rectangle X coordinate attribute initialization"""

    def testinvalidxnone(self):
        """test to check for invalid x: None"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 2, None)

    def testinvalidxstr(self):
        """test to check for invalid x: String"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 7, "a_string", 1)

    def testinvalidxlist(self):
        """test to check for invalid x: List"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 1, [2, 4, 6], 4)

    def testinvalidxtuple(self):
        """test to check for invalid x: Tuple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 2, (1, 3, 5), 6)

    def testinvalidxdict(self):
        """test to check for invalid x: Dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 2, {"key": 9, "val": 4}, 8)

    def testinvalidxset(self):
        """test to check for invalid x: Set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, {1, 4, 7}, 3)

    def testinvalidxfrozenset(self):
        """test to check for invalid x: Frozenset"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 7, frozenset({2, 5, 8}), 4)

    def testinvalidxfloat(self):
        """test to check for invalid x: Float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 1, 9.8, 6)

    def testinvalidxinf(self):
        """test to check for invalid x: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 2, float('inf'), 6)

    def testinvalidxnan(self):
        """test to check invalid x: nan"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 3, float('nan'), 7)

    def testnegativex(self):
        """test to check x with negative value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(6, 9, -8, 4)

    def testinvalidxcomplex(self):
        """test to check for invalid x: Complex number"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 2, complex(4), 5)

    def testinvalidxbytes(self):
        """test to check for invalid x: Bytes"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 4, b'Data', 3)

    def testinvalidxbytearray(self):
        """test to check for invalid x: Bytearray"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 6, bytearray(b'barr'), 5)

    def testinvalidxmemoryview(self):
        """test to check for invalid x: Memoryview"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 3, memoryview(b'memview'), 6)

    def testinvalidxrange(self):
        """test to check for invalid x: Range"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 7, range(4), 1)

    def testinvalidxbool(self):
        """test to check for invalid x: Bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 8, True, 9)


class TestRectangleYCoordinate(unittest.TestCase):
    """Unittest for Rectangle Y coordinate attribute initialization"""

    def testinvalidynone(self):
        """test to check for invalid y: None"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(9, 2, 7, None)

    def testinvalidystr(self):
        """test to check for invalid y: String"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 7, 1, "a_string")

    def testinvalidylist(self):
        """test to check for invalid y: List"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 1, 3, [2, 4, 6])

    def testinvalidytuple(self):
        """test to check for invalid y: Tuple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 2, 6, (1, 3, 5))

    def testinvalidydict(self):
        """test to check for invalid y: Dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 2, 8, {"key": 9, "val": 4})

    def testinvalidyset(self):
        """test to check for invalid y: Set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 3, {1, 4, 7})

    def testinvalidyfrozenset(self):
        """test to check for invalid y: Frozenset"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 7, 4, frozenset({2, 5, 8}))

    def testinvalidyfloat(self):
        """test to check for invalid y: Float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 1, 5, 9.8)

    def testinvalidyinf(self):
        """test to check for invalid y: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 2, 6, float('inf'))

    def testinvalidynan(self):
        """test to check invalid y: nan"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(9, 3, 7, float('nan'))

    def testnegativey(self):
        """test to check y with negative value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(6, 9, 4, -8)

    def testinvalidycomplex(self):
        """test to check for invalid y: Complex number"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(9, 2, 5, complex(4))

    def testinvalidybytes(self):
        """test to check for invalid y: Bytes"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 4, 3, b'Data')

    def testinvalidybytearray(self):
        """test to check for invalid y: Bytearray"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 6, 5, bytearray(b'barr'))

    def testinvalidymemoryview(self):
        """test to check for invalid y: Memoryview"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 3, 6, memoryview(b'memview'))

    def testinvalidyrange(self):
        """test to check for invalid y: Range"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 7, 1, range(4))

    def testinvalidybool(self):
        """test to check for invalid y: Bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 8, 9, False)


class TestRectangleInstanceOrder(unittest.TestCase):
    """Unittest for Rectangle attribute order of instances"""

    def testwidthorderbeforeheight(self):
        """test to check the order of the attribute width before height"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("thewidth", "theheight")

    def testwidthorderbeforeX(self):
        """test check the order of the attribute width before x"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("thewidth", 4, "thex")

    def testwidthbeforeY(self):
        """test check the order of the attribute width before Y"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("thewidth", 4, 7, "theY")

    def testheightbeforeX(self):
        """test check the order of the attribute height before X"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "theheight", "theX")

    def testheightbeforeY(self):
        """test check the order of the attribute height before Y"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "theheight", 7, "theY")

    def testXbeforeY(self):
        """test to check the order of the attribute X before Y"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, "theX", "theY")


class TestRectangleArea(unittest.TestCase):
    """Unittest for the area method of the Rectangle class"""

    def testsmallrectangle(self):
        """test to calcuate the area of a small rectangle"""
        rec = Rectangle(6, 9, 0, 0, 0)
        self.assertEqual(54, rec.area())

    def testbigrectangle(self):
        """test to calculate the area of a big/large rectangle"""
        rec = Rectangle(246813579, 135792468, 0, 0, 1)
        self.assertEqual(33515425028322972, rec.area())

    def testchangedattributes(self):
        """test to calculate the area after changing the attributes"""
        rec = Rectangle(3, 9, 1, 1, 1)
        rec.width = 8
        rec.height = 5
        self.assertEqual(40, rec.area())

    def testareawithonearg(self):
        """test when are method takes in one argument"""
        rec = Rectangle(4, 6, 3, 7, 2)
        with self.assertRaises(TypeError):
            rec.area(1)


class TestRectanglestdout(unittest.TestCase):
    """Unittest for __str__ and display maethods of the Rectangle class"""

    @staticmethod
    def capt_stdout(rec, method):
        """gets and return text printed to the stdout
        Args:
        rec (Rectangle): the rectangle to print to the stdout
        method (str): the method to run on the rec (rectangle)"""
        capt = StringIO()
        sys.stdout = capt
        if method == "print":
            print(rec)
        else:
            rec.display()
        sys.stdout = sys.__stdout__
        return capt

    def teststrwidthheight(self):
        """test __str__ method with width and height"""
        rec = Rectangle(3, 4)
        capt = TestRectanglestdout.capt_stdout(rec, "print")
        exp_output = "[Rectangle] ({}) 0/0 - 3/4\n".format(rec.id)
        self.assertEqual(exp_output, capt.getvalue())

    def teststrwidthheightx(self):
        """test __str__ method with width, height and x coordinate"""
        rec = Rectangle(3, 7, 2)
        exp_output = "[Rectangle] ({}) 2/0 - 3/7".format(rec.id)
        self.assertEqual(exp_output, rec.__str__())

    def teststrwidthheightxy(self):
        """test __str__ method with width, height, x and y coordinate"""
        rec = Rectangle(3, 5, 6, 2)
        exp_output = "[Rectangle] ({}) 6/2 - 3/5".format(rec.id)
        self.assertEqual(exp_output, str(rec))

    def teststrwidthheightxyid(self):
        """test __str__ method with width, height, x, y, id"""
        rec = Rectangle(12, 22, 3, 6, 9)
        self.assertEqual("[Rectangle] (9) 3/6 - 12/22", str(rec))

    def teststrchnagedattr(self):
        """test __str__ method with changed attributes"""
        rec = Rectangle(2, 4, 6, 8, [4])
        rec.width = 1
        rec.height = 3
        rec.x = 5
        rec.y = 7
        self.assertEqual("[Rectangle] ([4]) 5/7 - 1/3", str(rec))

    def teststronearg(self):
        """test __str__ method with one argument"""
        rec = Rectangle(2, 4, 6, 8, 3)
        with self.assertRaises(TypeError):
            rec.__str__(1)

    def testdisplaywidthheight(self):
        """test display method with width and height"""
        rec = Rectangle(3, 4, 0, 0, 0)
        capt = TestRectanglestdout.capt_stdout(rec, "display")
        self.assertEqual("###\n###\n###\n###\n", capt.getvalue())

    def testdisplaywidthheightx(self):
        """test display method with width, height and x coordinate"""
        rec = Rectangle(2, 3, 2, 0, 1)
        capt = TestRectanglestdout.capt_stdout(rec, "display")
        self.assertEqual("  ##\n  ##\n  ##\n", capt.getvalue())

    def testdisplaywidthheightxy(self):
        """test display method with width, height, x and y coordinate"""
        rec = Rectangle(3, 5, 0, 1, 0)
        capt = TestRectanglestdout.capt_stdout(rec, "display")
        exp_output = "\n###\n###\n###\n###\n###\n"
        self.assertEqual(exp_output, capt.getvalue())

    def testdisplaywidthheightxyid(self):
        """test display method with width, height, x, y, id"""
        rec = Rectangle(3, 4, 3, 2, 0)
        capt = TestRectanglestdout.capt_stdout(rec, "display")
        exp_output = "\n\n   ###\n   ###\n   ###\n   ###\n"
        self.assertEqual(exp_output, capt.getvalue())

    def testdisplayonearg(self):
        """test display method with one argument"""
        rec = Rectangle(2, 4, 6, 8, 3)
        with self.assertRaises(TypeError):
            rec.display(1)


class TestRectangleupdateargs(unittest.TestCase):
    """Unittest for update_args method of the Rectangle class"""

    def testupdateargszero(self):
        """test to update rectangle with zero arguments"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update()
        self.assertEqual("[Rectangle] (3) 6/7 - 12/3", str(rec))

    def testupdateargsone(self):
        """test to update rectangle with one argument"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(24)
        self.assertEqual("[Rectangle] (24) 6/7 - 12/3", str(rec))

    def testupdateargstwo(self):
        """test to update rectangle with two arguments"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(24, 9)
        self.assertEqual("[Rectangle] (24) 6/7 - 9/3", str(rec))

    def testupdateargsthree(self):
        """test to update rectangle with three arguments"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(24, 9, 8)
        self.assertEqual("[Rectangle] (24) 6/7 - 9/8", str(rec))

    def testupdateargsfour(self):
        """test to update rectangle with four arguments"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(24, 9, 8, 5)
        self.assertEqual("[Rectangle] (24) 5/7 - 9/8", str(rec))

    def testupdateargsfive(self):
        """test to update rectangle with five arguments"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(24, 9, 8, 5, 4)
        self.assertEqual("[Rectangle] (24) 5/4 - 9/8", str(rec))

    def testupdateargsabovefive(self):
        """test to update rectangle with over five arguments"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(24, 9, 8, 5, 4, 1)
        self.assertEqual("[Rectangle] (24) 5/4 - 9/8", str(rec))

    def testupdateargsNoneid(self):
        """test to update rectangle id with None"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(None)
        exp_output = "[Rectangle] ({}) 6/7 - 12/3".format(rec.id)
        self.assertEqual(exp_output, str(rec))

    def testupdateargsNoneidandothers(self):
        """test to update rectangle id with None and other attr"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(None, 2, 4, 3, 5)
        exp_output = "[Rectangle] ({}) 3/5 - 2/4".format(rec.id)
        self.assertEqual(exp_output, str(rec))

    def testupdateargstwice(self):
        """test to update rectangle twice"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(24, 9, 8, 5, 4, 1)
        rec.update(16, 5, 8, 9, 2, 1)
        self.assertEqual("[Rectangle] (16) 9/2 - 5/8", str(rec))

    def testupdateinvalidwidthargs(self):
        """test to update width with invalid type"""
        rec = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(24, "a_string")

    def testupdatewidthargswithzero(self):
        """test to update the value of width with zero"""
        rec = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(18, 0)

    def testupdatewidthargswithnegvalue(self):
        """test to update the width args with negative value"""
        rec = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(27, -2)

    def testupdateinvalidheightargs(self):
        """test to update height with invalid type"""
        rec = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(24, 5, "a_string")

    def testupdateheightargswithzero(self):
        """test to update the value of height with zero"""
        rec = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(18, 7, 0)

    def testupdateheightargswithnegvalue(self):
        """test to update the height args with negative value"""
        rec = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(27, 6, -2)

    def testupdateinvalidxargs(self):
        """test to update x with invalid type"""
        rec = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(24, 5, 9, "a_string")

    def testupdatexargswithnegvalue(self):
        """test to update the x args with negative value"""
        rec = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(27, 6, 8, -2)

    def testupdateinvalidyargs(self):
        """test to update y with invalid type"""
        rec = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.update(24, 5, 2, 6, "a_string")

    def testupdateyargswithnegvalue(self):
        """test to update the y args with negative value"""
        rec = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec.update(27, 6, 8, 7, -2)

    def testupdatewidthargsbeforeheight(self):
        """test to update the width args before height"""
        rec = Rectangle(13, 2, 4, 6, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(30, "thewidth", "theheight")

    def testupdatewidthargsbeforex(self):
        """test to update the width args before x"""
        rec = Rectangle(24, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(19, "thewidth", 6, "theX")

    def testupdatewidthargsbeforey(self):
        """test to update the width args before y"""
        rec = Rectangle(12, 2, 5, 3, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(23, "thewidth", 11, 9, "theY")

    def testupdateheightargsbeforex(self):
        """test to update the height args before x"""
        rec = Rectangle(24, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(19, 4, "theheight", "theX")

    def testupdateheightargsbeforey(self):
        """test to update the height args before y"""
        rec = Rectangle(12, 2, 5, 3, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(23, 11, "theheight", 9, "theY")

    def testupdatexargsbeforey(self):
        """test to update the x args before y"""
        rec = Rectangle(12, 2, 5, 3, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(23, 11, 10, "thex", "theY")


class TestRectangleupdatekwargs(unittest.TestCase):
    """Unittest for update_kwargs method of the Rectangle class"""

    def testupdatekwargsone(self):
        """test to update rectangle with one argument"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(id=24)
        self.assertEqual("[Rectangle] (24) 6/7 - 12/3", str(rec))

    def testupdatekwargstwo(self):
        """test to update rectangle with two arguments"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(width=9, id=24)
        self.assertEqual("[Rectangle] (24) 6/7 - 9/3", str(rec))

    def testupdatekwargsthree(self):
        """test to update rectangle with three arguments"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(width=9, height=8, id=24)
        self.assertEqual("[Rectangle] (24) 6/7 - 9/8", str(rec))

    def testupdatekwargsfour(self):
        """test to update rectangle with four arguments"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(id=24, width=9, height=8, x=5)
        self.assertEqual("[Rectangle] (24) 5/7 - 9/8", str(rec))

    def testupdatekwargsfive(self):
        """test to update rectangle with five arguments"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(id=24, width=9, height=8, x=5, y=4)
        self.assertEqual("[Rectangle] (24) 5/4 - 9/8", str(rec))

    def testupdatekwargsNoneid(self):
        """test to update rectangle id with None"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(id=None)
        exp_output = "[Rectangle] ({}) 6/7 - 12/3".format(rec.id)
        self.assertEqual(exp_output, str(rec))

    def testupdatekwargsNoneidandothers(self):
        """test to update rectangle id with None and other attr"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(id=None, width=2, height=4, x=3, y=5)
        exp_output = "[Rectangle] ({}) 3/5 - 2/4".format(rec.id)
        self.assertEqual(exp_output, str(rec))

    def testupdatekwargstwice(self):
        """test to update rectangle twice"""
        rec = Rectangle(12, 3, 6, 7, 3)
        rec.update(id=24, width=9, height=1)
        rec.update(id=16, width=5, height=8)
        self.assertEqual("[Rectangle] (16) 6/7 - 5/8", str(rec))

    def testupdateinvalidwidthkwargs(self):
        """test to update width with invalid type"""
        rec = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(width="a_string")

    def testupdatewidthkwargswithzero(self):
        """test to update the value of width with zero"""
        rec = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(width=0)

    def testupdatewidthkwargswithnegvalue(self):
        """test to update the width kwargs with negative value"""
        rec = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(width=-2)

    def testupdateinvalidheightkwargs(self):
        """test to update height with invalid type"""
        rec = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(height="a_string")

    def testupdateheightkwargswithzero(self):
        """test to update the value of height with zero"""
        rec = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(height=0)

    def testupdateheightkwargswithzero(self):
        """test to update the value of height with zero"""
        rec = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(height=-2)

    def testupdateinvalidxkwargs(self):
        """test to update x with invalid type"""
        rec = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(x="a_string")

    def testupdatexkwargswithnegvalue(self):
        """test to update the x kwargs with negative value"""
        rec = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(x=-2)

    def testupdateinvalidykwargs(self):
        """test to update y with invalid type"""
        rec = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.update(y="a_string")

    def testupdateykwargswithnegvalue(self):
        """test to update the y kwargs with negative value"""
        rec = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec.update(y=-2)

    def testupdateargsandkwargs(self):
        """test to update args and kwargs"""
        rec = Rectangle(12, 9, 7, 5, 3)
        rec.update(2, 4, height=6, y=8)
        self.assertEqual("[Rectangle] (2) 7/5 - 4/9", str(rec))

    def testpdatekwargswithwrongkeys(self):
        """test to update kwargs with wrong keys"""
        rec = Rectangle(10, 8, 6, 4, 2)
        rec.update(t=5, d=8)
        self.assertEqual("[Rectangle] (2) 6/4 - 10/8", str(rec))

    def testupdatekwargsandsomewrongkeys(self):
        """test to update kwargs and some wrong keys"""
        rec = Rectangle(9, 7, 5, 3, 1)
        rec.update(width=8, id=10, a=4, b=12, x=6, y=4)
        self.assertEqual("[Rectangle] (10) 6/4 - 8/7", str(rec))


class TestRectangletoDictionary(unittest.TestCase):
    """Unittest for the to_dictionary method of the Rectangle class"""

    def testoutputmatchtodictionary(self):
        """test if output dictionary matches the expected result"""
        rec = Rectangle(16, 12, 8, 4, 2)
        exp_output = {'id': 2, 'x': 8, 'y': 4, 'width': 16, 'height': 12}
        self.assertDictEqual(exp_output, rec.to_dictionary())

    def testnochangeofobject(self):
        """test to verify calling update does not modify original object"""
        rec1 = Rectangle(10, 8, 6, 4, 2)
        rec2 = Rectangle(9, 7, 5, 3, 1)
        rec2.update(**rec1.to_dictionary())
        self.assertNotEqual(rec1, rec2)

    def testpassingargtodict(self):
        """test to check when argument is passed to dictionary"""
        rec = Rectangle(10, 7, 6, 3, 2)
        with self.assertRaises(TypeError):
            rec.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
