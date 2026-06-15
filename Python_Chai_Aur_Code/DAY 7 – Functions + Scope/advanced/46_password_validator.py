# Password validator

def is_valid_password(p):
    return (
        len(p) >= 8 and
        any(c.isupper() for c in p) and
        any(c.islower() for c in p) and
        any(c.isdigit() for c in p)
    )


# Test
if __name__ == "__main__":
    print(is_valid_password("Password123"))  # Output: True
    print(is_valid_password("pass"))         # Output: False
    print(is_valid_password("password"))     # Output: False
