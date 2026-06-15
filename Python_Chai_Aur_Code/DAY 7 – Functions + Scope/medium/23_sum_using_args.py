# Sum using *args

def sum_all(*args):
    return sum(args)


# Test
if __name__ == "__main__":
    print(sum_all(1, 2, 3, 4, 5))   # Output: 15
    print(sum_all(10, 20))          # Output: 30
