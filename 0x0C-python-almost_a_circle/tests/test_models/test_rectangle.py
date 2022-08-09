
#!/usr/bin/python3
""" The rectangle testing module """


from models.rectangle import Rectangle
from models.base import Base
import unittest
from io import StringIO
import sys


class rectangleClassTestCases(unittest.TestCase):
    """ test casees for the rectangle class """
    
    def test_rec_class_member(self):
        """ checks instance membership """
        r = Rectangle(4, 2)
        self.assertIsInstance(r, Base)
        self.assertIsInstance(r, Rectangle)

    def test_rec_empty_arg(self):
        """ tests when no arg supppied """
        with self.assertRaises(TypeError):
            r0 = Rectangle()
            r0 = Rectangle(1)

    def test_rec_id_with_id_arg(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_rec_with_valid_args(self):
        r4 = Rectangle(1, 2)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        r4 = Rectangle(1, 2, 3)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        r4 = Rectangle(10, 2, 2, 4, 12)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 2)
        self.assertEqual(r4.y, 4)

    def test_rec_private_attribute_access(self):
        """ Test error thrown when trying to access private  attr.
        """        
        r5 = Rectangle(5, 3)
        with self.assertRaises(AttributeError):
            r5.___width
        with self.assertRaises(AttributeError):
            r5.___height
        with self.assertRaises(AttributeError):
            r5.__x
        with self.assertRaises(AttributeError):
            r5.___y

    def test_rec_private_attribute_setter(self):
        """ tests setting attr. with setter method """
        r6 = Rectangle(5, 3)
        r6.width = 10
        r6.height = 4
        r6.x = 2
        r6.y = 4
        self.assertEqual(r6.width, 10)
        self.assertEqual(r6.height, 4)
        self.assertEqual(r6.x, 2)
        self.assertEqual(r6.y, 4)

    def test_rec_private_attr_setter_non_int(self):
        """ tests when non int arg is supplied to setter """
        r6 = Rectangle(5, 3)
        with self.assertRaises(TypeError):
            r6.width = '10'
        with self.assertRaises(TypeError):
            r6.height = '3'
        with self.assertRaises(TypeError):
            r6.x = '6'
        with self.assertRaises(TypeError):
            r6.y = '6'

    def test_rec_private_attr_setter_neg_int(self):
        """ tests when negative int arg is supplied to setter """
        r6 = Rectangle(5, 3)
        with self.assertRaises(ValueError):
            r6.width = -10
        with self.assertRaises(ValueError):
            r6.height = -3
        with self.assertRaises(ValueError):
            r6.x = -6
        with self.assertRaises(ValueError):
            r6.y = -6

    def test_rec_on_non_int_arg(self):
        """ test when invalid int arg supplied """
        with self.assertRaises(TypeError):
            r7 = Rectangle('5', 6)
        with self.assertRaises(TypeError):
            r7 = Rectangle(5, '6')
        with self.assertRaises(TypeError):
            r7 = Rectangle(5, 3, '4', 6)
        with self.assertRaises(TypeError):
            r7 = Rectangle(5, 3, 4, '6')

    def test_rec_on_neg_0_int_val(self):
        """ tests negative arguments """
        with self.assertRaises(ValueError):
            r8 = Rectangle(-5, 2)
        with self.assertRaises(ValueError):
            r8 = Rectangle(5, -2)
        with self.assertRaises(ValueError):
            r8 = Rectangle(5, 2, -2, 2)
        with self.assertRaises(ValueError):
            r8 = Rectangle(5, 2, 2, -2)
        with self.assertRaises(ValueError):
            r8 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r8 = Rectangle(5, 0)

    def test_rec_area(self):
        """ tests the area of the rec obj """
        r9 = Rectangle(3, 2)
        self.assertEqual(r9.area(), 6)
        r10 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r10.area(), 56)

    def test_rec_display(self):
        """ tests the display public instance method """
        r11 = Rectangle(2, 3, 2, 2)
        io_obj = StringIO()
        sys.stdout = io_obj
        r11.display()
        value = io_obj.getvalue()
        self.assertEqual(value, "\n\n  ##\n  ##\n  ##\n")
        
    def test_rec_str_method(self):
        """ tests the __str__ method """
        r12 = Rectangle(4, 6, 2, 1, 12)
        r12_str = r12.__str__()
        r13 = Rectangle(5, 5, 1, 2, 13)
        r13_str = r13.__str__()
        self.assertEqual(r12_str, "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(r13_str, "[Rectangle] (13) 1/2 - 5/5")
    
    def test_rec_update_method(self):
        """ tests the update_method with non_keyword args """
        r14 = Rectangle(10, 10, 10, 10, 9)
        self.assertEqual(r14.__str__(), "[Rectangle] (9) 10/10 - 10/10")
        r14.update(89)
        self.assertEqual(r14.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r14.update(89, 2)
        self.assertEqual(r14.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r14.update(89, 2, 3)
        self.assertEqual(r14.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r14.update(89, 2, 3, 4)
        self.assertEqual(r14.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r14.update(89, 2, 3, 4, 5)
        self.assertEqual(r14.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_rec_update_method_kwargs(self):
        """ Test the method with keyword args """
        r15 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r15.__str__(), "[Rectangle] (10) 10/10 - 10/10")
        r15.update(height=1)
        self.assertEqual(r15.__str__(), "[Rectangle] (10) 10/10 - 10/1")
        r15.update(width=1, x=2)
        self.assertEqual(r15.__str__(), "[Rectangle] (10) 2/10 - 1/1")
        r15.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r15.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r15.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r15.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary_method(self):
        """ test the to_dictionary method """
        r16 = Rectangle(10, 2, 1, 9, 16)
        r16_dictionary = r16.to_dictionary()
        self.assertEqual(r16_dictionary, {'x': 1, 'y': 9, 'id': 16, 'height': 2, 'width': 10})
        self.assertIs(type(r16_dictionary), dict)
