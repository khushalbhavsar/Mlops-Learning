# REST API – Complete Theory Guide

---

## What is a REST API?

- **REST** = **RE**presentational **S**tate **T**ransfer
- An **architectural style** (not a protocol) for designing networked applications
- Invented by **Roy Fielding** in his 2000 PhD dissertation
- Uses **HTTP** as the communication protocol
- Data is exchanged as **JSON** (most common), XML, or plain text
- **Stateless** – each request is independent and contains all info needed
- REST APIs expose **resources** (data entities) via **endpoints** (URLs)
- Client sends a **request** → Server processes → Server sends a **response**

---

## 6 REST Constraints (Principles)

| # | Constraint | Meaning |
|---|-----------|---------|
| 1 | **Client-Server** | Client and server are separate; client handles UI, server handles data/logic |
| 2 | **Stateless** | Server does NOT store client state between requests; each request is self-contained |
| 3 | **Cacheable** | Responses must declare if they are cacheable; improves performance and scalability |
| 4 | **Uniform Interface** | Consistent URL patterns, standard HTTP methods, predictable resource naming |
| 5 | **Layered System** | Client doesn't know if it's talking to the actual server or a proxy/load-balancer |
| 6 | **Code on Demand** *(optional)* | Server can send executable code (e.g., JavaScript) to the client |

> If an API follows all 6 constraints → it is called a **RESTful** API.

---

## HTTP Methods (CRUD Mapping)

| HTTP Method | CRUD Operation | Purpose | Idempotent | Safe |
|-------------|---------------|---------|------------|------|
| **GET** | Read | Retrieve a resource or collection | ✅ Yes | ✅ Yes |
| **POST** | Create | Create a new resource | ❌ No | ❌ No |
| **PUT** | Update (Full) | Replace an entire resource | ✅ Yes | ❌ No |
| **PATCH** | Update (Partial) | Modify specific fields of a resource | ❌ No | ❌ No |
| **DELETE** | Delete | Remove a resource | ✅ Yes | ❌ No |
| **HEAD** | – | Same as GET but returns headers only (no body) | ✅ Yes | ✅ Yes |
| **OPTIONS** | – | Returns allowed HTTP methods for an endpoint | ✅ Yes | ✅ Yes |

### Key Terms

- **Idempotent** – Making the same request multiple times produces the same result (no side effects on repeat)
- **Safe** – The request does NOT modify any resource on the server (read-only)

---

## HTTP Status Codes

| Range | Category | Meaning |
|-------|----------|---------|
| **1xx** | Informational | Request received, processing continues |
| **2xx** | Success | Request was successful |
| **3xx** | Redirection | Further action needed (e.g., resource moved) |
| **4xx** | Client Error | Problem with the request from the client side |
| **5xx** | Server Error | Server failed to process a valid request |

### Most Common Codes

| Code | Name | When Used |
|------|------|-----------|
| 200 | OK | Successful GET, PUT, PATCH, DELETE |
| 201 | Created | Successful POST (resource created) |
| 204 | No Content | Successful DELETE (nothing to return) |
| 301 | Moved Permanently | Resource URL has permanently changed |
| 304 | Not Modified | Cached version is still valid |
| 400 | Bad Request | Malformed syntax, invalid input |
| 401 | Unauthorized | Authentication required or failed |
| 403 | Forbidden | Authenticated but not authorized |
| 404 | Not Found | Resource does not exist |
| 405 | Method Not Allowed | HTTP method not supported on this endpoint |
| 409 | Conflict | Conflict with current state (e.g., duplicate entry) |
| 422 | Unprocessable Entity | Valid syntax but semantic errors (validation failure) |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Generic server-side failure |
| 502 | Bad Gateway | Server received invalid response from upstream |
| 503 | Service Unavailable | Server is temporarily down (maintenance/overloaded) |

---

## Key REST Terminology

