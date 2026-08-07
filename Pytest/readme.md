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
