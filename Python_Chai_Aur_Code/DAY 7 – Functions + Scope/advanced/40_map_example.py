# Map example

def square_list(lst):
    return list(map(lambda x: x*x, lst))


# Test
if __name__ == "__main__":
    print(square_list([1, 2, 3, 4, 5]))   # Output: [1, 4, 9, 16, 25]
    print(square_list([6, 7, 8]))         # Output: [36, 49, 64]
