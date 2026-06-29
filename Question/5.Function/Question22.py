# 2. Try accessing a local variable outside the function.

def print_local_variable():
    local_var = 10
    print(local_var)

print_local_variable()
print(local_var)  # This will raise a NameError because local_var is not defined outside the function   

# Why loal_var is not accessible outside the function? It is because local_var is a local variable that is defined inside the function print_local_variable(). It can only be accessed within the function and will raise a NameError if accessed outside the function.