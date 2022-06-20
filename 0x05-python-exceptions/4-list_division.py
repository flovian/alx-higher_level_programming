#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides 2 lists element by element
    Args:
        my_list_1: list
        my_list_2: list
        list_length: integer
    Return: list of size list_length containing the result
    """
    result = []
    i = 0
    while i < list_length:
        res = 0

        try:
            res = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            i += 1
            result.append(res)

    return result
