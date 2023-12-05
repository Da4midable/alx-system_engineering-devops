import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Parameters:
    - my_obj: The Python object to be serialized.

    Returns:
    - str: The JSON representation of the object.

    Example:
    >>> to_json_string([1, 2, 3])
    '[1, 2, 3]'

    >>> to_json_string({'key': 'value'})
    '{"key": "value"}'

    >>> to_json_string(42)
    '42'

    """
    json_rep = json.dumps(my_obj)
    return json_rep
