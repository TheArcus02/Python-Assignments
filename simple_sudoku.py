"""
You have to check whether sudoku is correctly solved.
To make it a little simple you only have to check rows, columns.
Each row and each column must contain every number from 1 to 9.
(Do not check 3x3 squares!).

Additionally, we will check if diagonals also contain every digit from 1 to 9.

Input Format

9 rows each containing 9 digits.

Output Format

False if sudoku is incorrect

X if sudoku is correct and additionally each diagonal also has every number from 1 to 9

True if sudoku is correct, and it is not X variant
"""


def structure_solved(matrix: list[list[int]]):
    size = len(matrix[0])
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
            if idx == abs(row_idx - size+1):
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
