#!/usr/bin/python3
"""
<<<<<<< HEAD
a function that divides all elements of a matrix
=======

This module defines a matrix division function

>>>>>>> b612bec1a417e6f68f87579356986363fc43def5
"""


def matrix_divided(matrix, div):
<<<<<<< HEAD
        """
        Divides the list and Raises TypeError
        """
        if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
        elif div is 0:
                raise ZeroDivisionError("division by zero")
        typeErr = "matrix must be a matrix (list of lists) of integers/floats"
        sizeErr = "Each row of the matrix must have the same size"
        new = []
        if matrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
                raise TypeError(typeErr)
        old = len(matrix[0])
        for count, y in enumerate(matrix):
                if not isinstance(y, list):
                        raise TypeError(typeErr)
                if len(y) != old:
                        raise TypeError(sizeErr)
                old = len(y)
                new.append(y[:])
                for a, item in enumerate(y):
                        if not isinstance(item, (int, float)):
                                raise TypeError(typeErr)
                        new[count][a] = round(item / div, 2)
        else:
                return (new)
=======
    """This function divides all elements of a matrix by a given number

    Args:
        matrix: A list of lists (matrix)- members can be of type ints or floats
        div: Number to be used for the division (can be a float or an integer)
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix which represents the result of the divisions
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

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
>>>>>>> b612bec1a417e6f68f87579356986363fc43def5
