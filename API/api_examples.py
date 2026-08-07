"""
api_examples.py

Code examples extracted from README.md with explanatory comments.

Includes:
- GET and POST examples using `requests`
- Basic auth example using `requests`
- API key header example
- JWT creation and decoding using PyJWT
- A minimal Flask app demonstrating a protected endpoint

Notes:
- Do NOT store real secrets in source code. Replace placeholder values with secure configuration (environment variables, secrets manager).
- Install dependencies before running examples:
    pip install requests PyJWT flask

Run examples selectively; the Flask example will start a local server when executed.
"""

import json
import datetime

# External libraries used in examples
# Install with: pip install requests PyJWT flask
import requests
import jwt
from flask import Flask, request, jsonify


# ---------------------------
# Simple GET request example
# ---------------------------

def example_get():
    """Send a simple GET request and print the status code and parsed JSON response.

    This demonstrates a typical API read operation (HTTP GET).
    Replace the URL below with a real API endpoint for real testing.
    """
    url = "https://jsonplaceholder.typicode.com/users/1"

    # Perform the GET request. `requests.get` returns a Response object.
    response = requests.get(url)

    # Print HTTP status code and JSON body (if any).
    print("GET", url)
    print("Status code:", response.status_code)
    try:
        print("JSON response:")
        print(json.dumps(response.json(), indent=2))
    except ValueError:
        print("No JSON body returned")


# ---------------------------
# Simple POST request example
# ---------------------------

def example_post():
    """Send a JSON POST request to create a resource.

    This demonstrates how to send a JSON payload and read the resulting response.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Python",
        "body": "API Example",
        "userId": 1
    }

    # Use `json=` to let requests serialize the payload and set Content-Type header
    response = requests.post(url, json=payload)

    print("POST", url)
    print("Status code:", response.status_code)
    try:
        print("JSON response:")
        print(json.dumps(response.json(), indent=2))
    except ValueError:
        print("No JSON body returned")


# ---------------------------
# Basic Authentication
# ---------------------------

def example_basic_auth():
    """Example of HTTP Basic Auth using requests.

    Basic auth sends a base64-encoded username:password in the Authorization header.
    Always use HTTPS when using Basic Auth so credentials are protected in transit.
    """
    url = "https://httpbin.org/basic-auth/user/pass"

    # requests supports basic auth via the `auth` parameter
    response = requests.get(url, auth=("user", "pass"))

    print("Basic Auth GET", url)
    print("Status code:", response.status_code)
    print("Response body:", response.text)


# ---------------------------
# API Key header example
# ---------------------------

def example_api_key():
    """Send an API key in a custom header.

    Many APIs accept an API key via a header like `x-api-key` or via a query parameter.
    Keep API keys secret and rotate them if leaked.
    """
    url = "https://httpbin.org/headers"
    headers = {
        "x-api-key": "123456789abcdef"  # placeholder; DO NOT use real keys in code
    }

    response = requests.get(url, headers=headers)

    print("API Key GET", url)
    print("Status code:", response.status_code)
    print("Response headers/body:", response.text)


# ---------------------------
# JWT creation and decoding
# ---------------------------

# NOTE: Never commit production secrets. Use env vars or a secret manager.
JWT_SECRET = "mysecretkey"  # placeholder secret for examples only
JWT_ALGORITHM = "HS256"


def create_jwt_example():
    """Create a JSON Web Token (JWT) with a short expiry and return the encoded token.

    The payload typically includes user identity and claims (roles/scopes).
    """
    payload = {
        "user": "Khushal",
        "role": "admin",
        # `exp` claim is the expiry time (UTC). Use relatively short lifetimes for access tokens.
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    # jwt.encode returns a byte string in PyJWT <2 and a str in >=2; force str for printing
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    # PyJWT may return bytes on older versions; ensure string
    if isinstance(token, bytes):
        token = token.decode("utf-8")

    print("Generated JWT:", token)
    return token


def decode_jwt_example(token):
    """Decode and verify a JWT. Raises jwt.ExpiredSignatureError if expired or jwt.InvalidTokenError on bad token.

    In a real app, handle exceptions and return appropriate HTTP status codes (401/403).
    """
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        print("Decoded JWT payload:")
        print(json.dumps(decoded, indent=2, default=str))
        return decoded

    except jwt.ExpiredSignatureError:
        print("Token has expired")
    except jwt.InvalidTokenError as e:
        print("Invalid token:", e)


# ---------------------------
# Minimal Flask protected endpoint
# ---------------------------

# This demonstrates a simple token check. For real applications, use a production-ready
# authentication/authorization library (Flask-JWT-Extended, Auth0, etc.) and HTTPS.
app = Flask(__name__)

# Example in-memory token for demonstration — in production, verify signatures instead
DEMO_TOKEN = "<token>"  # replace with token returned from create_jwt_example()


@app.route("/profile")
def profile():
    """A protected endpoint that requires a Bearer token in the Authorization header."""
    auth_header = request.headers.get("Authorization", "")

    # Expect header like: "Authorization: Bearer <token>"
    if not auth_header.startswith("Bearer "):
        return jsonify({"message": "Unauthorized - missing Bearer token"}), 401

    token = auth_header.split(" ", 1)[1]

    # For demo only: compare to an expected token. Real apps verify signature and expiry.
    if token != DEMO_TOKEN:
        return jsonify({"message": "Unauthorized - invalid token"}), 401

    # Token is accepted; return protected data
    return jsonify({"name": "Khushal", "role": "admin"})


# ---------------------------
# Helper entry point
# ---------------------------

def main():
    print("--- GET example ---")
    example_get()
    print("\n--- POST example ---")
    example_post()
    print("\n--- Basic Auth example ---")
    example_basic_auth()
    print("\n--- API Key example ---")
    example_api_key()
    print("\n--- JWT example ---")
    token = create_jwt_example()
    print("Decoding token...")
    decode_jwt_example(token)

    print("\nTo run the Flask example, execute this file and set DEMO_TOKEN to the token created above, then call:\n    flask run\nOr: python api_examples.py --flask")


if __name__ == "__main__":
    import sys

    # If `--flask` is passed, run the Flask app; otherwise run the demonstration main() flow.
    if "--flask" in sys.argv:
        # Ensure the DEMO_TOKEN value is set to a valid token before starting the server.
        print("Starting Flask demo server on http://127.0.0.1:5000")
        app.run(debug=True)
    else:
        main()
