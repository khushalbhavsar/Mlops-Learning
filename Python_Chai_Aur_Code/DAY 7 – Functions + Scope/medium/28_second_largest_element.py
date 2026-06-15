# Second largest element

def second_largest(lst):
    return sorted(set(lst))[-2]


# Test
if __name__ == "__main__":
    print(second_largest([1, 5, 3, 9, 2]))   # Output: 5
    print(second_largest([10, 20, 30, 40]))  # Output: 30
