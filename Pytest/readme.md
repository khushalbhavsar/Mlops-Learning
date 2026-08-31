# PyTest Complete Roadmap (Basic → Advanced)

## Module 1: Introduction to PyTest

* What is Testing?
* Why Testing?
* What is Unit Testing?
* Why PyTest?
* PyTest vs unittest
* Installing PyTest
* First Test
* Running Tests
* Naming Conventions

## Module 2: Assertions

* assert keyword
* Assertion messages
* Comparing values
* Checking exceptions
* Floating point comparisons
* Multiple assertions

## Module 3: Test Discovery

* How PyTest finds tests
* Naming rules
* Directory structure
* Running specific tests
* Running test classes
* Running test methods
* Running by keyword

## Module 4: Fixtures

* What is Fixture?
* Why Fixtures?
* Creating Fixtures
* Using Fixtures
* Fixture Scope
* Autouse Fixtures
* yield Fixtures
* Dependency between Fixtures
* Fixture Best Practices

## Module 5: Parameterization

* @pytest.mark.parametrize
* Multiple parameters
* IDs
* Combining fixtures and parameterization

## Module 6: Markers

* @pytest.mark.skip
* skipif
* xfail
* custom markers
* smoke
* regression
* sanity
* api
* database

## Module 7: conftest.py

* What is conftest.py?
* Shared fixtures
* Global fixtures
* Multiple conftest files
* Real project examples

## Module 8: pytest.ini

* Configuration
* Register markers
* Default options
* Logging
* Test paths

## Module 9: Fixture Scope

* function
* class
* module
* package
* session

Performance comparison

## Module 10: HTML Reports

* pytest-html
* Custom reports
* Screenshots
* Environment details
* CI integration

## Module 11: Advanced Fixtures

* Temporary directories
* Monkeypatch
* capsys
* caplog
* request object

## Module 12: Mocking

* unittest.mock
* patch
* Mock APIs
* Mock Database
* Mock File System

## Module 13: API Testing

* requests library
* GET
* POST
* PUT
* PATCH
* DELETE
* Authentication
* Authorization
* Headers
* Cookies
* Response Validation

## Module 14: Database Testing

* SQLite
* MySQL
* PostgreSQL
* CRUD Testing

## Module 15: Selenium + PyTest

* Browser automation
* Fixtures
* Page Object Model
* Parallel execution

## Module 16: PyTest Plugins

* pytest-xdist
* pytest-html
* pytest-cov
* pytest-rerunfailures
* pytest-mock

## Module 17: CI/CD Integration

* Jenkins
* GitHub Actions
* Docker
* Kubernetes

## Module 18: Real Project

* API Automation Framework
* Folder Structure
* Reports
* Fixtures
* Logging
* Configurations
* CI Pipeline

---

# Learning Plan

Since you want **proper notes from basic to advanced**, we'll cover **one module at a time**, and each module will include:

* ✅ Theory (simple definitions)
* ✅ Why it is needed
* ✅ Syntax
* ✅ Code examples
* ✅ Output explanation
* ✅ Real-world examples
* ✅ Interview questions
* ✅ Common mistakes
* ✅ Best practices
* ✅ Hands-on exercises
* ✅ Mini project at the end of the module

---

# Module 1: Introduction to PyTest

## What is Testing?

### Definition

**Testing** is the process of verifying that a software application behaves as expected and meets its requirements.

The goal is to identify bugs before the software reaches users.

---

## Example

Imagine a calculator application.

If a user enters:

```text
2 + 3
```

Expected output:

```text
5
```

If the application returns:

```text
8
```

There is a bug.

Testing helps detect this issue.

---

# What is Unit Testing?

## Definition

**Unit Testing** is a type of software testing where the smallest testable units (usually functions or methods) are tested individually.

Each unit is tested in isolation.

---

Example

```python
def add(a, b):
    return a + b
```

We can test it:

```python
assert add(2, 3) == 5
```

---

# What is PyTest?

## Definition

**PyTest** is a powerful, open-source Python testing framework used to write, organize, and execute automated tests.

It supports:

* Unit Testing
* Functional Testing
* API Testing
* Integration Testing
* End-to-End Testing

---

# Why Use PyTest?

Without PyTest:

```python
def add(a, b):
    return a + b

print(add(2, 3))
```

You manually inspect the output.

