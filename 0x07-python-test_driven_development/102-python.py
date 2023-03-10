#!/usr/bin/python3
'''A module that prints information about Python string objects using
the Python C API.
'''
import ctypes


lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]

# Valid objects
lib.print_python_string('English: I do not know what you mean')
lib.print_python_string('Russian: Я не знаю, что вы имеете в виду')
lib.print_python_string('French: je ne sais pas ce que tu veux dire')
s = "French: L'huile et l'eau ne peuvent pas être mélangées"
lib.print_python_string(s)
lib.print_python_string('Chinese: 我不知道你想表达什么意思')
lib.print_python_string('Korean: 난 당신이 무슨 뜻인지 모르겠어요')
lib.print_python_string('Japanese: 意味が分からない')
lib.print_python_string('Yoruba: Emi ko mọ kini o tumọ si')
lib.print_python_string('Igbo: Amaghị m ihe ị na -ekwu')
lib.print_python_string('Kinyarwanda: Sinzi icyo ushaka kuvuga')
lib.print_python_string('Swahili: Sijui unamaanisha nini')

# Invalid objects
lib.print_python_string(b'I do not know what you mean')
lib.print_python_string(45)
lib.print_python_string(list('I do not know what you mean'))
