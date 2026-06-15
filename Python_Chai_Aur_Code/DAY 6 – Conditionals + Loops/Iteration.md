# 🔁 Behind the Scenes of Loops in Python

Python mainly has **two loops**:

1. `for` loop
2. `while` loop

Both work differently **internally**.

---

## 1️⃣ How `for` loop works internally

### Example:

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

### 🔍 Behind the scenes:

1. Python converts `numbers` into an **iterator**
2. Iterator has a method called `__next__()`
3. Loop calls `__next__()` again and again
4. Each call gives **one value**
5. When values finish → `StopIteration` → loop stops

### Internal view (simplified):

```python
iterator = iter(numbers)

while True:
    try:
        num = next(iterator)
        print(num)
    except StopIteration:
        break
```

👉 **Key idea**:
`for` loop = **automatic iterator handling**

---

## 2️⃣ `range()` behind the scenes

### Example:

```python
for i in range(5):
    print(i)
```

### What `range(5)` really does:

* It **does NOT create a list**
* It generates numbers **one by one**
* Saves memory

### Internal values:

```
0 → 1 → 2 → 3 → 4 → Stop
```

👉 `range()` is a **lazy object**

---

## 3️⃣ How `while` loop works internally

### Example:

```python
x = 1
while x <= 3:
    print(x)
    x += 1
```

### 🔍 Behind the scenes:

1. Condition is checked **first**
2. If `True` → body runs
3. After body → condition checked again
4. If `False` → loop stops

### Execution flow:

```
x=1 → True → print → x=2
x=2 → True → print → x=3
x=3 → True → print → x=4
x=4 → False → exit
```

👉 **Key idea**:
`while` loop = **manual control**

---

## 4️⃣ `break` behind the scenes

### Example:

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

### What happens:

* Loop runs normally
* When `break` hits → loop **immediately exits**
* Iterator is discarded

Output:

```
0 1 2
```

---

## 5️⃣ `continue` behind the scenes

### Example:

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

### What happens:

* `continue` skips **current iteration**
* Control goes back to loop start

Output:

```
0 1 2 4
```

---

## 6️⃣ Infinite loop – what’s happening?

### Example:

```python
while True:
    print("Hello")
```

### Internally:

* Condition is **always True**
* Loop never gets `False`
* Program runs forever unless:

  * `break`
  * Keyboard interrupt (Ctrl + C)

---

## 7️⃣ Nested loops (loop inside loop)

### Example:

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

### Execution order:

```
i=0 → j=0,1,2
i=1 → j=0,1,2
```

👉 Inner loop **completes fully** for each outer loop cycle

---

## 8️⃣ Time complexity intuition (important for interviews)

| Loop Type          | Internal Cost    |
| ------------------ | ---------------- |
| Single loop        | O(n)             |
| Nested loop        | O(n²)            |
| Loop + break early | Best case faster |
| range loop         | Memory efficient |

---

## 9️⃣ Common beginner mistake (behind the scenes)

❌ Forgetting to update condition:

```python
x = 1
while x <= 5:
    print(x)
```

👉 `x` never changes → **infinite loop**


Here are **clear VISUAL DIAGRAMS (ASCII diagrams)** showing what happens **behind the scenes of Python loops** 👇
Perfect for **understanding + interviews** ✅

---

# 🔁 1. `for` Loop – Internal Diagram

### Code:

```python
nums = [10, 20, 30]

for n in nums:
    print(n)
```

### Diagram:

```
List: [10, 20, 30]
        |
        v
Iterator created → iter(nums)
        |
        v
next() → 10 → print
        |
        v
next() → 20 → print
        |
        v
next() → 30 → print
        |
        v
next() → StopIteration ❌
        |
        v
Loop Ends
```

### 🔑 Key Point:

* Python **automatically** handles iterator & stopping
* You never see `next()` but it runs internally

---

# 🔄 2. `range()` Loop – Memory Efficient Diagram

### Code:

```python
for i in range(5):
    print(i)
```

### Diagram:

```
range(5)
  |
  v
0 → 1 → 2 → 3 → 4 → Stop
```

❌ No list created
✅ Numbers generated **one-by-one**

---

# 🔁 3. `while` Loop – Condition Based Diagram

### Code:

```python
x = 1
while x <= 3:
    print(x)
    x += 1
```

### Diagram:

```
Start
  |
  v
Check: x <= 3 ?
  |
  |-- YES --> Print x --> x = x + 1
  |               ↑
  |               |
  |---------------|
  |
  |-- NO --> Exit Loop
```

### 🔑 Key Point:

* Condition checked **before every iteration**
* Programmer controls everything

---

# ⛔ 4. `break` Statement Diagram

### Code:

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

### Diagram:

```
i=0 → print
i=1 → print
i=2 → print
i=3 → break ❌
         |
         v
      Loop Ends
```

---

# ⏭️ 5. `continue` Statement Diagram

### Code:

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

### Diagram:

```
i=0 → print
i=1 → print
i=2 → print
i=3 → continue ⏭️ (skip print)
i=4 → print
```

---

# ♾️ 6. Infinite Loop Diagram

### Code:

```python
while True:
    print("Hello")
```

### Diagram:

```
True
  |
  v
Print "Hello"
  |
  v
True
  |
  v
Print "Hello"
  |
  v
(repeats forever ♾️)
```

🛑 Stops only with:

* `break`
* Ctrl + C

---

# 🔂 7. Nested Loop Diagram

### Code:

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

### Diagram:

```
i=0
 ├─ j=0
 ├─ j=1
 └─ j=2

i=1
 ├─ j=0
 ├─ j=1
 └─ j=2
```

🔁 Inner loop completes **fully** every time



