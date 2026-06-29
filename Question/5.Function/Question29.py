# 9. Demonstrate variable shadowing.

def demonstrate_variable_shadowing():
    global_var = "I am a local variable that shadows the global variable"  # This local variable shadows the global variable
    print("Inside function, global_var:", global_var)  # This will print the local variable

global_var = "I am a global variable"
demonstrate_variable_shadowing()
print("Outside function, global_var:", global_var)  # This will print the global variable
