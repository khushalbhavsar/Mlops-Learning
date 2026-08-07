"""
examples_jwt.py

Create and decode JWT examples using PyJWT.

Dependencies: PyJWT
Install: pip install PyJWT

Do NOT store secrets in source code for real projects. Use environment variables or a secrets manager.
"""

import datetime
import json
import jwt

# Example secret for demo only. Replace with secure management in production.
JWT_SECRET = "mysecretkey"
JWT_ALGORITHM = "HS256"


def create_token(user='khushal', role='admin', hours_valid=1):
    """Create and return a signed JWT token with an expiry."""
    payload = {
        'user': user,
        'role': role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=hours_valid)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    print('Generated token:')
    print(token)
    return token


def decode_token(token):
    """Decode and validate the JWT. Handle expiry and invalid token errors."""
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        print('Decoded payload:')
        print(json.dumps(decoded, indent=2, default=str))
        return decoded
    except jwt.ExpiredSignatureError:
        print('Token has expired')
    except jwt.InvalidTokenError as e:
        print('Invalid token:', e)


if __name__ == '__main__':
    print('Creating token...')
    t = create_token()
    print('\nDecoding token...')
    decode_token(t)
