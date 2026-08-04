# Scholarship eligibility based on marks + income

marks = float(input("Enter your marks: "))
income = float(input("Enter your family income: "))

if marks >= 85:
    if income <= 50000:
        print("You are eligible for the scholarship!")
    else:
        print("You are not eligible for the scholarship due to high family income.")

else:
    print("You are not eligible for the scholarship due to low marks.")

