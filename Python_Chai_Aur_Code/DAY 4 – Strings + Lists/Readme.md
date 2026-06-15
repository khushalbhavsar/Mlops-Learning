# 🧵 Python String – All Important Methods with Examples

> Strings are **immutable** sequences of Unicode characters.

---

## 🔹 Case Conversion Methods

```python
text = "python Programming"
```

### `upper()`

```python
text.upper()   # 'PYTHON PROGRAMMING'
```

### `lower()`

```python
text.lower()   # 'python programming'
```

### `capitalize()`

```python
text.capitalize()  # 'Python programming'
```

### `title()`

```python
text.title()   # 'Python Programming'
```

### `swapcase()`

```python
text.swapcase()  # 'PYTHON pROGRAMMING'
```

---

## 🔹 Searching & Checking Methods

```python
s = "hello world"
```

### `find()`

```python
s.find("world")   # 6
```

### `index()`

```python
s.index("world")  # 6
```

### `count()`

```python
s.count("l")  # 3
```

### `startswith()`

```python
s.startswith("hello")  # True
```

### `endswith()`

```python
s.endswith("world")  # True
```

---

## 🔹 Validation (Boolean Check) Methods

```python
a = "Python123"
```

### `isalpha()`

```python
a.isalpha()   # False
```

### `isalnum()`

```python
a.isalnum()   # True
```

### `isdigit()`

```python
"123".isdigit()  # True
```

### `islower()`

```python
"python".islower()  # True
```

### `isupper()`

```python
"PYTHON".isupper()  # True
```

### `isspace()`

```python
"   ".isspace()  # True
```

---

## 🔹 Replace & Modify Methods

### `replace()`

```python
text = "I like Java"
text.replace("Java", "Python")
# 'I like Python'
```

### `strip()`

```python
"  hello  ".strip()   # 'hello'
```

### `lstrip()`

```python
"  hello".lstrip()   # 'hello'
```

### `rstrip()`

```python
"hello  ".rstrip()   # 'hello'
```

---

## 🔹 Split & Join Methods

### `split()`

```python
sentence = "Python is awesome"
sentence.split()
# ['Python', 'is', 'awesome']
```

### `split(",")`

```python
data = "a,b,c"
data.split(",")   # ['a', 'b', 'c']
```

### `join()`

```python
words = ['Hello', 'World']
" ".join(words)
# 'Hello World'
```

---

## 🔹 Formatting Methods

### `format()`

```python
name = "Khushal"
age = 22
"Name: {}, Age: {}".format(name, age)
```

### f-string (Modern & recommended)

```python
f"Name: {name}, Age: {age}"
```

---

## 🔹 Alignment & Padding

### `center()`

```python
"Python".center(10, "*")
# '**Python**'
```

### `ljust()`

```python
"Python".ljust(10, "-")
# 'Python----'
```

### `rjust()`

```python
"Python".rjust(10, "-")
# '----Python'
```

---

## 🔹 Encoding & Decoding

### `encode()`

```python
"hello".encode()
# b'hello'
```

### `decode()`

```python
b'hello'.decode()
# 'hello'
```

---

## 🔹 String Testing & Utility

### `len()`

```python
len("Python")  # 6
```

### `min()` / `max()`

```python
min("abc")  # 'a'
max("abc")  # 'c'
```

---

## 🔹 Escape Characters

```python
print("Hello\nWorld")   # New line
print("Hello\tWorld")   # Tab
print("He said \"Hi\"") # Quotes
```

---

## 🔹 String Slicing

```python
s = "Python"
s[0:4]   # 'Pyth'
s[::-1]  # 'nohtyP'
```

---

## ⚠️ Important Interview Points

✔ Strings are **immutable**
✔ Every method returns a **new string**
✔ Indexing starts from **0**
✔ Negative indexing supported

---

## 🎯 Most Asked Interview Methods

* `split()`
* `join()`
* `replace()`
* `find()` vs `index()`
* `strip()`
* `startswith()`
* `isalnum()`
* `format()` / f-strings

