#!/usr/bin/python3
"""Module Documentation: square.py

This module defines the `Square` class, a specific type of rectangle with
equal width and height.

Classes:
    Square: A class representing a square, inheriting from Rectangle.

Methods:
    __init__: Initialize a new Square instance.
    size: Get or set the size of the square.
    __str__: Return a string representation of the square.
    update: Update the attributes of the square using
    positional or keyword arguments.
    to_dictionary: Return a dictionary representation of the square.

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size (width and height) of the square.
            x (int, optional): The x-coordinate of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the square. Defaults to 0.
            id (int, optional): The unique identifier of the square.
            Defaults to None.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size (width and height) of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes of square using positional or keyword argument"""
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y,
        }
