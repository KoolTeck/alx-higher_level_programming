#!/bin/bash
# takes in a URL, sends a OPTIONS request to that URL, and displays the  the body of the response
curl -sI -X OPTIONS  "$1" | grep "Allow" | cut -d " " -f 2-
