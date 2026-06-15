# Decimal to binary

def to_binary(n):
    return bin(n)[2:]


# Test
if __name__ == "__main__":
    print(to_binary(10))   # Output: 1010
    print(to_binary(255))  # Output: 11111111
