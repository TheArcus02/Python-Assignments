"""
You are given a NxN matrix and a starting point [is, js].
You can move to position with the smallest number in the same row you
are currently in. If you are already in the position with the
smallest number in the row, you can move to the position with the
smallest number in the same column. You have to print the position you can
reach from the starting point, from which you cannot go anywhere else.

Input Format

The first line of input contains an integer N.

The second line of input contains two space-separated integers is, js.

Each of the N following lines contains N space separated integers.
The j-th integer in the i-th line is the value at position [i,j].

Constraints
1 <= N <= 100

Each row and each column will have only one minimum value.

Output Format

Two space-separated integers, the last position you can reach.
"""

def get_matrix():
    matrix_size = int(input(''))
    start_positions = [int(x) for x in input('').split(' ')]
    matrix = []

    for i in range(matrix_size):
        row = [int(x) for x in input('').split(' ')]
        matrix.append(row)

    return matrix, start_positions


def get_smallest_in_col(matrix: list[list[int]], col: int):
    col_values = []
    for row in matrix:
        col_values.append(row[col])

    min_col = min(col_values)
    return min_col, col_values.index(min_col)


def get_smallest(matrix: list[list[int]], row: int, col: int):
    min_row = min(matrix[row])

    if matrix[row][col] == min_row:
        min_col, min_col_index = get_smallest_in_col(matrix, col)
        if matrix[row][col] == min_col:
            return row, col
        return get_smallest(matrix, min_col_index, col)
    return get_smallest(matrix, row, matrix[row].index(min_row))


def main():
    matrix, positions = get_matrix()
    min_pos = get_smallest(matrix, positions[0], positions[1])
    for pos in min_pos:
        print(pos, end=" ")
main()
