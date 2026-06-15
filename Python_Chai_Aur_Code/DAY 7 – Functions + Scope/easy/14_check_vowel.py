# Check vowel

def is_vowel(ch):
    return ch.lower() in "aeiou"


# Test
if __name__ == "__main__":
    print(is_vowel("a"))   # Output: True
    print(is_vowel("b"))   # Output: False
    print(is_vowel("E"))   # Output: True
