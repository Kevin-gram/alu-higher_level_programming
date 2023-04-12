#!/usr/bin/python3
"""Defines a matrix with a function """


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): is a  list  of ints or floats.
        div (int/float): a  divisor.
    Raises:
        TypeError: If the matrix contains  not integer or float. 
        TypeError: If the matrix has rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If divide  zero .
    Returns:
        A new matrix representing the out put after division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])i
