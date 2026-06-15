# Square list elements

def square_list(lst):
    return [x*x for x in lst]


# Test
if __name__ == "__main__":
    print(square_list([1, 2, 3, 4]))   # Output: [1, 4, 9, 16]
    print(square_list([5, 6, 7]))      # Output: [25, 36, 49]
