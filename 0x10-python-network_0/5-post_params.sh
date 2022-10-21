#!/bin/bash
# takes in a URL, sends a POST request with body vars to that URL, and displays the  the body of the response
curl  -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
