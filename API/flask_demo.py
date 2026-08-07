"""
flask_demo.py

Minimal Flask app demonstrating a protected endpoint that expects a Bearer token.

Dependencies: Flask
Install: pip install flask

Usage:
  - Set DEMO_TOKEN to a value (e.g., copy the token from examples_jwt.create_token)
  - Run: python flask_demo.py
  - Request: curl -H "Authorization: Bearer <token>" http://127.0.0.1:5000/profile

Notes:
  This demo uses a simple equality check for the token. In production verify signatures and expiry using PyJWT
  (or use Flask-JWT-Extended / an external auth provider).
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# For demo only: set this to a valid token string before running the server
DEMO_TOKEN = "<token>"


@app.route('/profile')
def profile():
    """Protected endpoint requiring a Bearer token in the Authorization header."""
    auth = request.headers.get('Authorization', '')
    if not auth.startswith('Bearer '):
        return jsonify({'message': 'Unauthorized - missing Bearer token'}), 401

    token = auth.split(' ', 1)[1]
    if token != DEMO_TOKEN:
        return jsonify({'message': 'Unauthorized - invalid token'}), 401

    return jsonify({'name': 'Khushal', 'role': 'admin'})


if __name__ == '__main__':
    print('Starting demo Flask server on http://127.0.0.1:5000')
    print('Make sure to set DEMO_TOKEN to a valid token before calling /profile')
    app.run(debug=True)
