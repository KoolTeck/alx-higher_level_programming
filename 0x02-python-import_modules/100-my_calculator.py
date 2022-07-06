#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as av
    from calculator_1 import add, sub, mul, div
    if len(av) != 4:
        print("Usage: {:s} <a> <operator> <b>".format(av[0]))
        exit(1)
    op = av[2]
    a = int(av[1])
    b = int(av[3])
    fmt = "{:d} {:s} {:d} = {:d}"
    if op == '+':
        print(fmt.format(a, op, b, add(a, b)))
    elif op == '-':
        print(fmt.format(a, op, b, sub(a, b)))
    elif op == '*':
        print(fmt.format(a, op, b, mul(a, b)))
    elif op == '/':
        print(fmt.format(a, op, b, div(a, b)))
    else:
        error = "Unknown operator. Available operators: +, -, * and /"
        print("{}".format(error))
        exit(1)
