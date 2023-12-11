#!/usr/bin/python3
"""Unittest for base.py is defined"""
import unittest
from os import remove
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstance(unittest.TestCase):
    """Unittest for creating instances of the Base class"""

    def test_incr_id_no_arg(self):
        """test base increments ID properly with no arguments"""
        bs1 = Base()
        bs2 = Base()
        self.assertEqual(bs1.id, bs2.id - 1)

    def test_incr_id_thre_bases(self):
        """test base increments ID correctly with three instances"""
        bs1 = Base()
        bs2 = Base()
        bs3 = Base()
        self.assertEqual(bs1.id, bs3.id - 2)

    def test_incr_id_None(self):
        """test base increments ID correctly when initialized with None"""
        bs1 = Base(None)
        bs2 = Base(None)
        self.assertEqual(bs1.id, bs2.id - 1)

    def test_assign_unique_id(self):
        """test base sets the correct ID when initialized with a Unique ID"""
        self.assertEqual(23, Base(23).id)

    def test_inst_after_unique_id(self):
        """test number of instances is correct after unique ID assignment"""
        bs1 = Base()
        bs2 = Base(19)
        bs3 = Base()
        self.assertEqual(bs1.id, bs3.id - 1)

    def test_public_id_mod(self):
        """test ID can be modified publicly after instantation"""
        bs = Base(23)
        bs.id = 19
        self.assertEqual(19, bs.id)

    def test_private_nb_inst(self):
        """test __nb_instances attribute is private"""
        with self.assertRaises(AttributeError):
            print(Base(23).__nb_instances)

    def test_inst_with_two_args(self):
        """test base handles instances with two arguments"""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_string_id(self):
        """teest that handles string id correctly"""
        self.assertEqual("test", Base("test").id)

    def test_dictionary_id(self):
        """test that handles dictionary id correctly"""
        self.assertEqual({"key": 2, "val": 3}, Base({"key": 2, "val": 3}).id)

    def test_list_id(self):
        """test that handles list id correctly"""
        self.assertEqual([2, 3, 9], Base([2, 3, 9]).id)

    def test_tuple_id(self):
        """test that handles tuple id correctly"""
        self.assertEqual((9, 2), Base((9, 2)).id)

    def test_float_id(self):
        """test that handles float id correctly"""
        self.assertEqual(9.8, Base(9.8).id)

    def test_inf_id(self):
        """test that handles inf id correctly"""
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        """test that handles NaN id correctly"""
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_complex_id(self):
        """test that handles complex id correctly"""
        self.assertEqual(complex(7), Base(complex(7)).id)

    def test_bool_id(self):
        """test that handles bool id correctly"""
        self.assertEqual(False, Base(False).id)

    def test_set_id(self):
        """test that handles set id correctly"""
        self.assertEqual({2, 3, 4}, Base({2, 3, 4}).id)

    def test_frozenset_id(self):
        """test that handles frozenset id correctly"""
        self.assertEqual(frozenset({2, 3, 9}), Base({2, 3, 9}).id)

    def test_range_id(self):
        """test that handles range id correctly"""
        self.assertEqual(range(8), Base(range(8)).id)

    def test_bytes_id(self):
        """test that handles bytes id correctly"""
        self.assertEqual(b'Test', Base(b'Test').id)

    def test_bytearray_id(self):
        """test that handles byte array id correctly"""
        self.assertEqual(bytearray(b'val'), Base(bytearray(b'val')).id)

    def test_memoryview_id(self):
        """test that handles memory view id correctly"""
        self.assertEqual(memoryview(b'key'), Base(memoryview(b'key')).id)