| Term | Definition |
|------|-----------|
| **Resource** | Any data entity (user, book, order) represented by a URL |
| **Endpoint** | A specific URL path (e.g., `/api/users/5`) that points to a resource |
| **Base URL** | Root address of the API (e.g., `https://api.example.com/v1`) |
| **URI** | Uniform Resource Identifier — full path identifying a resource |
| **Payload / Body** | Data sent with POST/PUT/PATCH requests (usually JSON) |
| **Query Parameter** | Key-value pairs after `?` in URL for filtering/sorting (e.g., `?page=2&limit=10`) |
| **Path Parameter** | Variable part of the URL path (e.g., `/users/{id}`) |
| **Header** | Metadata sent with request/response (content type, auth token, caching info) |
| **Response** | Data returned by the server (status code + headers + body) |
| **Collection** | A list of resources (e.g., `/users` returns all users) |
| **Singleton** | A single resource instance (e.g., `/users/42`) |

---

## JSON – The Standard Data Format

- **JSON** = JavaScript Object Notation
- Lightweight, human-readable, language-independent text format
- Supported by virtually every programming language
- Used as the request **body** (POST/PUT/PATCH) and the response **body**
- Data types: string, number, boolean, null, object (nested), array

### JSON Structure Rules

- Keys must be **double-quoted** strings
- Values can be: string, number, boolean (`true`/`false`), `null`, object `{}`, or array `[]`
- No trailing commas allowed
- No comments allowed in standard JSON

### Example Structure (Conceptual)

A typical JSON resource has key-value pairs like:
- `"id"` → integer (auto-generated)
- `"name"` → string
- `"email"` → string
- `"active"` → boolean
- `"tags"` → array of strings
- `"address"` → nested object with its own key-value pairs

---

## HTTP Headers – Important Ones

| Header | Direction | Purpose |
|--------|-----------|---------|
| `Content-Type` | Request & Response | Specifies the format of the body (`application/json`, `text/html`) |
| `Accept` | Request | Tells server what format the client expects in the response |
| `Authorization` | Request | Carries authentication credentials (API key, Bearer token, Basic auth) |
| `User-Agent` | Request | Identifies the client software making the request |
| `Cache-Control` | Response | Directives for caching (e.g., `no-cache`, `max-age=3600`) |
| `ETag` | Response | Version identifier for a resource (used for conditional requests) |
| `X-RateLimit-Limit` | Response | Maximum number of requests allowed in a time window |
| `X-RateLimit-Remaining` | Response | How many requests are left in the current window |
| `Access-Control-Allow-Origin` | Response | CORS header — which origins can access the API |
| `Location` | Response | URL of a newly created resource (returned with 201) |

---

## Query Parameters vs Path Parameters

| Feature | Path Parameter | Query Parameter |
|---------|---------------|-----------------|
| **Location** | Inside the URL path | After `?` in the URL |
| **Syntax** | `/users/{id}` → `/users/42` | `/users?role=admin&active=true` |
| **Purpose** | Identify a **specific** resource | **Filter**, **sort**, **paginate** a collection |
| **Required?** | Usually required | Usually optional |
| **Examples** | `/orders/123`, `/users/42/posts` | `?page=2&limit=20&sort=name` |

---

## REST API Design Best Practices

1. **Use nouns, not verbs** → `/users` not `/getUsers`
2. **Use plural names** → `/books` not `/book`
3. **Use kebab-case** → `/user-profiles` not `/userProfiles`
4. **Version your API** → `/api/v1/users`
5. **Use proper HTTP methods** → GET for read, POST for create, etc.
6. **Return correct status codes** → 201 for created, 404 for not found, etc.
7. **Support filtering & pagination** → `?page=1&limit=20&sort=name`
8. **Use HATEOAS links** → Include related resource URLs in the response
9. **Handle errors consistently** → Return a standard error object with `message`, `code`, `details`
10. **Use HTTPS always** → Never expose APIs over plain HTTP in production

