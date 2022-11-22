"""
You are given an N x N matrix with integers.
An integer at position [i,j] represents knowledge level of given student.
The student can pass the exam if his knowledge level is greater or equal to 3,
or an average level of knowledge of students around him is greater or equal to 3.
Student in corner has 3 neighbours, on the edge - 5, and in the middle 8.
You have to determine which students can pass.

Input Format

The first line of input contains an integer N.
Each of the following N lines contains N space-separated integers - the knowledge level of students.

Constraints
1 <= N <= 50

Output Format

Print N lines each containing N space separated numbers 0 or 1. 0
means the student at this position will fail and 1 means he will pass.
"""


def get_matrix():

    matrix_size = int(input(''))
    matrix = []

    for row in range(matrix_size):
        matrix.append([int(x) for x in input('').split(' ')])

    return matrix


def get_neighbours_positions(row: int, col: int, matrix_size: int):
    neighbours = []
    for x in range(col-1, col+2):
        for y in range(row-1, row+2):
            if x == col and y == row:
                continue
            if 0 <= x <= matrix_size-1 and 0 <= y <= matrix_size-1:
                neighbours.append((y, x))
    return neighbours


def who_passed(matrix: list[list[int]]):

    new_matrix = []

    for row_idx, row_val in enumerate(matrix):
        new_row = []
        for col_idx, col_val in enumerate(row_val):
            if col_val >= 3:
                new_row.append(1)
            else:
                neighbours_positions = get_neighbours_positions(row_idx, col_idx, len(matrix))
                neighbours = [matrix[y][x] for y, x in neighbours_positions]
                if sum(neighbours) / len(neighbours) >= 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        new_matrix.append(new_row)
    return new_matrix


def main():
    matrix = get_matrix()
    for row in who_passed(matrix):
        print(*row)


if __name__ == '__main__':
    main()

