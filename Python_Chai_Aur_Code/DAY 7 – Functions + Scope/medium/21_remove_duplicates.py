# Remove duplicates

def remove_duplicates(lst):
    return list(set(lst))


# Test
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 3, 4]))   # Output: [1, 2, 3, 4]
    print(remove_duplicates([5, 5, 5, 5]))         # Output: [5]
