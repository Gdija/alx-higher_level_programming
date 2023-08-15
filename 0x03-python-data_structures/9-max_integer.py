#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_item = my_list[0]
    for y in my_list:
        if y > max_item:
            max_item = y
    return max_item
