def structure_solved(matrix: list[list[int]]):
    size = len(matrix)
    for row in matrix:
        nums_to_check = [x + 1 for x in range(size)]
        for col in row:
            if col in nums_to_check:
                nums_to_check.pop(nums_to_check.index(col))
        if len(nums_to_check) != 0:
            return False
    return True


def check_if_solved(board: list[list[int]], size: int):
    columns = [[] for _ in range(size)]
    diagonals = [[], []]

    for row_idx, row in enumerate(board):
        for idx, num in enumerate(row):
            columns[idx].append(num)
            if idx == row_idx:
                diagonals[0].append(num)
            if idx == abs(row_idx - size-1):
                diagonals[1].append(num)
    return structure_solved(board) and structure_solved(columns), "X" if structure_solved(diagonals) else False


def main():
    size = 9
    board = []

    for row in range(size):
        board.append([int(x) for x in input('').split(' ')])
    solved, diagonals_solved = check_if_solved(board, size)
    print('X' if diagonals_solved and solved else solved)


if __name__ == '__main__':
    main()
