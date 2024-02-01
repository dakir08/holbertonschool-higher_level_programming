#!/usr/bin/python3
"""
Fetching script
"""

import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
