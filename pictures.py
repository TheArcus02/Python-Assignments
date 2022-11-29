def get_possible_widths(wall: tuple[tuple[int]], x: int):

    all_streaks = []

    for row in wall:

        streaks = []
        width_streak = 0
        start_idx = -1

        for idx, col in enumerate(row):
            if col == 0:
                if width_streak == 0:
                    start_idx = idx
                width_streak += 1
            if idx == len(row)-1 or col == 1:
                if width_streak >= x:
                    streaks.append((width_streak, start_idx, idx - 1 if col == 1 else idx))
                #     change logic
                # check if can fit from here
                #  write a function that checks fields below
                # if matched return True
                width_streak = 0

        all_streaks.append(streaks)

    return all_streaks

def can_fit(streaks: list[list[tuple[int, int, int]]], wall: tuple[tuple[int]],
            y: int):
    for row_idx, streak in enumerate(streaks):
        for width_streak in streak:

            if row_idx != len(wall):
                for row in wall[row_idx+1:]:
                    next_row = row[width_streak[1]:width_streak[2]+1]


def main():
    height, width, y, x = (int(x) for x in input('').split())

    wall = tuple(map(lambda idx: tuple(int(i) for i in input('').split()), range(height)))
    print(wall)
    streaks = get_possible_widths(wall, x)
    print(streaks)



if __name__ == '__main__':
    main()
