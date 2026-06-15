# Filter example

def filter_even(lst):
    return list(filter(lambda x: x % 2 == 0, lst))


# Test
if __name__ == "__main__":
    print(filter_even([1, 2, 3, 4, 5, 6]))   # Output: [2, 4, 6]
    print(filter_even([10, 15, 20, 25]))     # Output: [10, 20]
