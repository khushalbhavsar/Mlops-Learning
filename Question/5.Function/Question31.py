# 1. Create a greeting function with a default name.

def greet(name="User"):
    print(f"Hello, {name}!")

greet()  # This will use the default name "User"
greet("Alice")  # This will use the provided name "Alice"

