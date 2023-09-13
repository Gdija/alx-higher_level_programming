#!/usr/bin/python3
"""function that returns the dictionary description"""


def class_to_json(obj):
    """return the dictionary"""
    return obj.__dict__
