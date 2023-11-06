#!/usr/bin/python3
def max_integer(my_list=None):
    if my_list is not None:
        if len(my_list) > 0:
            max_val = max(my_list)
            return max_val
    return None
