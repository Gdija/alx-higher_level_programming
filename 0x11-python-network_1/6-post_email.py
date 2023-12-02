#!/usr/bin/python3
"""
post an email
"""
import requests
import sys
if __name__ == "__main__":
    param = {'email': sys.argv[2]}
    url = requests.post(sys.argv[1], data=param)
    print(url.text)
