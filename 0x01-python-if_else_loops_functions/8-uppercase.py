#!/usr/bin/python3
def uppercase(str):
    for c in range(0, len(str)):
        uni = ord(str[c])
        if uni == 32:
            n = 32
        elif uni <= 90:
            n = uni
        else:
            n = uni - 32
        print('{:s}'.format(chr(n)), end='')
    print('{}'.format(''))
