"""

A module containing the `Square` class, which inherits
from the `Rectangle` class.

Classes:
- Square: A class representing a square with equal sides.

"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class representing a square with equal sides,
    inheriting from the `Rectangle` class.

    Attributes:
    - __size (int): The size of the square.

    Methods:
    - __init__(self, size): Constructor method to initialize a Square object
    with a given size.

    Usage:
    >>> from my_module import Square

    >>> square_instance = Square(4)
    """

    def __init__(self, size):
        """
        Initialize a Square object with a given size.

        Parameters:
        - size (int): The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than or equal to 0.

        Usage:
        >>> from my_module import Square

        >>> square_instance = Square(4)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
