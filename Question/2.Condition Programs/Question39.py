# Check if triangle valid by angles

angle1 = int(input("Enter the first angle of the triangle: "))
angle2 = int(input("Enter the second angle of the triangle: "))
angle3 = int(input("Enter the third angle of the triangle: "))
if angle1 + angle2 + angle3 == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
    