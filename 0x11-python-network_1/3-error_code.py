#!/usr/bin/python3
"""
    defines script that takes in a URL and sends arequest
    to the passed URL and displays the body of the response (decoded in utf-8)
    HttpError exception is handled
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as res:
            body = res.read().decode('utf-8')
            print(body)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
