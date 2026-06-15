# Custom map function

def my_map(func, iterable):
    return [func(x) for x in iterable]


# Test
if __name__ == "__main__":
    print(my_map(lambda x: x * 2, [1, 2, 3, 4]))   # Output: [2, 4, 6, 8]
    print(my_map(str.upper, ["a", "b", "c"]))      # Output: ['A', 'B', 'C']
