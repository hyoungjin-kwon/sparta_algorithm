input = "abcba"


def is_palindrome(string):
    n = len(string)
    if n <= 1:
        return True
    elif string[0] == string[len(string) - 1]:
        return is_palindrome(string[1:-1])
    else:
        return False



print(is_palindrome(input))
print(is_palindrome('tomato'))

