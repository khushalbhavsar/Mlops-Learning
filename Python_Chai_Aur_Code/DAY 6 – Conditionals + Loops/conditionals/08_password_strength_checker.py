# Password Strength Checker
# Check if a password is "Weak", "Medium", or "Strong"
# Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong)

password = input("Enter password: ")
length = len(password)

if length < 6:
    print("Weak password")
elif length <= 10:
    print("Medium password")
else:
    print("Strong password")
