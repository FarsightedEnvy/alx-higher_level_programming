#!/usr/bin/python3
"""Defines an integer addition function"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number (default is 98).

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    Example:
        >>> add_integer(1, 2)
        3
        >>> add_integer(3.5, 2)
        5
    """
    # Check if a and b are integers or floats
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the addition of a and b
    return a + b

# Example usage
if __name__ == "__main__":
    result = add_integer(5, 3)
    print(result)
