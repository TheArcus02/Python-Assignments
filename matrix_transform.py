def get_inputs():
    matrix_sizes = input('')
    matrix_sizes = matrix_sizes.split(' ')
    rows = int(matrix_sizes[0])
    matrix = []

    for row in range(rows):
        col = input('')
        matrix.append([int(x) for x in col.split(' ')])

    operations_count = int(input(''))
    operations = []

    for operation in range(operations_count):
        op = input('')
        operations.append(op)

    return matrix, operations


def make_operations(matrix: list[list[int]], operations: list):
    for operation in operations:
        op_split = operation.split(' ')
        if op_split[0] == 'T':
            matrix = transpose(matrix)
        elif op_split[0] == 'RR':
            row = int(op_split[1])
            matrix = reverse_row(matrix, row)
        elif op_split[0] == 'RC':
            col = int(op_split[1])
            matrix = reverse_col(matrix, col)

    return matrix


def reverse_row(matrix: list[list[int]], row: int):
    matrix[row] = matrix[row][::-1]
    return matrix


def reverse_col(matrix: list[list[int]], col: int):
    matrix_col = []
    for row in matrix:
        matrix_col.append(row[col])
    matrix_col = matrix_col[::-1]

    for i in range(len(matrix_col)):
        matrix[i][col] = matrix_col[i]

    return matrix


def transpose(matrix: list[list[int]]):
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    new_matrix = []
    for col in range(cols_count):
        new_row = []
        for row in range(rows_count):
            new_row.append(matrix[row][col])

        new_matrix.append(new_row)
    return new_matrix


def main():
    matrix, ops = get_inputs()
    transformed_matrix = make_operations(matrix, ops)
    for row in transformed_matrix:
        print(*row, sep=" ")

main()