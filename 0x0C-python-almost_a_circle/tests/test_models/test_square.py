#!/usr/bin/python3
"""Unittest for square.py is defined"""
import unittest
import sys
from io import StringIO
from models.base import Base
from models.square import Square


class TestSquareInstance(unittest.TestCase):
    """Unittest for creating instances of the Square class"""

    def testbaseinstance(self):
        """test to ensure square is an instance of Base class"""
        self.assertIsInstance(Square(18), Base)

    def testrectangleinstance(self):
        """test to ensure square is an instance of Rectangle class"""
        self.assertIsInstance(Square(12), Square)

    def testnoarguments(self):
        """test to check when Square has no arguments"""
        with self.assertRaises(TypeError):
            Square()

    def testoneargument(self):
        """test to check when Square has one argument"""
        sqr1 = Square(8)
        sqr2 = Square(6)
        self.assertEqual(sqr1.id, sqr2.id - 1)

    def testtwoarguments(self):
        """test to check when Square has two arguments"""
        sqr1 = Square(9, 3)
        sqr2 = Square(3, 9)
        self.assertEqual(sqr1.id, sqr2.id - 1)

    def testthreearguments(self):
        """test to check when Square has three arguments"""
        sqr1 = Square(8, 4, 4)
        sqr2 = Square(4, 4, 8)
        self.assertEqual(sqr1.id, sqr2.id - 1)

    def testfourarguments(self):
        """test to check when square has four arguments"""
        self.assertEqual(9, Square(8, 3, 3, 9).id)

    def testoverfourarguments(self):
        """test to check when Square has over four arguments"""
        with self.assertRaises(TypeError):
            Square(10, 8, 5, 4, 2)

    def testprivatesize(self):
        """test to check when accessing __size"""
        with self.assertRaises(AttributeError):
            print(Square(9, 7, 5, 3).___size)

    def testsizegetter(self):
        """test to get size"""
        self.assertEqual(8, Square(8, 6, 4, 2).size)

    def testsizesetter(self):
        """test to set size"""
        sqr = Square(8, 4, 6, 2)
        sqr.size = 9
        self.assertEqual(9, sqr.size)

    def testwidthgetter(self):
        """test to get width"""
        sqr = Square(8, 4, 6, 2)
        sqr.width = 9
        self.assertEqual(9, sqr.width)

    def testheightgetter(self):
        """test to get height"""
        sqr = Square(8, 4, 6, 2)
        sqr.height = 9
        self.assertEqual(9, sqr.height)

    def testxgetter(self):
        """test to get x coordinates"""
        self.assertEqual(0, Square(9).x)

    def testygetter(self):
        """test to get the y coordinates"""
        self.assertEqual(0, Square(9).y)


class TestSquaresize(unittest.TestCase):
    """Unittest for Square size attribute initialization"""

    def testinvalidsizenone(self):
        """test to check for invalid size: None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def testinvalidsizestr(self):
        """test to check for invalid size: String"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("a_string")

    def testinvalidsizelist(self):
        """test to check for invalid size: List"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2, 4, 6])

    def testinvalidsizetuple(self):
        """test to check for invalid size: Tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 3, 5), 8, 9)

    def testinvalidsizedict(self):
        """test to check for invalid size: Dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"key": 9, "val": 4}, 7)

    def testinvalidsizeset(self):
        """test to check for invalid size: Set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 4, 7}, 2)

    def testinvalidsizefrozenset(self):
        """test to check for invalid size: Frozenset"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({2, 5, 8}))

    def testinvalidsizefloat(self):
        """test to check for invalid size: Float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(9.8)

    def testinvalidsizeinf(self):
        """test to check for invalid size: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def testinvalidsizenan(self):
        """test to check invalid size: nan"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def testnegativesize(self):
        """test to check size with negative value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-8, 6)

    def testzerosize(self):
        """test to check size with zero value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 3)

    def testinvalidsizecomplex(self):
        """test to check for invalid size: Complex number"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(4))

    def testinvalidsizebytes(self):
        """test to check for invalid size: Bytes"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Data')

    def testinvalidsizebytearray(self):
        """test to check for invalid size: Bytearray"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'barr'))

    def testinvalidsizememoryview(self):
        """test to check for invalid size: Memoryview"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'memview'))

    def testinvalidsizerange(self):
        """test to check for invalid size: Range"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(4))

    def testinvalidsizebool(self):
        """test to check for invalid size: Bool"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False, 3, 4)


