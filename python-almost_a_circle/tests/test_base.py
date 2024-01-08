#!/usr/bin/python3
import json
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


if __name__ == "__main__":
    unittest.main()
