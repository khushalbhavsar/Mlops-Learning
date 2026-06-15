# GCD (Greatest Common Divisor)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Test
if __name__ == "__main__":
    print(gcd(48, 18))   # Output: 6
    print(gcd(100, 25))  # Output: 25
