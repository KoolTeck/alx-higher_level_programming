#!/bin/bash
# takes in a URL, sends a DELETE request to that URL, and displays the  the body of the response
curl -s -X DELETE "$1"
