#!/usr/bin/python3
""" create square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """task 10"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.size)

    @property
    def size(self):
        """task11"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """task 12"""
        if args and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    self.id = arg
                elif n == 1:
                    self.size = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg
                n += 1
        elif kwargs and len(kwargs):
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """task 14"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
