#!/usr/bin/python3
""" 0-main """
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")
    
    for rect_in, rect_out in zip(list_rectangles_input, list_rectangles_output):
        print(rect_in is rect_out, rect_in.to_dictionary is rect_out.to_dictionary)
        print(rect_in == rect_out, rect_in.to_dictionary() == rect_out.to_dictionary())
        print(rect_in.to_dictionary(), rect_out.to_dictionary())
