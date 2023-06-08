#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    if matrix is None:
        return
    if len(matrix) == 0:
        return
    NewMatrix = []

    for i in matrix:
        list = []

        for digit in i:
            list.append(digit ** 2)

        NewMatrix.append(list)

        return NewMatrix
