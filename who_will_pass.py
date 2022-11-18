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

