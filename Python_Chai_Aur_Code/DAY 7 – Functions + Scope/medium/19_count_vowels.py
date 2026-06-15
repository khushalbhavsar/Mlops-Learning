# Count vowels

def count_vowels(s):
    return sum(1 for ch in s if ch.lower() in "aeiou")


# Test
if __name__ == "__main__":
    print(count_vowels("Hello World"))   # Output: 3
    print(count_vowels("Python"))        # Output: 1
