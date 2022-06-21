#!/usr/bin/python3
"""Define a class Square.
Represent a square.
Initialize a new square.
Args:
    size (int): The size of the new square.
Return:
      the current area of the square.
"""


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
