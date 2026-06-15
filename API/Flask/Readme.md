# Flask – Complete Theory Guide

> All code examples are in separate `.py` files in this folder. This file covers **theory only**.

---

## What is Flask?

**Flask** is a lightweight **micro web framework** for Python. It is called "micro" because it keeps the core simple but is **extensible** — you add only the libraries you need.

- Created by **Armin Ronacher** in 2010.
- Built on top of **Werkzeug** (WSGI toolkit) and **Jinja2** (template engine).
- It does **NOT** come with a database layer, form validation, or authentication built-in — you pick and plug what you need.
- Used by companies like **Netflix, Reddit, Airbnb, Uber, LinkedIn**.

> **Analogy:** Flask is like an empty kitchen — it gives you the stove and sink (routing, request/response), but you bring your own ingredients (database, auth, etc.).

---

## Flask vs Django (Quick Comparison)

| Feature | Flask | Django |
|---------|-------|--------|
| **Type** | Micro framework | Full-stack framework |
| **Philosophy** | Minimalist, flexible | Batteries included |
| **ORM** | No built-in (use SQLAlchemy) | Built-in Django ORM |
| **Admin Panel** | No (use Flask-Admin) | Built-in |
| **Learning Curve** | Easy | Moderate |
| **Template Engine** | Jinja2 | Django Templates |
| **Best For** | APIs, microservices, small-medium apps | Large apps, CMS, e-commerce |
| **Flexibility** | Very high | Opinionated |
| **REST API** | Flask-RESTful / manual | Django REST Framework |

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **WSGI** | Web Server Gateway Interface — Python standard for web servers to communicate with web applications |
| **Routing** | Mapping URLs to Python functions |
| **View Function** | A Python function that handles a request and returns a response |
| **Template** | HTML file with placeholders filled by Jinja2 |
| **Blueprint** | A way to organize a Flask app into modular components |
| **Context** | Application context and request context that Flask manages |
| **Decorator** | `@app.route()` — used to bind a URL to a function |

---

## Installation

```bash
pip install flask
```

---

## Flask Project Structure

```
my_flask_app/
├── app.py              # Main application file
├── requirements.txt    # Dependencies
├── static/             # CSS, JS, images
├── templates/          # HTML templates (Jinja2)
├── blueprints/         # Modular route groups
└── models/             # Database models
```

---

## Code Files in This Folder

| File | Topic | What It Covers |
|------|-------|---------------|
| `01_hello_world.py` | Hello World | Simplest Flask app, `Flask(__name__)`, `@app.route`, `app.run()` |
| `02_routing.py` | Routing | Static routes, dynamic routes, path parameters, type converters, trailing slashes |
| `03_http_methods.py` | HTTP Methods | GET, POST, PUT, DELETE, full CRUD API |
| `04_request_object.py` | Request Object | Query params, form data, JSON body, headers, cookies |
| `05_response_object.py` | Response Object | jsonify, make_response, cookies, redirects, status codes |
| `06_templates.py` | Jinja2 Templates | render_template, variables, inheritance, loops, conditionals |
| `07_error_handling.py` | Error Handling | Custom 404/400/500 handlers, abort(), exception handler |
| `08_blueprints/` | Blueprints | Modular app with auth + api blueprints (3 files) |
| `09_middleware.py` | Middleware | before_request, after_request, teardown_request, flask.g |
| `10_configuration.py` | Configuration | 4 config methods, config classes, environment variables |
| `11_database_crud.py` | Database (SQLAlchemy) | Full CRUD with SQLite, model definition, ORM queries |
| `12_file_upload.py` | File Upload | Secure upload, file validation, size limits |
| `13_sessions_cookies.py` | Sessions & Cookies | Login/logout with session, secret_key |
| `14_cors.py` | CORS | Cross-origin setup with flask-cors |
| `15_testing.py` | Testing | pytest fixtures, test client, status code assertions |
| `templates/` | HTML Templates | base.html, index.html, users.html (used by 06_templates.py) |

---

## 1. Hello World

- `Flask(__name__)` creates the app. `__name__` tells Flask where to find templates and static files.
- `@app.route("/")` is a **decorator** that maps a URL to a function.
- `app.run(debug=True)` starts the dev server with **auto-reload** on code changes.
- Default: runs at `http://127.0.0.1:5000`

→ **Code:** `01_hello_world.py`

---

## 2. Routing – URL Mapping

Routing connects URLs to Python functions (called **view functions**).

### URL Type Converters

| Converter | Example | Matches |
|-----------|---------|---------|
| `string` (default) | `<username>` | Any text without slashes |
| `int` | `<int:id>` | Positive integers |
| `float` | `<float:price>` | Floating point values |
| `path` | `<path:subpath>` | Like string but allows slashes |
| `uuid` | `<uuid:code>` | UUID strings |

### Key Rules
- **Trailing slash** `/projects/` → both `/projects` and `/projects/` work (Flask redirects).
- **No trailing slash** `/about` → only `/about` works, `/about/` gives 404.
- Multiple decorators can map to the same function.

