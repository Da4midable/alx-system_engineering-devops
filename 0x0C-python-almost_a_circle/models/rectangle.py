#!/usr/bin/python3
"""Module Documentation: rectangle.py

This module defines the `Rectangle` class, a subclass of the `Base` class.

Classes:
    Rectangle: A class representing a rectangle with width, height,
    position, and unique identifier.

Methods:
    __init__: Initialize a new Rectangle instance.
    width: Get the width of the rectangle.
    width.setter: Set the width of rectangle with type and value validation.
    height: Get the height of the rectangle.
    height.setter: Set the height of rectangle with type and value validation.
    x: Get the x-coordinate of the rectangle.
    x.setter: Set the x-coordinate of the rectangle with
    type and value validation.
    y: Get the y-coordinate of the rectangle.
    y.setter: Set the y-coordinate of the rectangle
    with type and value validation.
    area: Calculate the area of the rectangle.
    display: Display the rectangle using the '#' character.
    __str__: Generate a formatted string representation of the rectangle.
    update: Update attributes of the rectangle with variable arguments
    and keyword arguments.
    to_dictionary: Convert the rectangle attributes to a dictionary.

"""


from models.base import Base

class Rectangle(Base):
    """A class representing a rectangle with width, height, position,
    and unique identifier."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of rectangle. Defaults to 0.
            id (int, optional): The unique identifier of the rectangle.
            Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validate_value(name, value, min_value=0, is_integer=True):
        if is_integer and not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= min_value:
            raise ValueError(f"{name} must be > {min_value}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_value('width', value, min_value=0)
        self.__width = value

    
    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with type and value validation.

        Args:
            value (int): The height value.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than or equal to 0.
        """
        
        self.validate_value('height', value, min_value=0)
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of rectangle with type and value validation.

        Args:
            value (int): The x-coordinate value.

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is less than 0.
        """
        
        self.validate_value('x', value, min_value=-1)
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of rectangle with type and value validation.

        Args:
            value (int): The y-coordinate value.

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than 0.
        """
        self.validate_value('y', value, min_value=-1)
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.height * self.width

    def display(self):
        """Display the rectangle using the '#' character."""
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Generate a formatted string representation of the rectangle.

        Returns:
            str: A formatted string representing the rectangle.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update attributes of the rectangle with variable arguments
        and keyword arguments.

        Args:
            *args: Variable arguments representing attributes in
            the order id, width, height, x, y.
            **kwargs: Keyword arguments representing attributes.

        Returns:
            None
        """
        num_of_args = len(args)
        if num_of_args >= 1:
            self.id = args[0]
        if num_of_args >= 2:
            self.width = args[1]
        if num_of_args >= 3:
            self.height = args[2]
        if num_of_args >= 4:
            self.x = args[3]
        if num_of_args == 5:
            self.y = args[4]

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """Convert the rectangle attributes to a dictionary.

        Returns:
            dict: A dictionary representing the rectangle attributes.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y}
