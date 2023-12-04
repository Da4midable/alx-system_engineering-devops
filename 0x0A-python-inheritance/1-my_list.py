#!/usr/bin/python3
class MyList(list):
    """
    Customized list class with additional functionality.

    This class inherits from the built-in list class and adds a method
    for printing the sorted elements of the list. It enforces that the
    elements in the list must be integers.

    Methods:
    - __init__(self, new_list=None): Constructor to initialize MyList instance
    - print_sorted(self): Print the sorted elements of the list.

    Example:
    >>> my_list_instance = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    >>> my_list_instance.print_sorted()
    [1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    Raises:
    - ValueError: If the list is empty.
    - TypeError: If any element in the list is not an integer.

    Usage:
    >>> my_list_instance = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    >>> my_list_instance.print_sorted()

    """

    def __init__(self, new_list=None):
        """
        Initialize a MyList instance.

        Parameters:
        - new_list: An optional list to initialize the MyList with.

        """
        super().__init__(new_list if new_list is not None else [])

    def print_sorted(self):
        """
        Print the sorted elements of the list.

        Raises:
        - ValueError: If the list is empty.
        - TypeError: If any element in the list is not an integer.

        Example:
        >>> my_list_instance = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        >>> my_list_instance.print_sorted()
        [1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

        """
        if not self:
            raise ValueError("List cannot be empty")

        for element in self:
            if not isinstance(element, int):
                raise TypeError("Each element must be an integer")

        sorted_list = sorted(self)
        print(sorted_list)
