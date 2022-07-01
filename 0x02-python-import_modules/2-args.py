#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = sys.argv
    av_l = len(av) - 1
    fmt1 = "{:d} {:s}{:s}"
    fmt2 = "{:d}{:s} {:s}"
    s1 = "argument" if av_l == 1 else "arguments"
    s2 = ":" if av_l > 0 else "."
    print(fmt1.format(av_l, s1, s2))
    if av_l > 0:
        n = 1
        while (av_l >= n):
            print(fmt2.format(n, ":", av[n]))
            n += 1
