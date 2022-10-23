#!/usr/bin/python3
"""
    defines script that takes in a URL, sends a POST request
    to the URL and displays the value of the variable response

"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print('Error code:', r.status_code)
    else:
        print(r.text)
