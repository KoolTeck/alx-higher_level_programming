#!/usr/bin/python3
def multiple_returns(sentence):
    s_len = len(sentence)
    c = sentence[0] if s_len > 0 else None
    return (len(sentence), c)
