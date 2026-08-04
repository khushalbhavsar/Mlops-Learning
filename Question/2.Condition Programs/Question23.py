# Check loan eligibility

age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
sivliscore = float(input("Enter your SIVLI score: "))
if age >= 21 and salary >= 30000 and sivliscore >= 700:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")
