#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    if matrix is None or len(matrix) == 0:
        return None

    NewMatrix = []

    for row in matrix:
        NewRow = []

        for digit in row:
            NewRow.append(digit ** 2)

        NewMatrix.append(NewRow)

    return NewMatrix
