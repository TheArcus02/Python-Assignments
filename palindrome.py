"""
You are given string S. You have to check whether it
is possible to obtain palindrome from S by removing up
to 2 letters (palindrome is sequence that reads the same
backwards as forwards (case-insensitive))

Input Format

One line containing string S.

Constraints

S consists of only english letters.

Output Format

One word - YES if it is possible to obtain palindrome and NO otherwise.
"""

def check_if_palindrome(text: str):
    def test_palindrome(tested_str: str):
        reversed_text = tested_str[::-1]
        if tested_str == reversed_text:
            return True
        return False

    for i in range(len(text)):
        once_sliced_text = text[:i] + text[i+1:]

        if test_palindrome(once_sliced_text):
            return True

        for j in range(len(once_sliced_text)):
            twice_sliced_text = once_sliced_text[:j] + once_sliced_text[j+1:]

            if test_palindrome(twice_sliced_text):
                return True

    return False

def main():
    text = str(input(''))
    result = 'YES' if check_if_palindrome(text.lower()) else 'NO'
    print(result)


main()