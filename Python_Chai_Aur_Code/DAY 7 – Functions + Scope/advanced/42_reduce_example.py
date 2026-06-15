# Reduce example

from functools import reduce


def product(lst):
    return reduce(lambda a, b: a*b, lst)


# Test
if __name__ == "__main__":
    print(product([1, 2, 3, 4, 5]))   # Output: 120
    print(product([2, 3, 4]))         # Output: 24
