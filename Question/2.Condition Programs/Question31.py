# Login system with username and password

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "pass123":
    print("Login successful!")
else:
    print("Invalid username or password.")
