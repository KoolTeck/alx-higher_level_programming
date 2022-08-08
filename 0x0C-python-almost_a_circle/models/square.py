#!/usr/bin/python3
""" The square module inherits from rectangle module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inherits from the rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        s1 = "[{}] ({:d}) ".format(self.__class__.__name__, self.id)
        s2 = "{:d}/{:d} - {:d}".format(self.x, self.y, self.width)
        return (s1 + s2)

    @property
    def size(self):
        """ returns the square obj size """
        return self.width

    @size.setter
    def size(self, value):
        """ sets the size value for the square obj """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates the obj attrbutes """
        if len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returns dic repr of Square """
        id = self.id
        size = self.size
        x = self.x
        y = self.y
        return ({'id': id, 'size': size, 'x': x, 'y': y})
