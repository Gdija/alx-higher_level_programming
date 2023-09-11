#!/usr/bin/python3
"""function that prints a text with 2 new lines after some characters"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    ch = 0
    while ch < len(text) and text[ch] == ' ':
        ch += 1

    while ch < len(text):
        print(text[ch], end="")
        if text[ch] == "\n" or text[ch] in ".?:":
            if text[ch] in ".?:":
                print("\n")
            ch += 1
            while ch < len(text) and text[ch] == ' ':
                ch += 1
            continue
        ch += 1
