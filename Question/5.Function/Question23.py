# 3. Create a global variable and access it inside a function.

def print_global_variable():
    print(global_var)  # Accessing the global variable inside the function

global_var = 20  # This is a global variable
print_global_variable()  # This will print 20 because global_var is accessible inside the function
print(global_var)  # This will also print 20 because global_var is a global variable

# What is global_var? It is a global variable that is defined outside the function print_global_variable(). It can be accessed both inside and outside the function.

