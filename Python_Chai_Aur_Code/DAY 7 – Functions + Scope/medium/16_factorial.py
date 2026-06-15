# Factorial

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


# Test
if __name__ == "__main__":
    print(factorial(5))   # Output: 120
    print(factorial(0))   # Output: 1
