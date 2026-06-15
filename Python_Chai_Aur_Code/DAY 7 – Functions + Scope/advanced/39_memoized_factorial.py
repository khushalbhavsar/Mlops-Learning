# Memoized factorial

from functools import lru_cache


@lru_cache(None)
def fact(n):
    return 1 if n == 0 else n * fact(n-1)


# Test
if __name__ == "__main__":
    print(fact(5))    # Output: 120
    print(fact(10))   # Output: 3628800
