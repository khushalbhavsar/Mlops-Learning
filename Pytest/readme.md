# Pytest

Pytest is a widely used Python testing framework for unit, integration, API, automation, and cloud validation testing.

---

## Table of Contents

1. [What is Pytest?](#1-what-is-pytest)
2. [Pytest Architecture](#2-pytest-architecture)
3. [Pytest Project Structure](#3-pytest-project-structure)
4. [Test Discovery](#4-test-discovery)
5. [Assertions](#5-assertions)
6. [Fixtures](#6-fixtures)
7. [Fixture Scope](#7-fixture-scope)
8. [conftest.py](#8-conftestpy)
9. [Markers](#9-markers)
10. [Parameterization](#10-parameterization)
11. [pytest.ini](#11-pytestini)
12. [Complete Project Structure](#12-complete-project-structure)
13. [Important Commands](#13-important-commands)
14. [Complete Pytest Flow](#14-complete-pytest-flow)
15. [Best Practices](#15-best-practices)
16. [Most Asked Interview Questions](#16-most-asked-interview-questions)
17. [Final Revision Table](#17-final-revision-table)

---

## 1. What is Pytest?

### Definition

**Pytest** is an open-source Python testing framework used for writing and executing automated tests.

It supports:

- Unit testing
- Functional testing
- API testing
- Integration testing
- Automation testing

### Why Pytest?

Instead of manually checking outputs:

```python
if add(2, 3) == 5:
    print("PASS")
else:
    print("FAIL")
```

Use Pytest:

```python
def test_add():
    assert add(2, 3) == 5
```

Advantages:

- Easy syntax
- Automatic discovery
- Reusable setup
- Better reports
- Powerful fixtures

---

## 2. Pytest Architecture

```text
Pytest
  ↓
Test Discovery Engine
  ↓
Collect Test Files
  ↓
Load conftest.py
  ↓
Execute Fixtures
  ↓
Run Test Functions
  ↓
Assertions
  ↓
Pass / Fail Report
```

---

## 3. Pytest Project Structure

```text
project/
├── app/
│   └── calculator.py
├── tests/
│   ├── test_calculator.py
│   ├── test_login.py
│   └── test_api.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

### calculator.py

```python
def add(a, b):
    return a + b


def sub(a, b):
    return a - b
```

### test_calculator.py

```python
from app.calculator import *


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 5) == 5
```

Run:

```bash
pytest
```

---

## 4. Test Discovery

### Definition

Pytest automatically finds test files, test functions, and test classes.

### Rules

Files:

```text
test_login.py
test_api.py
test_math.py
```

Or:

```text
login_test.py
```

Functions:

```python
def test_login():
    ...


def test_add():
    ...
```

Classes:

```python
class TestLogin:
    ...
```

Example:

```text
tests/
├── test_login.py
├── test_api.py
└── math.py
```

Only `test_login.py` and `test_api.py` are executed.

Run discovery:

```bash
pytest --collect-only
```

---

## 5. Assertions

Assertions verify expected results.

### Equal

```python
assert 5 == 5
```

### Not Equal

```python
assert 5 != 10
```

### True

```python
assert True
```

### False

```python
assert not False
```

### List

```python
assert 5 in [1, 2, 3, 4, 5]
```

### Dictionary

```python
user = {"name": "Khushal"}
assert user["name"] == "Khushal"
```

### Exception

```python
import pytest


def divide(a, b):
    return a / b


def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
```

---

## 6. Fixtures

### Definition

Fixtures provide reusable setup and cleanup logic.

Instead of:

```python
def test_login():
    open_browser()
    login()
    close_browser()


def test_logout():
    open_browser()
    logout()
    close_browser()
```

Use fixture:

```python
import pytest


@pytest.fixture
def browser():
    print("Browser Started")
    yield
    print("Browser Closed")


def test_login(browser):
    print("Login")


def test_logout(browser):
    print("Logout")
```

Output:

```text
Browser Started
Login
Browser Closed
Browser Started
Logout
Browser Closed
```

### Fixture Workflow

```text
Fixture
  ↓
Setup
  ↓
Test
  ↓
Yield
  ↓
Cleanup
```

---

## 7. Fixture Scope

### Function Scope

Runs before every test.

```python
@pytest.fixture(scope="function")
```

### Class Scope

Runs once per class.

```python
@pytest.fixture(scope="class")
```

### Module Scope

Runs once per module (file).

```python
@pytest.fixture(scope="module")
```

### Session Scope

Runs once for the complete test session.

```python
@pytest.fixture(scope="session")
```

Example:

```python
import pytest


@pytest.fixture(scope="session")
def database():
    print("Database Connected")
    yield
    print("Database Closed")
```

---

## 8. conftest.py

### Definition

A special Pytest file for shared fixtures.

Project:

```text
project/
├── conftest.py
└── tests/
    ├── test_login.py
    └── test_api.py
```

`conftest.py`:

```python
import pytest


@pytest.fixture
def token():
    return "ABC123"
```

`test_api.py`:

```python
def test_api(token):
    assert token == "ABC123"
```

Fixtures are automatically available. No import required.

---

## 9. Markers

### Definition

Markers group and categorize tests.

Example:

```python
import pytest


@pytest.mark.smoke
def test_login():
    pass


@pytest.mark.regression
def test_signup():
    pass
```

Run only smoke:

```bash
pytest -m smoke
```

Run regression:

```bash
pytest -m regression
```

---

## 10. Parameterization

### Definition

Run one test multiple times with different inputs.

Without parameterization:

```python
def test_add1():
    assert 2 + 3 == 5


def test_add2():
    assert 5 + 5 == 10


def test_add3():
    assert 7 + 8 == 15
```

With parameterization:

```python
import pytest


@pytest.mark.parametrize(
    "a,b,result",
    [
        (2, 3, 5),
        (5, 5, 10),
        (7, 8, 15),
    ],
)
def test_add(a, b, result):
    assert a + b == result
```

Output:

```text
PASS
PASS
PASS
```

One function, three test cases.

---

## 11. pytest.ini

### Definition

Configuration file for Pytest defaults and test behavior.

Example:

```ini
[pytest]
addopts = -v
markers =
    smoke
    regression
    api
python_files = test_*.py
python_functions = test_*
```

Purpose:

- Register markers
- Configure default options
- Set test discovery naming rules

---

## 12. Complete Project Structure

```text
project/
├── app/
│   └── calculator.py
├── tests/
│   ├── test_calculator.py
│   ├── test_login.py
│   └── test_api.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 13. Important Commands

Run all tests:

```bash
pytest
```

Verbose:

```bash
pytest -v
```

Show print statements:

```bash
pytest -s
```

Run one file:

```bash
pytest tests/test_api.py
```

Run one function:

```bash
pytest tests/test_api.py::test_login
```

Run marker:

```bash
pytest -m smoke
```

Collect tests:

```bash
pytest --collect-only
```

HTML report:

```bash
pytest --html=report.html
```

Last failed:

```bash
pytest --lf
```

Stop after first failure:

```bash
pytest -x
```

---

## 14. Complete Pytest Flow

```text
Developer
  ↓
Write Python Code
  ↓
Write Tests
  ↓
pytest
  ↓
Test Discovery
  ↓
Load conftest.py
  ↓
Load Fixtures
  ↓
Execute Tests
  ↓
Assertions
  ↓
Pass / Fail
  ↓
Generate Report
```

---

## 15. Best Practices

- Keep tests independent.
- Use meaningful test names.
- Use fixtures instead of duplicate setup code.
- Store common fixtures in `conftest.py`.
- Register custom markers in `pytest.ini`.
- Use parameterization to reduce duplicate test cases.
- Use assertions for validation instead of `print`.
- Organize tests under a dedicated `tests/` directory.
- Generate reports for CI/CD pipelines.

---

## 16. Most Asked Interview Questions

### What is Pytest?

An open-source Python testing framework for writing and executing automated tests.

### What is Test Discovery?

Pytest automatically discovers:

- test files (`test_*.py` or `*_test.py`)
- test functions (`test_*`)
- test classes (`Test*`)

### What is a Fixture?

Reusable setup and teardown logic shared across tests.

### What is `conftest.py`?

A special file that contains shared fixtures and hooks. Fixtures defined here are automatically available to tests in the same directory hierarchy.

### What is a Marker?

A label used to categorize tests (for example: `smoke`, `regression`) and run selected groups.

### What is Parameterization?

A feature that runs the same test function multiple times with different input values.

### What is `pytest.ini`?

A configuration file used to define default options, register markers, and customize test discovery.

### What are Fixture Scopes?

- **function**: Runs before each test
- **class**: Runs once per test class
- **module**: Runs once per module
- **session**: Runs once per test session

---

## 17. Final Revision Table

| Topic | Definition | Most Important Syntax |
| --- | --- | --- |
| **Framework Structure** | Organizes tests into a maintainable project layout | `tests/`, `conftest.py`, `pytest.ini` |
| **Fixtures** | Reusable setup and cleanup code | `@pytest.fixture` |
| **Fixture Scope** | Controls how often a fixture runs | `scope="function"`, `"class"`, `"module"`, `"session"` |
| **Markers** | Categorize tests | `@pytest.mark.smoke` |
| **Parameterization** | Run one test with multiple inputs | `@pytest.mark.parametrize()` |
| **Assertions** | Validate expected outcomes | `assert actual == expected` |
| **Test Discovery** | Automatically finds test files/functions | `pytest --collect-only` |
| **conftest.py** | Stores shared fixtures and hooks | `@pytest.fixture` |
| **pytest.ini** | Global Pytest configuration | `addopts=-v`, `markers=...` |

---
