def get_matrix():
    _, rows_count = (int(x) for x in input('').split(' '))
    matrix = []

    for row in range(rows_count):
        matrix.append([int(x) for x in input('').split(' ')])
    return matrix


def sort_columns(matrix: [list[int]]):
    col_count = len(matrix[0])
    row_count = len(matrix)
    new_matrix = [list() for _ in range(row_count)]

    for col_idx in range(col_count):
        current_col = []
        for row_idx in range(row_count):
            current_col.append(matrix[row_idx][col_idx])
        sorted_col = sorted(current_col)
        for new_col_idx, new_col_val in enumerate(sorted_col):
            new_matrix[new_col_idx].append(new_col_val)
    return new_matrix


def main():
    matrix = get_matrix()
    sorted_matrix = sort_columns(matrix)
    for row in sorted_matrix:
        print(*row)


if __name__ == "__main__":
    main()
