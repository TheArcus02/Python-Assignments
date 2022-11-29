def can_fit(wall: tuple[tuple[int]],
            h: int, w: int, y: int, x: int,
            start: int, end: int,
            y_streak: int):

    print(wall, start, end, y_streak)

    for row_idx, row in enumerate(wall):
        curr_width_streak = 0
        curr_start_idx = 0
        print('row', row)
        for idx, val in enumerate(row[start: end]):
            print('val', val)
            if val == 0:
                if curr_width_streak == 0:
                    curr_start_idx = idx
                curr_width_streak += 1

            if idx == len(row[start:end]) - 1 or val == 1:
                print('streak', curr_width_streak)
                if curr_width_streak >= x:
                    if y_streak + 1 == y:
                        return True
                    if can_fit(wall[row_idx + 1:], h, w, y, x,
                               curr_start_idx,
                               idx if val == 1 else idx + 1,
                               y_streak + 1):
                        return True
                curr_width_streak = 0
        y_streak = 0
    return False


def main():
    height, width, y, x = (int(x) for x in input('').split())

    wall = tuple(map(lambda idx: tuple(int(i) for i in input('').split()), range(height)))
    print(can_fit(wall, height, width, y, x, 0, width, 0))


if __name__ == '__main__':
    main()
