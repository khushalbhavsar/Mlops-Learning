# 4. Modify a global variable using `global`.

def modify_global_variable():
    global global_var  # Declare that we are using the global variable
    global_var += 5  # Modify the global variable

global_var = 20  # This is a global variable
print("Before modification:", global_var)  # This will print 20
modify_global_variable()
print("After modification:", global_var)  # This will print 25 because global_var has been modified inside the function

