import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    # Tests for initialization
    def test_rectangle_init_two_args(self):
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height), (1, 2))

    def test_rectangle_init_three_args(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.width, r.height, r.x), (1, 2, 3))

    def test_rectangle_init_four_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_rectangle_with_string_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_with_string_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_with_string_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_with_string_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_with_five_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), (1, 2, 3, 4, 5))

    def test_rectangle_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    # Tests for methods
    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    # Assuming display() prints a string representation of the rectangle
    # Here you would need to capture stdout to test the display method
    # For simplicity, this test is omitted

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(), {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_update(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (2, 2, 2, 2, 2))

if __name__ == '__main__':
    unittest.main()
