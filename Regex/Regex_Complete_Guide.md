# Regular Expressions (Regex) in Python – Complete Guide

**Regex (Regular Expression)** is a sequence of characters that defines a **search pattern**.  
It is used to search, match, validate, extract, replace, or split text.

Python provides the built-in **`re`** module for working with regular expressions.

---

## Why Use Regex?
Regex is commonly used for:

- Validating email addresses
- Validating phone numbers
- Password validation
- Extracting URLs
- Searching log files
- Data cleaning
- Finding IP addresses
- Parsing text
- Web scraping
- DevOps log analysis

---

## Import Regex Module

```python
import re
```

---

## Basic Regex Functions

| Function | Description |
|---|---|
| `re.match()` | Matches pattern at the beginning of a string |
| `re.search()` | Searches for the first occurrence anywhere in the string |
| `re.findall()` | Returns all matches as a list |
| `re.finditer()` | Returns an iterator of match objects |
| `re.sub()` | Replaces matched text |
| `re.split()` | Splits text using a pattern |
| `re.compile()` | Compiles a regex pattern for reuse |
| `re.fullmatch()` | Checks if the entire string matches the pattern |

---

## 1. `re.match()`
Matches only at the **beginning** of the string.

```python
import re

text = "Python is easy"
result = re.match("Python", text)
print(result)
```

Output:

```text
<re.Match object>
```

Example:

```python
import re

text = "I love Python"
print(re.match("Python", text))
```

Output:

```text
None
```

Because `"Python"` is not at the start.

---

## 2. `re.search()`
Searches anywhere in the string.

```python
import re

text = "I love Python"
result = re.search("Python", text)
print(result)
```

Output:

```text
<re.Match object>
```

---

## 3. `re.findall()`
Returns every match.

```python
import re

text = "Python Java Python C Python"
result = re.findall("Python", text)
print(result)
```

Output:

```text
['Python', 'Python', 'Python']
```

---

## 4. `re.finditer()`
Returns an iterator containing match objects.

```python
import re

text = "Python Java Python"
for match in re.finditer("Python", text):
    print(match.start(), match.end())
```

Output:

```text
0 6
12 18
```

---

## 5. `re.sub()`
Replace text.

```python
import re

text = "Python is easy"
new_text = re.sub("easy", "powerful", text)
print(new_text)
```

Output:

```text
Python is powerful
```

---

## 6. `re.split()`
Split string using regex.

```python
import re

text = "apple,banana;orange mango"
result = re.split("[,; ]", text)
print(result)
```

Output:

```text
['apple', 'banana', 'orange', 'mango']
```

---

## 7. `re.fullmatch()`
Checks if the **entire** string matches.

```python
import re

print(re.fullmatch(r"\d+", "12345"))
```

Output:

```text
Match
```

---

## Regex Syntax

### Dot (`.`)
Matches any single character.

```python
import re
print(re.findall("c.t", "cat cut cot"))
```

Output:

```text
['cat', 'cut', 'cot']
```

### Caret (`^`)
Beginning of string.

```python
re.match("^Hello", "Hello World")
```

### Dollar (`$`)
End of string.

```python
re.search("World$", "Hello World")
```

### Star (`*`)
Zero or more occurrences.

```python
re.findall("ab*", "a ab abb abbb")
```

Output:

```text
['a', 'ab', 'abb', 'abbb']
```

### Plus (`+`)
One or more occurrences.

```python
re.findall("ab+", "a ab abb abbb")
```

Output:

```text
['ab', 'abb', 'abbb']
```

### Question Mark (`?`)
Zero or one occurrence.

```python
re.findall("colou?r", "color colour")
```

Output:

```text
['color', 'colour']
```

### Curly Braces (`{}`)
Specify repetition.

```python
re.findall(r"\d{3}", "1234 567 89")
```

Output:

```text
['123', '567']
```

---

## Character Classes

### Digits (`\d`)
Matches digits.

```python
re.findall(r"\d", "A1B2C3")
```

Output:

```text
['1', '2', '3']
```

### Non-Digits (`\D`)

```python
re.findall(r"\D", "A1B2")
```

Output:

```text
['A', 'B']
```

### Word Characters (`\w`)
Matches letters, numbers, and underscore.

```python
re.findall(r"\w", "A_12")
```

Output:

```text
['A', '_', '1', '2']
```

### Non-Word Characters (`\W`)

```python
re.findall(r"\W", "A@12")
```

Output:

```text
['@']
```

### Whitespace (`\s`)
Matches space, tab, newline.

### Non-Whitespace (`\S`)

---

## Character Sets

Example:

```python
re.findall("[abc]", "apple banana cat")
```

