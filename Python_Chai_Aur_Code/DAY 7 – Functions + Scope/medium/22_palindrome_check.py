# Palindrome check

def is_palindrome(s):
    return s == s[::-1]


# Test
if __name__ == "__main__":
    print(is_palindrome("radar"))   # Output: True
    print(is_palindrome("hello"))   # Output: False
