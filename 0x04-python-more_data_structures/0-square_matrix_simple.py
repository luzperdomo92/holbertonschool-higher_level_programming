#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = list(map(list, matrix))
        return [[x * x for x in row]for row in new_matrix]
