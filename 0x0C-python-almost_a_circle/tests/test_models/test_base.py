import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class baseClassTestCase(unittest.TestCase):
    def setUp(self):
        b1 = Base()
        self.id1 = b1.id
        b2 = Base()
        self.id2 = b2.id
        b3 = Base(12)
        self.id3 = b3.id
        b4 = Base(-13)
        self.id4 = b4.id
        b5 = Base(None)
        self.id5 = b5.id
        b6 = Base('5')
        self.id6 = b6.id

    def test_class_member(self):
        """ test class membership """
        b = Base()
        self.assertIsInstance(b, Base)

    def test_base_empty_param(self):
        self.assertEqual(self.id1, 1)
        self.assertEqual(self.id2, 2)
        
    def test_base_with_param(self):
        self.assertEqual(self.id3, 12)
        self.assertEqual(self.id4, -13)
        self.assertEqual(self.id5, 6)
        self.assertEqual(self.id6, '5')

    def test_to_json_string_with_dict_list(self):
        """ test the to_json_string static method with dictionary list """
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIs(type(dictionary), dict)
        self.assertIs(type(json_dictionary), str)

    def test_to_json_string_with_empty_list(self):
        """ test the to_json_string static method with empty list """
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")
    
    def test_to_json_string_with_none_arg(self):
        """ test the to_json_string static method with non arg """
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_save_to_file_method_with_valid_arg(self):
        """ test the save_to_file class method with valid param """
        r1 = Rectangle(10, 7, 2, 8, 40)
        r2 = Rectangle(2, 4, 0, 0, 40)
        dict_lis = []
        expected = [{"y": 8, "x": 2, "id": 40, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 40, "width": 2, "height": 4}]

        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            dict_lis = json.load(file)
        self.assertEqual(len(dict_lis), 2)
        self.assertIsInstance(dict_lis, list)
        self.assertEqual(expected, dict_lis)

        s1 = Square(5, 2, 3, 4)
        s2 = Square(4, 3, 3, 21)
        Square.save_to_file([s1, s2])
        dict_lis = []
        expected = [{"x": 2, "y": 3, "id": 4, "size": 5}, {"x": 3, "y": 3, "id": 21, "size": 4}]
        with open("Square.json", "r") as file:
            dict_lis = json.load(file)
        self.assertEqual(len(dict_lis), 2)
        self.assertIsInstance(dict_lis, list)
        self.assertEqual(expected, dict_lis)

    def test_save_to_file_method_with_none_arg(self):
        """ test the save_to_file class method with None param """
        r3 = Rectangle(4, 5)
        r3.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            result = json.load(file)
        self.assertEqual(result, [])
    
        s3 = Square(4, 5)
        s3.save_to_file(None)
        with open("Square.json", "r") as file:
            result = json.load(file)
        self.assertEqual(result, [])

    def test_save_to_file_method_with_empty_arg(self):
        """ test the save_to_file class method with empty list """
        r4 = Rectangle(4, 5)
        r4.save_to_file([])

        with open("Rectangle.json", "r") as file:
            result = json.load(file)
        self.assertEqual(result, [])

        s4 = Square(4, 5)
        s4.save_to_file([])
        with open("Square.json", "r") as file:
            result = json.load(file)
        self.assertEqual(result, [])
    
    def test_from_json_string_with_valid_arg(self):
        """ test the from_json_string static methid with valid param """
        list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_output, list)
        self.assertEqual(list_input, list_output)
    
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)

        self.assertIsInstance(list_output, list)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_with_none_arg(self):
        """ test the from_json_string static methid with None param """
        output = Base.from_json_string(None)
        self.assertEqual(output, [])

    def test_from_json_string_with_empty_arg(self):
        """ test the from_json_string static method with empty list """
        output = Base.from_json_string([])
        self.assertEqual(output, [])

    def test_create_method_with_valid_args(self):
        """ test the create class method with valid params """
        r3 = Rectangle(3, 5, 1)
        r3_dictionary = r3.to_dictionary()
        r4 = Rectangle.create(**r3_dictionary)
        self.assertIs(type(r4), Rectangle)
        self.assertIsNot(r3, r4)
        self.assertNotEqual(r3, r4)

        self.assertIsInstance(r4, Base)

        s4 = Square.create(size=4, x=2, y=3)
        self.assertIs(type(s4), Square)
        self.assertIsInstance(s4, Base)
        
    def test_create_method_with_invalid_args(self):
        """ test the create class method with invalid params """
        with self.assertRaises(TypeError):
            r5 = Rectangle.create({'width': 3, 'height': 6})
        with self.assertRaises(TypeError):
            r5 = Rectangle.create(width='5', height='6')
        with self.assertRaises(ValueError):
            r5 = Rectangle.create(width=-5, height=-6)
        with self.assertRaises(TypeError):
            r5 = Rectangle.create(None)


        with self.assertRaises(TypeError):
            s5 = Square.create({'size': 3, 'y': 6})
        with self.assertRaises(TypeError):
            s5 = Square.create(size='6')
        with self.assertRaises(ValueError):
            s5 = Square.create(size=-6)
        with self.assertRaises(TypeError):
            s5 = Square.create(None)

    def test_load_from_file_method_with_rec_inst(self):
        """ test the load_from_file with valid file name on Rectangle instance """
        r6 = Rectangle(10, 7, 2, 8)
        r7 = Rectangle(2, 4)
        list_rectangles_input = [r6, r7]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        

        for rect_in, rect_out in zip(list_rectangles_input, list_rectangles_output):
            self.assertIs(type(rect_out), Rectangle)
            self.assertFalse(rect_in is rect_out)
            self.assertFalse(rect_in.to_dictionary() is rect_out.to_dictionary())

            self.assertFalse(rect_in == rect_out)
            self.assertTrue(rect_in.to_dictionary() == rect_out.to_dictionary())
        
    def test_load_from_file_method_with_square_inst(self):
        """ test the load_from_file with valid file name on Square instance """
        s5 = Square(5)
        s6 = Square(7, 9, 1)
        list_squares_input = [s5, s6]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()
        

        for sq_in, sq_out in zip(list_squares_input, list_squares_output):
            self.assertIs(type(sq_out), Square)
            self.assertFalse(sq_in is sq_out)
            self.assertFalse(sq_in.to_dictionary() is sq_out.to_dictionary())

            self.assertFalse(sq_in == sq_out)
            self.assertTrue(sq_in.to_dictionary() == sq_out.to_dictionary())

    def test_load_from_file_method_with_none(self):
        """ test the method on None existing file """
        self.assertEqual(Base.load_from_file(), [])
