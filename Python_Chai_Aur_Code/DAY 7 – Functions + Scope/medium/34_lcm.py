# LCM (Least Common Multiple)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


# Test
if __name__ == "__main__":
    print(lcm(4, 6))    # Output: 12
    print(lcm(15, 20))  # Output: 60
