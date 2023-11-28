#!/usr/bin/python3
"""Defines a name-printing function."""

def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string containing the first and last names.

    Args:
        first_name (str): The first name.
        last_name (str): The last name (default is an empty string).

    Raises:
        TypeError: If first_name or last_name is not a string.

    Example:
        >>> say_my_name("John", "Doe")
        My name is John Doe

        >>> say_my_name("Alice")
        My name is Alice
    """
    # Check if first_name and last_name are strings
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    # Print the formatted string
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))

# Example usage
if __name__ == "__main__":
    say_my_name("John", "Doe")
    say_my_name("Alice")
