#!/usr/bin/python3
'''Contains a say_my_name function for a TDD project.
'''


def say_my_name(first_name, last_name=""):
    '''Prints a given first and last name of a person.

    Args:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.

    Raises:
        TypeError: If the first_name and last_name are not strings.
    '''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print('My name is {} {}'.format(first_name, last_name))
