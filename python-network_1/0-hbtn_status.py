#!/usr/bin/python3
import urllib.request
"""
script that fetches https://intranet.hbtn.io/status
"""

with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
    content = res.read()
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
