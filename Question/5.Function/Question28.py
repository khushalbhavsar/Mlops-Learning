# 8. Create a program with both local and global variables.

def print_variables():
    local_var = "I am a local variable"  # This is a local variable
    print("Local variable:", local_var)
    print("Global variable:", global_var)  # Accessing the global variable inside the function
    
global_var = "I am a global variable"
print_variables()  # This will print both the local and global variables
