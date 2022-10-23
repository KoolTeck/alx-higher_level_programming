#!/usr/bin/python3
"""
    defines script that takes in a URL, sends a POST request
    to the URL and displays the value of the variable response

"""
import sys
import requests


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
