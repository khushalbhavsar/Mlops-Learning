# API (Application Programming Interface) — Complete Guide

API is a core concept for Python, AWS, DevOps, Cloud, Kubernetes, Web Development, and Software Engineering interviews.

---

## Table of Contents

- What is an API?
- Real-life example
- API Workflow
- Components of an API
- HTTP methods
- Request & Response structure
- HTTP status codes
- Headers
- Authentication vs Authorization
  - Token-based (Bearer/JWT)
  - Basic, API Key, OAuth
- Examples (Python, Flask)
- JWT overview
- Security best practices
- Quick reference / FAQ

---

## What is an API?

An API (Application Programming Interface) is a set of rules and protocols that allows two or more software applications to communicate and exchange data. Think of an API as a messenger between a client and a server.

> Interview definition: An API is a software interface that enables different applications, services, or systems to communicate with each other by sending requests and receiving responses using predefined rules and protocols.

---

## Real-life example

Imagine you're at a restaurant:

- Customer → Client (browser, mobile app)
- Waiter → API
- Kitchen → Server/database

The waiter takes your order, gives it to the kitchen, and returns with the food — similar to how an API forwards a request and returns a response.

---

## API Workflow (high level)

Client → Request → API → Business Logic → Database → Response → Client

---

## Components of an API

- Client: Browser, mobile app, script, Postman
- API Endpoint: URL where requests are sent (e.g., `https://api.example.com/users`)
- Request: URL, headers, parameters, body
- Server: Processes the request
- Database: Stores and returns data
- Response: Typically JSON (or XML/HTML)

---

## HTTP Methods

- GET — Retrieve data
- POST — Create a resource
- PUT — Replace a resource
- PATCH — Modify partial fields
- DELETE — Remove a resource

Examples:

```http
GET /users
POST /users
PUT /users/1
PATCH /users/1
DELETE /users/1
```

---

## HTTP Request structure (example)

```
POST /users HTTP/1.1
Host: api.example.com
Headers:
  Authorization: <token>
  Content-Type: application/json
Body:
{
  "name": "Khushal"
}
```

## HTTP Response structure (example)

```
HTTP/1.1 200 OK
Content-Type: application/json
Body:
{
  "message": "Success"
}
```

---

## Common HTTP status codes

- 200 OK — Success
- 201 Created — Resource created
- 204 No Content — Success, no body
- 400 Bad Request — Invalid request
- 401 Unauthorized — Authentication required / missing or invalid credentials
- 403 Forbidden — Authenticated but not permitted
- 404 Not Found — Resource not found
- 500 Internal Server Error — Server-side error

**Interview tip:** 401 = unauthenticated, 403 = authenticated but not authorized.

---

## Headers

Headers carry metadata such as content type and authorization tokens.

Example header lines:

```
Content-Type: application/json
Authorization: <token>
```

---

## Authentication vs Authorization

- Authentication: Verifies identity — "Who are you?"
- Authorization: Determines permissions — "What are you allowed to do?"

Authentication happens first; authorization happens after identity is confirmed.

---

## Types of Authentication

### 1) Basic Authentication

Sends username and password with each request (base64 encoded). Always require HTTPS.

Example header:

```
Authorization: Basic <base64-credentials>
```

### 2) API Key

A unique key sent in headers or query parameters.

```
x-api-key: 123456789abcdef
```

### 3) Token-based Authentication (Bearer / JWT)

After successful login, the server issues a token. The client sends this token with subsequent requests:

```
Authorization: Bearer <token>
```

(Refers to tokens such as JWTs; servers verify signature and expiry.)

### 4) OAuth 2.0

Allows a user to authorize a third-party app without sharing credentials directly (e.g., Login with Google/GitHub). OAuth issues access tokens with scopes.

---

## JWT (JSON Web Token) — overview

A JWT typically contains three parts: header, payload, and signature. It is commonly used for stateless authentication.

Typical flow:

1. User logs in with credentials.
2. Server issues a signed JWT with an expiry (`exp`).
3. Client stores the token (e.g., in memory or secure storage) and sends it in `Authorization: Bearer <token>`.
4. Server verifies the token signature and expiry for protected endpoints.

Example using PyJWT:

```bash
pip install PyJWT
```

```python
import jwt
import datetime

secret = "mysecretkey"
payload = {
    "user": "Khushal",
    "role": "admin",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}

token = jwt.encode(payload, secret, algorithm="HS256")
print(token)
```

Decode example:

```python
decoded = jwt.decode(token, secret, algorithms=["HS256"])
print(decoded)
```

---

## Examples: Python (requests)

### GET

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)
print(response.status_code)
print(response.json())
```

### POST

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python",
    "body": "API Example",
    "userId": 1
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
```

---

## Flask quick example (protected endpoint)

```python
from flask import Flask, request, jsonify
app = Flask(__name__)

TOKEN = "<token>"

@app.route("/profile")
def profile():
    token = request.headers.get("Authorization")
    if token != f"Bearer {TOKEN}":
        return jsonify({"message": "Unauthorized"}), 401
    return jsonify({"name": "Khushal"})

if __name__ == '__main__':
    app.run(debug=True)
```

Request:

```
GET /profile
Authorization: Bearer <token>
```

Response:

```json
{
  "name": "Khushal"
}
```

---

## API Design: REST reminders

- REST is stateless: each request contains all necessary authentication/state
- Use clear, resource-based URLs
- Prefer standard HTTP methods and status codes
- Use JSON for data interchange in most modern web APIs

---

## API Security Best Practices

- Always use HTTPS
- Hash and salt passwords (e.g., bcrypt)
- Use token expiration and refresh flows
- Enforce role-based access control (RBAC) or permissions
- Validate and sanitize inputs
- Implement rate limiting
- Log authentication and authorization events for audit

---

## FAQ / Quick interview pointers

- What is an API? — Interface enabling communication between systems using requests/responses.
- Why JSON? — Lightweight, human-readable, language-agnostic, easy to parse.
- PUT vs PATCH? — PUT replaces the entire resource; PATCH applies partial updates.
- 401 vs 403? — 401 means not authenticated; 403 means authenticated but not authorized.

---

## Quick Reference: Common HTTP Codes

| Code | Meaning |
| ---- | ------- |
| 200  | OK |
| 201  | Created |
| 204  | No Content |
| 400  | Bad Request |
| 401  | Unauthorized |
| 403  | Forbidden |
| 404  | Not Found |
| 500  | Internal Server Error |

---

If you'd like, the cleaned file can replace the original README.md or be further adjusted (add a table of contents with jump links, condense into a one-page cheat sheet, or perform a full professional rewrite). Tell me which of these you'd prefer next.