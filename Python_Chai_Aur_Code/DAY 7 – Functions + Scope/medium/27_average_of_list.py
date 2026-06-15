# Average of list

def average(lst):
    return sum(lst) / len(lst)


# Test
if __name__ == "__main__":
    print(average([1, 2, 3, 4, 5]))   # Output: 3.0
    print(average([10, 20, 30]))      # Output: 20.0
