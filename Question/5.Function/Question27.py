# 7. Use a global counter variable.

def increment_counter():
    global counter  # Declare that we are using the global variable
    counter += 1  # Increment the global counter variable

counter = 0  # This is a global variable
increment_counter()  # Increment the global counter variable
print("Counter after first increment:", counter)  # This will print 1
increment_counter()  # Increment the global counter variable again
print("Counter after second increment:", counter)  # This will print 2