class TestSquareXCoordinate(unittest.TestCase):
    """Unittest for Square X coordinate attribute initialization"""

    def testinvalidxnone(self):
        """test to check for invalid x: None"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, None)

    def testinvalidxstr(self):
        """test to check for invalid x: String"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, "a_string", )

    def testinvalidxlist(self):
        """test to check for invalid x: List"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, [2, 4, 6])

    def testinvalidxtuple(self):
        """test to check for invalid x: Tuple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, (1, 3, 5))

    def testinvalidxdict(self):
        """test to check for invalid x: Dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, {"key": 9, "val": 4}, 8)

    def testinvalidxset(self):
        """test to check for invalid x: Set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {1, 4, 7})

    def testinvalidxfrozenset(self):
        """test to check for invalid x: Frozenset"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, frozenset({2, 5, 8}))

    def testinvalidxfloat(self):
        """test to check for invalid x: Float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 9.8)

    def testinvalidxinf(self):
        """test to check for invalid x: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, float('inf'), 6)

    def testinvalidxnan(self):
        """test to check invalid x: nan"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, float('nan'), 7)

    def testnegativex(self):
        """test to check x with negative value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(6, -8, 4)

    def testinvalidxcomplex(self):
        """test to check for invalid x: Complex number"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, complex(4))

    def testinvalidxbytes(self):
        """test to check for invalid x: Bytes"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Data')

    def testinvalidxbytearray(self):
        """test to check for invalid x: Bytearray"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, bytearray(b'barr'))

    def testinvalidxmemoryview(self):
        """test to check for invalid x: Memoryview"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, memoryview(b'memview'))

    def testinvalidxrange(self):
        """test to check for invalid x: Range"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, range(4))

    def testinvalidxbool(self):
        """test to check for invalid x: Bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, True)


class TestSquareYCoordinate(unittest.TestCase):
    """Unittest for Square Y coordinate attribute initialization"""

    def testinvalidynone(self):
        """test to check for invalid y: None"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(9, 2, None)

    def testinvalidystr(self):
        """test to check for invalid y: String"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 7, "a_string")

    def testinvalidylist(self):
        """test to check for invalid y: List"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 1, [2, 4, 6])

    def testinvalidytuple(self):
        """test to check for invalid y: Tuple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 2, (1, 3, 5))

    def testinvalidydict(self):
        """test to check for invalid y: Dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 2, {"key": 9, "val": 4})

    def testinvalidyset(self):
        """test to check for invalid y: Set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 5, {1, 4, 7})

    def testinvalidyfrozenset(self):
        """test to check for invalid y: Frozenset"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 7, frozenset({2, 5, 8}))

    def testinvalidyfloat(self):
        """test to check for invalid y: Float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, 9.8)

    def testinvalidyinf(self):
        """test to check for invalid y: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 6, float('inf'))

    def testinvalidynan(self):
        """test to check invalid y: nan"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(9, 7, float('nan'))

    def testnegativey(self):
        """test to check y with negative value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(6, 4, -8)

    def testinvalidycomplex(self):
        """test to check for invalid y: Complex number"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(9, 5, complex(4))

    def testinvalidybytes(self):
        """test to check for invalid y: Bytes"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 4, b'Data')

    def testinvalidybytearray(self):
        """test to check for invalid y: Bytearray"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 5, bytearray(b'barr'))

    def testinvalidymemoryview(self):
        """test to check for invalid y: Memoryview"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 6, memoryview(b'memview'))

    def testinvalidyrange(self):
        """test to check for invalid y: Range"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 1, range(4))

    def testinvalidybool(self):
        """test to check for invalid y: Bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 9, False)


