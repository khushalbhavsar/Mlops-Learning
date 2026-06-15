# Simple interest

def simple_interest(p, r, t):
    return (p * r * t) / 100


# Test
if __name__ == "__main__":
    print(simple_interest(1000, 5, 2))   # Output: 100.0
    print(simple_interest(5000, 10, 3))  # Output: 1500.0
