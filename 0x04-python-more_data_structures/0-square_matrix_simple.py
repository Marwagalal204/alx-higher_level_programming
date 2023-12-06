#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_list = []
        for column in row:
            column = column ** 2
            new_list.append(column)
        new_matrix.append(new_list)
    return new_matrix
