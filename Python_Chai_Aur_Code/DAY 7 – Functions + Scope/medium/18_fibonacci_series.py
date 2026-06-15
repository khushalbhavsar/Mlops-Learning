# Fibonacci series

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Test
if __name__ == "__main__":
    print(list(fibonacci(10)))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
