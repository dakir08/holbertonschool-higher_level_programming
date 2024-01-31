#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
it use the package urllib
"""


if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request(url='http://intranet.hbtn.io/status', headers={'User-Agent': 'Mozilla/5.0'})

    with urllib.request.urlopen(req) as res:
        content = res.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
