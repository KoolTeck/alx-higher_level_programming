#!/usr/bin/python3
"""
    defines script that takes in GitHub credentials (username and password)
    and uses the GitHub API to display user id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = " https://api.github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=auth)
    print(r.json().get('id'))
