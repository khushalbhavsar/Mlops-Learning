# 5. Find the difference between local and global variables.

def print_variables():
    local_var = 10  # This is a local variable
    print("Local variable:", local_var)
    print("Global variable:", global_var)  # Accessing the global variable inside the function

global_var = 20  # This is a global variable
print_variables()  # This will print both the local and global variables
print("Global variable outside function:", global_var)  # This will also print 20
# print("Local variable outside function:", local_var)  # This will raise a NameError because local_var is not defined outside the function

