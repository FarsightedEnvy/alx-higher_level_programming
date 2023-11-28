#!/usr/bin/python3
"""Defines a text-indentation function."""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("This is a sentence. Another sentence? Yes, it is.")
        This is a sentence
        Another sentence
        Yes, it is
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Iterate through each character in the text
    for char in text:
        # Print the character without spaces at the beginning or end of the line
        if char not in ['.', '?', ':']:
            print(char, end="")
        else:
            # If the character is '.', '?', or ':', print two new lines after it
            print(char)
            print()

# Example usage
if __name__ == "__main__":
    text_indentation("This is a sentence. Another sentence? Yes, it is.")
