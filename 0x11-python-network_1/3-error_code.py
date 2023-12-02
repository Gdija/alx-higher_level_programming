#!/usr/bin/python3
"""
display the error code
"""
import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as error:
        print('Error code: ', error.code)
