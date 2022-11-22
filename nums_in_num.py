"""
You are given an integer N.
Consider all numbers that are written within it.
For each possible length print the number,
that occurred the most often
(if there is a draw print the smallest one).

Input Format

One line containing integer N.

Constraints
1 <= len(N) <= 30

N will not have zeroes in it.

Output Format

len(N) lines. -th line should contain the most frequent number of length i (if there is a draw print the smallest one).
"""


def get_possible_nums(nums: str):
    all_possible_nums = []
    for i in range(len(nums)):
        possible_nums = []

        for j in range(len(nums)):
            if j+i+1 > len(nums):
                continue
            possible_num = nums[j:j+i+1]
            possible_nums.append(int(possible_num))
        all_possible_nums.append(possible_nums)

    return all_possible_nums


def get_most_frequent(nums: list):

    frequency_count = {}
    maxes = []
    for num in nums:
        if num not in frequency_count:
            frequency_count[num] = 1
        else:
            frequency_count[num] += 1
    for key, val in frequency_count.items():
        if val is max(frequency_count.values()):
            maxes.append(key)

    return maxes


def get_answers(all_nums: list):
    answers = []

    for nums in all_nums:
        most_frequent_nums = get_most_frequent(nums)
        if len(most_frequent_nums) == 1:
            answers.append(most_frequent_nums[0])
        else:
            answers.append(min(most_frequent_nums))
    return answers


def main():
    nums = input('')
    possible_nums = get_possible_nums(nums)
    answers = get_answers(possible_nums)
    for answer in answers:
        print(answer)

    # print(get_most_frequent([1,2,3,3,2]))
main()