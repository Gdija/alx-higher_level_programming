#!/usr/bin/python3
"""
display the error code
"""
import requests
import sys
if __name__ == "__main__":
    url = requests.get(sys.argv[1])
    if url.status_code >= 400:
        print("Error code: {}".format(url.status_code))
    else:
        print(url.text)
