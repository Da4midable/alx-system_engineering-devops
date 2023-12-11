#!/usr/bin/python3
"""Module for testing class Square"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Class Square tests"""

    def test_init(self):
        """Test if __init__() initializes the square correctly."""
        s1 = Square(10)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(5, 3, 4)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)

        s3 = Square(10, id=5)
        self.assertEqual(s3.id, 5)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.width, 10)
        self.assertEqual(s3.height, 10)
        self.assertEqual(s3.x, 0)
        self.assertEqual(s3.y, 0)

    def test_property_size(self):
        """Test if size property works correctly."""
        s = Square(10)
        s.size = 5
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

        with self.assertRaises(TypeError):
            s.size = 'invalid'
        with self.assertRaises(ValueError):
            s.size = -1

    def test_str(self):
        """Test if __str__() method returns a formatted string."""
        s = Square(10, 3, 4)
        expected_str = "[Square] (2) 3/4 - 10"
        self.assertEqual(str(s), expected_str)

    def test_update(self):
        """Test if update() method updates attributes correctly."""
        s = Square(10, 3, 4)
        s.update(5, 8, 1, 2)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

        s.update(id=10)
        self.assertEqual(s.id, 10)

    def test_to_dictionary(self):
        """Test if to_dictionary() method returns a correct dictionary."""
        s = Square(10, 3, 4)
        expected_dict = {
            'id': 1,
            'x': 3,
            'size': 10,
            'y': 4,
        }
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
