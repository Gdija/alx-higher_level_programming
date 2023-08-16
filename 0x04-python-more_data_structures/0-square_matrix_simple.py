#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = []
    for row in matrix:
        n_row = list([i**2 for i in row])
        copy_matrix.append(n_row)
    return copy_matrix
