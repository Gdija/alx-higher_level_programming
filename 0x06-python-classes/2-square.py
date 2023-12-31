#!/usr/bin/python3
"""defines a square by size"""


class Square:
    """square
    Args:
        size: size o the square
    Raises:
        TypeError: if size is not integer
        ValueError: if size is less than zero
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