class TestSquareInstanceOrder(unittest.TestCase):
    """Unittest for Square attribute order of instances"""

    def testsizeorderbeforex(self):
        """test to check the order of the attribute size before x"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("thesize", "thex")

    def testsizeorderbeforey(self):
        """test to check the order of the attribute size before y"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("thesize", 2, "theY")

    def testxorderbeforey(self):
        """test to check the order of the attribute x before y"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, "thex", "theY")


class TestSquareArea(unittest.TestCase):
    """Unittest for the area method of the Square class"""

    def testsmallsquare(self):
        """test to calcuate the area of a small square"""
        self.assertEqual(144, Square(12, 0, 0, 1).area())

    def testbigsquare(self):
        """test to calculate the area of a large/big square"""
        sqr = Square(246813579, 0, 0, 1)
        self.assertEqual(60916942778789241, sqr.area())

    def testchangedattributes(self):
        """test to calculate the area after changing the attributes"""
        sqr = Square(3, 0, 0, 1)
        sqr.size = 8
        self.assertEqual(64, sqr.area())

    def testareawithonearg(self):
        """test when are method takes in one argument"""
        sqr = Square(4, 6, 3, 7)
        with self.assertRaises(TypeError):
            sqr.area(1)


class TestSquarestdout(unittest.TestCase):
    """Unittest for __str__ and display maethods of the Square class"""

    @staticmethod
    def capt_stdout(sqr, method):
        """gets and return text printed to the stdout
        Args:
        sqr (Square): the sqrtangle to print to the stdout
        method (str): the method to run on the sqr (sqrtangle)"""
        capt = StringIO()
        sys.stdout = capt
        if method == "print":
            print(sqr)
        else:
            sqr.display()
        sys.stdout = sys.__stdout__
        return capt

    def teststrsize(self):
        """test __str__ method with size"""
        sqr = Square(3)
        capt = TestSquarestdout.capt_stdout(sqr, "print")
        exp_output = "[Square] ({}) 0/0 - 3\n".format(sqr.id)
        self.assertEqual(exp_output, capt.getvalue())

    def teststrsizex(self):
        """test __str__ method with size and x coordinate"""
        sqr = Square(3, 2)
        exp_output = "[Square] ({}) 2/0 - 3".format(sqr.id)
        self.assertEqual(exp_output, sqr.__str__())

    def teststrsizexy(self):
        """test __str__ method with size, x and y coordinate"""
        sqr = Square(3, 6, 2)
        exp_output = "[Square] ({}) 6/2 - 3".format(sqr.id)
        self.assertEqual(exp_output, str(sqr))

    def teststrsizexyid(self):
        """test __str__ method with size, x, y, id"""
        sqr = Square(12, 3, 6, 9)
        self.assertEqual("[Square] (9) 3/6 - 12", str(sqr))

    def teststrchnagedattr(self):
        """test __str__ method with changed attributes"""
        sqr = Square(2, 6, 8, [4])
        sqr.size = 1
        sqr.x = 5
        sqr.y = 7
        self.assertEqual("[Square] ([4]) 5/7 - 1", str(sqr))

    def teststronearg(self):
        """test __str__ method with one argument"""
        sqr = Square(2, 4, 6, 8)
        with self.assertRaises(TypeError):
            sqr.__str__(1)

    def testdisplaysize(self):
        """test display method with size"""
        sqr = Square(3, 0, 0, 1)
        capt = TestSquarestdout.capt_stdout(sqr, "display")
        self.assertEqual("###\n###\n###\n", capt.getvalue())

    def testdisplaysizex(self):
        """test display method with size and x coordinate"""
        sqr = Square(2, 1, 0, 6)
        capt = TestSquarestdout.capt_stdout(sqr, "display")
        self.assertEqual(" ##\n ##\n", capt.getvalue())

    def testdisplaysizexy(self):
        """test display method with size, x and y coordinate"""
        sqr = Square(3, 0, 1, 7)
        capt = TestSquarestdout.capt_stdout(sqr, "display")
        exp_output = "\n###\n###\n###\n"
        self.assertEqual(exp_output, capt.getvalue())

    def testdisplaysizexyid(self):
        """test display method with size, x, y, id"""
        sqr = Square(3, 3, 2, 1)
        capt = TestSquarestdout.capt_stdout(sqr, "display")
        exp_output = "\n\n   ###\n   ###\n   ###\n"
        self.assertEqual(exp_output, capt.getvalue())

    def testdisplayonearg(self):
        """test display method with one argument"""
        sqr = Square(2, 4, 6, 8)
        with self.assertRaises(TypeError):
            sqr.display(1)


class TestSquareupdateargs(unittest.TestCase):
    """Unittest for update_args method of the Square class."""

    def testupdateargszero(self):
        """test to update square with zero arguments"""
        sqr = Square(13, 13, 13, 13)
        sqr.update()
        self.assertEqual("[Square] (13) 13/13 - 13", str(sqr))

    def testupdateargsone(self):
        """test to update square with one argument"""
        sqr = Square(13, 13, 13, 13)
        sqr.update(89)
        self.assertEqual("[Square] (89) 13/13 - 13", str(sqr))

    def testupdateargstwo(self):
        """test to update square with two arguments"""
        sqr = Square(13, 13, 13, 13)
        sqr.update(89, 2)
        self.assertEqual("[Square] (89) 13/13 - 2", str(sqr))

    def testupdateargsthree(self):
        """test to update square with three arguments"""
        sqr = Square(13, 13, 13, 13)
        sqr.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/13 - 2", str(sqr))

    def testupdateargsfour(self):
        """test to update square with four arguments"""
        sqr = Square(13, 13, 13, 13)
        sqr.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sqr))

    def testupdateargsmorethanfour(self):
        """test to update square with over four arguments"""
        sqr = Square(13, 13, 13, 13)
        sqr.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sqr))

    def testupdateargswidthsetter(self):
        """test to update the width setter"""
        sqr = Square(13, 13, 13, 13)
        sqr.update(89, 6)
        self.assertEqual(6, sqr.width)

    def testupdateargsheightsetter(self):
        """test to update the height setter"""
        sqr = Square(13, 13, 13, 13)
        sqr.update(89, 6)
        self.assertEqual(6, sqr.height)

    def testupdateargsNoneid(self):
        """test to update square id with None"""
        sqr = Square(13, 13, 13, 13)
        sqr.update(None)
        exp_output = "[Square] ({}) 13/13 - 13".format(sqr.id)
        self.assertEqual(exp_output, str(sqr))

    def testupdateargsNoneidandmore(self):
        """test to update square id with None and other attr"""
        sqr = Square(13, 13, 13, 13)
        sqr.update(None, 4, 5)
        exp_output = "[Square] ({}) 5/13 - 4".format(sqr.id)
        self.assertEqual(exp_output, str(sqr))

    def testupdateargstwice(self):
        """test to update square twice"""
        sqr = Square(13, 13, 13, 13)
        sqr.update(89, 2, 3, 4)
        sqr.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(sqr))

    def testupdateargsinvalidsizetype(self):
        """test to update size with invalid type"""
        sqr = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.update(89, "not_valid")

    def testupdateargssizezero(self):
        """test to update the value of size with zero"""
        sqr = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.update(89, 0)

    def testupdateargssizenegative(self):
        """test to update the size args with negative value"""
        sqr = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.update(89, -4)

    def testupdateargsinvalidx(self):
        """test to update x with invalid type"""
        sqr = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr.update(89, 1, "not_valid")

    def testupdateargsxnegative(self):
        """test to update the x args with negative value"""
        sqr = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sqr.update(98, 1, -4)

    def testupdateargsinvalidy(self):
        """test to update y with invalid type"""
        sqr = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sqr.update(89, 1, 2, "not_valid")

    def testupdateargsynegative(self):
        """test to update the y args with negative value"""
        sqr = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sqr.update(98, 1, 2, -4)

    def testupdateargssizebeforex(self):
        """test to update the size args before x"""
        sqr = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.update(89, "not_valid", "not_valid")

    def testupdateargssizebeforey(self):
        """test to update the size args before y"""
        sqr = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.update(89, "not_valid", 2, "not_valid")

    def testupdateargsxbeforey(self):
        """test to update the x args before y"""
        sqr = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr.update(89, 1, "not_valid", "not_valid")


class TestSquareupdatekwargs(unittest.TestCase):
    """Unittest for update_kwargs method of the Square class."""

    def testupdatekwargsone(self):
        """test to update square with one argument"""
        sqr = Square(27, 27, 27, 27)
        sqr.update(id=32)
        self.assertEqual("[Square] (32) 27/27 - 27", str(sqr))

    def testupdatekwargstwo(self):
        """test to update square with two arguments"""
        sqr = Square(27, 27, 27, 27)
        sqr.update(id=32, size=2)
        self.assertEqual("[Square] (32) 27/27 - 2", str(sqr))

    def testupdatekwargsthree(self):
        """test to update square with three arguments"""
        sqr = Square(27, 27, 27, 27)
        sqr.update(id=32, size=2, x=3)
        self.assertEqual("[Square] (32) 3/27 - 2", str(sqr))

    def testupdatekwargsfour(self):
        """test to update square with four arguments"""
        sqr = Square(27, 27, 27, 27)
        sqr.update(id=32, size=2, x=3, y=4)
        self.assertEqual("[Square] (32) 3/4 - 2", str(sqr))

    def testupdatekwargswidthsetter(self):
        """test to update the width setter"""
        sqr = Square(27, 27, 27, 27)
        sqr.update(id=32, size=6)
        self.assertEqual(6, sqr.width)

    def testupdatekwargsheightsetter(self):
        """test to update the height setter"""
        sqr = Square(27, 27, 27, 27)
        sqr.update(id=32, size=6)
        self.assertEqual(6, sqr.height)

    def testupdatekwargsNoneid(self):
        """test to update square id with None"""
        sqr = Square(27, 27, 27, 27)
        sqr.update(id=None)
        exp_output = "[Square] ({}) 27/27 - 27".format(sqr.id)
        self.assertEqual(exp_output, str(sqr))

    def testupdatekwargsNoneidandmore(self):
        """test to update square id with None and other attr"""
        sqr = Square(27, 27, 27, 27)
        sqr.update(id=None, size=4, x=5)
        exp_output = "[Square] ({}) 5/27 - 4".format(sqr.id)
        self.assertEqual(exp_output, str(sqr))

    def testupdatekwargstwice(self):
        """test to update square twice"""
        sqr = Square(27, 27, 27, 27)
        sqr.update(id=32, size=2, x=3)
        sqr.update(id=4, size=3, x=2, y=32)
        self.assertEqual("[Square] (4) 2/32 - 3", str(sqr))

    def testupdatekwargsinvalidsizetype(self):
        """test to update size with invalid type"""
        sqr = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.update(size="not_valid")

    def testupdatekwargssizezero(self):
        """test to update the value of size with zero"""
        sqr = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.update(size=0)

    def testupdatekwargssizenegative(self):
        """test to update the size kwargs with negative value"""
        sqr = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.update(size=-4)

    def testupdatekwargsinvalidx(self):
        """test to update x with invalid type"""
        sqr = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr.update(x="not_valid")

    def testupdatekwargsxnegative(self):
        """test to update the x kwargs with negative value"""
        sqr = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sqr.update(x=-4)

    def testupdatekwargsinvalidy(self):
        """test to update y with invalid type"""
        sqr = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sqr.update(y="not_valid")

    def testupdatekwargsynegative(self):
        """test to update the y kwargs with negative value"""
        sqr = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sqr.update(y=-4)

    def testupdateargsandkwargs(self):
        """test to update args and kwargs"""
        sqr = Square(9, 7, 5, 3)
        sqr.update(23, 5, x=17)
        self.assertEqual("[Square] (23) 7/5 - 5", str(sqr))

    def testpdatekwargswithwrongkeys(self):
        """test to update kwargs with wrong keys"""
        sqr = Square(10, 8, 6, 4)
        sqr.update(t=4, d=7)
        self.assertEqual("[Square] (4) 8/6 - 10", str(sqr))

    def testupdatekwargsandsomewrongkeys(self):
        """test to update kwargs and some wrong keys"""
        sqr = Square(9, 7, 5, 3)
        sqr.update(size=8, id=2, t=6, d=31)
        self.assertEqual("[Square] (2) 7/5 - 8", str(sqr))


class TestSquaretoDictionary(unittest.TestCase):
    """Unittest for the to_dictionary method of the Square class"""

    def testoutputmatchtodictionary(self):
        """test if output dictionary matches the expected result"""
        sqr = Square(16, 8, 4, 2)
        exp_output = {'id': 2, 'x': 8, 'y': 4, 'size': 16}
        self.assertDictEqual(exp_output, sqr.to_dictionary())

    def testnochangeofobject(self):
        """test to verify calling update does not modify original object"""
        sqr1 = Square(10, 8, 6, 2)
        sqr2 = Square(9, 7, 1)
        sqr2.update(**sqr1.to_dictionary())
        self.assertNotEqual(sqr1, sqr2)

    def testpassingargtodict(self):
        """test to check when argument is passed to dictionary"""
        sqr = Square(10, 7, 6, 3)
        with self.assertRaises(TypeError):
            sqr.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
