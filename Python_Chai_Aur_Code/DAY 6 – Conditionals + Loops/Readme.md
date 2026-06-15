# DAY 6 – Conditionals + Loops

## 📝 Questions on Conditionals in Python

Below are basic conditional coding exercises:

| # | Problem | Description |
|---|---------|-------------|
| 1 | **Age Group Categorization** | Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+) |
| 2 | **Movie Ticket Pricing** | Movie tickets are priced based on age: $12 for adults (18+), $8 for children. Everyone gets a $2 discount on Wednesday |
| 3 | **Grade Calculator** | Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60) |
| 4 | **Fruit Ripeness Checker** | Determine if a fruit is ripe, overripe, or unripe based on its color (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe) |
| 5 | **Weather Activity Suggestion** | Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman) |
| 6 | **Transportation Mode Selection** | Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car) |
| 7 | **Coffee Customization** | Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso |
| 8 | **Password Strength Checker** | Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong) |
| 9 | **Leap Year Checker** | Determine if a year is a leap year (divisible by 4, but not by 100 unless also divisible by 400) |
| 10 | **Pet Food Recommendation** | Recommend a type of pet food based on the pet's species and age (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food) |

---

## 💻 Solutions

Below are **basic Python conditional code examples** for each question.
*(Simple, beginner-friendly, using `if / elif / else`)*


---

### 1️⃣ Age Group Categorization

```python
age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")
```

---

### 2️⃣ Movie Ticket Pricing

```python
age = int(input("Enter age: "))
day = input("Enter day: ").lower()

if age >= 18:
    price = 12
else:
    price = 8

if day == "wednesday":
    price -= 2

print("Ticket price:", price)
```

---

### 3️⃣ Grade Calculator

```python
score = int(input("Enter score: "))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")
```

---

### 4️⃣ Fruit Ripeness Checker (Banana Example)

```python
color = input("Enter banana color: ").lower()

if color == "green":
    print("Unripe")
elif color == "yellow":
    print("Ripe")
elif color == "brown":
    print("Overripe")
else:
    print("Unknown color")
```

---

### 5️⃣ Weather Activity Suggestion

```python
weather = input("Enter weather: ").lower()

if weather == "sunny":
    print("Go for a walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("Build a snowman")
else:
    print("Stay indoors")
```

---

### 6️⃣ Transportation Mode Selection

```python
distance = float(input("Enter distance in km: "))

if distance < 3:
    print("Walk")
elif distance <= 15:
    print("Bike")
else:
    print("Car")
```

---

### 7️⃣ Coffee Customization

```python
size = input("Enter size (Small/Medium/Large): ").lower()
extra_shot = input("Extra shot? (yes/no): ").lower()

print("Coffee size:", size.capitalize())

if extra_shot == "yes":
    print("With extra espresso shot")
else:
    print("No extra shot")
```

---

### 8️⃣ Password Strength Checker

```python
password = input("Enter password: ")
length = len(password)

if length < 6:
    print("Weak password")
elif length <= 10:
    print("Medium password")
else:
    print("Strong password")
```

---

### 9️⃣ Leap Year Checker

```python
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

---

### 🔟 Pet Food Recommendation

```python
pet = input("Enter pet (dog/cat): ").lower()
age = int(input("Enter pet age: "))

if pet == "dog":
    if age < 2:
        print("Puppy food")
    else:
        print("Adult dog food")

elif pet == "cat":
    if age > 5:
        print("Senior cat food")
    else:
        print("Adult cat food")
else:
    print("Unknown pet")
```

---

## 📝 Questions on Loops in Python

Below are basic loop coding exercises:

| # | Problem | Description |
|---|---------|-------------|
| 1 | **Counting Positive Numbers** | Given a list of numbers, count how many are positive. `numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]` |
| 2 | **Sum of Even Numbers** | Calculate the sum of even numbers up to a given number n |
| 3 | **Multiplication Table Printer** | Print the multiplication table for a given number up to 10, but skip the fifth iteration |
| 4 | **Reverse a String** | Reverse a string using a loop |
| 5 | **Find the First Non-Repeated Character** | Given a string, find the first non-repeated character |
| 6 | **Factorial Calculator** | Compute the factorial of a number using a while loop |
| 7 | **Validate Input** | Keep asking the user for input until they enter a number between 1 and 10 |
| 8 | **Prime Number Checker** | Check if a number is prime |
| 9 | **List Uniqueness Checker** | Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate. `items = ["apple", "banana", "orange", "apple", "mango"]` |
| 10 | **Exponential Backoff** | Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries |

---

## 💻 Solutions

Below are **basic Python loop code examples** for each question.
*(Simple, beginner-friendly, using `for` and `while` loops)*
---

### 1️⃣ Counting Positive Numbers

```python
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

count = 0
for num in numbers:
    if num > 0:
        count += 1

print("Positive numbers count:", count)
```

---

### 2️⃣ Sum of Even Numbers (up to n)

```python
n = 10
total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total += i

print("Sum of even numbers:", total)
```

---

### 3️⃣ Multiplication Table (Skip 5th iteration)

```python
num = 5

for i in range(1, 11):
    if i == 5:
        continue
    print(num, "x", i, "=", num * i)
```

---

### 4️⃣ Reverse a String (using loop)

```python
text = "python"
reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed string:", reverse)
```

---

### 5️⃣ First Non-Repeated Character

```python
text = "programming"

for char in text:
    if text.count(char) == 1:
        print("First non-repeated character:", char)
        break
```

---

### 6️⃣ Factorial Calculator (while loop)

```python
num = 5
factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print("Factorial:", factorial)
```

---

### 7️⃣ Validate Input (1 to 10)

```python
while True:
    num = int(input("Enter a number between 1 and 10: "))
    if 1 <= num <= 10:
        print("Valid input!")
        break
    else:
        print("Invalid input, try again.")
```

---

### 8️⃣ Prime Number Checker

```python
num = 7
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

print("Prime number:", is_prime)
```

---

### 9️⃣ List Uniqueness Checker

```python
items = ["apple", "banana", "orange", "apple", "mango"]
seen = []

for item in items:
    if item in seen:
        print("Duplicate found:", item)
        break
    seen.append(item)
```

---

### 🔟 Exponential Backoff

```python
wait_time = 1
retries = 0

while retries < 5:
    print("Retry", retries + 1, "- wait time:", wait_time, "seconds")
    wait_time *= 2
    retries += 1
```

---

