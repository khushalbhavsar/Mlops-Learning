# 20. Find result for multiple subjects.

marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))
total_marks = marks1 + marks2 + marks3
if total_marks >= 180:
    print("Result: Pass")
else:
    print("Result: Fail")
    