→ **Code:** `02_routing.py`

---

## 3. HTTP Methods

| Method | Purpose | CRUD |
|--------|---------|------|
| `GET` | Retrieve data | Read |
| `POST` | Send new data | Create |
| `PUT` | Replace entire resource | Update (full) |
| `PATCH` | Modify part of resource | Update (partial) |
| `DELETE` | Remove resource | Delete |

- Use `methods=["GET", "POST"]` in `@app.route()` to allow specific methods.
- `request.method` tells you which method was used.

→ **Code:** `03_http_methods.py`

---

## 4. Request Object – Accessing Incoming Data

| Source | Access | Example |
|--------|--------|---------|
| Query Params | `request.args.get("key")` | `/search?q=flask` |
| Form Data | `request.form.get("key")` | HTML `<form>` POST |
| JSON Body | `request.get_json()` | API POST with JSON |
| URL Params | Function argument | `/user/<name>` |
| Headers | `request.headers.get("key")` | `Authorization: Bearer ...` |
| Cookies | `request.cookies.get("key")` | Session cookies |
| Files | `request.files["key"]` | File upload |

### Other Useful Attributes
- `request.method` → GET, POST, etc.
- `request.url` → Full URL
- `request.path` → Just the path portion
- `request.host` → Server address
- `request.remote_addr` → Client IP

→ **Code:** `04_request_object.py`

---

## 5. Response Object – Sending Data Back

### Ways to Return Responses
- **String** → `return "Hello"`
- **JSON** → `return jsonify({"key": "value"}), 200`
- **Custom** → `make_response()` with custom headers
- **Redirect** → `redirect(url_for("function_name"))`
- **Tuple** → `return data, status_code, headers`

### HTTP Status Codes

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful GET/PUT/PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 301 | Moved Permanently | URL changed forever |
| 302 | Found (Redirect) | Temporary redirect |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | No permission |
| 404 | Not Found | Resource doesn't exist |
| 500 | Internal Server Error | Server bug |

→ **Code:** `05_response_object.py`

---

## 6. Templates (Jinja2) – Rendering HTML

Templates let you generate dynamic HTML pages.

### Jinja2 Syntax

| Syntax | Purpose | Example |
|--------|---------|---------|
| `{{ }}` | Output a variable | `{{ name }}` |
| `{% %}` | Logic (if, for, block) | `{% if logged_in %}` |
| `{# #}` | Comment | `{# This is a comment #}` |
| `{{ x\|filter }}` | Filter (transform) | `{{ name\|capitalize }}` |
| `{% extends %}` | Template inheritance | `{% extends "base.html" %}` |
| `{% block %}` | Replaceable block | `{% block content %}{% endblock %}` |
| `{% include %}` | Include another template | `{% include "header.html" %}` |

### Common Filters

| Filter | Output |
|--------|--------|
| `upper` | HELLO |
| `lower` | hello |
| `capitalize` | Hello |
| `length` | 3 (list length) |
| `default("Guest")` | Guest (if empty) |
| `join(", ")` | "a, b, c" |
| `safe` | Renders raw HTML |

→ **Code:** `06_templates.py` + `templates/` folder

---

## 7. Error Handling

- `@app.errorhandler(404)` → Custom handler for specific status codes.
- `abort(404)` → Manually trigger an error from any route.
- `@app.errorhandler(Exception)` → Catch-all for unhandled exceptions.
- Always return JSON for APIs, HTML for web apps.

→ **Code:** `07_error_handling.py`

---

## 8. Blueprints – Organizing Large Apps

Blueprints split a Flask app into **modular components**, each with its own routes.

- `Blueprint("name", __name__, url_prefix="/prefix")` → creates a blueprint.
- `app.register_blueprint(bp)` → registers it in the main app.
- Each blueprint can have its own templates, static files, and error handlers.
- Essential for apps with 10+ routes.

→ **Code:** `08_blueprints/` folder (app.py, auth_routes.py, api_routes.py)

---

## 9. Middleware – Before & After Requests

| Hook | When It Runs | Must Return |
|------|-------------|-------------|
| `@app.before_request` | Before every request | Nothing (or response to short-circuit) |
| `@app.after_request` | After every request | The response object |
| `@app.teardown_request` | After request, even on error | Nothing |

- Use `flask.g` to store per-request data (e.g., start time, current user).
- Common uses: logging, timing, authentication checks, adding headers.

→ **Code:** `09_middleware.py`

---

## 10. Flask Configuration

### 4 Methods to Configure

| Method | Description |
|--------|-------------|
| Direct | `app.config["DEBUG"] = True` |
| Dictionary | `app.config.update(TESTING=True)` |
| Environment | `os.environ.get("SECRET_KEY")` |
| Config Class | `app.config.from_object(DevConfig)` |

### Important Config Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DEBUG` | False | Auto-reload + debugger |
| `TESTING` | False | Testing mode |
| `SECRET_KEY` | None | Required for sessions/CSRF |
| `MAX_CONTENT_LENGTH` | None | Max upload size in bytes |
| `JSON_SORT_KEYS` | True | Sort JSON output keys |

