#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_value = sorted(a_dictionary.items())
    for key, value in sorted_value:
        print("{}: {}".format(key, value))
