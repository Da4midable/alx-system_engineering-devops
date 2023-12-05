#!/usr/bin/python3

import json


def load_from_json_file(filename):
    """
    Load a JSON file and return the deserialized Python object.

    Parameters:
    - filename (str): The path to the JSON file to be loaded.

    Returns:
    - object: The Python object representing the data in the JSON file.

    Raises:
    - JSONDecodeError: If the file does not contain valid JSON data.

    Example:
    >>> loaded_data = load_from_json_file('example.json')
    """
    with open(filename, 'r') as file:
        return json.load(file)
