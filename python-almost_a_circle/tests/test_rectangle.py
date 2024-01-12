import io
import sys
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

    def test_display_without_x_y(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r = Rectangle(3, 4)
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "###\n###\n###\n###\n")

    def test_display_without_y(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r = Rectangle(3, 4, 2)
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "  ###\n  ###\n  ###\n  ###\n")

    def test_display(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r = Rectangle(1, 2, 2, 3)
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "\n\n\n  #\n  #\n")

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(), {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_update(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (2, 2, 2, 2, 2))

    # Tests for update with args
    def test_update_with_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (2, 3, 4, 5, 6))

    # Tests for update with kwargs
    def test_update_with_kwargs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (2, 3, 4, 5, 6))

    # Tests for create
    def test_create(self):
        r = Rectangle.create(id=1, width=2, height=3, x=4, y=5)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (1, 2, 3, 4, 5))

    # Tests for save_to_file and load_from_file
    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_single(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertIn('"id": 1', file.read())

    def test_load_from_file_no_file(self):
        Rectangle.save_to_file(None)  # Ensure no file exists
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_with_file(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual((rectangles[0].id, rectangles[0].width, rectangles[0].height, rectangles[0].x, rectangles[0].y), (5, 1, 2, 3, 4))

if __name__ == '__main__':
    unittest.main()
