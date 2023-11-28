#!/usr/bin/python3
"""Module to find the max integer in a list."""

def max_integer(lst=[]):
    """
    Returns the maximum integer from a list.

    Args:
        lst (list): The input list of integers.

    Returns:
        int: The maximum integer in the list.

    Example:
        >>> max_integer([1, 3, 5, 7])
        7
    """
    if not lst:
        return None

    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num
