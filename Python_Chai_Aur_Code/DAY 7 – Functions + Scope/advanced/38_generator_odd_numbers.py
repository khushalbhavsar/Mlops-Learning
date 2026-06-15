# Generator for odd numbers

def odd_numbers(n):
    for i in range(1, n+1, 2):
        yield i


# Test
if __name__ == "__main__":
    print(list(odd_numbers(10)))   # Output: [1, 3, 5, 7, 9]
    print(list(odd_numbers(20)))   # Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