class TestBasetojsonstring(unittest.TestCase):
    """Unittest for converting Base class instances to JSON strings"""

    def test_to_json_string_rect_type(self):
        """test to_json_string returns a string for a rectangle"""
        rec = Rectangle(11, 8, 6, 4, 7)
        self.assertEqual(str, type(Base.to_json_string([rec.to_dictionary()])))

    def test_to_json_string_rect_one_dict(self):
        """test to_json_string returns length of one rectangle dict"""
        rec = Rectangle(11, 8, 6, 4, 7)
        self.assertTrue(len(Base.to_json_string([rec.to_dictionary()])) == 53)

    def test_to_json_string_rect_two_dict(self):
        """test to_json_string returns length of two rectangle dict"""
        rec1 = Rectangle(3, 6, 9, 23, 4)
        rec2 = Rectangle(3, 6, 5, 9, 13)
        lst_dicts = [rec1.to_dictionary(), rec2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(lst_dicts)) == 106)

    def test_to_json_string_sqr_type(self):
        """test to_json_string returns a string for a square"""
        sqr = Square(12, 6, 8, 9)
        self.assertEqual(str, type(Base.to_json_string([sqr.to_dictionary()])))

    def test_to_json_string_sqr_one_dict(self):
        """test to_json_string returns length of one square dict"""
        sqr = Square(12, 6, 8, 9)
        self.assertTrue(len(Base.to_json_string([sqr.to_dictionary()])) == 39)

    def test_to_json_string_sqr_two_dict(self):
        """test to_json_string returns length of two square dict"""
        sqr1 = Square(13, 6, 9, 2)
        sqr2 = Square(4, 6, 8, 23)
        lst_dicts = [sqr1.to_dictionary(), sqr2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(lst_dicts)) == 78)

    def test_to_json_string_empt_lst(self):
        """test to_json_string for an empty list"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        """test to_json_string for a None list"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        """test to_json_string for a list with no arguments"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_err_more_than_one_arg(self):
        """test to_json_string for a list with more than one argument"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBasesavetofile(unittest.TestCase):
    """Unittest for saving Base calss instances to a file"""

    @classmethod
    def tearDown(self):
        """checks and deletes any created files"""
        try:
            remove("Rectangle.json")
        except IOError:
            pass
        try:
            remove("Square.json")
        except IOError:
            pass
        try:
            remove("Base.json")
        except IOError:
            pass

    def test_savetofile_onerect(self):
        """test save_to_file creates a file for one rectangle"""
        rec = Rectangle(12, 5, 6, 9, 2)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 53)

    def test_savetofile_tworect(self):
        """test save_to_file creates a file for two rectangles"""
        rec1 = Rectangle(12, 5, 8, 7, 1)
        rec2 = Rectangle(2, 5, 6, 9, 22)
        Rectangle.save_to_file([rec1, rec2])
        with open("Rectangle.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 106)

    def test_savetofile_onesqr(self):
        """test save_to_file creates a file for one square"""
        sqr = Square(9, 6, 5, 4)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 38)

    def test_savetofile_twosqr(self):
        """test save_to_file creates a file for two squares"""
        sqr1 = Square(7, 4, 9, 6)
        sqr2 = Square(3, 5, 1, 2)
        Square.save_to_file([sqr1, sqr2])
        with open("Square.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 76)

    def test_savetofile_clsnameforfilename(self):
        """test save_to_file use class name for filename"""
        sqr = Square(12, 8, 4, 9)
        Base.save_to_file([sqr])
        with open("Base.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 39)

    def test_savetofile_overwrite(self):
        """test save_to_file overwrites the file content"""
        sqr = Square(2, 7, 4, 30)
        Square.save_to_file([sqr])
        sqr = Square(12, 5, 7, 9)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 39)

    def test_savetofile_empt_list(self):
        """test save_to_file for an empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as fl:
            self.assertEqual("[]", fl.read())

    def test_savetofile_none(self):
        """test save_to_file for a none list"""
        Square.save_to_file(None)
        with open("Square.json", "r") as fl:
            self.assertEqual("[]", fl.read())

    def test_savetofile_noargs(self):
        """test save_to_file for a list with no arguments"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_savetofile_errmorethanonearg(self):
        """test save_to_file for a list with more than one argument"""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBasefromjsonstring(unittest.TestCase):
    """Unittest for creating base class instances from JSON strings"""

    def testfromjsonstringtype(self):
        """test from_json_string if a list of rectangle dict is returned"""
        s_data = [{"id": 23, "width": 15, "height": 7}]
        json_dt = Rectangle.to_json_string(s_data)
        ds_data = Rectangle.from_json_string(json_dt)
        self.assertEqual(list, type(ds_data))

    def testfromjsonstringonerect(self):
        """test from_json_string to return correct output for one rectangle"""
        s_data = [{"id": 77, "width": 23, "height": 4, "x": 8}]
        json_dt = Rectangle.to_json_string(s_data)
        ds_data = Rectangle.from_json_string(json_dt)
        self.assertEqual(s_data, ds_data)

    def testfromjsonstringtworect(self):
        """test from_json_string to return correct output for two rectangles"""
        s_data = [
            {"id": 33, "width": 15, "height": 8, "x": 2, "y": 7},
            {"id": 65, "width": 9, "height": 3, "x": 4, "y": 8}
        ]
        json_dt = Rectangle.to_json_string(s_data)
        ds_data = Rectangle.from_json_string(json_dt)
        self.assertEqual(s_data, ds_data)

    def testfromjsonstringonesqr(self):
        """test from_json_string to return correct output for one square"""
        s_data = [{"id": 22, "size": 12, "height": 5}]
        json_dt = Square.to_json_string(s_data)
        ds_data = Square.from_json_string(json_dt)
        self.assertEqual(s_data, ds_data)

    def testfromjsonstringtwosqr(self):
        """test from_json_string to return correct output for two squares"""
        s_data = [
            {"id": 23, "size": 15, "height": 8},
            {"id": 6, "size": 9, "height": 3}
        ]
        json_dt = Square.to_json_string(s_data)
        ds_data = Square.from_json_string(json_dt)
        self.assertEqual(s_data, ds_data)

    def testfromjsonstringemptlist(self):
        """test from_json_string for an empty list"""
        self.assertEqual([], Base.from_json_string("[]"))

    def testfromjsonstringnone(self):
        """test from_json_string for a none list"""
        self.assertEqual([], Base.from_json_string(None))

    def testfromjsonstringnoaargs(self):
        """test from_json_string for a list with no arguments"""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def testfromjsonstringerrmorethanonearg(self):
        """test from_json_string for a list with more than one argument"""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBasecreate(unittest.TestCase):
    """unittest for creating instances with the create method of Base class"""

    def testcreateoriginalrect(self):
        """test create to return original rectangle"""
        rec1 = Rectangle(2, 5, 8, 3, 4)
        rec1_dct = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dct)
        self.assertEqual("[Rectangle] (4) 8/3 - 2/5", str(rec1))

    def testcreatenewrect(self):
        """test create to return new rectangle"""
        rec1 = Rectangle(3, 4, 5, 8, 9)
        rec1_dct = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dct)
        self.assertEqual("[Rectangle] (9) 5/8 - 3/4", str(rec2))

    def testcreaterectinst(self):
        """test create to return new instance of the rectangle"""
        rec1 = Rectangle(2, 5, 8, 3, 4)
        rec1_dct = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dct)
        self.assertIsNot(rec1, rec2)

    def testcreaterectdiffinst(self):
        """test create to return different instance from the original"""
        rec1 = Rectangle(2, 5, 8, 3, 4)
        rec1_dct = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dct)
        self.assertNotEqual(rec1, rec2)

    def testcreateoriginalsqr(self):
        """test create to return original square"""
        sqr1 = Square(4, 5, 9, 2)
        sqr1_dct = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dct)
        self.assertEqual("[Square] (2) 5/9 - 4", str(sqr1))

    def testcreatenewsqr(self):
        """test create to return new square"""
        sqr1 = Square(4, 6, 7, 2)
        sqr1_dct = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dct)
        self.assertEqual("[Square] (2) 6/7 - 4", str(sqr2))

    def testcreatesqrinst(self):
        """test create to return new instance of the square"""
        sqr1 = Square(4, 5, 9, 2)
        sqr1_dct = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dct)
        self.assertIsNot(sqr1, sqr2)

    def testcreatediffinst(self):
        """test create to return different instance from the original"""
        sqr1 = Square(4, 6, 7, 2)
        sqr1_dct = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dct)
        self.assertNotEqual(sqr1, sqr2)


class TestBaseloadfromfile(unittest.TestCase):
    """unittest for loading Base class instances from a file"""

    @classmethod
    def tearDown(self):
        """checks and deletes any created files"""
        try:
            remove("Rectangle.json")
        except IOError:
            pass
        try:
            remove("Square.json")
        except IOError:
            pass

    def testloadfromfilefstrect(self):
        """test load_from_file to return first rectangle from the file"""
        rec1 = Rectangle(12, 7, 5, 9, 1)
        rec2 = Rectangle(3, 6, 8, 5, 4)
        Rectangle.save_to_file([rec1, rec2])
        loaded_rec = Rectangle.load_from_file()
        self.assertEqual(str(rec1), str(loaded_rec[0]))

    def testloadfromfilescdrect(self):
        """test load_from_file to return second rectangle from the file"""
        rec1 = Rectangle(12, 7, 5, 9, 1)
        rec2 = Rectangle(3, 6, 8, 5, 4)
        Rectangle.save_to_file([rec1, rec2])
        loaded_rec = Rectangle.load_from_file()
        self.assertEqual(str(rec2), str(loaded_rec[1]))

    def testloadfromfilerectype(self):
        """test load_from_file to return a list of rectangles"""
        rec1 = Rectangle(12, 7, 5, 9, 1)
        rec2 = Rectangle(3, 6, 8, 5, 4)
        Rectangle.save_to_file([rec1, rec2])
        loaded_rec = Rectangle.load_from_file()
        self.assertTrue(all(type(objct) == Rectangle for objct in loaded_rec))

    def testloadfromfilefstsqr(self):
        """test load_from_file to return the first square from the file"""
        sqr1 = Square(4, 7, 8, 9)
        sqr2 = Square(3, 6, 1, 5)
        Square.save_to_file([sqr1, sqr2])
        loaded_sqr = Square.load_from_file()
        self.assertEqual(str(sqr1), str(loaded_sqr[0]))

    def testloadfromfilescdsqr(self):
        """test load_from_file to return the second square from the file"""
        sqr1 = Square(4, 7, 8, 9)
        sqr2 = Square(3, 6, 1, 5)
        Square.save_to_file([sqr1, sqr2])
        loaded_sqr = Square.load_from_file()
        self.assertEqual(str(sqr2), str(loaded_sqr[1]))

    def testloadfromfilesqrtype(self):
        """test load_from_file to return list of squares"""
        sqr1 = Square(4, 7, 8, 9)
        sqr2 = Square(3, 6, 1, 5)
        Square.save_to_file([sqr1, sqr2])
        loaded_sqr = Square.load_from_file()
        self.assertTrue(all(type(objct) == Square for objct in loaded_sqr))

    def testloadfromfilenofile(self):
        """test load_from_file no file"""
        loaded_sqr = Square.load_from_file()
        self.assertEqual([], loaded_sqr)

    def testloadfromfileerrmorethanonearg(self):
        """test load_from_file for more than argument"""
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBasesavetofilecsv(unittest.TestCase):
    """unittest for saving Base class instances to a csv file"""

    @classmethod
    def tearDown(self):
        """checks and deletes any created files"""
        try:
            remove("Rectangle.csv")
        except IOError:
            pass
        try:
            remove("Square.csv")
        except IOError:
            pass
        try:
            remove("Base.csv")
        except IOError:
            pass

    def testsavetofilecsvonerect(self):
        """test save_to_file_csv creates a file for one rectangle"""
        rec = Rectangle(11, 6, 2, 9, 7)
        Rectangle.save_to_file_csv([rec])
        with open("Rectangle.csv", "r") as fl:
            self.assertTrue("7,11,6,2,9", fl.read())

    def testsavetofilecsvtworects(self):
        """test save_to_file_csv creates a file for two rectangles"""
        rec1 = Rectangle(12, 5, 6, 8, 9)
        rec2 = Rectangle(2, 5, 7, 9, 1)
        Rectangle.save_to_file_csv([rec1, rec2])
        with open("Rectangle.csv", "r") as fl:
            self.assertTrue("9,12,5,6,8\n2,5,7,9,1", fl.read())

    def testsavetofilecsvonesqr(self):
        """test save_to_file_csv creates a file for one square"""
        sqr = Square(12, 8, 5, 4)
        Square.save_to_file_csv([sqr])
        with open("Square.csv", "r") as fl:
            self.assertTrue("4,12,8,5", fl.read())

    def testsavetofilecsvtwosqrs(self):
        """test save_to_file_csv creates a file for two squares"""
        sqr1 = Square(14, 8, 4, 7)
        sqr2 = Square(5, 8, 1, 4)
        Square.save_to_file_csv([sqr1, sqr2])
        with open("Square.csv", "r") as fl:
            self.assertTrue("7,14,8,4\n4,5,8,1", fl.read())

    def testsavetofilecsvclsnameforfilename(self):
        """test save_to_file_csv use class name for filename"""
        sqr = Square(12, 8, 4, 9)
        Base.save_to_file_csv([sqr])
        with open("Base.csv", "r") as fl:
            self.assertTrue("9,12,8,4", fl.read())

    def testsavetofilecsvoverwrite(self):
        """test save_to_file_csv overwrites the file content"""
        sqr = Square(2, 7, 4, 30)
        Square.save_to_file([sqr])
        sqr = Square(12, 5, 7, 9)
        Square.save_to_file_csv([sqr])
        with open("Square.csv", "r") as fl:
            self.assertTrue("9,12,5,7", fl.read())

    def testsavetofilecsvemptlist(self):
        """test save_to_file_csv for an empty list"""
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as fl:
            self.assertEqual("[]", fl.read())

    def testsavetofilecsvnone(self):
        """test save_to_file_csv for a none list"""
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as fl:
            self.assertEqual("[]", fl.read())

    def testsavetofilecsvnoargs(self):
        """test save_to_file_csv for a list with no arguments"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def testsavetofilecsverrmorethanonearg(self):
        """test save_to_file _csv for a list with more than one argument"""
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBaseloadfromfilecsv(unittest.TestCase):
    """unittest for loading Base class instances from a csv file"""

    @classmethod
    def tearDown(self):
        """checks and deletes any created files"""
        try:
            remove("Rectangle.csv")
        except IOError:
            pass
        try:
            remove("Square.csv")
        except IOError:
            pass

    def testloadfromfilecsvfstrect(self):
        """test load_from_file_csv to return first rectangle from the file"""
        rec1 = Rectangle(12, 7, 5, 9, 1)
        rec2 = Rectangle(3, 6, 8, 5, 4)
        Rectangle.save_to_file_csv([rec1, rec2])
        loaded_rec = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec1), str(loaded_rec[0]))

    def testloadfromfilecsvscdrect(self):
        """test load_from_file_csv to return second rectangle from the file"""
        rec1 = Rectangle(12, 7, 5, 9, 1)
        rec2 = Rectangle(3, 6, 8, 5, 4)
        Rectangle.save_to_file_csv([rec1, rec2])
        loaded_rec = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec2), str(loaded_rec[1]))

    def testloadfromfilecsvrectype(self):
        """test load_from_file_csv to return a list of rectangles"""
        rec1 = Rectangle(12, 7, 5, 9, 1)
        rec2 = Rectangle(3, 6, 8, 5, 4)
        Rectangle.save_to_file_csv([rec1, rec2])
        loaded_rec = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(objct) == Rectangle for objct in loaded_rec))

    def testloadfromfilecsvfstsqr(self):
        """test load_from_file_csv to return the first square from the file"""
        sqr1 = Square(4, 7, 8, 9)
        sqr2 = Square(3, 6, 1, 5)
        Square.save_to_file_csv([sqr1, sqr2])
        loaded_sqr = Square.load_from_file_csv()
        self.assertEqual(str(sqr1), str(loaded_sqr[0]))

    def testloadfromfilecsvscdsqr(self):
        """test load_from_file_csv to return the second square from the file"""
        sqr1 = Square(4, 7, 8, 9)
        sqr2 = Square(3, 6, 1, 5)
        Square.save_to_file_csv([sqr1, sqr2])
        loaded_sqr = Square.load_from_file_csv()
        self.assertEqual(str(sqr2), str(loaded_sqr[1]))

    def testloadfromfilecsvsqrtype(self):
        """test load_from_file_csv to return list of squares"""
        sqr1 = Square(4, 7, 8, 9)
        sqr2 = Square(3, 6, 1, 5)
        Square.save_to_file_csv([sqr1, sqr2])
        loaded_sqr = Square.load_from_file_csv()
        self.assertTrue(all(type(objct) == Square for objct in loaded_sqr))

    def testloadfromfilecsvnofile(self):
        """test load_from_file_csv no file"""
        loaded_sqr = Square.load_from_file_csv()
        self.assertEqual([], loaded_sqr)

    def testloadfromfilecsverrmorethanonearg(self):
        """test load_from_file_csv for more than argument"""
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
