#!/usr/bin/python3
"""
Fetching script
"""

from urllib import request


if __name__ == "__main__":
    r = request.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
