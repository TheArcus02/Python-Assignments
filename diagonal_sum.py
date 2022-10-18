"""
You are given an NxM matrix. Each matrix contains 2N +2M -2 diagonals,
which starts at cells adjacent to edges of a matrix.
A diagonal goes through following cells until
it reaches a cell adjacent to the second edge of a
matrix (one of the sample test cases contains a picture with diagonals marked green).

The value of a diagonal is the sum of cells that are contained by this diagonal.

The answer is the value of the diagonal with the highest value.

Input Format

The first line of input contains two integer N and M.

Each of the N following lines contains M space separated integers.
The j-th integer in the i-th line is the value at position [i,j].

Constraints
1 <= N,M <= 100
0 <= aij< 10^6


Where aij is value of matrix cell at position [i,j].

Output Format

One integer number, the value of most valuable diagonal.
"""


def get_matrix():
    metrics = str(input(''))
    splitted_metrics = metrics.split(' ')
    rows = int(splitted_metrics[0])
    matrix = []

    for row in range(rows):
        row_val = str(input(''))
        row_list = [int(x) for x in row_val.split(' ')]
        matrix.append(row_list)

    return matrix


def sum_diagonal(matrix: list, row: int, col: int, rev=False):
    if not rev:
        if row == len(matrix)-1 or col == len(matrix[0])-1:
            return matrix[row][col]
        return matrix[row][col] + sum_diagonal(matrix, row + 1, col + 1)
    if row == len(matrix)-1 or col == 0:
        return matrix[row][col]
    return matrix[row][col] + sum_diagonal(matrix, row + 1, col - 1, True)


def sum_diagonals(matrix: list):
    rows_len = len(matrix)
    cols_len = len(matrix[0])
    diagonals = []
    for row in range(rows_len):
        for col in range(cols_len):
            diagonals.append(sum_diagonal(matrix, row, col))
            diagonals.append(sum_diagonal(matrix, row, col, True))
    return diagonals


def main():
    matrix = get_matrix()
    print(max(sum_diagonals(matrix)))

main()