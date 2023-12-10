import unittest
from models.base import Base  # Replace with the actual module name

class TestBase(unittest.TestCase):

    def test_init_with_id(self):
        """Test __init__ with a specific id."""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_init_without_id(self):
        """Test __init__ without specifying an id."""
        current_count = Base._Base__nb_objects
        b = Base()
        self.assertEqual(b.id, current_count + 1)

if __name__ == "__main__":
    unittest.main()