→ **Code:** `10_configuration.py`

---

## 11. Database Integration (Flask-SQLAlchemy)

- **ORM** (Object-Relational Mapping) → Python classes represent database tables.
- `db.Model` → base class for all models.
- `db.Column(type, ...)` → defines a column.
- `db.session.add()` / `.commit()` / `.delete()` → CRUD operations.
- `Model.query.all()` → get all records.
- `db.session.get(Model, id)` → get by primary key.

### Column Types
| Type | Python | SQL |
|------|--------|-----|
| `db.Integer` | int | INTEGER |
| `db.String(n)` | str | VARCHAR(n) |
| `db.Float` | float | FLOAT |
| `db.Boolean` | bool | BOOLEAN |
| `db.DateTime` | datetime | DATETIME |
| `db.Text` | str | TEXT |

→ **Code:** `11_database_crud.py`

---

## 12. File Upload

- Use `request.files["key"]` to access uploaded files.
- `secure_filename()` from Werkzeug prevents malicious filenames.
- `MAX_CONTENT_LENGTH` limits file size (returns 413 if exceeded).
- Always **validate file extensions** before saving.

→ **Code:** `12_file_upload.py`

---

## 13. Sessions & Cookies

- Flask sessions use **signed cookies** (stored client-side, signed with SECRET_KEY).
- `session["key"] = value` → set session data.
- `session.get("key")` → read session data.
- `session.clear()` → destroy session (logout).
- `SECRET_KEY` is **required** for sessions to work.

→ **Code:** `13_sessions_cookies.py`

---

## 14. CORS (Cross-Origin Resource Sharing)

- CORS errors happen when frontend (e.g., React on `localhost:3000`) calls backend (Flask on `localhost:5000`).
- `flask-cors` extension solves this.
- `CORS(app)` → allow all origins (dev only).
- `CORS(app, origins=["https://mysite.com"])` → restrict in production.

→ **Code:** `14_cors.py`

---

## 15. Popular Flask Extensions

| Extension | Purpose |
|-----------|---------|
| **Flask-SQLAlchemy** | Database ORM |
| **Flask-Migrate** | DB migrations (Alembic) |
| **Flask-CORS** | Cross-origin requests |
| **Flask-JWT-Extended** | JWT authentication |
| **Flask-Login** | User session management |
| **Flask-WTF** | Form validation & CSRF |
| **Flask-Mail** | Email sending |
| **Flask-RESTful** | REST API building |
| **Flask-Caching** | Response caching |
| **Flask-Limiter** | Rate limiting |
| **Flask-Admin** | Admin dashboard |
| **Flask-SocketIO** | WebSocket support |

---

## 16. Deployment

| Item | Development | Production |
|------|------------|------------|
| **Server** | `app.run()` | Gunicorn / Waitress |
| **Debug** | `True` | **`False`** |
| **Secret Key** | Hard-coded | Environment variable |
| **Database** | SQLite | PostgreSQL / MySQL |
| **HTTPS** | No | Yes (Nginx + SSL) |
| **Error Pages** | Stack trace | Custom error pages |
| **Logging** | Console | File / monitoring |

> **Never use `app.run(debug=True)` in production!** Use Gunicorn (Linux) or Waitress (Windows).

---

## 17. Flask CLI Commands

| Command | Description |
|---------|-------------|
| `flask run` | Start the development server |
| `flask run --debug` | Start with debug mode |
| `flask run --host=0.0.0.0 --port=8080` | Custom host/port |
| `flask shell` | Interactive Python shell with app context |
| `flask routes` | Show all registered routes |

---

## 18. Testing

- `app.test_client()` creates a fake client (no real server needed).
- Call `client.get("/")`, `client.post("/api", json={...})` etc.
- Assert on `response.status_code` and `response.get_json()`.
- Use `@pytest.fixture` to set up and tear down test state.

→ **Code:** `15_testing.py`

---

## Summary

| Topic | Key Takeaway |
|-------|-------------|
| **Flask** | Lightweight micro web framework for Python |
| **Routing** | `@app.route("/path")` maps URLs to functions |
| **Methods** | GET (read), POST (create), PUT (update), DELETE (remove) |
| **Request** | `request.args`, `request.form`, `request.get_json()`, `request.headers` |
| **Response** | `jsonify()`, `make_response()`, `redirect()`, status codes |
| **Templates** | Jinja2 with `{{ var }}`, `{% logic %}`, inheritance |
| **Blueprints** | Modular app organization for larger projects |
| **Middleware** | `@app.before_request`, `@app.after_request` |
| **Database** | Flask-SQLAlchemy for ORM-based DB operations |
| **Auth** | Sessions, JWT tokens, API keys |
| **Deployment** | Use Gunicorn/Waitress, never `debug=True` in production |
| **Testing** | `app.test_client()` with pytest |

---

> **Next Steps:** Build a full project combining Flask + SQLAlchemy + JWT Auth + Blueprints, then deploy it with Gunicorn behind Nginx.
