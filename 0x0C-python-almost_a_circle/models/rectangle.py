#!/usr/bin/python3
"""create rectangle"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """task2 initialize the class"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """task2"""
        return self.__width

    @width.setter
    def width(self, value):
        """Task 3: add TypeError and ValueError execption"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """task2"""
        return self.__height

    @height.setter
    def height(self, value):
        """Task 3: add TypeError and ValueError execption"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """task2"""
        return self.__x

    @x.setter
    def x(self, value):
        """Task 3: add TypeError and ValueError execption"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """task2"""
        return self.__y

    @y.setter
    def y(self, value):
        """Task 3: add TypeError and ValueError execption"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """task 4"""
        return self.__width * self.__height

    def display(self):
        """task5 and 7"""
        print("{}".format("\n"*self.y), end="")
        for i in range(self.height):
            print("{}{}".format(" "*self.x, "#"*self.width))

    def __str__(self):
        """task6"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """task 8 and 9"""
        if args and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    self.id = arg
                elif n == 1:
                    self.width = arg
                elif n == 2:
                    self.height = arg
                elif n == 3:
                    self.x = arg
                elif n == 4:
                    self.y = arg
                n += 1
        elif kwargs and len(kwargs):
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
