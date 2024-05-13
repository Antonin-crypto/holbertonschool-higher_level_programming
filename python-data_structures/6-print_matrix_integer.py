#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for first in range(len(matrix)):
        for second in range(len(matrix[first])):
            print("{:d}".format(matrix[first][second]), end="")
            if second != len(matrix[0]) - 1:
                print(" ", end="")
        print("")
