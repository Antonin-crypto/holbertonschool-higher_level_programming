#!/usr/bin/python3
"""divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    # Message d'Error
    list_matr = "matrix must be a matrix (list of lists) of integers/floats"
    size_matr = "Each row of the matrix must have the same size"
    div_matr = "div must be a number"
    div_matr0 = "division by zero"
    # Check if the matrix is a list of lists containing integers or floats
    # isinstance allows you to check the object type of a variable
    # row object represents the row of a table
    if not (isinstance(matrix, list) and
            all(isinstance(row, list) for row in matrix)):
        raise TypeError(list_matr)

    # Check if each row has the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(size_matr)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(list_matr)

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError(div_matr)

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError(div_matr0)

    # Divide all elements of the matrix by div and round to 2 decimal places
    # round  The number to be rounded
    # append allows you to add an element to the end of an existing list
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
