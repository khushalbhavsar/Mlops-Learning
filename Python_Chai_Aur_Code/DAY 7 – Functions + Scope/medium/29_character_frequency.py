# Character frequency

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# Test
if __name__ == "__main__":
    print(char_frequency("hello"))   # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(char_frequency("aabbcc"))  # Output: {'a': 2, 'b': 2, 'c': 2}
