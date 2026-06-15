# Count function calls

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner


# Test
if __name__ == "__main__":
    my_counter = counter()
    print(my_counter())   # Output: 1
    print(my_counter())   # Output: 2
    print(my_counter())   # Output: 3
