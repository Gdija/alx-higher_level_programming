#!/usr/bin/python3
"""defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initialize instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
