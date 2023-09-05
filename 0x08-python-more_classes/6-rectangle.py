#!/usr/bin/python3
""" define a rectangle"""


class Rectangle:

    number_of_instances = 0

    """define rectangle"""
    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1

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

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        return (('#'*self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Deletes instance of Rectangle"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
