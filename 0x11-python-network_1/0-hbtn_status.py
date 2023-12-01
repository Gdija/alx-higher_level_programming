#!/usr/bin/python3
"""
fetche an URL
"""
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')
    as response:
        res = response.read()
        res_utf8 = res.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res_utf8))
