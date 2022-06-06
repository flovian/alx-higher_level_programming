#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        print(" ".join("{:d}".format(el) for el in row))
