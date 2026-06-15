# Retry function

def retry(func, times):
    for _ in range(times):
        try:
            return func()
        except:
            pass


# Test
if __name__ == "__main__":
    attempt = 0
    
    def flaky_function():
        global attempt
        attempt += 1
        if attempt < 3:
            raise Exception("Failed")
        return "Success!"
    
    result = retry(flaky_function, 5)
    print(result)   # Output: Success!
