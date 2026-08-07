"""
examples_get_post.py

Contains small, standalone GET and POST examples using the requests library.
Run as a script to see outputs.

Dependencies: requests
Install: pip install requests
"""

import json
import requests


def get_example():
    """Perform a GET request and print JSON response."""
    url = "https://jsonplaceholder.typicode.com/users/1"
    resp = requests.get(url)
    print("GET", url)
    print("Status:", resp.status_code)
    try:
        print(json.dumps(resp.json(), indent=2))
    except ValueError:
        print("No JSON returned")


def post_example():
    """Perform a POST request with JSON body and print response."""
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Python",
        "body": "API Example",
        "userId": 1
    }
    resp = requests.post(url, json=payload)
    print("POST", url)
    print("Status:", resp.status_code)
    try:
        print(json.dumps(resp.json(), indent=2))
    except ValueError:
        print("No JSON returned")


if __name__ == '__main__':
    print('Running GET example')
    get_example()
    print('\nRunning POST example')
    post_example()