With PyTest:

```python
def test_add():
    assert add(2, 3) == 5
```

PyTest automatically reports whether the test passed or failed.

---

# Why is PyTest Popular?

* Simple syntax
* Powerful assertion introspection
* Automatic test discovery
* Rich plugin ecosystem
* Fixture support
* Parameterized testing
* HTML reporting
* Parallel execution
* Easy CI/CD integration (Jenkins, GitHub Actions)

---

# PyTest vs unittest

| Feature          | PyTest           | unittest                  |
| ---------------- | ---------------- | ------------------------- |
| Syntax           | Simple           | More verbose              |
| Assertions       | `assert` keyword | Many `assert*` methods    |
| Fixtures         | Built-in         | Uses `setUp` / `tearDown` |
| Parameterization | Built-in         | Requires extra code       |
| Plugins          | Extensive        | Limited                   |
| Learning Curve   | Easy             | Moderate                  |

---

# Installing PyTest

Check Python version:

```bash
python --version
```

Install PyTest:

```bash
pip install pytest
```

Verify installation:

```bash
pytest --version
```

Example output:

```text
pytest 8.x.x
```

---

# Project Structure

```text
pytest-course/
│
├── app/
│   ├── calculator.py
│
├── tests/
│   └── test_calculator.py
│
├── requirements.txt
│
└── pytest.ini
```

---

# Create a Simple Python File

**`app/calculator.py`**

```python
def add(a, b):
    return a + b
```

---

# Write Your First Test

**`tests/test_calculator.py`**

```python
from app.calculator import add

def test_add():
    assert add(2, 3) == 5
```

---

# Running Tests

Run all tests:

```bash
pytest
```

Run with detailed output:

```bash
pytest -v
```

Run a specific file:

```bash
pytest tests/test_calculator.py
```

Run a specific test function:

```bash
pytest tests/test_calculator.py::test_add
```

---

# Understanding the Output

If the implementation is correct:

```text
=============================
1 passed in 0.02s
=============================
```

If the function is incorrect:

```python
def add(a, b):
    return a - b
```

PyTest reports:

```text
> assert -1 == 5
E AssertionError
```

This makes it easy to identify the failing assertion.

---

# Naming Conventions

PyTest automatically discovers tests when you follow these conventions:

### Test files

```text
test_calculator.py
test_login.py
```

### Test functions

```python
def test_add():
    ...

def test_login():
    ...
```

### Test classes

```python
class TestCalculator:

    def test_add(self):
        ...
```

---

# Real-World Example

Suppose your team develops an API:

```python
GET /users/1
```

You want to ensure it always returns status code **200**.

```python
import requests

def test_get_user():
    response = requests.get("https://api.example.com/users/1")
    assert response.status_code == 200
```

Whenever a developer changes the backend, PyTest immediately tells you if this endpoint has broken.

---

# Best Practices

* Keep one responsibility per test.
* Use descriptive test names (`test_login_with_valid_credentials`).
* Avoid dependencies between tests.
* Store tests in a separate `tests/` directory.
* Use fixtures instead of duplicating setup code.

---

# Module 1 Exercises

1. Install PyTest.
2. Create a `calculator.py` with `add()` and `subtract()` functions.
3. Write tests for both functions.
4. Intentionally introduce a bug and observe the failure output.
5. Run:

   * `pytest`
   * `pytest -v`
   * A single test file
   * A single test function

---

## Next Module

**Module 2: Assertions (Complete Guide)**

We'll cover:

* `assert` in detail
* How PyTest rewrites assertions
* Comparing lists, dictionaries, and objects
* Exception testing with `pytest.raises`
* Floating-point comparisons
* Custom assertion messages
* Real-world examples and interview questions

By the end of this course, you'll be able to build a **production-ready PyTest automation framework** for **API testing, Selenium, CI/CD (Jenkins/GitHub Actions), Docker, and Kubernetes**, which is the level typically expected in DevOps and SRE roles.

# PyTest Complete Course

# Module 2 – Assertions (Basic → Advanced)

Assertions are the **heart of PyTest**. Every test ultimately checks whether something is true by using an assertion.

---

# What is an Assertion?

## Definition

An **assertion** is a statement that verifies whether an expected condition is true.

If the condition is:

* **True** → Test Passes ✅
* **False** → Test Fails ❌

---

## Interview Definition

