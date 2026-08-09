# 6. Create two functions using the same local variable name.

def function_one():
    local_var = 10
    print("Function One - Local Variable:", local_var) # This will print 10 because local_var is defined inside function_one()

def function_two():
    local_var = 20
    print("Function Two - Local Variable:", local_var) # This will print 20 because local_var is defined inside function_two() and is different from the local_var in function_one()

function_one() # This will print 10 because local_var is defined inside function_one()
function_two() # This will print 20 because local_var is defined inside function_two() and is different from the local_var in function_one()


