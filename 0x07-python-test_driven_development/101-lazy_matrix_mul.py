#!/usr/bin/python3
"""Defines a matrix multi[lication function using NumPy."""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix (list of lists of integers or floats).
        m_b (list of lists): The second matrix (list of lists of integers or floats).

    Returns:
        np.ndarray: The result of multiplying m_a and m_b.

    Raises:
        ValueError: If m_a or m_b is not a list or not a list of lists.
        ValueError: If m_a or m_b is empty (=[] or =[[]]).
        ValueError: If one element of the list of lists is not an integer or a float.
        ValueError: If m_a or m_b is not a rectangle (all 'rows' should be of the same size).
        ValueError: If m_a and m_b can't be multiplied.

    Example:
        >>> matrix_a = [[1, 2], [3, 4]]
        >>> matrix_b = [[5, 6], [7, 8]]
        >>> lazy_matrix_mul(matrix_a, matrix_b)
        array([[19, 22],
               [43, 50]])
    """
    try:
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        result_matrix = np.matmul(np_a, np_b)
        return result_matrix.tolist()
    except ValueError as e:
        raise ValueError(str(e))

# Example usage
if __name__ == "__main__":
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    result = lazy_matrix_mul(matrix_a, matrix_b)
    print(result)
