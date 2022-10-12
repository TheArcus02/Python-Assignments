# In this problem you will be given a list of students and their scores for particular tests. You have to calculate
# the average score of each student and the average score for each test.
#
# Input Format
#
# The first line contains an integer N - the number of students.
#
# Then N lines follow. Each line looks like the following:
#
# student_name test_id:score ...
#
# ... symbolizes there can be any number of test scores per line (separated by a space).
#
# Constraints
#
# - Each student_name will be unique.
# - Each line will have at least one test score.
# - The number of students will be less than 200.
# - The number of tests will be less than 200.
# - student_name and test_id will be composed only of lowercase
#   english letters. score is a floating point number.
#
# Output Format
#
# First, you have to print, for each student, his student_name and average score separated by a space. The students
# have to be printed in ascending order by their student_name.
#
# Then you have to print for each test its test_id and average score separated by a space. The tests have to be
# printed in ascending order by their test_id.

def main():
    students_count = int(input(''))

    students_data = {}
    tests_data = {}

    for line in range(students_count):
        text_input = str(input(''))
        splitted_text = text_input.split(' ')
        student_name = splitted_text[0]
        tests = splitted_text[1:]

        students_data[student_name] = []

        for test in tests:
            splitted_test = test.split(':')
            test_id = splitted_test[0]

            if test_id not in tests_data.keys():
                tests_data[test_id] = []
            test_score = float(splitted_test[1])

            students_data[student_name].append(test_score)
            tests_data[test_id].append(test_score)

    for name, test_scores in sorted(students_data.items()):
        average_grades = sum(test_scores) / len(test_scores)
        print(name, average_grades)

    for test_id, scores in sorted(tests_data.items()):
        average_score = sum(scores) / len(scores)
        print(test_id, average_score)

main()
