# 1. Create a local variable and print it.

def print_local_variable():
    local_var = 10
    print(local_var)

print_local_variable()

# What is local_var? It is a local variable that is defined inside the function print_local_variable(). It can only be accessed within the function and will raise a NameError if accessed outside the function.
