#!/usr/bin/python3
""" defines getting a header info from a response """
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as res:
        header = res.headers
        id = header.get("X-Request-Id")
        print(id)
