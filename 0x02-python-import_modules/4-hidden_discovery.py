#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidden_list = dir(hidden_4)
    for s in hidden_list:
        if s[0] == "_":
            continue
        print("{:s}".format(s))
