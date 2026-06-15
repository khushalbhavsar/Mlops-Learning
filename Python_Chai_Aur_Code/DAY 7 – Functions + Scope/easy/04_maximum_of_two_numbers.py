# Maximum of two numbers

def maximum(a, b):
    return a if a > b else b


# Test
if __name__ == "__main__":
    print(maximum(10, 20))  # Output: 20
    print(maximum(50, 30))  # Output: 50
