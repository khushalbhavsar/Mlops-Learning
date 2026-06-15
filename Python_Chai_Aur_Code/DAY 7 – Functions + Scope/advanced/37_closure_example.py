# Closure example

def outer(x):
    def inner(y):
        return x + y
    return inner


# Test
if __name__ == "__main__":
    add_five = outer(5)
    print(add_five(10))   # Output: 15
    print(add_five(20))   # Output: 25
