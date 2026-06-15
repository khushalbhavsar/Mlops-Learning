# Timer decorator

import time


def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        print("Time:", time.time() - start)
        return result
    return wrapper


# Test
if __name__ == "__main__":
    @timer
    def slow_function():
        time.sleep(1)
        return "Done"
    
    print(slow_function())
    # Output:
    # Time: ~1.0
    # Done
