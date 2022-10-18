def get_inputs():

    lines_and_letters = input('')
    lines = int(lines_and_letters.split(' ')[0])
    letters = int(lines_and_letters.split(' ')[1])

    searched_letter = input('')

    return lines, letters, searched_letter


def get_matrix(lines: int):
    matrix = []
    for i in range(lines):
        row = str(input(''))
        matrix.append(row)
    return matrix


def matrix_contains(searched: str, letters_count: int, matrix: []):
    for column in range(letters_count):
        word_in_col = ''
        for row in matrix:
            if searched in row or searched in row[::-1]:
                return True
            word_in_col += row[column]
        if searched in word_in_col or searched in word_in_col[::-1]:
            return True
    return False


def main():
    lines, letters, searched_letter = get_inputs()
    matrix = get_matrix(lines)
    word_in_matrix = "YES" if matrix_contains(searched_letter, letters, matrix) else "NO"
    print(word_in_matrix)


main()
