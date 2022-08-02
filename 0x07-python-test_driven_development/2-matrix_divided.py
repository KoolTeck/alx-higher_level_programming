#!/usr/bin/python3

"""
    This is the 2-matrix_divided module.

    It supplies a single function matrix_divided(matrix, div):

    for example:

    >>> matrix = [[1, 2, 3], [4, 5, 6]]

    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

"""


def matrix_divided(matrix=[[]], div=1):
    """
    computes the divsion of each element of a matrix

    Args:
        matrix(int, floats): list of lists of ints and floats
        div(int): non zero based parameter

    Returns:
            the a new list of list
    """

    err1 = 'matrix must be a matrix (list of lists) of integers/floats'
    err2 = 'Each row of the matrix must have the same size'
    if len(matrix[0]) == 0:
        return
    if type(matrix) is not list:
        raise TypeError(err1)
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) is int or type(div) is float:
        pass
    else:
        raise TypeError("div must be a number")
    i = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err1)
        if (i == len(matrix) - 1):
            break
        if len(row) == len(matrix[i + 1]):
            pass
        else:
            raise TypeError(err2)
        i += 1
        for ele in row:
            if type(ele) is int or type(ele) is float:
                pass
            else:
                raise TypeError(err1)
    new_matrix = []
    for row in matrix:
        new = [round(ele / div, 2) for ele in row]
        new_matrix.append(new)
    return (new_matrix)
