#!/usr/bin/python3
"""function that returns an obj represented by JSON"""


import json


def from_json_string(my_str):
    """function to convert from json"""
    return json.loads(my_str)
