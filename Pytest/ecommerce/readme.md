These testing types are **testing strategies**, not Python language features. There isn't a direct Python syntax for "Smoke Testing" or "Regression Testing." Instead, they are implemented by organizing **Pytest test cases** using markers, assertions, fixtures, and parameterization.

Below is a practical example using an **E-Commerce application**.

---

# Project Structure

```text
ecommerce/
│
├── app.py
├── test_app.py
├── pytest.ini
└── conftest.py
```

---

# app.py

```python
def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Success"
    return "Login Failed"


def add(a, b):
    return a + b


def checkout(total):
    if total > 0:
        return "Order Placed"
    return "Order Failed"
```

---

# 1. Smoke Testing 

## Definition

Smoke Testing verifies the **critical functionalities** of the application after a new build.

### Example

```python
import pytest
from app import login, checkout

@pytest.mark.smoke
def test_login():
    assert login("admin", "admin123") == "Login Success"

@pytest.mark.smoke
def test_checkout():
    assert checkout(1000) == "Order Placed"
```

Run

```bash
pytest -m smoke
```

### What is Tested?

* Login
* Checkout
* Home Page
* Search

Only the most important features.

---

# 2. Sanity Testing 

## Definition

Sanity Testing verifies a **specific bug fix**.

### Example

Bug Fixed:

```text
Login was failing
```

Test

```python
import pytest
from app import login

@pytest.mark.sanity
def test_login_fix():
    assert login("admin", "admin123") == "Login Success"
```

Run

```bash
pytest -m sanity
```

Only the changed functionality is tested.

---

# 3. Regression Testing 

## Definition

Regression Testing ensures existing features still work after changes.

### Example

```python
import pytest
from app import *

@pytest.mark.regression
def test_login():
    assert login("admin","admin123") == "Login Success"

@pytest.mark.regression
def test_add():
    assert add(10,20) == 30

@pytest.mark.regression
def test_checkout():
    assert checkout(2000) == "Order Placed"
```

Run

```bash
pytest -m regression
```

Tests the complete application.

---

# 4. Performance Testing 

## Definition

Checks response time and application performance.

### Python Example

```python
import time

start = time.time()

# Simulate API Call
time.sleep(2)

end = time.time()

print("Execution Time:", end-start)
```

Pytest Example

```python
import time

def test_response_time():

    start = time.time()

    time.sleep(1)

    end = time.time()

    assert (end-start) < 2
```

Checks whether the response time is acceptable.

---

# 5. Stress Testing 

## Definition

Tests the application beyond its expected capacity.

### Example

```python
for i in range(100000):
    print("Request", i)
```

API Example

```python
import requests

for i in range(1000):
    response = requests.get("http://localhost:5000")
```

Purpose

```text
1000+

5000+

10000+

Concurrent Requests
```

Typically performed with tools like **JMeter**, **Locust**, or **k6**, not plain Pytest.

---

# 6. Load Testing 

## Definition

Tests the application under the expected number of users.

### Python Example

```python
import requests

for i in range(100):

    response = requests.get("http://localhost:5000")

    print(response.status_code)
```

Real-world load testing is commonly done with **Locust**:

```python
from locust import HttpUser, task

class WebsiteUser(HttpUser):

    @task
    def homepage(self):
        self.client.get("/")
```

Run

```bash
locust
```

---

# 7. Longevity (Soak) Testing 

## Definition

Runs the application continuously for hours or days to detect issues like memory leaks.

### Example

```python
import time

while True:

    print("Running Test")

    time.sleep(5)
```

API Example

```python
import requests
import time

while True:

    requests.get("http://localhost:5000")

    time.sleep(1)
```

Purpose

```text
Run for

24 Hours

48 Hours

7 Days
```

Look for:

* Memory leaks
* CPU increase
* Database connection leaks

---

# pytest.ini

```ini
[pytest]

markers =
    smoke
    sanity
    regression
```

---

# Running Commands

Run Smoke Tests

```bash
pytest -m smoke
```

Run Sanity Tests

```bash
pytest -m sanity
```

Run Regression Tests

```bash
pytest -m regression
```

Run All Tests

```bash
pytest -v
```

---

# Real CI/CD Flow

```text
Developer
      │
      ▼
GitHub
      │
      ▼
Jenkins Pipeline
      │
      ▼
Build Application
      │
      ▼
Run Smoke Tests
      │
      ▼
Run Sanity Tests (if bug fix)
      │
      ▼
Run Regression Tests
      │
      ▼
Deploy to Dev
      │
      ▼
Performance Testing
      │
      ├── Load Testing
      ├── Stress Testing
      └── Soak Testing
      │
      ▼
Deploy to Production
```

---

# Interview Summary

| Testing Type            | Purpose                       | Python/Pytest Implementation                                   |
| ----------------------- | ----------------------------- | -------------------------------------------------------------- |
| **Smoke Testing**       | Verify critical features      | `@pytest.mark.smoke`                                           |
| **Sanity Testing**      | Verify a specific bug fix     | `@pytest.mark.sanity`                                          |
| **Regression Testing**  | Verify all existing features  | `@pytest.mark.regression`                                      |
| **Performance Testing** | Measure response time         | `time.time()` assertions or dedicated performance tools        |
| **Load Testing**        | Simulate expected user load   | Prefer **Locust**, **k6**, or **JMeter**                       |
| **Stress Testing**      | Push beyond expected capacity | Prefer **Locust**, **k6**, or **JMeter** with high concurrency |
| **Soak Testing**        | Verify long-term stability    | Long-running load tests with monitoring                        |

