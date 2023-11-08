#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = []
    for num in my_list:
        if num not in unique_numbers:
            unique_numbers.append(num)
    total_sum = sum(unique_numbers)
    return total_sum
