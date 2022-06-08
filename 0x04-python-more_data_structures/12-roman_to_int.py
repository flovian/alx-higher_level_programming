#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if not roman_string:
        return None
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_val = 0
    for i in range(len(roman_string)):
        for key, val in num.items():
            if key == roman_string[i]:
                total += val
                if prev_val < val:
                    total -= (prev_val * 2)
                    prev_val = val
    return total
