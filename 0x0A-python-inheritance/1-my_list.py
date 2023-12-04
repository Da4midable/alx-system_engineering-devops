#!/usr/bin/python3
class MyList(list):
    def __init__(self, new_list=None):
        super().__init__(new_list if new_list is not None else [])

    def print_sorted(self):
        if not self:
            raise ValueError("List cannot be empty")

        for element in self:
            if not isinstance(element, int):
                raise TypeError("Each element must be an integer")

        sorted_list = sorted(self)
        print(sorted_list)
