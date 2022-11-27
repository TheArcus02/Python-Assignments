"""
You are given integer N, matrix A of size N x M,
and matrix B of size (N - 1) x (N - 1).
You have to check whether it is possible to
transform matrix A into matrix B by removing one
row and one column.

Input Format

The first line of input contains integer N.

Each of the N following lines contains N space
separated strings - matrix A.

Each of the N - 1 following lines contains N - 1
space separated strings - matrix B.

Constraints
2 <= N <= 30

Elements of the matrices does not contain spaces.

Output Format

Print "True" if it is possible to transform A into B
and "False" otherwise.
"""


def get_matrices():
    size = int(input(''))
    matrix_a = [input().split(' ') for i in range(size)]
    matrix_b = [input().split(' ') for i in range(size - 1)]

    return matrix_a, matrix_b


def transpose(matrix: list[list[any]]):
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    new_matrix = []
    for col in range(cols_count):
        new_row = []
        for row in range(rows_count):
            new_row.append(matrix[row][col])

        new_matrix.append(new_row)
    return new_matrix


def transformable(a: list[list[str]], b: list[list[str]]):
    for i in range(len(a)):
        sliced_list = a[:i] + a[i+1:]
        transposed = transpose(sliced_list)

        for j in range(len(transposed)):
            sliced_list = transposed[:j] + transposed[j+1:]

            if transpose(sliced_list) == b:
                return True

    return False


def main():
    a, b = get_matrices()
    print(transformable(a, b))


if __name__ == '__main__':
    main()
