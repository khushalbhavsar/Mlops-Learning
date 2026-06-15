# Count words

def word_count(sentence):
    return len(sentence.split())


# Test
if __name__ == "__main__":
    print(word_count("Hello World"))              # Output: 2
    print(word_count("Python is a great language"))  # Output: 5