> **An assertion is a validation statement used in testing to compare the actual result with the expected result. If both values match, the test passes; otherwise, it fails with an AssertionError.**

---

# Why Do We Need Assertions?

Suppose you have a function:

```python
def add(a, b):
    return a + b
```

Without assertion:

```python
print(add(2, 3))
```

Output

```
5
```

You must manually verify the output.

---

With assertion:

```python
assert add(2, 3) == 5
```

PyTest automatically verifies the result.

---

# How assert Works

Syntax

```python
assert condition
```

Example

```python
assert 10 > 5
```

Passes because condition is True.

---

Example

```python
assert 5 > 10
```

Fails.

Output

```
AssertionError
```

---

# Basic Example

calculator.py

```python
def add(a, b):
    return a + b
```

test_calculator.py

```python
from app.calculator import add

def test_add():
    assert add(10, 20) == 30
```

Run

```bash
pytest
```

Output

```
1 passed
```

---

# Why PyTest Assertions Are Better

Traditional Python

```python
assert add(10,20)==30
```

PyTest automatically shows

```
Expected :30
Actual   :40
```

No extra code needed.

---

# Example

Wrong function

```python
def add(a,b):
    return a*b
```

Test

```python
assert add(10,20)==30
```

Output

```
> assert 200 == 30
```

PyTest clearly shows

* Actual Value
* Expected Value

---

# Types of Assertions

---

# 1. Equality

Most common assertion.

```python
def test_equal():

    assert 10 == 10
```

Pass

---

Fail

```python
assert 10 == 20
```

---

# 2. Not Equal

```python
assert 10 != 20
```

---

# 3. Greater Than

```python
assert 20 > 10
```

---

# 4. Less Than

```python
assert 10 < 20
```

---

# 5. Greater Than Equal

```python
assert 20 >= 20
```

---

# 6. Less Than Equal

```python
assert 10 <= 20
```

---

# 7. Boolean Assertions

```python
assert True
```

---

```python
assert not False
```

---

# String Assertions

```python
name = "Khushal"

assert name == "Khushal"
```

---

Contains

```python
assert "DevOps" in "DevOps Engineer"
```

---

Not Contains

```python
assert "Java" not in "Python"
```

---

Startswith

```python
assert "Python".startswith("Py")
```

---

Endswith

```python
assert "python.py".endswith(".py")
```

---

# List Assertions

```python
numbers = [10,20,30]

assert 20 in numbers
```

---

```python
assert len(numbers)==3
```

---

Compare Lists

```python
assert [1,2]==[1,2]
```

---

# Dictionary Assertions

```python
user = {
    "name":"Khushal",
    "age":23
}
```

Check key

```python
assert "name" in user
```

---

Check value

```python
assert user["name"]=="Khushal"
```

---

# None Assertions

```python
value = None

assert value is None
```

---

Not None

```python
value = 100

assert value is not None
```

---

# Identity Assertions

```python
a = [1,2]

b = a
```

Same object

```python
assert a is b
```

Different object

```python
c=[1,2]

assert a is not c
```

---

# Floating Point Assertions

Sometimes

```python
0.1 + 0.2
```

returns

```
0.30000000000000004
```

Wrong

```python
assert 0.1+0.2==0.3
```

Use

```python
import pytest

def test_float():

    assert 0.1+0.2 == pytest.approx(0.3)
```

Best practice.

---

# Exception Assertions

One of the most important interview topics.

Suppose

```python
def divide(a,b):

    return a/b
```

If

```python
divide(10,0)
```

Raises

```
ZeroDivisionError
```

Testing

```python
import pytest

def test_divide():

    with pytest.raises(ZeroDivisionError):

        divide(10,0)
```

Passes.

---

# Multiple Exceptions

```python
with pytest.raises(ValueError):

    int("abc")
```

---

# Checking Exception Message

```python
import pytest

def check(age):

    if age<0:

        raise ValueError("Invalid Age")
```

Test

```python
def test_age():

    with pytest.raises(ValueError,match="Invalid Age"):

        check(-10)
```

---

# Assert Collections

Tuple

```python
assert (1,2)==(1,2)
```

---

Set

```python
assert {1,2}=={2,1}
```

---

Dictionary

```python
assert {"a":1}=={"a":1}
```

---

# Real Project Example

Suppose

Login API

Returns

