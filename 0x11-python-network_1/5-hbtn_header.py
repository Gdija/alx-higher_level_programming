#!/usr/bin/python3
"""
display X-Request-Id value's
"""
import requests
import sys
if __name__ == "__main__":
    url = requests.get(sys.argv[1])
    url_Id = url.headers.get('X-Request-Id')
    print(url_Id)
