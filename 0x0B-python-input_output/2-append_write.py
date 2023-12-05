#!/usr/bin/python3
"""
Module: file_operations
~~~~~~~~~~~~~~~~~~~~~~~

A module providing file operations in Python.

Functions:
- append_write(filename="", text=""): Appends text to a file.

"""


def append_write(filename="", text=""):
    """
    Append text to the end of a file.

    Parameters:
    - filename (str): The name or path of the file.
    - text (str): The text to be appended to the file.

    Raises:
    - FileNotFoundError: If the specified file is not found.

    Example:
    >>> from file_operations import append_write

    >>> append_write("example.txt", "This is additional text.")
    """

    try:
        with open(filename, 'a') as file:
            file.write(text)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")
