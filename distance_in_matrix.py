def get_matrix():
    size = int(input(''))
    matrix = []

    for i in range(size):
        matrix.append([int(x) for x in input('').split()])
    return matrix


def get_ones(matrix:list[list[int]]):
    ones = []
    for row_idx, row in enumerate(matrix):
        for col_idx, num in enumerate(row):
            if num == 1:
                ones.append((row_idx+1, col_idx+1))
    return ones


def find_distance(positions: list[tuple[int, int]]):
    distances = []
    for idx, pos in enumerate(positions):
        i1, j1 = pos
        remaining = positions[idx+1:]
        for i2, j2 in remaining:
            if i2%i1 == 0 and j2%j1 == 0:
                distance = abs(i1 - i2) + abs(j1 - j2)
            else:
                distance = 1000
            distances.append(distance)
    return min(distances)


def main():
    matrix = get_matrix()
    points = get_ones(matrix)
    smallest_distance = find_distance(points)
    print(smallest_distance)


if __name__ == '__main__':
    main()