Matches: `a`, `b`, `c`

Range:

```text
[A-Z]  # Uppercase letters
[a-z]  # Lowercase letters
[0-9]  # Numbers
[A-Za-z0-9]  # Alphanumeric
```

---

## Negation

```python
[^0-9]
```

Matches everything except digits.

---

## Groups

```python
import re

text = "2026-08-05"
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)

print(match.group(1))
print(match.group(2))
print(match.group(3))
```

Output:

```text
2026
08
05
```

---

## Named Groups

```python
match = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})", "2026-08")
print(match.group("year"))
```

---

## OR Operator

```python
re.findall("cat|dog", "cat dog lion")
```

Output:

```text
['cat', 'dog']
```

---

## Regex Flags

### Ignore Case

```python
re.findall("python", "Python", re.IGNORECASE)
```

### Multiline

```python
re.MULTILINE
```

### Dotall

```python
re.DOTALL
```

Makes `.` match newlines.

---

## Compile Regex

```python
import re

pattern = re.compile(r"\d+")
print(pattern.findall("123 abc 456"))
```

Output:

```text
['123', '456']
```

---

## Email Validation

```python
import re

email = "user@gmail.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.fullmatch(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
```

---

## Mobile Number Validation

```python
import re

number = "9876543210"
pattern = r"^[6-9]\d{9}$"

print(bool(re.fullmatch(pattern, number)))
```

---

## Password Validation

Requirements:

- Minimum 8 characters
- One uppercase letter
- One lowercase letter
- One digit
- One special character

```python
import re

password = "Pass@123"

pattern = (
    r"^(?=.*[A-Z])"
    r"(?=.*[a-z])"
    r"(?=.*\d)"
    r"(?=.*[@$!%*?&])"
    r"[A-Za-z\d@$!%*?&]{8,}$"
)

print(bool(re.fullmatch(pattern, password)))
```

---

## Extract URLs

```python
import re

text = "Visit https://example.com or http://test.com"
urls = re.findall(r"https?://\S+", text)
print(urls)
```

---

## Extract IP Addresses

```python
import re

text = "Server IP: 192.168.1.100"
ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)
print(ips)
```

---

## Extract Numbers from Logs

```python
import re

log = "CPU=85 Memory=72 Disk=90"
numbers = re.findall(r"\d+", log)
print(numbers)
```

Output:

```text
['85', '72', '90']
```

---

## DevOps Example: Extract Error Lines

```python
import re

logs = """
INFO Server started
ERROR Database failed
INFO Request received
ERROR Disk full
"""

errors = re.findall(r"ERROR.*", logs)
print(errors)
```

Output:

```text
['ERROR Database failed', 'ERROR Disk full']
```

---

## DevOps Example: Extract Pod Names

```python
import re

pods = """
nginx-54df7
redis-1ab2
mongo-7788
"""

print(re.findall(r"\w+-\w+", pods))
```

---

## Difference Between Common Functions

| Function | Searches From | Returns |
|---|---|---|
| `match()` | Beginning only | First match or `None` |
| `search()` | Anywhere | First match or `None` |
| `findall()` | Entire string | List of all matches |
| `finditer()` | Entire string | Iterator of match objects |
| `sub()` | Entire string | New string with replacements |
| `split()` | Entire string | List of substrings |
| `fullmatch()` | Entire string | Match only if whole string matches |

---

## Most Common Regex Symbols

| Symbol | Meaning | Example |
|---|---|---|
| `.` | Any character except newline | `c.t` |
| `^` | Start of string | `^Hello` |
| `$` | End of string | `World$` |
| `*` | 0 or more | `ab*` |
| `+` | 1 or more | `ab+` |
| `?` | 0 or 1 | `colou?r` |
| `{n}` | Exactly n times | `\d{4}` |
| `{n,m}` | Between n and m times | `\d{2,4}` |
| `[]` | Character set | `[A-Z]` |
| `[^]` | Negated character set | `[^0-9]` |
| `\d` | Digit | `5` |
| `\D` | Non-digit | `A` |
| `\w` | Word character | `A`, `1`, `_` |
| `\W` | Non-word character | `@`, `#` |
| `\s` | Whitespace | Space, tab |
| `\S` | Non-whitespace | `A`, `1` |
| `()` | Capture group | `(\d+)` |
| `\|` | OR operator | `cat\|dog` |

---

## Interview Definition

> **Regex (Regular Expression)** is a sequence of characters used to define search patterns. In Python, the built-in `re` module provides functions to search, match, extract, validate, split, and replace text efficiently. Regex is widely used for input validation, log analysis, data extraction, and text processing in automation, DevOps, and web applications.

