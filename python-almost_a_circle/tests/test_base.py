#!/usr/bin/python3
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_base_instances_with_no_argument(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_base_instances_with_three_arguments(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_base_instances_with_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id_assignment(self):
        self.assertEqual(12, Base(12).id)

    def test_number_of_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_setting_id_publicly(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_attempt_access_private_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id_assignment(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id_assignment(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id_assignment(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id_assignment(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id_assignment(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id_assignment(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id_assignment(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id_assignment(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id_assignment(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id_assignment(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id_assignment(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id_assignment(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id_assignment(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id_assignment(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id_assignment(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_attempt_two_args_assignment(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_attempt_two_args_assignment(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

class TestJsonStringConversion(unittest.TestCase):
    def test_convert_rectangle_to_string_type(self):
        r = Rectangle(2, 3, 3, 3, 5)
        result = Base.to_json_string([r.to_dictionary()])
        self.assertIsInstance(result, str)

    def test_single_rectangle_json_string_length(self):
        r = Rectangle(2, 3, 3, 3, 5)
        json_string = Base.to_json_string([r.to_dictionary()])
        expected_length = len(json.dumps([r.to_dictionary()]))
        self.assertEqual(len(json_string), expected_length)

    def test_combined_length_two_rectangles_json_string(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        json_string = Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()])
        expected_length = len(json.dumps([r1.to_dictionary(), r2.to_dictionary()]))
        self.assertEqual(len(json_string), expected_length)

    def test_convert_square_to_string_type(self):
        s = Square(5, 1, 1, 4)
        result = Base.to_json_string([s.to_dictionary()])
        self.assertIsInstance(result, str)

    def test_single_square_json_string_length(self):
        s = Square(5, 1, 1, 4)
        json_string = Base.to_json_string([s.to_dictionary()])
        expected_length = len(json.dumps([s.to_dictionary()]))
        self.assertEqual(len(json_string), expected_length)

    def test_combined_length_two_squares_json_string(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        json_string = Base.to_json_string([s1.to_dictionary(), s2.to_dictionary()])
        expected_length = len(json.dumps([s1.to_dictionary(), s2.to_dictionary()]))
        self.assertEqual(len(json_string), expected_length)

    def test_empty_list_returns_empty_json_array(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none_argument_returns_empty_json_array(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_raises_type_error_without_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_raises_type_error_with_multiple_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

class TestBaseSaveToFile(unittest.TestCase):
    def test_save_one_rectangle_to_file(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(len(contents), 52)

    def test_save_two_rectangles_to_file(self):
        r1 = Rectangle(3, 5, 7, 9, 2)
        r2 = Rectangle(3, 6, 2, 3, 5)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(len(contents), 104)

    def test_save_one_square_to_file(self):
        s = Square(5, 2, 3, 4)
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            contents = file.read()
            self.assertEqual(len(contents), 38)

    def test_save_two_squares_to_file(self):
        s1 = Square(4, 4, 4, 4)
        s2 = Square(6, 6, 6, 6)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            contents = file.read()
            self.assertEqual(len(contents), 76)

    def test_save_to_file_using_base_class(self):
        s = Square(5, 5, 5, 5)
        Base.save_to_file([s])
        with open("Base.json", "r") as file:
            contents = file.read()
            self.assertEqual(len(contents), 38)

    def test_save_to_file_overwrites_existing_file(self):
        s = Square(6, 6 ,6 ,6)
        Square.save_to_file([s])
        s = Square(5, 5, 5, 5)
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            contents = file.read()
            self.assertEqual(len(contents), 38)

    def test_save_to_file_with_None_creates_empty_file(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            contents = file.read()
            self.assertEqual(contents, "[]")

    def test_save_empty_list_to_file_creates_empty_file(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            contents = file.read()
            self.assertEqual(contents, "[]")

    def test_save_to_file_raises_error_without_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_raises_error_with_multiple_arguments(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBaseCreate(unittest.TestCase):
    """Unittests for testing the create method of the Base class."""

    def test_create_rectangle_with_original_attributes(self):
        original_rectangle = Rectangle(2, 3, 4, 5, 7)
        created_rectangle = Rectangle.create(**original_rectangle.to_dictionary())
        self.assertEqual(str(original_rectangle), "[Rectangle] (7) 4/5 - 2/3")
        self.assertIsNot(original_rectangle, created_rectangle)
        self.assertNotEqual(original_rectangle, created_rectangle)

    def test_create_rectangle_with_created_attributes(self):
        original_rectangle = Rectangle(2, 3, 4, 5, 7)
        created_rectangle = Rectangle.create(**original_rectangle.to_dictionary())
        self.assertEqual(str(created_rectangle), "[Rectangle] (7) 4/5 - 2/3")

    def test_create_square_with_original_attributes(self):
        original_square = Square(6, 3, 2, 1)
        created_square = Square.create(**original_square.to_dictionary())
        self.assertEqual(str(original_square), "[Square] (1) 3/2 - 6")
        self.assertIsNot(original_square, created_square)
        self.assertNotEqual(original_square, created_square)

    def test_create_square_with_created_attributes(self):
        original_square = Square(6, 3, 2, 1)
        created_square = Square.create(**original_square.to_dictionary())
        self.assertEqual(str(created_square), "[Square] (1) 3/2 - 6")

# class TestBaseLoadFromFile(unittest.TestCase):
#     def test_load_rectangles_from_file_matches_saved_instances(self):
#         r1 = Rectangle(2, 4, 5, 9, 1)
#         r2 = Rectangle(1, 2, 5, 4, 5)
#         Rectangle.save_to_file([r1, r2])
#         loaded_rectangles = Rectangle.load_from_file()
#         self.assertEqual(str(r1), str(loaded_rectangles[0]))
#         self.assertEqual(str(r2), str(loaded_rectangles[1]))

#     def test_loaded_rectangle_objects_are_of_correct_type(self):
#         Rectangle.save_to_file([Rectangle(5, 2, 3, 1, 1), Rectangle(6, 5, 4, 8, 2)])
#         loaded_rectangles = Rectangle.load_from_file()
#         self.assertTrue(all(isinstance(obj, Rectangle) for obj in loaded_rectangles))

#     def test_load_squares_from_file_matches_saved_instances(self):
#         s1 = Square(2, 5, 4, 1)
#         s2 = Square(7, 8, 6, 7)
#         Square.save_to_file([s1, s2])
#         loaded_squares = Square.load_from_file()
#         self.assertEqual(str(s1), str(loaded_squares[0]))
#         self.assertEqual(str(s2), str(loaded_squares[1]))

#     def test_loaded_square_objects_are_of_correct_type(self):
#         Square.save_to_file([Square(7, 6, 6, 6), Square(6, 7, 7, 7)])
#         loaded_squares = Square.load_from_file()
#         self.assertTrue(all(isinstance(obj, Square) for obj in loaded_squares))

#     def test_load_from_file_returns_empty_list_when_no_file_exists(self):
#         self.assertEqual([], Square.load_from_file())

#     def test_load_from_file_raises_error_with_multiple_arguments(self):
#         with self.assertRaises(TypeError):
#             Base.load_from_file([], 1)

if __name__ == "__main__":
    unittest.main()
