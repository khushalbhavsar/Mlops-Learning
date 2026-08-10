users = {
    "admin": {
        "username": "admin",
        "password": "admin123",
        "role": "admin",
    },
    "customer": {
        "username": "customer",
        "password": "customer123",
        "role": "customer",
    },
}


def login(username, password):
    user = users.get(username)

    if user and user["password"] == password:
        return {
            "success": True,
            "username": username,
            "role": user["role"],
        }

    return {
        "success": False,
        "message": "Invalid credentials",
    }
