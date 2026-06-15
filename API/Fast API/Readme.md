# FastAPI – Theory & Quick Reference Guide

> Full code examples for each topic are in the corresponding `.py` files in this folder.

---

## What is FastAPI?

- A **modern, high-performance** Python web framework for building APIs
- Built on top of **Starlette** (for web handling) and **Pydantic** (for data validation)
- Created by **Sebastián Ramírez** in 2018
- Uses **Python type hints** to auto-validate, serialize, and document APIs
- Supports **async/await** natively — ideal for high-concurrency workloads
- Automatically generates **Swagger UI** (`/docs`) and **ReDoc** (`/redoc`) documentation
- One of the **fastest** Python frameworks — on par with Node.js and Go

---

## Why FastAPI over Flask/Django?

| Feature | FastAPI | Flask | Django REST |
|---------|---------|-------|-------------|
| **Speed** | ⚡ Very fast (async, Uvicorn) | Moderate (sync) | Moderate (sync) |
| **Type Hints** | ✅ Built-in, required | ❌ Optional | ❌ Optional |
| **Auto Docs** | ✅ Swagger + ReDoc free | ❌ Needs extensions | ❌ Needs DRF + config |
| **Data Validation** | ✅ Pydantic (automatic) | ❌ Manual / WTForms | ✅ Serializers (manual setup) |
| **Async Support** | ✅ Native | ❌ Limited (Flask 2.0+) | ❌ Limited (Django 4.1+) |
| **Learning Curve** | Low-Medium | Low | High |
| **Best For** | APIs, microservices | Small apps, prototypes | Full-stack, admin panels |

---

## Installation

```bash
pip install fastapi uvicorn
pip install python-multipart python-jose[cryptography] passlib[bcrypt] sqlalchemy httpx pydantic[email] pydantic-settings
```

---

## 1. Hello World – Minimal App
📄 **Code:** `01_hello_world.py`

Create a FastAPI instance and define a route with a decorator. Run with Uvicorn.

```python
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
```

- `uvicorn main:app --reload` → starts the dev server
- `/docs` → Swagger UI | `/redoc` → ReDoc documentation

---

## 2. Path Parameters
📄 **Code:** `02_path_parameters.py`

Path parameters are part of the URL and identify specific resources. FastAPI auto-validates the type.

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

- `{user_id}` is extracted automatically and validated as `int`
- **Order matters**: fixed paths (`/users/me`) must come before dynamic paths (`/users/{id}`)
- Use `Enum` to restrict path values to a specific set

---

## 3. Query Parameters
📄 **Code:** `03_query_parameters.py`

Query parameters come after `?` in the URL. Any function parameter NOT in the path becomes a query parameter.

```python
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

- **Default value** → optional (`skip=0`)
- **No default** → required (returns 422 if missing)
- **`Optional[str] = None`** → explicitly optional

---

## 4. Request Body (Pydantic Models)
📄 **Code:** `04_request_body.py`

Pydantic models define the shape of request/response data with automatic validation.

```python
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=0, le=150)
```

| Feature | Description |
|---------|------------|
| `Field(...)` | Required field |
| `min_length`, `max_length` | String constraints |
| `ge`, `le`, `gt`, `lt` | Numeric range constraints |
| `model_dump()` | Model → dictionary |
| `from_attributes = True` | Read from ORM objects |

---

## 5. CRUD API – Complete Example
📄 **Code:** `05_crud_api.py`

A full Book API with Create, Read (all + one), Update (PATCH), and Delete operations using in-memory storage.

```python
@app.post("/books", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate): ...

@app.get("/books", response_model=list[BookResponse])
def get_books(genre: Optional[str] = None, skip: int = 0, limit: int = 10): ...

@app.patch("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate): ...

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int): ...
```

---

## 6. Response Model & Status Codes
📄 **Code:** `06_response_status.py`

`response_model` controls what fields are included in the response — useful for hiding sensitive data like passwords.

```python
@app.get("/users/{user_id}", response_model=UserPublic)
def get_user(user_id: int):
    return users_db[user_id]  # hashed_password is stripped from output
