# 5. Print the multiplication table of a given number from n × 1 to n × 10.

number = int(input("Enter a number: "))
count = 1
while count <= 10:
    result = number * count
    print(f"{number} x {count} = {result}")
    count += 1
    