# Print kwargs

def show_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)


# Test
if __name__ == "__main__":
    show_kwargs(name="Alice", age=25, city="New York")
    # Output:
    # name : Alice
    # age : 25
    # city : New York
