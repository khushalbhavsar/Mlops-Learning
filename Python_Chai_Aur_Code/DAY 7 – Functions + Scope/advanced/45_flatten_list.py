# Flatten list

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


# Test
if __name__ == "__main__":
    print(flatten([1, [2, 3], [4, [5, 6]]]))   # Output: [1, 2, 3, 4, 5, 6]
    print(flatten([[1, 2], [[3, 4], 5]]))      # Output: [1, 2, 3, 4, 5]
