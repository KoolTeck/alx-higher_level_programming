#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 15 == 0:
            print("{:s}".format("FizzBuzz"), end=' ')
            continue
        elif n % 3 == 0:
            print("{:s}".format("Fizz"), end=' ')
            continue
        elif n % 5 == 0:
            print("{:s}".format("Buzz"), end=' ')
            continue
        print("{:d}".format(n), end=' ')
