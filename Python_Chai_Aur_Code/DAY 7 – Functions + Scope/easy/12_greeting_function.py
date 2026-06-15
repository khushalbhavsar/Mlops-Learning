# Greeting function

def greet(name="User"):
    return f"Hello {name}"


# Test
if __name__ == "__main__":
    print(greet())           # Output: Hello User
    print(greet("Alice"))    # Output: Hello Alice
