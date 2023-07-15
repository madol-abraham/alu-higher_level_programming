#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate over each row in the matrix
    for row in matrix:
        # Iterate over each element in the row
        for element in row:
            # Print the element using str.format() without casting to string
            print("{:d}".format(element), end=' ')
        # Move to the next line after printing all elements in the row
        print()
