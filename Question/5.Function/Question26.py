# 6. Create two functions using the same local variable name.

def function_one():
    local_var = 10
    print("Function One - Local Variable:", local_var)

def function_two():
    local_var = 20
    print("Function Two - Local Variable:", local_var)

function_one()
function_two()
