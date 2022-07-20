#!/usr/bin/python3
"""The Square module docstrings.

This module demonstrates creating a Square class and atrributes

File calling:

        $ python3 0-square.py

"""


class Square:
    """ creates an empty Square class  defining a class """

    def __init__(self, size=0, position=(0, 0)):
        """docstring on the __init__ method.

        Args:
            size (str): the size of the square

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ gets the current size """
        return (self.__size)

    @size.setter
    def size(self, size):
        """ sets the current size """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """ gets the current position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        check_v1 = type(value[0]) is int
        check_v2 = type(value[1]) is int
        err = TypeError("position must be a tuple of 2 positive integers")
        if check_v1 and check_v2:
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise err
        else:
            raise err

    def area(self):
        """ compute and return the current square area

        Returns:
            the square area

        """
        return (self.__size ** 2)

    def my_print(self):
        """ prints the square """
        p1 = self.__position[0]
        p2 = self.__position[1]
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(p1):
                print(" ", end="")
                if p2 > 0:
                    break
            for k in range(self.__size):
                print("#", end="")
            print()


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square()
    my_square_2.size = 10
    my_square_2.position = (5, "0")
    my_square_2.my_print()

    print("--")
