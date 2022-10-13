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