### URL Design Examples

| Action | Method + Endpoint |
|--------|------------------|
| Get all users | `GET /api/v1/users` |
| Get user by ID | `GET /api/v1/users/42` |
| Create a user | `POST /api/v1/users` |
| Update a user (full) | `PUT /api/v1/users/42` |
| Update a user (partial) | `PATCH /api/v1/users/42` |
| Delete a user | `DELETE /api/v1/users/42` |
| Get posts by a user | `GET /api/v1/users/42/posts` |
| Search users | `GET /api/v1/users?name=John&role=admin` |

---

## Authentication Methods

| Method | How It Works | Security Level | Use Case |
|--------|-------------|----------------|----------|
| **API Key** | Client sends a unique key in header or query param (`X-API-Key: abc123`) | 🟡 Medium | Public APIs, simple internal services |
| **Basic Auth** | Username + password encoded in Base64 in the `Authorization` header | 🔴 Low | Quick prototyping; must use HTTPS |
| **Bearer Token (JWT)** | Client sends a JSON Web Token in `Authorization: Bearer <token>` header | 🟢 High | Modern web/mobile apps, microservices |
| **OAuth 2.0** | Delegated auth — user grants limited access via authorization server | 🟢 High | Third-party integrations (Google, GitHub login) |
| **Session-Based** | Server stores session state; client sends session cookie | 🟡 Medium | Traditional web apps with server-rendered pages |

### JWT (JSON Web Token) – How It Works

1. Client sends **login credentials** (username + password) to the auth endpoint
2. Server **verifies** credentials, generates a JWT containing user info + expiry
3. Server sends the JWT back to the client
4. Client stores the JWT (localStorage, cookie, or memory)
5. For every subsequent request, client sends `Authorization: Bearer <JWT>`
6. Server **decodes and verifies** the JWT on each request — no session stored

### JWT Structure (3 Parts, dot-separated)

| Part | Contains |
|------|----------|
| **Header** | Algorithm (`HS256`) and token type (`JWT`) |
| **Payload** | Claims — user ID, role, expiry (`exp`), issued at (`iat`) |
| **Signature** | HMAC of header + payload using a secret key (ensures integrity) |

### OAuth 2.0 Flow (Authorization Code Grant)

1. Client redirects user to the **Authorization Server** (e.g., Google)
2. User **logs in and grants permission**
3. Authorization Server redirects back with an **authorization code**
4. Client exchanges the code for an **access token** (server-to-server call)
5. Client uses the access token to call the **Resource Server** (API)
6. Resource Server validates token and returns data

---

## Rate Limiting

- Restricts the number of API requests a client can make in a time window
- Protects the server from abuse, DDoS, and excessive load
- Common strategies:

| Strategy | Description |
|----------|------------|
| **Fixed Window** | Count requests in fixed time slots (e.g., 100 req per minute) |
| **Sliding Window** | Rolling time window for smoother rate tracking |
| **Token Bucket** | Tokens are added at a fixed rate; each request consumes a token |
| **Leaky Bucket** | Requests are queued and processed at a constant rate |

