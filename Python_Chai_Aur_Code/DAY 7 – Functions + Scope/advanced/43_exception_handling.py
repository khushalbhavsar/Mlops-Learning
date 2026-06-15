# Exception handling

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


# Test
if __name__ == "__main__":
    print(safe_divide(10, 2))   # Output: 5.0
    print(safe_divide(10, 0))   # Output: Cannot divide by zero
