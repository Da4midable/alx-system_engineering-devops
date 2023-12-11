#!/usr/bin/python3

import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):

    def test_init_default_id(self):
        """Test if id is assigned properly when not provided."""
        base1 = Base()
        self.assertEqual(base1.id, 1)

    def test_init_with_id(self):
        """Test if id is assigned properly when provided."""
        base2 = Base(10)
        self.assertEqual(base2.id, 10)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with a list."""
        list_dicts = [{'id': 1}, {'id': 2}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json_string, json.dumps(list_dicts))

    def test_save_to_file_none(self):
        """Test save_to_file with None."""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            json_string = file.read()
            self.assertEqual(json_string, "[]")

    def test_save_to_file_list(self):
        """Test save_to_file with a list."""
        list_objs = [Base(1), Base(2)]
        Base.save_to_file(list_objs)
        with open("Base.json", "r") as file:
            json_string = file.read()
            list_dicts = json.loads(json_string)
            self.assertEqual(list_dicts, [{"id": 1}, {"id": 2}])

    def test_save_to_file_invalid_object(self):
        """Test save_to_file with invalid object."""
        list_objs = [Base(1), object()]
        with self.assertRaises(TypeError):
            Base.save_to_file(list_objs)

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        list_dicts = Base.from_json_string(None)
        self.assertEqual(list_dicts, [])

    def test_from_json_string_json(self):
        """Test from_json_string with valid JSON."""
        json_string = '[{"id": 1}, {"id": 2}]'
        list_dicts = Base.from_json_string(json_string)
        self.assertEqual(list_dicts, [{'id': 1}, {'id': 2}])

    def test_create_unsupported_class(self):
        """Test create with unsupported class."""
        with self.assertRaises(ValueError):
            Base.create()

    def test_create_rectangle(self):
        """Test create for Rectangle class."""
        rectangle = Base.create(width=10, height=20)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)

    def test_create_square(self):
        """Test create for Square class."""
        square = Base.create(size=5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)

    def test_load_from_file_no_file(self):
        """Test load_from_file with no file."""
        list_objs = Base.load_from_file()
        self.assertEqual(list_objs, [])

    def test_load_from_file_with_file(self):
        """Test load_from_file with existing file."""
        list_objs = [Base(1), Base(2)]
        Base.save_to_file(list_objs)
        loaded_objs = Base.load_from_file()
        self.assertEqual(loaded_objs, list_objs)


if __name__ == "__main__":
    unittest.main()