#!/usr/bin/python3
"""Module Documentation: base.py

This module defines the `Base` class, a foundation class
for managing unique identifiers and file I/O operations.

Classes:
    Base: A class providing functionality
    for managing unique identifiers and file I/O operations.

Methods:
    __init__: Initialize a new Base instance with a unique identifier.
    to_json_string: Convert a list of dictionaries to a JSON string.
    save_to_file: Save a list of instances to a JSON file.
    from_json_string: Convert a JSON string to a list of dictionaries.
    create: Create an instance with attributes from a dictionary.
    load_from_file: Load instances from a JSON file.

"""

import json

class Base:
    """A class providing functionality for managing unique identifiers
    and file I/O operations."""
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance with a unique identifier.

        Args:
            id (int, optional): The unique identifier. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted.

        Returns:
            str: A JSON-formatted string.
        """
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances to be saved.

        Returns:
            None
        """
        list_objs = list(filter(lambda obj: isinstance(obj, cls), list_objs or []))
        json_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(json_list)
        with open(cls.__name__ + ".json", "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON-formatted string.

        Returns:
            list: A list of dictionaries.
        """
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes from a dictionary.

        Args:
            **dictionary: Keyword arguments representing instance attributes.

        Returns:
            instance: An instance of the class.
        """
        dummy_instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        try:
            dummy_instance.update(**dictionary)
        except AttributeError:
            raise ValueError(f"Unsupported class: {cls.__name__}")
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file.

        Returns:
            list: A list of instances.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
