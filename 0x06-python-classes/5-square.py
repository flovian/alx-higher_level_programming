#!/usr/bin/python3
"""Define a class Square.
Represent a square.
Initialize a new square.
Args:
    size (int): The size of the new square.
Get/set the current size of the square.
Return:
      the current area of the square.
      Print the square with the # character

"""


class Square:
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
