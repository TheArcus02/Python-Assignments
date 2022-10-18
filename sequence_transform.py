"""
You are given string S of length N and M edit operations.

One edit operation consists of two integers a,b and string s.

The edit operation creates a new string in the following way:

- take substring of S from beginning to index min(a,b)
- add string s
- add substring of  from index max(a,b)+1 to end

You have to print the string you obtain after all edit operations and the
longest string you obtained in the process (if there are several
strings of the same length print the one that appeared first)

Input Format

First line of input contains two space-separated integers N and M.

Second line of input contains string of length N composed of letters of english alphabet.

Each of the following M lines contains one edit operation in the following format:

a;b;s

Constraints
1 <= N,M <= 100
len(s)<=100

Output Format

In the first line of output print the string you obtained after all edit operations.
In the second line of output should contain the longest string you obtained in the process.
"""


def get_inputs():
    settings = str(input(''))
    settings_split = settings.split(' ')
    operators_count = int(settings_split[1])
    string = str(input(''))
    operators = []
    for i in range(operators_count):
        new_operator = str(input(''))
        operators.append(new_operator)

    return string, operators


def get_string_info(string: str, operators: list):
    longest_str = len(string)
    longest_str_val = string
    new_str = string
    for op in operators:
        op_slice = op.split(';')
        first_idx = int(op_slice[0])
        sec_idx = int(op_slice[1])
        op_str = str(op_slice[2])
        new_str = new_str[:min(first_idx, sec_idx)] + op_str + new_str[max(first_idx, sec_idx)+1:]

        if len(new_str) > longest_str:
            longest_str = len(new_str)
            longest_str_val = new_str

    return new_str, longest_str_val

def main():
    string, operators = get_inputs()
    refactored_str, longest_str = get_string_info(string, operators)
    print(refactored_str)
    print(longest_str)
main()