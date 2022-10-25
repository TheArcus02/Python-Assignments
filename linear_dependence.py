"""
You are given NxN matrix. Each column and each row represents
one vector (there are 2N vectors in total).

image

Your task is to check how many pairs of vectors are linearly dependent.

Two vectors are linearly dependent if there exists some number  such that:
    r * [a0, a1, a2, a3, a4] = [r*a0, r*a1, r*a2, r*a3, r*a4] = [b0, b1, b2, b3, b4]
and
    r != 0

Input Format

First line of input contains integer N.

Each of the following N lines contains N space-separated integers.

Constraints
    1 <= N <= 50
    1'000 <= aij <= 1'000
    aij in Z

Output Format

One integer - number of linearly dependent pairs of vectors.
"""


def get_matrix():
    matrix_size = int(input(''))
    matrix = []

    for i in range(matrix_size):
        row = input('')
        matrix.append([int(x) for x in row.split(' ')])
    return matrix


def get_col_vectors(matrix: list[list[int]]):
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    new_matrix = []
    for col in range(cols_count):
        new_row = []
        for row in range(rows_count):
            new_row.append(matrix[row][col])

        new_matrix.append(new_row)
    return new_matrix


def get_linear_dependent(vectors: list[list[int]]):
    good_pairs = 0
    last_index = 0

    for vector in vectors:

        last_index = vectors.index(vector, last_index) + 1
        sliced_vectors = vectors[last_index:]

        if len(sliced_vectors) > 0:

            for sec_vector in sliced_vectors:
                multipliers = []

                for i in range(len(vector)):
                    if vector[i] == 0 and sec_vector[i] == 0:
                        continue
                    if vector[i] == 0:
                        multipliers.append(0)
                    else:
                        multipliers.append(sec_vector[i] / vector[i])

                multipliers = set(multipliers)

                if len(multipliers) == 1:
                    if next(iter(multipliers)) != 0:
                        good_pairs += 1

    return good_pairs


def main():
    matrix = get_matrix()
    col_vectors = get_col_vectors(matrix)
    good_pairs_count = get_linear_dependent(matrix + col_vectors)
    print(good_pairs_count)


main()
