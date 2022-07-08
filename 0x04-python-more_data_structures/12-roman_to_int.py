#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) and roman_string is not None:
        rom_sym = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        res = 0
        is_roman = check_roman(rom_sym, roman_string)
        if is_roman:
            s_len = len(roman_string)
            for n in range(s_len):
                current = roman_string[n]
                if s_len == 1:
                    res = rom_sym[current]
                    return (res)
                nex = roman_string[n + 1]
                c_val = rom_sym[current]
                n_val = rom_sym[nex]
                if s_len == 2:
                    res = c_val + n_val if c_val >= n_val else n_val - c_val
                    return (res)
                if c_val >= n_val:
                    res += c_val
                else:
                    res = res - c_val
                if n == s_len - 2:
                    res += n_val
                    break
            return (res)
    return (0)


def check_roman(symbol_dict, string):
    """ checks if the inputed string is numeral """
    for s in string:
        if s in symbol_dict:
            continue
        else:
            return False
    return True
