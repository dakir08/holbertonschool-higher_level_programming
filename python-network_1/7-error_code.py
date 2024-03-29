#!/usr/bin/python3
"""
script that takes in a URL
sends a request to the URL
displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code is not 200:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
