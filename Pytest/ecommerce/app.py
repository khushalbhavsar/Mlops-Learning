def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Success"
    return "Login Failed"


def add(a, b):
    return a + b


def checkout(total):
    if total > 0:
        return "Order Placed"
    return "Order Failed"