- When limit exceeded → server returns **429 Too Many Requests**
- Response headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`

---

## CORS (Cross-Origin Resource Sharing)

- **Same-Origin Policy** blocks browser requests to a different domain by default
- **CORS** allows the server to specify which origins can access the API
- The browser sends a **preflight request** (OPTIONS) before certain cross-origin requests
- Server responds with allowed origins, methods, and headers

| CORS Header | Purpose |
|-------------|---------|
| `Access-Control-Allow-Origin` | Which origins are permitted (`*` for all) |
| `Access-Control-Allow-Methods` | Which HTTP methods are allowed |
| `Access-Control-Allow-Headers` | Which custom headers are allowed |
| `Access-Control-Max-Age` | How long the preflight response is cached |

---

## Pagination Patterns

| Pattern | How It Works | Pros | Cons |
|---------|-------------|------|------|
| **Offset-based** | `?offset=20&limit=10` | Simple, standard | Slow on large datasets; data shift issues |
| **Page-based** | `?page=3&limit=10` | Easy to understand | Same issues as offset |
| **Cursor-based** | `?cursor=abc123&limit=10` | Fast, consistent with real-time data | More complex to implement |
| **Keyset-based** | `?after_id=100&limit=10` | Efficient for sorted data | Requires a unique sortable field |

- Best practice: Include pagination metadata in the response — `total`, `page`, `per_page`, `next`, `prev`

---

## Versioning Strategies

| Strategy | Example | Pros | Cons |
|----------|---------|------|------|
| **URL Path** | `/api/v1/users` | Clear, easy to understand | URL changes with version |
| **Query Param** | `/api/users?version=1` | Flexible | Easy to miss/forget |
| **Header** | `Accept: application/vnd.api.v1+json` | Clean URLs | Hidden, harder to test |
| **Content Negotiation** | `Accept: application/json; version=1` | Standards-based | Complex |

> **Most common**: URL path versioning (`/v1/`, `/v2/`)

---

## Idempotency in Detail

| Method | Idempotent? | Explanation |
|--------|-------------|-------------|
| GET | ✅ | Reading data doesn't change anything |
| PUT | ✅ | Replacing a resource with the same data gives the same result |
| DELETE | ✅ | Deleting once or multiple times → resource is gone |
| POST | ❌ | Each POST can create a new resource (side effect) |
| PATCH | ❌ | Depends on implementation; may have side effects |

- **Why it matters**: Idempotent methods are safe to retry on network failure
- **Idempotency Key**: Some APIs accept an `Idempotency-Key` header to ensure a POST is processed only once (used in payment APIs like Stripe)

---

## Error Response Best Practices

A consistent error format helps clients handle errors predictably:

| Field | Purpose |
|-------|---------|
| `status` | HTTP status code (e.g., 404) |
| `error` | Short error type (e.g., "Not Found") |
| `message` | Human-readable explanation |
| `details` | Array of specific issues (e.g., validation errors per field) |
| `timestamp` | When the error occurred |
| `path` | The endpoint that was called |

---

## REST vs GraphQL vs gRPC vs SOAP

| Feature | REST | GraphQL | gRPC | SOAP |
|---------|------|---------|------|------|
| **Protocol** | HTTP | HTTP | HTTP/2 | HTTP/SMTP |
| **Data Format** | JSON/XML | JSON | Protobuf (binary) | XML only |
| **Contract** | Loose (OpenAPI optional) | Schema (SDL) | Strict (.proto files) | Strict (WSDL) |
| **Flexibility** | Fixed response structure | Client chooses exact fields | Fixed per RPC method | Fixed per operation |
| **Over-fetching** | Common | Solved (query what you need) | No (binary efficiency) | Common |
| **Performance** | Good | Good | Excellent (binary, streaming) | Slow (XML heavy) |
| **Learning Curve** | Low | Medium | High | High |
| **Best For** | Public APIs, CRUD apps | Complex frontend data needs | Microservices, real-time | Enterprise, legacy systems |
| **Caching** | Easy (HTTP caching) | Complex | Custom | Built-in (WS-Security) |

---

## Request / Response Flow

```
Client (Browser/App)
       │
       ▼
  ┌──────────┐
  │  REQUEST  │── Method: GET/POST/PUT/DELETE
  │           │── URL: /api/v1/resource
  │           │── Headers: Content-Type, Authorization
  │           │── Body: JSON payload (POST/PUT/PATCH)
  └──────────┘
       │
       ▼
  ┌──────────┐
  │  SERVER   │── Routes request to handler
  │           │── Validates input
  │           │── Processes business logic
  │           │── Queries database
  └──────────┘
       │
       ▼
  ┌──────────┐
  │ RESPONSE  │── Status Code: 200, 201, 404, 500...
  │           │── Headers: Content-Type, Cache-Control
  │           │── Body: JSON data or error object
  └──────────┘
       │
       ▼