```json
{
   "status":"success",
   "user":"Khushal"
}
```

Test

```python
response = {
    "status":"success",
    "user":"Khushal"
}

assert response["status"]=="success"

assert response["user"]=="Khushal"
```

---

# API Testing Example

```python
import requests

def test_get_users():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    assert response.status_code==200

    data = response.json()

    assert data["id"]==1

    assert "name" in data
```

---

# Database Example

```python
employee = {
    "id":101,
    "salary":50000
}

assert employee["salary"]>40000
```

---

# File Example

```python
import os

assert os.path.exists("config.json")
```

---

# Best Practices

✔ One assertion should validate one behavior (it's okay to have multiple related assertions in one test if they verify the same outcome).

✔ Write descriptive test names.

✔ Use `pytest.approx()` for floating-point comparisons.

✔ Use `pytest.raises()` to test exceptions.

✔ Compare actual values to expected values.

✔ Avoid unnecessary or redundant assertions.

---

# Common Mistakes

## Comparing Float

Wrong

```python
assert 0.1+0.2==0.3
```

Correct

```python
assert 0.1+0.2==pytest.approx(0.3)
```

---

## Ignoring Exception

Wrong

```python
divide(10,0)
```

Correct

```python
with pytest.raises(ZeroDivisionError):
    divide(10,0)
```

---

# Interview Questions

### Q1 What is an assertion?

**Answer**

An assertion verifies whether the actual result matches the expected result. If the condition evaluates to true, the test passes; otherwise, it fails with an `AssertionError`.

---

### Q2 Why does PyTest use Python's assert?

Because PyTest enhances the built-in `assert` statement by providing detailed failure information, such as the actual and expected values, without requiring additional assertion methods.

---

### Q3 What is pytest.approx()?

It is used to compare floating-point numbers while accounting for small precision differences.

Example

```python
assert 0.1+0.2==pytest.approx(0.3)
```

---

### Q4 How do you test exceptions?

```python
with pytest.raises(ValueError):
    function()
```

---

### Q5 How do you verify an exception message?

```python
with pytest.raises(ValueError,match="Invalid"):
    function()
```

---

# Practice Questions

## Easy

Write assertions for:

* Equality
* Greater than
* List length
* Dictionary value
* String contains

---

## Medium

Test:

```python
def subtract(a,b):

    return a-b
```

Write:

* Positive test
* Negative test
* Zero test

---

## Advanced

Create

```python
def login(username,password):
```

Write tests for:

* Valid user
* Wrong password
* Empty username
* Empty password
* Invalid username
* Exception handling

---

# Mini Project

Project Structure

```text
pytest-learning/
│
├── app/
│   ├── calculator.py
│   └── login.py
│
├── tests/
│   ├── test_calculator.py
│   └── test_login.py
│
└── requirements.txt
```

Implement:

* Calculator functions (`add`, `subtract`, `multiply`, `divide`)
* Login function
* Write assertion-based tests for every function
* Include tests for valid cases, invalid cases, and exceptions

This module builds the foundation you'll use throughout the rest of PyTest, especially when testing APIs, databases, files, and automation frameworks.

---

# Next Module (Module 3: Test Discovery)

In the next module, you'll learn:

* How PyTest automatically discovers tests
* Test naming conventions
* Organizing test files and directories
* Running a single test, file, class, or directory
* Using `-k`, `-m`, and `::` selectors
* Test collection and execution order
* Real-world project structures used in automation frameworks

# PyTest Complete Course

# Module 3 – Test Discovery (Basic → Advanced)

**Test Discovery** is one of the most important PyTest concepts because it determines **which tests PyTest finds and executes automatically**.

Understanding test discovery is essential for real-world automation frameworks, CI/CD pipelines, and interview questions.

---

# What is Test Discovery?

## Definition

**Test Discovery** is the process by which PyTest automatically searches for, identifies, and collects test files, test classes, and test functions before executing them.

You don't need to manually list your test files.

PyTest automatically discovers them based on naming conventions.

---

## Interview Definition

> **Test Discovery is PyTest's automatic mechanism for locating and collecting test files, test classes, and test functions using predefined naming conventions and directory structures.**

---

# Why Do We Need Test Discovery?

Imagine a project with:

```text
500 Test Files

2500 Test Functions

100 Developers
```

Without automatic discovery:

```text
Run test1.py

Run test2.py

Run test3.py

...

Run test500.py
```

Impossible.

PyTest automatically finds them.

---

# How PyTest Finds Tests

PyTest searches for

```
Current Directory

↓

Subdirectories

↓

Python Files

↓

Test Functions

↓

Execute Tests
```

---

# Default Naming Rules

PyTest follows specific naming conventions.

## Test File

Must start with

```text
test_
```

Example

```text
test_login.py

test_api.py

test_database.py
```

---

OR end with

```text
_test.py
```

Example

```text
login_test.py

api_test.py
```

---

## Wrong Names

```text
login.py

tests.py

api.py
```

These will **not** be discovered automatically.

---

# Test Functions

Must begin with

```python
def test_login():
```

Correct

```python
def test_add():
    pass
```

Correct

```python
def test_delete_user():
    pass
```

---

Wrong

```python
def add():
```

Wrong

```python
def login():
```

PyTest ignores them.

---

# Test Classes

Class name should start with

```python
class TestCalculator:
```

Correct

```python
class TestLogin:
```

---

Wrong

```python
class Login:
```

Not discovered automatically.

---

# Class Methods

Methods must begin with

```python
def test_add(self):
```

---

Example

```python
class TestCalculator:

    def test_add(self):
        assert 2+3==5

    def test_subtract(self):
        assert 10-5==5
```

---

# Project Structure

Example

```text
pytest-course/

│

├── app/

│      calculator.py

│

├── tests/

│      test_login.py

│      test_api.py

│      test_math.py

│

└── pytest.ini
```

PyTest automatically discovers

```
test_login.py

test_api.py

test_math.py
```

---

# Example

calculator.py

```python
def add(a,b):
    return a+b
```

---

test_calculator.py

```python
from app.calculator import add

def test_add():

    assert add(10,20)==30
```

---

Run

```bash
pytest
```

Output

```
1 Passed
```

---

# Running Tests

---

Run All Tests

```bash
pytest
```

Runs every discovered test.

---

Verbose Mode

```bash
pytest -v
```

Output

```text
tests/test_login.py

PASSED

tests/test_api.py

PASSED
```

---

Run Specific File

```bash
pytest tests/test_login.py
```

Only

```
test_login.py
```

Runs.

---

Run Specific Function

```bash
pytest tests/test_login.py::test_valid_login
```

Only

```
test_valid_login()
```

Runs.

---

Run Specific Class

```bash
pytest tests/test_login.py::TestLogin
```

Runs all methods inside

```
TestLogin
```

---

Run Specific Method

```bash
pytest tests/test_login.py::TestLogin::test_valid_login
```

Runs only one method.

---

# Real Example

Suppose

test_login.py

```python
class TestLogin:

    def test_valid():

        pass

    def test_invalid():

        pass
```

Run

```bash
pytest tests/test_login.py::TestLogin::test_valid
```

Only

```
test_valid()
```

executes.

---

# Using -k

Very important interview topic.

Search by keyword.

Suppose

```python
def test_login():
```

```python
def test_logout():
```

```python
def test_register():
```

Run only login

```bash
pytest -k login
```

Runs

```
test_login()
```

---

Run

```bash
pytest -k register
```

Runs

```
test_register()
```

---

Multiple Keywords

```bash
pytest -k "login or logout"
```

Runs

```
test_login()

test_logout()
```

---

AND

```bash
pytest -k "login and admin"
```

---

NOT

```bash
pytest -k "not api"
```

---

# Using -q

Quiet Mode

```bash
pytest -q
```

Output

```
10 Passed
```

Minimal output.

---

# Using -s

Display print()

Example

```python
def test_demo():

    print("Hello")

    assert True
```

Run

```bash
pytest -s
```

Output

```
Hello
```

Without `-s`, PyTest captures the output and does not display `print()` for passing tests.

---

# Stop After First Failure

```bash
pytest -x
```

Stops immediately after the first failed test.

---

# Maximum Failures

```bash
pytest --maxfail=2
```

Stops after

```
2 Failed Tests
```

---

# Collect Only

Interview Question

```bash
pytest --collect-only
```

Shows

```
Collected

test_login.py

test_api.py

test_payment.py
```

No tests execute.

Useful for debugging discovery.

---

# Discover Tests in Directory

```bash
pytest tests/
```

Runs every test inside

```
tests/
```

---

# Run Multiple Files

```bash
pytest tests/test_api.py tests/test_login.py
```

Runs only those files.

---

# Discovery Order

PyTest performs these steps:

```
Start

↓

Find Test Files

↓

Import Modules

↓

Find Test Classes

↓

Find Test Functions

↓

Collect Tests

↓

Execute Tests

↓

Generate Report
```

---

# Ignore Directories

Example

```text
project/

tests/

old_tests/

scripts/
```

To ignore

```
old_tests
```

you can configure it in `pytest.ini` (covered in a later module).

---

# Real Project Structure

```text
automation-framework/

│

├── src/

│     login.py

│     api.py

│

├── tests/

│     api/

│         test_user.py

│         test_product.py

│

│     ui/

│         test_login.py

│         test_cart.py

│

│     database/

│         test_mysql.py

│

├── reports/

│

├── conftest.py

│

└── pytest.ini
```

Run

```bash
pytest
```

Automatically discovers every test matching the naming rules.

---

# Example

Suppose

```
tests/

test_login.py

test_logout.py

login.py

sample.py
```

PyTest discovers

```
test_login.py

test_logout.py
```

Not

```
login.py

sample.py
```

---

# Test Collection Example

Suppose

```python
def test_one():
    pass

def test_two():
    pass

def add():
    pass
```

PyTest collects

```
test_one()

test_two()
```

Not

```
add()
```

---

# Common Mistakes

## Wrong File Name

Wrong

```text
login.py
```

Correct

```text
test_login.py
```

---

## Wrong Function Name

Wrong

```python
def login():
```

Correct

```python
def test_login():
```

---

## Wrong Class Name

Wrong

```python
class Login:
```

Correct

```python
class TestLogin:
```

---

# Best Practices

* Store all tests under a dedicated `tests/` directory.
* Use descriptive file names like `test_user_api.py` or `test_payment.py`.
* Keep one logical feature per test file.
* Give test functions meaningful names, e.g., `test_login_with_valid_credentials`.
* Avoid adding business logic inside test functions.

---

# Interview Questions

## Q1 What is Test Discovery?

**Answer**

Test Discovery is the automatic process used by PyTest to locate and collect test files, test classes, and test functions based on predefined naming conventions.

---

## Q2 How does PyTest discover tests?

PyTest discovers:

* Files starting with `test_` or ending with `_test.py`
* Classes beginning with `Test`
* Functions or methods beginning with `test_`

---

## Q3 How do you run one test?

```bash
pytest tests/test_login.py::test_valid_login
```

---

## Q4 How do you run one class?

```bash
pytest tests/test_login.py::TestLogin
```

---

## Q5 What does `pytest -k login` do?

It runs only the tests whose names match the keyword `login`.

---

## Q6 What does `pytest --collect-only` do?

It discovers and lists all tests without executing them.

---

# Practice Exercises

### Exercise 1

Create

```text
tests/

test_math.py

test_string.py

sample.py
```

Run

```bash
pytest
```

Observe which files are collected.

---

### Exercise 2

Create

```python
def test_add():
    pass

def add():
    pass
```

Run

```bash
pytest --collect-only
```

Notice that only `test_add()` is collected.

---

### Exercise 3

Run:

```bash
pytest -k add
pytest -k login
pytest -k "login or logout"
pytest -k "not api"
```

Observe which tests execute.

---

# Mini Project

```text
pytest-learning/

│

├── app/

│      calculator.py

│      login.py

│

├── tests/

│      test_calculator.py

│      test_login.py

│      test_api.py

│

└── pytest.ini
```

Tasks:

1. Create three test files following PyTest naming conventions.
2. Add multiple test functions and a test class.
3. Practice:

   * `pytest`
   * `pytest -v`
   * `pytest -q`
   * `pytest -s`
   * `pytest -k`
   * `pytest --collect-only`
   * Running a single file, class, and function.

---

# Next Module (Module 4: Fixtures)

Module 4 is one of the most important PyTest topics. You'll learn:

* What fixtures are and why they're needed
* `@pytest.fixture`
* Passing fixtures to tests
* Fixture dependencies
* `yield` fixtures for setup and teardown
* `autouse=True`
* Fixture scopes (function, class, module, package, session)
* Real-world examples with databases, APIs, Selenium, and DevOps automation

