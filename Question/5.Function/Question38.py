# 8. Create a function with two default parameters.

def greet(name="User", greeting="Hello"):
    print(f"{greeting}, {name}!")

greet()  # This will use the default name "User" and default greeting "Hello"
greet("Alice")  # This will use the provided name "Alice" and default greeting
