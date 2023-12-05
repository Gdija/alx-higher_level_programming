#!/usr/bin/python3
"""
GITHUB autentication
"""
import requests
from requests.auth import HTTPBasicAuth
import sys
if __name__ == "__main__":
    test = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = requests.get('https://api.github.com/user', auth=test)
    url_json = url.json()
    print(url_json.get('id'))
