#!/usr/bin/python3
import unittest
from models.base import Base
class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0  # Resetting the __nb_objects class attribute before each test

    def test_auto_id_assignment(self):
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)

    def test_auto_id_increment(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)

    def test_manual_id_assignment(self):
        base_instance = Base(89)
        self.assertEqual(base_instance.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_single_dict(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_to_json_string_return_type(self):
        result = Base.to_json_string([{'id': 12}])
        self.assertTrue(isinstance(result, str))

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_single_dict(self):
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])

    def test_from_json_string_return_type(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertTrue(isinstance(result, list))

if __name__ == '__main__':
    unittest.main()
