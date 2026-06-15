# Generate even numbers

def even_numbers(n):
    return [i for i in range(2, n+1, 2)]


# Test
if __name__ == "__main__":
    print(even_numbers(10))   # Output: [2, 4, 6, 8, 10]
    print(even_numbers(20))   # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
