#!/usr/bin/python3
"""
Fetching script
"""

from urllib import request


if __name__ == "__main__":
    r = request.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))