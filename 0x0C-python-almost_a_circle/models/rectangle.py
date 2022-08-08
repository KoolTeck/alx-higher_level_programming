#!/usr/bin/python3
""" The models/rectangle module """

from models.base import Base


class Rectangle(Base):
    """
    defines a rectangle class that inherits from

    the base class

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ gets the width of the current obj """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ sets the width of the current obj """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height of the current obj """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ sets the width of the current obj """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets the x coordinate of the current obj """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ gets the x coordinate of the current obj """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets the y coordinate of the current obj """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ gets the y coordinate of the current obj """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the rect """
        return (self.__width * self.__height)

    def display(self):
        """ prints the rec to stdout with char # """
        for i in range(self.y):
            print()
        for j in range(self.__height):
            print(' ' * self.x, end='')
            print('#' * self.__width)

    def __str__(self):
        """ prints the string rep of the rec object """
        s1 = "[{}] ({:d}) ".format(self.__class__.__name__, self.id)
        s2 = "{:d}/{:d} - {:d}/{:d}"
        return (s1 + s2.format(self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ update the obj attr. with non-keywords args and keyworded args """
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ returns the dict repr of the rec. obj """
        h = self.height
        w = self.width
        x = self.x
        y = self.y
        id = self.id
        return {'x': x, 'y': y, 'id': id, 'height': h, 'width': w}
