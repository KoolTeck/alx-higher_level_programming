#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new = list(map(lambda x: x ** 2, row))
        new_matrix.append(new)
    return (new_matrix)