Client receives & processes response
```

---

## Common Testing Tools

| Tool | Type | Best For |
|------|------|----------|
| **Postman** | GUI | Manual API testing, collections, environments |
| **Insomnia** | GUI | Lightweight alternative to Postman |
| **cURL** | CLI | Quick terminal-based testing, scripting |
| **HTTPie** | CLI | Human-friendly cURL alternative |
| **Swagger UI** | Browser | Interactive docs generated from OpenAPI spec |
| **pytest + requests** | Code | Automated API testing in Python |
| **Thunder Client** | VS Code Extension | API testing inside VS Code |

---

## HATEOAS (Hypermedia as the Engine of Application State)

- A REST constraint where the server provides **links to related resources** in every response
- The client discovers available actions through these links (no hardcoded URLs)
- Makes the API **self-describing** and **navigable**

### Example Concept

A response for a user resource would include links like:
- `self` → URL to this user
- `posts` → URL to this user's posts
- `update` → URL to update this user
- `delete` → URL to delete this user

> Most real-world APIs skip HATEOAS due to complexity. It's a mature REST practice.

---

## Content Negotiation

- The process of selecting the best representation of a resource based on client preferences
- Client uses the `Accept` header to specify desired format
- Server uses `Content-Type` header to indicate the format of the response

| Accept Header | Format |
|---------------|--------|
| `application/json` | JSON |
| `application/xml` | XML |
| `text/html` | HTML |
| `text/csv` | CSV |

---

## Webhooks vs REST API Polling

| Feature | REST Polling | Webhooks |
|---------|-------------|----------|
| **Direction** | Client → Server (repeated) | Server → Client (push) |
| **Efficiency** | Low (constant requests) | High (only on events) |
| **Real-time** | Near real-time (depends on interval) | Real-time |
| **Complexity** | Simple client, heavy server load | Requires client endpoint to receive |
| **Use Case** | Checking order status periodically | Payment confirmation, GitHub event notifications |

---

## Code Files Reference

> All executable code examples are in separate Python files:

| File | Topic |
|------|-------|
| → `01_flask_crud_api.py` | Building a full CRUD REST API with Flask |
| → `02_api_client.py` | Consuming APIs with the `requests` library |
| → `03_fastapi_crud.py` | FastAPI CRUD with Pydantic models & auto-docs |
| → `04_auth_examples.py` | API Key, JWT Bearer Token, Basic Auth examples |
| → `05_error_handling_and_patterns.py` | Error handling, retry, sessions, pagination |

---

## Summary Table

| Topic | Key Point |
|-------|-----------|
| REST | Architectural style using HTTP for stateless client-server communication |
| HTTP Methods | GET (read), POST (create), PUT (replace), PATCH (modify), DELETE (remove) |
| Status Codes | 2xx = success, 4xx = client error, 5xx = server error |
| JSON | Standard data format — lightweight, human-readable, key-value pairs |
| Headers | Metadata for requests/responses (Content-Type, Authorization, Cache-Control) |
| Authentication | API Key, Basic Auth, Bearer Token (JWT), OAuth 2.0 |
| Rate Limiting | Controls request volume per client to protect server |
| CORS | Allows cross-origin browser requests via server headers |
| Pagination | Offset, page, cursor, or keyset-based for large datasets |
| Versioning | URL path (`/v1/`) is the most common strategy |
| Idempotency | GET, PUT, DELETE are idempotent; POST is not |
| Error Handling | Consistent error objects with status, message, details |
| HATEOAS | Server provides hyperlinks to related resources in responses |
| REST vs Others | REST (simple), GraphQL (flexible), gRPC (fast), SOAP (enterprise) |
| Testing | Postman, cURL, Swagger UI, pytest, Thunder Client |

---
