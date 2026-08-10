# PyTest E-Commerce Testing Framework

This project demonstrates PyTest fundamentals in one practical mini e-commerce flow:

- Fixtures and fixture scope
- Markers (smoke, regression)
- Assertions
- Parameterization
- Test discovery
- `conftest.py`
- `pytest.ini`
- HTML reports (`pytest-html`)

## Project Structure

```text
pytest-ecommerce/
├── app/
│   ├── __init__.py
│   ├── users.py
│   ├── products.py
│   ├── cart.py
│   └── orders.py
├── tests/
│   ├── __init__.py
│   ├── test_users.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_orders.py
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run Tests

```bash
pytest
```

## Common Commands

```bash
pytest -v
pytest -m smoke
pytest -m regression
pytest -k login
pytest tests/test_users.py
pytest tests/test_users.py::test_valid_login
pytest --html=reports/report.html --self-contained-html
```

HTML report path:

```text
reports/report.html
```