```

| Code | Constant | Use |
|------|----------|-----|
| 200 | `HTTP_200_OK` | Successful GET/PUT/PATCH |
| 201 | `HTTP_201_CREATED` | Successful POST |
| 204 | `HTTP_204_NO_CONTENT` | Successful DELETE |
| 404 | `HTTP_404_NOT_FOUND` | Resource not found |
| 422 | `HTTP_422_UNPROCESSABLE_ENTITY` | Validation error |

---

## 7. HTTPException – Error Handling
📄 **Code:** `07_error_handling.py`

Raise `HTTPException` to return error responses. You can also create custom exception classes with dedicated handlers.

```python
raise HTTPException(status_code=404, detail="Item not found")
```

Custom exception handlers return `JSONResponse` with structured error payloads.

---

## 8. Dependency Injection
📄 **Code:** `08_dependency_injection.py`

Dependencies are reusable functions that FastAPI auto-calls before endpoints. Common for DB sessions, auth, pagination.

```python
def get_db():
    db = SessionLocal()
    try:
        yield db        # provide to endpoint
    finally:
        db.close()      # cleanup after request

@app.get("/users")
def get_users(db: Session = Depends(get_db)): ...
```

| Feature | Description |
|---------|------------|
| `Depends()` | Declares a dependency |
| `yield` | Setup + cleanup pattern |
| Class-based | Use `Depends()` with a class for structured params |
| Global | `app = FastAPI(dependencies=[Depends(...)])` |

---

## 9. Async / Await
📄 **Code:** `09_async_await.py`

FastAPI supports both sync (`def`) and async (`async def`) endpoints natively.

| Scenario | Use |
|----------|-----|
| CPU-bound (calculations) | `def` (sync) |
| I/O-bound (HTTP, DB, files) | `async def` |
| Using async libraries (httpx, asyncpg) | `async def` |

> **Rule**: If you `await` inside the function → use `async def`. Otherwise → `def`.

---

## 10. Middleware
📄 **Code:** `10_middleware.py`

Middleware runs **before every request** and **after every response**. Common uses: CORS, logging, timing, auth.

```python
@app.middleware("http")
async def add_process_time_header(request, call_next):
    start = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.time() - start)
    return response
```

CORS middleware is added via `app.add_middleware(CORSMiddleware, ...)`.

---

## 11. Authentication – JWT Bearer Token
📄 **Code:** `11_jwt_auth.py`

JWT auth flow: client sends credentials → server returns token → client sends token in `Authorization` header.

**Auth Flow:**
1. `POST /token` with username + password
2. Server returns `{"access_token": "...", "token_type": "bearer"}`
3. Client sends `Authorization: Bearer <token>` on subsequent requests
4. `Depends(get_current_user)` validates the token on protected routes

**Key packages:** `python-jose` (JWT), `passlib` (password hashing), `OAuth2PasswordBearer` (token extraction)

---

## 12. File Upload
📄 **Code:** `12_file_upload.py`

Use `UploadFile` for file handling. Requires `python-multipart`.

```python
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}
```

Properties: `filename`, `content_type`, `read()`, `seek(0)`, `file`

---

## 13. Form Data
📄 **Code:** `13_form_data.py`

Use `Form(...)` for HTML form submissions. Sends `application/x-www-form-urlencoded`. Requires `python-multipart`.

```python
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)): ...
```

---

## 14. Headers & Cookies
📄 **Code:** `14_headers_cookies.py`

Read headers with `Header()`, read cookies with `Cookie()`, set cookies via `Response`.

```python
@app.get("/headers")
def read_headers(user_agent: str = Header(None)): ...

