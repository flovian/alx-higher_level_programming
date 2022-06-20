#!/usr/bin/python3
def magic_calculation(a, b):
    """Python bytecode
    Args:
        a: integer
        b: integer
    Returns: 0
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except BaseException:
            result = b + a
            break
    return result
