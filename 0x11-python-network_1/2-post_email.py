#!/usr/bin/python3
"""
post an email
"""
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    param = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(param)
    data = data.encode('ascii')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        email = response.read()
        email_utf8 = email.decode('utf-8')
        print(email_utf8)
