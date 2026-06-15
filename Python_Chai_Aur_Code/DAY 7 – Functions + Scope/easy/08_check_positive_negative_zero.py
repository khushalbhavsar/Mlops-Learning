# Check positive, negative, or zero

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"


# Test
if __name__ == "__main__":
    print(check_number(10))   # Output: Positive
    print(check_number(-5))   # Output: Negative
    print(check_number(0))    # Output: Zero
