#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\language that combines remarkable power with very clear syntax"
str = str[39:66] + str[106: 112] + str[:7]
str = str[:-1]
print(str)