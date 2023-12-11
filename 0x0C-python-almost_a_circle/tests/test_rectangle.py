#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_width_getter(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)

    def test_width_setter(self):
        r = Rectangle(10, 2)
        r.width = 20
        self.assertEqual(r.width, 20)
        with self.assertRaises(TypeError):
            r.width = '10'
        with self.assertRaises(ValueError):
            r.width = -10

    def test_height_getter(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.height, 2)

    def test_height_setter(self):
        r = Rectangle(10, 2)
        r.height = 20
        self.assertEqual(r.height, 20)
        with self.assertRaises(TypeError):
            r.height = '2'
        with self.assertRaises(ValueError):
            r.height = -2

    def test_x_getter(self):
        r = Rectangle(10, 2, 3)
        self.assertEqual(r.x, 3)

    def test_x_setter(self):
        r = Rectangle(10, 2, 3)
        r.x = 5
        self.assertEqual(r.x, 5)
        with self.assertRaises(TypeError):
            r.x = '3'
        with self.assertRaises(ValueError):
            r.x = -3

    def test_y_getter(self):
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_y_setter(self):
        r = Rectangle(10, 2, 3, 4)
        r.y = 5
        self.assertEqual(r.y, 5)
        with self.assertRaises(TypeError):
            r.y = '4'
        with self.assertRaises(ValueError):
            r.y = -4

    def test_area(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)

    def test_update_args(self):
        r = Rectangle(10, 2, 3, 4, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        r = Rectangle(10, 2, 3, 4, 1)
        r.update(height=6, width=7, y=8, x=9, id=10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 8)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 3, 4, 1)
        self.assertEqual(r.to_dictionary(), {'id': 1, 'width': 10, 'height': 2, 'x': 3, 'y': 4})

if __name__ == '__main__':
    unittest.main()
