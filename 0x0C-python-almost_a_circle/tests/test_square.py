import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        with self.assertRaises(TypeError):
            s.size = '10'
        with self.assertRaises(ValueError):
            s.size = -10

    def test_str(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), '[Square] (3) 1/2 - 5')

    def test_update_args(self):
        s = Square(5, 1, 2, 3)
        s.update(10, 15, 20, 25)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 25)

    def test_update_kwargs(self):
        s = Square(5, 1, 2, 3)
        s.update(size=30, y=35, x=40, id=45)
        self.assertEqual(s.id, 45)
        self.assertEqual(s.size, 30)
        self.assertEqual(s.x, 40)
        self.assertEqual(s.y, 35)

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.to_dictionary(), {'id': 3, 'x': 1, 'size': 5, 'y': 2})

if __name__ == '__main__':
    unittest.main()
