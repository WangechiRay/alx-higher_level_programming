#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[row[i][j] * 2 for row in matrix] for i in range(3)] 
    return (new_matrix)