@app.get("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(key="session_id", value="abc123", httponly=True)
```

---

## 15. Background Tasks
📄 **Code:** `15_background_tasks.py`

Run tasks **after** the response is sent — useful for emails, logging, cleanup.

```python
@app.post("/register")
def register(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, "Welcome!")
    return {"message": "User registered"}
```

---

## 16. APIRouter – Organizing Routes
📄 **Code:** `16_api_router/` (folder with `main.py`, `routes/users.py`, `routes/items.py`)

Split your app into multiple files using `APIRouter` for better organization.

```python
router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users(): ...
```

Then in main: `app.include_router(users_router)`

| Feature | Description |
|---------|------------|
| `prefix` | URL prefix for all routes |
| `tags` | Group in Swagger UI |
| `dependencies` | Apply to all routes in router |

---

## 17. SQLAlchemy + FastAPI (Database)
📄 **Code:** `17_database/` (folder with `database.py`, `models.py`, `schemas.py`, `main.py`)

Standard pattern: SQLAlchemy engine/session setup → ORM models → Pydantic schemas → `Depends(get_db)` in endpoints.

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=UserOut, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)): ...
```

---

## 18. Testing with pytest
📄 **Code:** `18_testing.py`

Use `TestClient` from FastAPI with pytest. It wraps `httpx` for sync test calls.

```python
client = TestClient(app)

def test_create_book():
    response = client.post("/books", json={"title": "Guide", "author": "A", "year": 2024})
    assert response.status_code == 201
```

Run: `pytest 18_testing.py -v`

---

## 19. WebSockets
📄 **Code:** `19_websockets.py`

Real-time bi-directional communication. Accept connection, then loop receiving/sending messages.

```python
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_text()
    await websocket.send_text(f"Echo: {data}")
```

---

## 20. Startup & Shutdown Events (Lifespan)
📄 **Code:** `20_lifespan.py`

Use `asynccontextmanager` to define startup/shutdown logic (DB init, cache warmup, ML model loading).

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")   # Before yield = startup
    yield
    print("Shutting down...")  # After yield = shutdown

app = FastAPI(lifespan=lifespan)
```

---

## 21. Environment Variables & Settings
📄 **Code:** `21_settings.py`

Use `pydantic-settings` to load config from `.env` files with type validation.

```python
class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    class Config:
        env_file = ".env"
```

---

## 22. Pydantic Validators
📄 **Code:** `22_pydantic_validators.py`

Use `@field_validator` for single-field validation and `@model_validator` for cross-field validation.

```python
@field_validator("name")
@classmethod
def name_must_not_be_empty(cls, v):
    if not v.strip():
        raise ValueError("Name cannot be empty")
    return v.strip()

@model_validator(mode="after")
def passwords_must_match(self): ...
```

---

## FastAPI Project Structure (Best Practice)

```
my_api/
├── main.py              # FastAPI app + lifespan
├── config.py            # Settings / environment variables
├── database.py          # SQLAlchemy engine, session, base
├── models/              # SQLAlchemy ORM models
├── schemas/             # Pydantic request/response models
├── routes/              # APIRouter files
├── services/            # Business logic layer
├── dependencies/        # Reusable Depends() functions
├── middleware/           # Custom middleware
├── tests/               # pytest test files
├── .env                 # Environment variables
└── requirements.txt
```

---

## Key Decorators & Parameters

| Decorator / Parameter | Purpose |
|-----------------------|---------|
| `@app.get/post/put/patch/delete` | HTTP method handlers |
| `response_model=` | Filter response to match a Pydantic model |
| `status_code=` | Set the HTTP status code |
| `tags=["name"]` | Group endpoint in Swagger UI |
| `summary="..."` | Short description in Swagger |
| `deprecated=True` | Mark as deprecated in docs |

---

## Summary Table

| Topic | Key Point |
|-------|-----------|
| FastAPI | Modern Python framework — fast, type-safe, auto-documented |
| Pydantic | Data validation via type hints and models |
| Path Params | `{param}` in URL → auto-extracted and validated |
| Query Params | After `?` in URL → function params without path match |
| Request Body | Pydantic model as parameter → auto-validated JSON |
| Response Model | `response_model=` strips extra fields from response |
| HTTPException | Raise to return error responses with status codes |
| Dependency Injection | `Depends()` for DB sessions, auth, pagination |
| Async | `async def` for I/O-bound; `def` for CPU-bound |
| Middleware | Runs before/after every request (CORS, logging) |
| JWT Auth | OAuth2PasswordBearer + python-jose + passlib |
| File Upload | `UploadFile` for file handling |
| APIRouter | Split routes into files with prefixes and tags |
| SQLAlchemy | ORM integration with `Depends(get_db)` pattern |
| Testing | `TestClient` + pytest |
| WebSockets | Real-time via `@app.websocket()` |
| Lifespan | Startup/shutdown via `asynccontextmanager` |
| Settings | `pydantic-settings` + `.env` for configuration |

---
