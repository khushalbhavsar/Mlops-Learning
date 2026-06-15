# Prime check

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Test
if __name__ == "__main__":
    print(is_prime(7))    # Output: True
    print(is_prime(10))   # Output: False
    print(is_prime(2))    # Output: True
