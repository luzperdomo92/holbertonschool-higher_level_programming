#!/usr/bin/python3
"""
    matrix_divided: divides all elements of a matrix.
    Return a new matrix.
"""


def matrix_divided(matrix, div):
    """
    TypeError: If either of element is a non-integer and non-float.
    or list of lists.
    """

    error_message = """matrix must be a matrix (list of lists) \
                        of integers/floats"""
    if not matrix:
        raise TypeError(error_message)

    if type(matrix) is not list:
        raise TypeError(error_message)

    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(error_message)

        for number in lists:
            if not isinstance(number, int) and not isinstance(number, float):
                raise TypeError(error_message)

    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(error_message)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(
        lambda lists:
            list(map(
                lambda number:
                    round(number / div, 2),
                lists)),
        matrix))
