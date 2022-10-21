#!/bin/bash
# takes in a URL, sends a GET request with header var to that URL, and displays the  the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
