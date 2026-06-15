# Sum of first n natural numbers

def sum_n(n):
    return n * (n + 1) // 2


# Test
if __name__ == "__main__":
    print(sum_n(10))   # Output: 55
    print(sum_n(100))  # Output: 5050
