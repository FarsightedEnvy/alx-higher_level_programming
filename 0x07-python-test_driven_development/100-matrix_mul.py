#!/usr/bin/python3
"""Defines a matrix multiplication function."""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix (list of lists of integers or floats).
        m_b (list of lists): The second matrix (list of lists of integers or floats).

    Returns:
        list of lists: The result of multiplying m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        ValueError: If m_a or m_b is empty (=[] or =[[]]).
        TypeError: If one element of the list of lists is not an integer or a float.
        TypeError: If m_a or m_b is not a rectangle (all 'rows' should be of the same size).
        ValueError: If m_a and m_b can't be multiplied.

    Example:
        >>> matrix_a = [[1, 2], [3, 4]]
        >>> matrix_b = [[5, 6], [7, 8]]
        >>> matrix_mul(matrix_a, matrix_b)
        [[19, 22], [43, 50]]
    """
    # Validate m_a and m_b
    for matrix, name in [(m_a, 'm_a'), (m_b, 'm_b')]:
        # Check if matrix is a list
        if not isinstance(matrix, list):
            raise TypeError("{} must be a list".format(name))

        # Check if matrix is a list of lists
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("{} must be a list of lists".format(name))

        # Check if matrix is not empty
        if not matrix or any(not row for row in matrix):
            raise ValueError("{} can't be empty".format(name))

        # Check if elements are integers or floats
        if any(not isinstance(elem, (int, float)) for row in matrix for elem in row):
            raise TypeError("{} should contain only integers or floats".format(name))

        # Check if matrix is a rectangle (all 'rows' should be of the same size)
        if any(len(row) != len(matrix[0]) for row in matrix):
            raise TypeError("Each row of {} must be of the same size".format(name))

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result_matrix = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result_matrix

# Example usage
if __name__ == "__main__":
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    result = matrix_mul(matrix_a, matrix_b)
    print(result)
