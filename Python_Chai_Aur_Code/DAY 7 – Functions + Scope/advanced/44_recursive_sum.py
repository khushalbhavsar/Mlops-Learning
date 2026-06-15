# Recursive sum

def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])


# Test
if __name__ == "__main__":
    print(recursive_sum([1, 2, 3, 4, 5]))   # Output: 15
    print(recursive_sum([10, 20, 30]))      # Output: 60
