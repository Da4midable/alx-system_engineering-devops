"""Module for testing class Rectangle"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Class Rectangle tests"""

    def test_init(self):
        """Test if __init__() initializes the rectangle correctly."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(10, 2, 3, 4)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

        r3 = Rectangle(10, 2, id=5)
        self.assertEqual(r3.id, 5)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_validate_value(self):
        """Test if validate_value() performs validation correctly."""
        # Valid values
        Rectangle.validate_value('width', 10)
        Rectangle.validate_value('height', 2)
        Rectangle.validate_value('x', 3)
        Rectangle.validate_value('y', 4)

        # Invalid values
        with self.assertRaises(TypeError):
            Rectangle.validate_value('width', 'invalid')
        with self.assertRaises(ValueError):
            Rectangle.validate_value('height', -1)
        with self.assertRaises(ValueError):
            Rectangle.validate_value('x', 3.14)
        with self.assertRaises(ValueError):
            Rectangle.validate_value('y', -2)

    def test_property_width(self):
        """Test if width property works correctly."""
        r = Rectangle(10, 2)
        r.width = 5
        self.assertEqual(r.width, 5)

        with self.assertRaises(TypeError):
            r.width = 'invalid'
        with self.assertRaises(ValueError):
            r.width = -1

    def test_property_height(self):
        """Test if height property works correctly."""
        r = Rectangle(10, 2)
        r.height = 8
        self.assertEqual(r.height, 8)

        with self.assertRaises(TypeError):
            r.height = 'invalid'
        with self.assertRaises(ValueError):
            r.height = -1

    def test_property_x(self):
        """Test if x property works correctly."""
        r = Rectangle(10, 2)
        r.x = 3
        self.assertEqual(r.x, 3)

        with self.assertRaises(TypeError):
            r.x = 'invalid'
        with self.assertRaises(ValueError):
            r.x = -2

    def test_property_y(self):
        """Test if y property works correctly."""
        r = Rectangle(10, 2)
        r.y = 4
        self.assertEqual(r.y, 4)

        with self.assertRaises(TypeError):
            r.y = 'invalid'
        with self.assertRaises(ValueError):
            r.y = -2

    def test_area(self):
        """Test if area() method calculates area correctly."""
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)

    def test_display(self):
        """Test if display() method displays the rectangle correctly."""
        r = Rectangle(10, 2, 3, 4)
        expected_output = "\n\n\n   ##########\n   ##########\n"
        self.assertEqual(r.display(), expected_output)

    def test_str(self):
        """Test if __str__() method returns a formatted string."""
        r = Rectangle(10, 2, 3, 4)
        expected_str = "[Rectangle] (2) 3/4 - 10/2"
        self.assertEqual(str(r), expected_str)
