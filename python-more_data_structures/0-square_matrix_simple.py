#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    if matrix is None:
        return

    if len(matrix) == 0:
        return

    NewMatrix = []

    for i in matrix:
        list = []

        for dgt in i:
            list.append(dgt ** 2)

        NewMatrix.append(list)

        return NewMatrix
