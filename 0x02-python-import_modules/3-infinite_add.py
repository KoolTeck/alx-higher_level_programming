#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    av_len = len(argv) - 1
    sum = 0
    n = 1
    if av_len > 0:
        while av_len >= n:
            sum += int(argv[n])
            n += 1
    print("{:d}".format(sum))
