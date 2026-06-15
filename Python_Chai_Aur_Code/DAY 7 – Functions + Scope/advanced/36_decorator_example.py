# Decorator example

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


# Test
if __name__ == "__main__":
    @my_decorator
    def say_hello():
        print("Hello!")
    
    say_hello()
    # Output:
    # Before function
    # Hello!
    # After function
