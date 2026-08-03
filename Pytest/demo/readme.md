# How to Write Pytest (Step-by-Step)

Pytest follows a simple pattern:

```text
1. Import pytest
        ↓
2. Write function to test
        ↓
3. Create test function (starts with test_)
        ↓
4. Use assert
        ↓
5. Run pytest
```

---

# Step 1. Install Pytest

```bash
pip install pytest
```

Check Version

```bash
pytest --version
```

---

# Step 2. Create Project Structure

```text
pytest-demo/
│
├── calculator.py
├── test_calculator.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

# Step 3. Write Application Code

## calculator.py

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b
```

---

# Step 4. Create Test File

**Rule:** Test file name should start with `test_`.

## test_calculator.py

```python
from calculator import add

def test_add():
    assert add(10, 20) == 30
```

---

# Step 5. Run Test

```bash
pytest
```

Output

```text
============================
1 passed
============================
```

---

# Step 6. Multiple Test Cases

```python
from calculator import *

def test_add():
    assert add(5, 5) == 10

def test_subtract():
    assert subtract(20, 10) == 10

def test_multiply():
    assert multiply(2, 5) == 10

def test_divide():
    assert divide(20, 2) == 10
```

Run

```bash
pytest -v
```

Output

```text
test_add PASSED

test_subtract PASSED

test_multiply PASSED

test_divide PASSED
```

---

# Step 7. Assertions

```python
def test_number():

    assert 5 == 5


def test_string():

    assert "AWS" == "AWS"


def test_list():

    assert [1,2] == [1,2]


def test_boolean():

    assert True
```

---

# Step 8. Fixtures

```python
import pytest

@pytest.fixture
def username():
    return "Khushal"

def test_name(username):
    assert username == "Khushal"
```

Run

```bash
pytest -v
```

---

# Step 9. Parameterization

Instead of writing

```python
def test_add1():
    assert add(1,2)==3

def test_add2():
    assert add(2,3)==5

def test_add3():
    assert add(10,20)==30
```

Write

```python
import pytest

from calculator import add

@pytest.mark.parametrize(
    "a,b,result",
    [
        (1,2,3),
        (2,3,5),
        (10,20,30)
    ]
)

def test_add(a,b,result):

    assert add(a,b)==result
```

Output

```text
PASSED

PASSED

PASSED
```

---

# Step 10. Markers

```python
import pytest

@pytest.mark.smoke
def test_login():
    assert True

@pytest.mark.regression
def test_signup():
    assert True
```

Run Smoke

```bash
pytest -m smoke
```

Run Regression

```bash
pytest -m regression
```

---

# Step 11. conftest.py

Create

```python
import pytest

@pytest.fixture
def setup():

    print("Database Connected")

    return "Connected"
```

Use

```python
def test_db(setup):

    assert setup=="Connected"
```

No need to import the fixture.

---

# Step 12. pytest.ini

```ini
[pytest]

addopts = -v

markers =
    smoke
    regression
```

---

# Step 13. Fixture Scope

```python
import pytest

@pytest.fixture(scope="session")
def database():

    print("Database Connected")

    return "DB"
```

Other scopes

```python
scope="function"

scope="class"

scope="module"

scope="package"

scope="session"
```

---

# Step 14. Exception Testing

```python
import pytest

def divide(a,b):
    return a/b

def test_divide():

    with pytest.raises(ZeroDivisionError):
        divide(10,0)
```

---

# Step 15. API Testing

```python
import requests

def test_get_api():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status_code == 200
```

---

# Step 16. Run Specific Tests

Run all

```bash
pytest
```

Verbose

```bash
pytest -v
```

Specific file

```bash
pytest test_calculator.py
```

Specific function

```bash
pytest test_calculator.py::test_add
```

Stop on first failure

```bash
pytest -x
```

Show print statements

```bash
pytest -s
```

Generate HTML report

```bash
pytest --html=report.html
```

---

# Complete Project Structure

```text
pytest-demo/
│
├── calculator.py
│
├── test_calculator.py
│
├── conftest.py
│
├── pytest.ini
│
├── requirements.txt
│
└── reports/
```

---

# Complete Flow

```text
Write Python Code
        │
        ▼
calculator.py
        │
        ▼
Write Test Cases
(test_calculator.py)
        │
        ▼
Run pytest
        │
        ▼
Assertions
        │
        ▼
PASS / FAIL
        │
        ▼
Generate Report
        │
        ▼
CI/CD (Jenkins)
```

---

# Pytest Syntax Cheat Sheet

| Feature          | Syntax                           |
| ---------------- | -------------------------------- |
| Import           | `import pytest`                  |
| Test Function    | `def test_add():`                |
| Assertion        | `assert actual == expected`      |
| Fixture          | `@pytest.fixture`                |
| Marker           | `@pytest.mark.smoke`             |
| Parameterization | `@pytest.mark.parametrize()`     |
| Exception        | `with pytest.raises()`           |
| Run All Tests    | `pytest`                         |
| Verbose Mode     | `pytest -v`                      |
| Run One File     | `pytest test_file.py`            |
| Run One Test     | `pytest test_file.py::test_name` |
| Stop on Failure  | `pytest -x`                      |
| Show Prints      | `pytest -s`                      |


