import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    # Tests for initialization
    def test_square_init_one_arg(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_init_two_args(self):
        s = Square(1, 2)
        self.assertEqual((s.size, s.x), (1, 2))

    def test_square_init_three_args(self):
        s = Square(1, 2, 3)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 3))

    def test_square_init_four_args(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual((s.size, s.x, s.y, s.id), (1, 2, 3, 4))

    def test_square_with_string_size(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_with_string_x(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_with_string_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)

    # Tests for methods
    def test_str(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.to_dictionary(), {'id': 4, 'size': 1, 'x': 2, 'y': 3})

    # Tests for update
    def test_update(self):
        s = Square(1, 1, 1, 1)
        s.update(2, 3, 4, 5)
        self.assertEqual((s.id, s.size, s.x, s.y), (2, 3, 4, 5))

    # Tests for update with args
    def test_update_with_args(self):
        s = Square(1, 1, 1, 1)
        s.update(2, 3, 4, 5)
        self.assertEqual((s.id, s.size, s.x, s.y), (2, 3, 4, 5))

    # Tests for update with kwargs
    def test_update_with_kwargs(self):
        s = Square(1, 1, 1, 1)
        s.update(id=2, size=3, x=4, y=5)
        self.assertEqual((s.id, s.size, s.x, s.y), (2, 3, 4, 5))

    # Tests for create
    def test_create(self):
        s = Square.create(id=1, size=2, x=3, y=4)
        self.assertIsInstance(s, Square)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 2, 3, 4))

    # Tests for save_to_file and load_from_file
    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_single(self):
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            self.assertIn('"id": 1', file.read())

    def test_load_from_file_no_file(self):
        Square.save_to_file(None)  # Ensure no file exists
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_with_file(self):
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        squares = Square.load_from_file()
        self.assertIsInstance(squares[0], Square)
        self.assertEqual((squares[0].id, squares[0].size, squares[0].x, squares[0].y), (4, 1, 2, 3))

if __name__ == '__main__':
    unittest.main()
