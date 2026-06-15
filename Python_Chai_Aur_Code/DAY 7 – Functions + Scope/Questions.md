# 🟢 EASY (1–15)

### 1️⃣ Square of a number

```python
def square(n):
    return n * n
```

---

### 2️⃣ Check even or odd

```python
def is_even(n):
    return n % 2 == 0
```

---

### 3️⃣ Add two numbers

```python
def add(a, b):
    return a + b
```

---

### 4️⃣ Maximum of two numbers

```python
def maximum(a, b):
    return a if a > b else b
```

---

### 5️⃣ Convert Celsius to Fahrenheit

```python
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
```

---

### 6️⃣ Count characters in a string

```python
def count_chars(s):
    return len(s)
```

---

### 7️⃣ Reverse a string

```python
def reverse_string(s):
    return s[::-1]
```

---

### 8️⃣ Check positive, negative, or zero

```python
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"
```

---

### 9️⃣ Sum of first n natural numbers

```python
def sum_n(n):
    return n * (n + 1) // 2
```

---

### 🔟 Simple interest

```python
def simple_interest(p, r, t):
    return (p * r * t) / 100
```

---

### 1️⃣1️⃣ Area of a rectangle

```python
def rectangle_area(l, w):
    return l * w
```

---

### 1️⃣2️⃣ Greeting function

```python
def greet(name="User"):
    return f"Hello {name}"
```

---

### 1️⃣3️⃣ Length of list

```python
def list_length(lst):
    return len(lst)
```

---

### 1️⃣4️⃣ Check vowel

```python
def is_vowel(ch):
    return ch.lower() in "aeiou"
```

---

### 1️⃣5️⃣ Square list elements

```python
def square_list(lst):
    return [x*x for x in lst]
```

---

# 🟡 MEDIUM (16–35)

### 1️⃣6️⃣ Factorial

```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
```

---

### 1️⃣7️⃣ Prime check

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

---

### 1️⃣8️⃣ Fibonacci series

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

---

### 1️⃣9️⃣ Count vowels

```python
def count_vowels(s):
    return sum(1 for ch in s if ch.lower() in "aeiou")
```

---

### 2️⃣0️⃣ Find maximum in list

```python
def max_list(lst):
    return max(lst)
```

---

### 2️⃣1️⃣ Remove duplicates

```python
def remove_duplicates(lst):
    return list(set(lst))
```

---

### 2️⃣2️⃣ Palindrome check

```python
def is_palindrome(s):
    return s == s[::-1]
```

---

### 2️⃣3️⃣ Sum using *args

```python
def sum_all(*args):
    return sum(args)
```

---

### 2️⃣4️⃣ Print kwargs

```python
def show_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)
```

---

### 2️⃣5️⃣ Lambda square

```python
square = lambda x: x ** 2
```

---

### 2️⃣6️⃣ Count words

```python
def word_count(sentence):
    return len(sentence.split())
```

---

### 2️⃣7️⃣ Average of list

```python
def average(lst):
    return sum(lst) / len(lst)
```

---

### 2️⃣8️⃣ Second largest element

```python
def second_largest(lst):
    return sorted(set(lst))[-2]
```

---

### 2️⃣9️⃣ Character frequency

```python
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
```

---

### 3️⃣0️⃣ Merge two lists

```python
def merge_lists(a, b):
    return a + b
```

---

### 3️⃣1️⃣ Generate even numbers

```python
def even_numbers(n):
    return [i for i in range(2, n+1, 2)]
```

---

### 3️⃣2️⃣ Decimal to binary

```python
def to_binary(n):
    return bin(n)[2:]
```

---

### 3️⃣3️⃣ GCD

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

---

### 3️⃣4️⃣ LCM

```python
def lcm(a, b):
    return (a * b) // gcd(a, b)
```

---

### 3️⃣5️⃣ Power function

```python
def power(a, b):
    return a ** b
```

---

# 🔴 ADVANCED (36–50)

### 3️⃣6️⃣ Decorator example

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
```

---

### 3️⃣7️⃣ Closure example

```python
def outer(x):
    def inner(y):
        return x + y
    return inner
```

---

### 3️⃣8️⃣ Generator for odd numbers

```python
def odd_numbers(n):
    for i in range(1, n+1, 2):
        yield i
```

---

### 3️⃣9️⃣ Memoized factorial

```python
from functools import lru_cache

@lru_cache(None)
def fact(n):
    return 1 if n == 0 else n * fact(n-1)
```

---

### 4️⃣0️⃣ Map example

```python
def square_list(lst):
    return list(map(lambda x: x*x, lst))
```

---

### 4️⃣1️⃣ Filter example

```python
def filter_even(lst):
    return list(filter(lambda x: x % 2 == 0, lst))
```

---

### 4️⃣2️⃣ Reduce example

```python
from functools import reduce

def product(lst):
    return reduce(lambda a, b: a*b, lst)
```

---

### 4️⃣3️⃣ Exception handling

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
```

---

### 4️⃣4️⃣ Recursive sum

```python
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])
```

---

### 4️⃣5️⃣ Flatten list

```python
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
```

---

### 4️⃣6️⃣ Password validator

```python
def is_valid_password(p):
    return (
        len(p) >= 8 and
        any(c.isupper() for c in p) and
        any(c.islower() for c in p) and
        any(c.isdigit() for c in p)
    )
```

---

### 4️⃣7️⃣ Timer decorator

```python
import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        print("Time:", time.time() - start)
        return result
    return wrapper
```

---

### 4️⃣8️⃣ Count function calls

```python
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner
```

---

### 4️⃣9️⃣ Retry function

```python
def retry(func, times):
    for _ in range(times):
        try:
            return func()
        except:
            pass
```

---

### 5️⃣0️⃣ Custom map function

```python
def my_map(func, iterable):
    return [func(x) for x in iterable]
```

---

