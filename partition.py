def sub_lists(l: list[int]):
    lists = []
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists


def get_sums(lists: list[list[int]]):
    sec_sums = []
    thirds_sums = []

    for sublist in lists:
        curr_sec_sum = sum(sublist[0::2])
        curr_thirds_sum = sum(sublist[0::3])

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
    possible = sub_lists(numbers)
    sec_sums, thirds_sums = get_sums(possible)
    result = get_highest_sum_pair(sorted(sec_sums, reverse=True), sorted(thirds_sums, reverse=True))
    print(result)


if __name__ == '__main__':
    main()
