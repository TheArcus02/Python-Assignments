"""
You are given a N x M matrix with integers.
If at some positions [i,j] number zero appears you have to set
all values in row i and column j to zero.

Input Format

The first line of input contains two space-separated integers N and M.

Each of the N following lines contains M space separated integers.
The j-th integer in the i-th line is the value at position [i,j].

Constraints
1<= N,M <= 100

Output Format

N lines, each with M space-separated integers - the matrix after transformation
"""


def zero(matrix: list[list[int]], row: int, col: int):

    new_matrix = []

    for row_idx, row_val in enumerate(matrix):
        new_row = []
        for col_idx, col_val in enumerate(row_val):
            if (row_idx == row or col_idx == col) and col_val != 0:
                new_row.append(0)
            else:
                new_row.append(col_val)
        new_matrix.append(new_row)
    return new_matrix


def zero_matrix(matrix: list[list[int]]):
    new_matrix = matrix
    for row_idx, row in enumerate(matrix):
        for col_idx, col in enumerate(row):
            if col == 0:
                new_matrix = zero(new_matrix, row_idx, col_idx)
    return new_matrix


def main():
    matrix_sizes = [int(x) for x in input('').split(' ')]
    matrix = []
    for row in range(matrix_sizes[0]):
        matrix.append([int(x) for x in input('').split(' ')])
    transformed_matrix = zero_matrix(matrix)
    for row in transformed_matrix:
        print(*row, sep=" ")


if __name__ == '__main__':
    main()
