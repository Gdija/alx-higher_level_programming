#!/usr/bin/python3
""" define a rectangle"""


class Rectangle:

    """define rectangle"""
    def __init__(self, width=0, height=0):

        self.height = height
        self.width = width

    @property
    def width(self):
        """define width"""
        return self.__width

    @property
    def height(self):
        """define height"""
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
