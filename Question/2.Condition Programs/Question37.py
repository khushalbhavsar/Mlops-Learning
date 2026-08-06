# Check if person eligible for job (age + degree)
# strip() is used to remove any leading or trailing whitespace from the input string
# lower() is used to convert the input to lowercase for easier comparison.

age = int(input("Enter your age: "))
degree = input("Do you have a degree? (yes/no): ").strip().lower()  

if age >= 18 and degree == "yes":
    print("You are eligible for the job.")
elif age < 18:
    print("You are not eligible for the job due to age.")
elif degree != "yes":
    print("You are not eligible for the job due to lack of degree.")
else:
    print("You are not eligible for the job.")