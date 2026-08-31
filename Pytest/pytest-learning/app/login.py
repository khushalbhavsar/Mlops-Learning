def login(username, password):
    valid_credentials = {"admin": "admin123", "user": "user123"}
    return valid_credentials.get(username) == password
