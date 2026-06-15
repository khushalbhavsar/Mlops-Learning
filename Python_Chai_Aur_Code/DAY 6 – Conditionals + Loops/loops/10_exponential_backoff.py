# Exponential Backoff
# Implement an exponential backoff strategy that doubles the wait time between retries,
# starting from 1 second, but stops after 5 retries

wait_time = 1
retries = 0

while retries < 5:
    print("Retry", retries + 1, "- wait time:", wait_time, "seconds")
    wait_time *= 2
    retries += 1
