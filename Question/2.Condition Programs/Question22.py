# Calculate tax based on salary slab

salary = float(input("Enter the employee's salary: "))
if salary < 50000:
    tax = 0
elif salary <= 100000:
    tax = salary * 0.1
elif salary <= 150000:
    tax = salary * 0.15
else:
    tax = salary * 0.2
print(f"The calculated tax for the employee is: {tax}")