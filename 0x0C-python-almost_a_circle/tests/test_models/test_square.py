#!/usr/bin/python3
""" Module testing the square file """

from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
from io import StringIO
import sys
import unittest


class TestSquareClass(unittest.TestCase):
    """ unittest cases for the square class """
    
    def test_base_rec_class_membership(self):
        """ test if the square is a member of the rec. and base class """
        sq = Square(5)
        self.assertIsInstance(sq, Rectangle)
        self.assertIsInstance(sq, Base)
        self.assertIsInstance(sq, Square)

    def test_square_instance_with_empty_arg(self):
        """ test if nor arg is passed to the square instanciation """
        with self.assertRaises(TypeError):
            sq = Square()

    def test_square_instance_with_normal_args(self):
        """ test when all valid args are passed into the class """
        sq1 = Square(2, 2, 2, 4)
        self.assertEqual(sq1.id, 4)
        self.assertEqual(sq1.width, 2)
        self.assertEqual(sq1.height, 2)
        self.assertEqual(sq1.x, 2)
        self.assertEqual(sq1.y, 2)

    def test_square_with_invalid_arg(self):
        """ test when invalid arg is passed into square """
        with self.assertRaises(TypeError):
            sq2 = Square('2')
        with self.assertRaises(TypeError):
            sq2 = Square(2, '2')
        with self.assertRaises(TypeError):
            sq2 = Square(1, 2, '3')
        with self.assertRaises(ValueError):
            sq2 = Square(-2)
        with self.assertRaises(ValueError):
            sq2 = Square(1, -2)
        with self.assertRaises(ValueError):
            sq2 = Square(1, 2, -2)
        with self.assertRaises(ValueError):
            sq2 = Square(0)
            
    def test_square_private_attr_accsess(self):
        """ tests for the object private attr access """
        sq3 = Square(5)
        with self.assertRaises(AttributeError):
            sq3 = sq3.__width
        with self.assertRaises(AttributeError):
            sq3 = sq3.__height
        with self.assertRaises(AttributeError):
            sq3 = sq3.__x
        with self.assertRaises(AttributeError):
            sq3 = sq3.__y

    def test_square_area_method(self):
        """ test the square method of the square class """
        sq4 = Square(4)
        self.assertEqual(sq4.area(), 16)

    def test_square_display_method_with_cordinates(self):
        """ test the display method of the class """
        sq5 = Square(2, 2, 2, 4)
        io_obj = StringIO()
        sys.stdout = io_obj
        sq5.display()
        self.assertEqual(io_obj.getvalue(), "\n\n  ##\n  ##\n")

    def test_square_display_method_without_cordinates(self):
        """ test the display method of the class without x/y cordinates"""
        sq5 = Square(2)
        io_obj = StringIO()
        sys.stdout = io_obj
        sq5.display()
        self.assertEqual(io_obj.getvalue(), "##\n##\n")

    def test_square_str_method(self):
        """ test the __str__ method of the sqaure class """
        sq6 = Square(4, 2, 2, 5)
        self.assertEqual(sq6.__str__(), "[Square] (5) 2/2 - 4")

    def test_square_attribute_setter(self):
        """ tests setting attr. with setter method """
        sq7 = Square(5, 3)
        sq7.width = 10
        sq7.height = 4
        sq7.x = 2
        sq7.y = 4
        self.assertEqual(sq7.width, 10)
        self.assertEqual(sq7.height, 4)
        self.assertEqual(sq7.x, 2)
        self.assertEqual(sq7.y, 4)

    def test_square_attr_setter_non_int(self):
        """ tests when non int arg is supplied to setter """
        sq8= Square(5, 3)
        with self.assertRaises(TypeError):
            sq8.width = '10'
        with self.assertRaises(TypeError):
            sq8.height = '3'
        with self.assertRaises(TypeError):
            sq8.x = '6'
        with self.assertRaises(TypeError):
            sq8.y = '6'

    def test_square_attr_setter_with_neg_val(self):
        sq9 = Square(5, 3)
        with self.assertRaises(ValueError):
            sq9.width = -10
        with self.assertRaises(ValueError):
            sq9.height = -3
        with self.assertRaises(ValueError):
            sq9.x = -2
        with self.assertRaises(ValueError):
            sq9.y = -6

    def test_size_method_with_valid_arg(self):
        sq10 = Square(8)
        sq10.size = 10
        self.assertEqual(sq10.size, 10)
    
    def test_size_method_with_invalid_arg(self):
        """ test the size method with wrong arg """
        sq11 = Square(6)
        with self.assertRaises(TypeError):
            sq11.size = '8'
        with self.assertRaises(ValueError):
            sq11.size = -4

    def test_update_method_with_valid_args(self):
        """ test the update method of the class """
        sq12 = Square(5, 0, 0, 12)
        self.assertEqual(sq12.__str__(), "[Square] (12) 0/0 - 5")
        sq12.update(10)
        self.assertEqual(sq12.__str__(), "[Square] (10) 0/0 - 5")
        sq12.update(1, 2)
        self.assertEqual(sq12.__str__(), "[Square] (1) 0/0 - 2")
        sq12.update(1, 2, 3)
        self.assertEqual(sq12.__str__(), "[Square] (1) 3/0 - 2")
        sq12.update(1, 2, 3, 4)
        self.assertEqual(sq12.__str__(), "[Square] (1) 3/4 - 2")
        sq12.update(x=12)
        self.assertEqual(sq12.__str__(), "[Square] (1) 12/4 - 2")
        sq12.update(size=7, y=1)
        self.assertEqual(sq12.__str__(), "[Square] (1) 12/1 - 7")
        sq12.update(size=7, id=89, y=1)
        self.assertEqual(sq12.__str__(), "[Square] (89) 12/1 - 7")

    def test_to_dictionary_method(self):
        """ test the to_dictonary method """
        sq13 = Square(10, 2, 1, 13)
        sq13_dictionary = sq13.to_dictionary()
        self.assertEqual(sq13_dictionary, {'id': 13, 'x': 2, 'size': 10, 'y': 1})
        self.assertIs(type(sq13_dictionary), dict)
