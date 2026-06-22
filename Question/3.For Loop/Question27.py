# - Q27: Reverse a given number using a loop

n = int(input("Enter a number: "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
print(f"The reverse of the given number is {reverse}")