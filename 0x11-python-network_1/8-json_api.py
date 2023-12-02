#!/usr/bin/python3
"""
search api using json
"""
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    url = requests.post("http://0.0.0.0:5000/search_user", data={'q': letter})
    try:
        url_json = url.json()
        if len(url_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(url_json.get('id'), url_json.get('name')))
    except valueError as error:
        print("Not a valid JSON")
