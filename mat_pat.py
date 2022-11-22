"""
There is one white King and some number of black Rooks on the chessboard.
White is making the move. What is the result of the game?

Input Format

Eight lines with 8 characters each. k denotes white king, w denotes black rook and o denotes empty field.

Constraints

There will be exactly one king and 0-63 rooks.

Output Format

Print the result of the game.

mat if the king is under attack and cannot move to a safe field.

pat if the king is NOT under attack, but cannot move to a safe field

game goes on if king can move to a safe field
"""

def get_game_info(size: int):

    king_pos = (-1, -1)
    rooks_pos = []
    attacked_columns = []
    attacked_rows = []

    for y in range(size):
        row = input('')
        positions = tuple((x, y) for x, field in enumerate(row) if field == 'w')
        for pos in positions:
            if pos[0] not in attacked_columns:
                attacked_columns.append(pos[0])
            if pos[1] not in attacked_rows:
                attacked_rows.append(pos[1])
            rooks_pos.append(pos)
        if 'k' in row:
            king_pos = (row.index('k'), y)

    return king_pos, rooks_pos, attacked_columns, attacked_rows


def get_possible_moves(col: int, row: int, matrix_size: int):
    neighbours = []

    for x in range(col - 1, col + 2):
        for y in range(row - 1, row + 2):
            if x == col and y == row:
                continue
            if 0 <= x <= matrix_size - 1 and 0 <= y <= matrix_size - 1:
                neighbours.append((x, y))
    return neighbours


def check_if_can_move(moves: list[tuple[int, int]], attacked_cols: list[int],
                      attacked_rows: list[int], rooks_pos: list[tuple[int, int]]):

    for move in moves:
        if move[0] not in attacked_cols and move[1] not in attacked_rows:
            return True
        if move in rooks_pos:
            rooks_copy = rooks_pos.copy()
            rooks_copy.pop(rooks_copy.index(move))
            can_move = True
            for rook in rooks_copy:
                if rook[0] is move[0] or rook[1] is move[1]:
                    can_move = False
                    break
            if can_move:
                return True
    return False


def main():

    board_size = 8
    king_pos, rooks_pos, attacked_columns, attacked_rows = get_game_info(board_size)

    is_under_attack = False

    if king_pos[0] in attacked_columns or king_pos[1] in attacked_rows:
        is_under_attack = True

    possible_moves = get_possible_moves(king_pos[0], king_pos[1], board_size)

    can_move = check_if_can_move(possible_moves, attacked_columns, attacked_rows, rooks_pos)
    if is_under_attack and not can_move:
        print('mat')
    elif not is_under_attack and not can_move:
        print('pat')
    else:
        print('game goes on')


if __name__ == '__main__':
    main()
