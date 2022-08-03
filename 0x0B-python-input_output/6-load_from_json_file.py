#!/usr/bin/python3
""" The 6-load_from_json_file module """


import json


def load_from_json_file(filename):
    """ creates an object from a json file """

    with open(filename, 'r', encoding='utf-8') as f:
        return (json.load(f))
