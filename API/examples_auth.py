"""
examples_auth.py

Contains Basic Auth and API Key header examples using requests.

Dependencies: requests
Install: pip install requests
"""

import requests


def basic_auth_example():
    """Example using HTTP Basic Auth. The server expects basic auth credentials.

    Note: Basic auth sends credentials in Base64; always use HTTPS.
    """
    url = "https://httpbin.org/basic-auth/user/pass"
    resp = requests.get(url, auth=("user", "pass"))
    print("Basic Auth GET", url)
    print("Status:", resp.status_code)
    print(resp.text)


def api_key_example():
    """Example sending an API key via a custom header.

    Replace the placeholder key with your real key stored securely.
    """
    url = "https://httpbin.org/headers"
    headers = {"x-api-key": "123456789abcdef"}  # placeholder
    resp = requests.get(url, headers=headers)
    print("API Key GET", url)
    print("Status:", resp.status_code)
    print(resp.text)


if __name__ == '__main__':
    print('Running Basic Auth example')
    basic_auth_example()
    print('\nRunning API Key example')
    api_key_example()
