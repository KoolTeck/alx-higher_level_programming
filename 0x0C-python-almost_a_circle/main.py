#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle
from models.square import Square


if __name__ == "__main__":

    r3 = Rectangle(2, 5)
    r3.save_to_file([])

    s3 = Square(2, 3)
    s3.save_to_file([])

        
