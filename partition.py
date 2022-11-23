def get_possible_sublist(start_list: list[int]):
    possible = []
    current_middle_1 = start_list.copy()
    current_middle_2 = start_list.copy()

    for i in range(len(start_list) - 1):

        left = start_list[i:]
        left not in possible and possible.append(left)

        if i != 0:
            right = start_list[:-i]
            right not in possible and possible.append(right)

            if i % 2 == 0:
                current_middle_1.pop(0)
                current_middle_2.pop()
            else:
                current_middle_1.pop()
                current_middle_2.pop(0)

            current_middle_1 not in possible and possible.append(current_middle_1)
            current_middle_2 not in possible and possible.append(current_middle_2)

    return possible if len(possible) > 0 else [start_list]


def get_sums(lists: list[list[int]]):
    sec_sums = []
    thirds_sums = []

    for sublist in lists:
        curr_sec_sum = sum(sublist[0::2])
        curr_thirds_sum = sum(sublist[0::3])
        print(curr_sec_sum, curr_thirds_sum, sublist)
        curr_sec_sum not in sec_sums and sec_sums.append(curr_sec_sum)
        curr_thirds_sum not in thirds_sums and thirds_sums.append(curr_thirds_sum)

    return sec_sums, thirds_sums


def get_highest_sum_pair(sums_one: list[int], sums_two: list[int]):
    for number in sums_one:
        if number in sums_two:
            return number
    return None


def main():
    size = int(input(''))
    numbers = [int(x) for x in input('').split(' ')]
    possible = get_possible_sublist(numbers)
    print(possible)
    sec_sums, thirds_sums = get_sums(possible)
    result = get_highest_sum_pair(sorted(sec_sums, reverse=True), sorted(thirds_sums, reverse=True))
    print(result)


if __name__ == '__main__':
    main()
