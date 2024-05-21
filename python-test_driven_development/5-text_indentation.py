#!/usr/bin/python3
"""define text_indetation function"""


def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    for char in text:
        print(char, end='')
        if char in punctuations:
            print("{}".format('\n\n'), end='')
